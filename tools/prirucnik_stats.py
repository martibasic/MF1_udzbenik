"""Mjere i jezične provjere teksta priručnika prema docs/konvencije_pisanja.md.

Alat čita kanonske izvore u ``source/`` i ne mijenja nijednu datoteku.
Nalazi su upute za čitanje, ne presude: pravilo iz konvencija navodi što
treba provjeriti, a autorica odlučuje. Alat nije dio objavnog CI-ja.

Načini rada (pokreću se iz korijena repozitorija):

    python tools/prirucnik_stats.py                    # profil svih poglavlja i dodataka
    python tools/prirucnik_stats.py source/u08_*.md    # profil odabranih izvora
    python tools/prirucnik_stats.py --nalazi [IZVORI]  # svaki nalaz s retkom i pravilom
    python tools/prirucnik_stats.py --nacrt IZVOR      # obrnuti nacrt: odjeljci, blokovi, odlomci
    python tools/prirucnik_stats.py --usporedi REV [IZVORI]
                                                       # provjera značenja nakon prerade
    python tools/prirucnik_stats.py --json [...]       # strojni izlaz profila i nalaza

``--usporedi REV`` uspoređuje radnu kopiju s Git revizijom REV (npr. HEAD ili
hash commita prije lekture). Ispisuje izgubljene i dodane brojeve, ID-jeve i
citate te parove promijenjenih rečenica u kojima se promijenio broj, nijekanje,
ograda ili snaga tvrdnje.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"

# Prag za ispis duge rečenice u --nalazi (pravilo K3). Prompt za čitanje, ne granica.
DUGA_RECENICA = 40

# ---------------------------------------------------------------------------
# Pravila. Svako pravilo ima oznaku iz docs/konvencije_pisanja.md.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Pravilo:
    oznaka: str          # npr. "K7"
    kratko: str          # kratki naziv nalaza
    uzorak: re.Pattern[str]
    prijedlog: str


def _r(uzorak: str, zastavice: int = re.IGNORECASE) -> re.Pattern[str]:
    return re.compile(uzorak, zastavice)


# Pravila nad vidljivim tekstom (bez matematike, poveznica, atributa i HTML-a).
PRAVILA_TEKST: list[Pravilo] = [
    # K1 — registar priručnika: bez povijesti izrade i internog rječnika
    Pravilo("K1", "interni naziv alata", _r(r"\b(verifikator\w*|manifest\w*|commit\w*|Codex|Claude|GPT)\b"),
            "Opiši što čitatelj treba znati; alati izrade ne pripadaju studentskom tekstu."),
    Pravilo("K1", "oznaka CI", _r(r"\bCI\b", 0), "Interni pojam izrade; ukloni iz vidljivog teksta."),
    Pravilo("K1", "radna oznaka", _r(r"\b(TODO|FIXME|XXX)\b|radno izdanje|\bu pripremi\b|NOVA PEDAGOŠKA|\blegacy\b|treći sloj|\bVal\s*\d"),
            "Ostatak izrade; ukloni ili prenesi u docs/radno/."),
    Pravilo("K1", "interna oznaka poglavlja ili dodatka", _r(r"(?<![\w/.-])(U\d{2}|D0\d)(?![\w-])", 0),
            "U tekstu piši „pog. N” (chapter-ref) ili „dodatak A–F”."),
    Pravilo("K1", "povijest verzija", _r(r"\b(ov[aeoj]{1,2}|prethodn\w*|ranij\w*|stari\w*|nov[oj]\w*)\s+(verzij|inačic|revizij|izdanj)\w*"),
            "Priručnik opisuje stanje, ne povijest izmjena (osim impresuma i errate)."),
    # K4 — naslovi su izjavni (provjera naslova je zasebna, vidi provjeri_naslov)
    # K7 — autorsko nazivlje i pravopis
    Pravilo("K7", "zadaci → zadatci", _r(r"\bzadac(i|ima)\b"), "zadatci, zadatcima"),
    Pravilo("K7", "podaci → podatci", _r(r"\bpodac(i|ima)\b"), "podatci, podatcima"),
    Pravilo("K7", "gubici → gubitci", _r(r"\bgubic(i|ima)\b"), "gubitci, gubitcima"),
    Pravilo("K7", "pumpa → crpka", _r(r"\bpump(a|e|i|u|om|ama|n\w*)\b"), "crpka; kućište crpke, crpna stanica"),
    Pravilo("K7", "omočen → oplakan", _r(r"\bomočen\w*"), "oplakani opseg, oplakana ploha"),
    Pravilo("K7", "horizontalno/vertikalno", _r(r"\b(horizontaln|vertikaln)\w*"), "vodoravno; okomito ili uspravno prema smislu"),
    Pravilo("K7", "pod-/nadkritični", _r(r"\b(podkritičn|nadkritičn)\w*"), "potkritični, natkritični"),
    Pravilo("K7", "hidrostatski → hidrostatički", _r(r"\bhidrostatsk\w*"), "hidrostatički"),
    Pravilo("K7", "okr/min → min⁻¹", _r(r"\bokr\s*/\s*min\b|\bo/min\b"), "brzina vrtnje u min⁻¹"),
    Pravilo("K7", "impeler → radno kolo", _r(r"\bimpeler\w*"), "radno kolo"),
    Pravilo("K7", "usisna košara → usisni koš", _r(r"\busisn\w*\s+košar\w*"), "usisni koš (engl. sea chest)"),
    Pravilo("K7", "brodski vijak → propeler", _r(r"\bbrodsk\w*\s+vij(ak|ka|ku|kom|ci|aka)\b"), "propeler"),
    Pravilo("K7", "disipacijski → umirni bazen", _r(r"\bdisipacijsk\w*\s+bazen\w*"), "umirni bazen"),
    Pravilo("K7", "no-slip bez oznake engl.", _r(r"(?<!engl\. )\bno-?slip\b"), "uvjet prianjanja; engleski izraz kao (engl. *no-slip*)"),
    Pravilo("K7", "izračunat- → izračunan-", _r(r"\bizračunat(a|o|u|om|oj|ih|im|e)?\b"), "izračunan, izračunana, izračunano"),
    Pravilo("K7", "Bernoulli jednadžba", _r(r"\bBernoulli\s+jednadžb\w*"), "Bernoullijeva jednadžba"),
    Pravilo("K7", "kratica MF1 u tekstu", _r(r"(?<![\w/.-])MF1(?![\w-])", 0), "„u ovom priručniku” ili „Mehanika fluida 1”"),
    Pravilo("K7", "ravni navodnici", _r(r'"[^"\n]{1,80}"', 0), "hrvatski navodnici „…”"),
    # K12 — upućivanja brojem
    Pravilo("K12", "upućivanje „ispod/iznad”",
            _r(r"\b(slik\w*|skic\w*|tablic\w*|jednadžb\w*|formul\w*)\s+(ispod|iznad|dolje|gore)\b|\b(ispod|iznad)\s+(prikazan\w*|naveden\w*|dan[aeiou]?)\b"),
            "Uputi brojem: Slika [-@fig-…], jednadžba ([-@eq-…])."),
]

# Pravila nad matematikom ($…$ i $$…$$).
PRAVILA_MATEMATIKA: list[Pravilo] = [
    Pravilo("K8", "decimalna točka u formuli", _r(r"(?<![\w.])\d+\.\d+(?![\w.])", 0), "decimalni zarez kao {,}: 9{,}81"),
    Pravilo("K8", "zarez bez {,} među znamenkama", _r(r"(?<=\d),(?=\d)", 0), "decimale 9{,}81; popis (26;\\,0)"),
    Pravilo("K8", "konst. bez \\text", _r(r"(?<!\\text\{)\bkonst\b|\bconst\b", 0), "\\text{konst.}"),
]

# Riječi kojima se u --usporedi prati promjena značenja.
NIJEKANJE = _r(r"\b(ne|nije|nisu|nema|nemaju|bez|nikad\w*|nijed\w*|ništa)\b")
SNAGA = _r(r"\b(uvijek|samo|točno|isključivo|svak\w*|mora\w*|nužno|jedin\w*|potpuno|nikad\w*)\b")
OGRADA = _r(r"\b(približno|oko|otprilike|može|mogu|smije|obično|uglavnom|pretežno|reda|gotovo|tipično)\b|\\approx|≈")
POREDBA = _r(r"\b(već\w*|manj\w*|viš\w*|niž\w*|brž\w*|sporij\w*|dulj\w*|krać\w*|deblj\w*|tanj\w*)\b")

KRATICE = (
    "pog", "npr", "tj", "sl", "engl", "konst", "str", "itd", "br", "god", "prof", "dr",
    "sc", "izv", "pribl", "tzv", "odn", "min", "max", "sv", "tablica", "jedn", "usp", "vidi", "red",
)
KRATICA_RE = re.compile(r"\b(" + "|".join(KRATICE) + r")\.(?=\s)", re.IGNORECASE)
RECENICA_RE = re.compile(r"(?<=[.!?…])[\"”»)]*\s+(?=[„\"(\[A-ZČĆŽŠĐ0-9$])")
RIJEC_RE = re.compile(r"[0-9A-Za-zČĆŽŠĐčćžšđ]+(?:[-’'][0-9A-Za-zČĆŽŠĐčćžšđ]+)*")

BLOKOVI = {
    "mf1-temelj": "Temelj",
    "mf1-izvod": "Izvod",
    "mf1-fizikalno-znacenje": "Fizikalno značenje",
    "mf1-cfd": "CFD",
    "mf1-granica-modela": "Granica modela",
    "mf1-numerika": "Numerički pokus",
    "mf1-dublje": "Dublje",
    "mf1-interaktivno": "Interaktivni prikaz",
    "mf1-we": "Riješeni primjer",
    "mf1-ch": "Riješeni primjer",
    "mf1-samoprovjera": "Provjeri sebe",
    "mf1-vjezbe-list": "Zadatci",
    "mf1-zavrsni-okvir": "Sažetak",
}


# ---------------------------------------------------------------------------
# Čišćenje retka
# ---------------------------------------------------------------------------

INLINE_MATH_RE = re.compile(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$")
HTML_TAG_RE = re.compile(r"<[^>]+>")
ATTR_RE = re.compile(r"\{[#.][^}]*\}|\{[a-z-]+=[^}]*\}")
LINK_RE = re.compile(r"\]\([^)]*\)")
URL_RE = re.compile(r"https?://\S+")
CHREF_RE = re.compile(r"\[\]\{[^}]*\}")
CROSSREF_RE = re.compile(r"\[?-?@[\w:-]+\]?")
IMAGE_RE = re.compile(r"^\s*!\[(?P<cap>.*?)\]\((?P<path>[^)]*)\)(?P<attrs>\{.*\})?\s*$")
FIG_ALT_RE = re.compile(r'fig-alt="([^"]*)"')
HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<text>.*?)\s*(?P<attrs>\{[^}]*\})?\s*$")
FENCE_OPEN_RE = re.compile(r"^\s*(?P<colons>:{3,})\s*(?P<rest>\{[^}]*\}|[\w-]+)\s*$")
FENCE_CLOSE_RE = re.compile(r"^\s*:{3,}\s*$")


def _math_zamjena(m: re.Match[str]) -> str:
    # Formula na kraju rečenice često nosi završnu točku u sebi: „… = \text{konst.}$ Svaki …”.
    kraj = m.group(1).rstrip()
    return " X" + (kraj[-1] if kraj.endswith((".", ",")) else "") + " "


OZNAKA_POLJA_RE = re.compile(r"^\s*\*\*[^*]{1,60}\*\*[.:]?\s*$")
UVODNA_GLAVA_RE = re.compile(r"^\s*\*\*[^*]{1,50}[.:]\*\*\s*")
OZNAKA_POPISA_RE = re.compile(r"^\s*(?:\d+[.)]|[-*+])\s+")


def vidljivi_tekst(redak: str) -> str:
    """Tekst koji čitatelj vidi, bez matematike, poveznica, atributa i oznaka."""
    s = CHREF_RE.sub(" pog. N ", redak)
    s = INLINE_MATH_RE.sub(_math_zamjena, s)
    s = URL_RE.sub(" ", s)
    s = LINK_RE.sub("]", s)
    s = ATTR_RE.sub(" ", s)
    s = HTML_TAG_RE.sub(" ", s)
    s = CROSSREF_RE.sub(" R ", s)
    s = s.replace("**", "").replace("__", "")
    s = re.sub(r"(?<!\w)[*_](?=\S)|(?<=\S)[*_](?!\w)", "", s)
    s = s.replace("[", " ").replace("]", " ")
    return re.sub(r"\s+", " ", s).strip()


def recenice(tekst: str) -> list[str]:
    zasticeno = KRATICA_RE.sub(lambda m: m.group(1) + "§", tekst)
    zasticeno = re.sub(r"(\d)\.(?=\s+[a-zčćžšđ])", r"\1§", zasticeno)  # „15. listopada”
    dijelovi = [d.replace("§", ".").strip() for d in RECENICA_RE.split(zasticeno)]
    return [d for d in dijelovi if RIJEC_RE.search(d)]


def broj_rijeci(tekst: str) -> int:
    return len(RIJEC_RE.findall(tekst))


# ---------------------------------------------------------------------------
# Raščlamba izvora
# ---------------------------------------------------------------------------

@dataclass
class Odlomak:
    redak: int
    odjeljak: str
    blok: str
    tekst: str             # vidljivi tekst
    rijeci: int
    recenice: list[str]


@dataclass
class Nalaz:
    datoteka: str
    redak: int
    oznaka: str
    kratko: str
    isjecak: str
    prijedlog: str


@dataclass
class Profil:
    datoteka: str
    oznaka: str
    odlomci: list[Odlomak] = field(default_factory=list)
    nalazi: list[Nalaz] = field(default_factory=list)
    jednadzbe: int = 0
    numerirane: int = 0
    primjeri: int = 0
    zadatci: int = 0
    blokovi: Counter = field(default_factory=Counter)
    komentari: int = 0

    @property
    def rijeci(self) -> int:
        return sum(o.rijeci for o in self.odlomci)

    @property
    def sve_recenice(self) -> list[str]:
        return [r for o in self.odlomci for r in o.recenice]


def oznaka_dokumenta(path: Path) -> str:
    m = re.match(r"([ud])(\d{2})_", path.name)
    if not m:
        return path.stem
    return str(int(m.group(2))) if m.group(1) == "u" else "dod. " + chr(64 + int(m.group(2)))


def _isjecak(tekst: str, m: re.Match[str], sirina: int = 40) -> str:
    a, b = max(0, m.start() - sirina), min(len(tekst), m.end() + sirina)
    return ("…" if a else "") + tekst[a:b].strip() + ("…" if b < len(tekst) else "")


def provjeri_tekst(profil: Profil, broj: int, tekst: str) -> None:
    for p in PRAVILA_TEKST:
        for m in p.uzorak.finditer(tekst):
            profil.nalazi.append(Nalaz(profil.datoteka, broj, p.oznaka, p.kratko, _isjecak(tekst, m), p.prijedlog))


def provjeri_matematiku(profil: Profil, broj: int, formula: str) -> None:
    for p in PRAVILA_MATEMATIKA:
        for m in p.uzorak.finditer(formula):
            profil.nalazi.append(Nalaz(profil.datoteka, broj, p.oznaka, p.kratko, _isjecak(formula, m, 25), p.prijedlog))


def analiziraj(path: Path, tekst: str | None = None) -> Profil:
    if tekst is None:
        tekst = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix() if path.is_absolute() and ROOT in path.parents else str(path)
    profil = Profil(rel, oznaka_dokumenta(path))
    if path.name.startswith("d06_"):
        # Ključ rezultata generira skripta; jezik se popravlja u izvoru zadataka.
        return profil

    odjeljak = "(uvod)"
    stog: list[str] = []
    u_jednadzbi = False
    jednadzba: list[str] = []
    u_komentaru = False
    u_kodu = False

    for broj, redak in enumerate(tekst.splitlines(), start=1):
        s = redak.strip()

        # HTML komentari: brojimo, ne čitamo kao tekst
        if u_komentaru:
            if "-->" in s:
                u_komentaru = False
            continue
        if s.startswith("<!--"):
            if not broj == 1 or "Generirano" not in s:
                profil.komentari += 1
                profil.nalazi.append(Nalaz(rel, broj, "K1", "komentar u izvoru", s[:80], "Ostatak uređivanja; premjesti u docs/radno/ ili ukloni."))
            u_komentaru = "-->" not in s
            continue

        if s.startswith("```"):
            u_kodu = not u_kodu
            continue
        if u_kodu:
            continue

        # Istaknuta matematika
        if u_jednadzbi:
            if s.startswith("$$"):
                u_jednadzbi = False
                provjeri_matematiku(profil, broj, " ".join(jednadzba))
                jednadzba = []
                if "{#eq-" in s:
                    profil.numerirane += 1
            else:
                jednadzba.append(s)
            continue
        if s.startswith("$$"):
            profil.jednadzbe += 1
            unutra = s[2:]
            if unutra.rstrip().endswith("$$") or re.search(r"\$\$\s*\{#eq-", unutra):
                provjeri_matematiku(profil, broj, unutra.split("$$")[0])
                if "{#eq-" in s:
                    profil.numerirane += 1
            else:
                u_jednadzbi = True
                jednadzba = [unutra]
            continue

        # Ograde blokova
        if FENCE_CLOSE_RE.match(s):
            if stog:
                stog.pop()
            continue
        m = FENCE_OPEN_RE.match(s)
        if m:
            rest = m.group("rest")
            naziv = ""
            for klasa, ime in BLOKOVI.items():
                if re.search(r"\." + re.escape(klasa) + r"(?![\w-])", rest):
                    naziv = ime
                    break
            if not naziv and "data-hint-key" in rest:
                naziv = "Naputak"
            if not naziv and "data-answer-key" in rest:
                naziv = "Kontrolni rezultat"
            stog.append(naziv)
            if naziv:
                profil.blokovi[naziv] += 1
            if naziv == "Riješeni primjer":
                profil.primjeri += 1
            continue

        if not s:
            continue

        # Naslovi
        h = HEADING_RE.match(s)
        if h:
            naslov = h.group("text")
            attrs = h.group("attrs") or ""
            if "#task-" in attrs:
                profil.zadatci += 1
            if len(h.group("hashes")) == 2:
                odjeljak = naslov
            vid = vidljivi_tekst(naslov)
            provjeri_tekst(profil, broj, vid)
            if vid.endswith("?") and not re.search(r"Zastani|Provjeri sebe", vid):
                profil.nalazi.append(Nalaz(rel, broj, "K4", "naslov kao pitanje", vid, "Izjavni naslov: imenuj temu ili problem."))
            continue

        # Slike
        im = IMAGE_RE.match(s)
        if im:
            cap = vidljivi_tekst(im.group("cap"))
            alt_m = FIG_ALT_RE.search(im.group("attrs") or "")
            alt = alt_m.group(1).strip() if alt_m else ""
            provjeri_tekst(profil, broj, cap + " " + alt)
            if cap and not cap.rstrip("”\")").endswith((".", "!", "?")):
                profil.nalazi.append(Nalaz(rel, broj, "K13", "potpis bez završne točke", cap[-60:], "Potpis je opisna rečenica s točkom."))
            if alt and cap and alt.rstrip(".") == cap.rstrip("."):
                profil.nalazi.append(Nalaz(rel, broj, "K13", "fig-alt jednak potpisu", alt[:60], "Alt opisuje što je nacrtano, potpis što slika pokazuje."))
            continue

        # Retci koji su HTML (tipke, QR, sidra) ili tablice: samo leksička provjera
        if s.startswith("<"):
            provjeri_tekst(profil, broj, vidljivi_tekst(s))
            continue
        if s.startswith("|"):
            if not re.fullmatch(r"[|:\-\s]+", s):
                provjeri_tekst(profil, broj, vidljivi_tekst(s))
                for fm in INLINE_MATH_RE.finditer(s):
                    provjeri_matematiku(profil, broj, fm.group(1))
            continue

        for fm in INLINE_MATH_RE.finditer(redak):
            provjeri_matematiku(profil, broj, fm.group(1))
        if 'class="mf1-box-label"' in s:
            provjeri_tekst(profil, broj, vidljivi_tekst(s))
            continue
        vid = vidljivi_tekst(redak)
        if not vid:
            continue
        provjeri_tekst(profil, broj, vid)
        if OZNAKA_POLJA_RE.match(redak):      # „**Tekst zadatka**”, „**Traži se**”
            continue
        proza = vidljivi_tekst(OZNAKA_POPISA_RE.sub("", UVODNA_GLAVA_RE.sub("", OZNAKA_POPISA_RE.sub("", redak))))
        blok = next((b for b in reversed(stog) if b), "tekst")
        # Za mjeru duljine broje se samo dovršene rečenice; uvodi u formulu
        # („odnosno”, „Uvrštavanjem brojeva dobiva se”) nastavljaju se u istaknutoj formuli.
        rec = [r for r in recenice(proza) if r.rstrip("”\")»").endswith((".", "!", "?", "…"))
               and re.search(r"[A-Za-zČĆŽŠĐčćžšđ]{2,}", r)]
        vid = proza
        profil.odlomci.append(Odlomak(broj, odjeljak, blok, vid, broj_rijeci(vid), rec))
        for r in rec:
            n = broj_rijeci(r)
            if n > DUGA_RECENICA:
                profil.nalazi.append(Nalaz(rel, broj, "K3", f"duga rečenica ({n} riječi)", r[:90] + "…", "Podijeli ako je teško pratiti tvrdnju."))

    return profil


# ---------------------------------------------------------------------------
# Ispis profila
# ---------------------------------------------------------------------------

def sazetak(profil: Profil) -> dict[str, object]:
    duljine = [broj_rijeci(r) for r in profil.sve_recenice]
    n = len(duljine)
    poredano = sorted(duljine)
    kat = Counter(nal.oznaka for nal in profil.nalazi if nal.oznaka != "K3")
    return {
        "datoteka": profil.datoteka,
        "oznaka": profil.oznaka,
        "rijeci": profil.rijeci,
        "recenice": n,
        "prosjek": round(sum(duljine) / n, 1) if n else 0.0,
        "medijan": poredano[n // 2] if n else 0,
        "udio_iznad_30": round(100 * sum(d > 30 for d in duljine) / n, 1) if n else 0.0,
        "duge": sum(d > DUGA_RECENICA for d in duljine),
        "jednadzbe": profil.jednadzbe,
        "numerirane": profil.numerirane,
        "primjeri": profil.primjeri,
        "zadatci": profil.zadatci,
        "granica_modela": profil.blokovi.get("Granica modela", 0),
        "cfd": profil.blokovi.get("CFD", 0),
        "nalazi": dict(sorted(kat.items(), key=lambda kv: int(kv[0][1:]))),
    }


def ispisi_profil(profili: list[Profil]) -> None:
    redovi = [sazetak(p) for p in profili]
    print("Profil teksta (vidljiva proza; bez istaknutih formula, tablica i HTML-a)\n")
    print(f"{'Pog.':>6} {'riječi':>7} {'reč.':>5} {'prosj.':>6} {'med.':>4} {'>30 %':>6} {'>40':>4} "
          f"{'jedn.':>5} {'num.':>5} {'P':>3} {'Z':>3} {'GM':>3} {'CFD':>4}  nalazi po pravilu")
    ukupno = Counter()
    for r in redovi:
        nal = " ".join(f"{k}:{v}" for k, v in r["nalazi"].items()) or "—"
        print(f"{r['oznaka']:>6} {r['rijeci']:>7} {r['recenice']:>5} {r['prosjek']:>6} {r['medijan']:>4} "
              f"{r['udio_iznad_30']:>6} {r['duge']:>4} {r['jednadzbe']:>5} {r['numerirane']:>5} "
              f"{r['primjeri']:>3} {r['zadatci']:>3} {r['granica_modela']:>3} {r['cfd']:>4}  {nal}")
        for k in ("rijeci", "recenice", "jednadzbe", "numerirane", "duge"):
            ukupno[k] += r[k]
    sve = [broj_rijeci(x) for p in profili for x in p.sve_recenice]
    if sve:
        print(f"\nUkupno: {ukupno['rijeci']} riječi, {ukupno['recenice']} rečenica, prosjek "
              f"{sum(sve) / len(sve):.1f} riječi po rečenici, {100 * sum(d > 30 for d in sve) / len(sve):.1f} % "
              f"rečenica iznad 30 riječi, {ukupno['duge']} iznad {DUGA_RECENICA}; "
              f"{ukupno['jednadzbe']} istaknutih formula, {ukupno['numerirane']} numeriranih.")
    print("\nP riješeni primjeri, Z zadatci za vježbu, GM blokovi „Granica modela”. "
          "Strogu strukturu provjerava tools/audit_publication.py; ovdje su brojke informativne.")
    print("Nalazi su upute za čitanje (docs/konvencije_pisanja.md); popis: --nalazi.")


def ispisi_nalaze(profili: list[Profil]) -> None:
    for p in profili:
        if not p.nalazi:
            continue
        print(f"\n## {p.datoteka} (pog. {p.oznaka}) — {len(p.nalazi)} nalaza")
        for nal in sorted(p.nalazi, key=lambda x: (int(x.oznaka[1:]), x.redak)):
            print(f"  {nal.oznaka:<4} r. {nal.redak:<5} {nal.kratko}: {nal.isjecak}")
            print(f"       → {nal.prijedlog}")


def ispisi_nacrt(profil: Profil) -> None:
    print(f"Obrnuti nacrt: {profil.datoteka} (pog. {profil.oznaka})")
    print("Za svaki odlomak upiši poantu i oznaku uloge (vidi skill recenzija-prirucnika, korak 3).\n")
    trenutni = None
    for o in profil.odlomci:
        if o.odjeljak != trenutni:
            trenutni = o.odjeljak
            rij = sum(x.rijeci for x in profil.odlomci if x.odjeljak == trenutni)
            print(f"\n### {trenutni}  ({rij} riječi)")
        prvi = o.recenice[0] if o.recenice else o.tekst
        print(f"  r. {o.redak:<5} [{o.blok}] {o.rijeci:>4} r.  {prvi[:110]}{'…' if len(prvi) > 110 else ''}")


# ---------------------------------------------------------------------------
# Provjera značenja nakon prerade
# ---------------------------------------------------------------------------

BROJ_RE = re.compile(r"(?<![\w#-])\d+(?:[.,]\d+)?(?![\w-])")
ID_RE = re.compile(r"#((?:eq|fig|ex|task|sec|tbl|cfd)-[\w-]+)")
CIT_RE = re.compile(r"(?<![\w-])@([A-Za-z][\w:-]+)")


def _za_usporedbu(tekst: str) -> str:
    s = re.sub(r"<!--.*?-->", " ", tekst, flags=re.S)
    s = s.replace("{,}", ",")
    return s


def _brojevi(tekst: str) -> Counter:
    s = URL_RE.sub(" ", tekst)
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r"\{[#.][^}]*\}", " ", s)
    s = re.sub(r"\.\./assets/\S+", " ", s)
    s = re.sub(r"\\(?:frac|tfrac|dfrac)\{1\}\{2\}", " ½ ", s)
    return Counter(m.group(0).replace(".", ",") for m in BROJ_RE.finditer(s))


def _recenice_izvora(tekst: str) -> list[str]:
    out: list[str] = []
    for redak in _za_usporedbu(tekst).splitlines():
        s = redak.strip()
        if not s or FENCE_CLOSE_RE.match(s) or FENCE_OPEN_RE.match(s) or s.startswith(("<", "|", "![")):
            continue
        s = re.sub(r"\{[#.][^}]*\}", " ", s)
        out.extend(recenice(s))
    return out


def _oznake(recenica: str) -> dict[str, Counter]:
    return {
        "brojevi": _brojevi(recenica),
        "nijekanje": Counter(m.group(0).lower() for m in NIJEKANJE.finditer(recenica)),
        "snaga": Counter(m.group(0).lower() for m in SNAGA.finditer(recenica)),
        "ograda": Counter(m.group(0).lower() for m in OGRADA.finditer(recenica)),
        "poredba": Counter(m.group(0).lower() for m in POREDBA.finditer(recenica)),
    }


def _razlika(a: Counter, b: Counter) -> tuple[list[str], list[str]]:
    return sorted((a - b).elements()), sorted((b - a).elements())


def usporedi(rev: str, putanje: list[Path]) -> int:
    ukupno_promjena = 0
    for path in putanje:
        rel = path.relative_to(ROOT).as_posix()
        try:
            staro = subprocess.run(["git", "show", f"{rev}:{rel}"], cwd=ROOT, capture_output=True,
                                   check=True).stdout.decode("utf-8")
        except subprocess.CalledProcessError:
            print(f"\n## {rel}: nema ga u {rev} (nova datoteka)")
            continue
        novo = path.read_text(encoding="utf-8")
        if staro == novo:
            continue
        ukupno_promjena += 1
        print(f"\n## {rel}")
        s_old, s_new = _za_usporedbu(staro), _za_usporedbu(novo)
        izg, dod = _razlika(_brojevi(s_old), _brojevi(s_new))
        print(f"  brojevi izgubljeni: {', '.join(izg) or '—'}")
        print(f"  brojevi dodani:     {', '.join(dod) or '—'}")
        for ime, uzorak in (("ID-jevi", ID_RE), ("citati", CIT_RE)):
            a = Counter(uzorak.findall(s_old)); b = Counter(uzorak.findall(s_new))
            i, d = _razlika(a, b)
            if i or d:
                print(f"  {ime}: izgubljeni {', '.join(i) or '—'}; dodani {', '.join(d) or '—'}")
        eq_old = len(re.findall(r"^\s*\$\$", staro, re.M)) // 2
        eq_new = len(re.findall(r"^\s*\$\$", novo, re.M)) // 2
        if eq_old != eq_new:
            print(f"  istaknute formule: {eq_old} → {eq_new}")

        stare = _recenice_izvora(staro); nove = _recenice_izvora(novo)
        skup_novih, skup_starih = set(nove), set(stare)
        uklonjene = [r for r in stare if r not in skup_novih]
        dodane = [r for r in nove if r not in skup_starih]
        iskoristene: set[int] = set()
        parovi = 0
        for r in uklonjene:
            o_r = _oznake(r)
            if not any(o_r.values()):
                continue
            najbolja, omjer = -1, 0.0
            for j, d in enumerate(dodane):
                q = difflib.SequenceMatcher(None, r, d).ratio()
                if q > omjer:
                    najbolja, omjer = j, q
            par = dodane[najbolja] if najbolja >= 0 and omjer >= 0.45 else None
            if par is not None:
                iskoristene.add(najbolja)
            o_d = _oznake(par) if par else {k: Counter() for k in o_r}
            promjene = []
            for k in ("brojevi", "nijekanje", "snaga", "ograda", "poredba"):
                i, d = _razlika(o_r[k], o_d[k])
                if i or d:
                    promjene.append(f"{k}: −[{', '.join(i)}] +[{', '.join(d)}]")
            if not promjene:
                continue
            parovi += 1
            print(f"\n  • STARO: {r[:220]}")
            print(f"    NOVO:  {par[:220] if par else '— nema bliske zamjene (rečenica uklonjena?) —'}")
            print(f"    promjena: {'; '.join(promjene)}")
        nove_tvrdnje = [d for j, d in enumerate(dodane) if j not in iskoristene
                        and (SNAGA.search(d) or _brojevi(d))]
        if nove_tvrdnje:
            print(f"\n  Dodane rečenice s brojem ili jakom tvrdnjom ({len(nove_tvrdnje)}):")
            for d in nove_tvrdnje[:40]:
                print(f"    + {d[:200]}")
        if not parovi and not nove_tvrdnje:
            print("  Nema promijenjenih rečenica s brojem, nijekanjem, ogradom ili poredbom.")
    if not ukupno_promjena:
        print(f"Nema razlika prema {rev} u odabranim izvorima.")
    print("\nAlat pokazuje gdje čitati; ne dokazuje da je značenje sačuvano. "
          "Pročitaj cijeli diff (git diff --word-diff).")
    return 0


# ---------------------------------------------------------------------------

def zadani_izvori() -> list[Path]:
    return sorted(SOURCE.glob("u[0-9][0-9]_*.md")) + sorted(SOURCE.glob("d[0-9][0-9]_*.md"))


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("izvori", nargs="*", type=Path, help="izvori u source/ (zadano: svi)")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--nalazi", action="store_true", help="ispiši svaki nalaz s retkom")
    g.add_argument("--nacrt", action="store_true", help="obrnuti nacrt po odjeljcima i odlomcima")
    g.add_argument("--usporedi", metavar="REV", help="provjera značenja prema Git reviziji")
    ap.add_argument("--json", action="store_true", help="strojni izlaz profila i nalaza")
    a = ap.parse_args(argv)

    putanje = [p if p.is_absolute() else (Path.cwd() / p) for p in a.izvori] or zadani_izvori()
    putanje = [p.resolve() for p in putanje]
    for p in putanje:
        if not p.exists():
            ap.error(f"nema datoteke: {p}")

    if a.usporedi:
        return usporedi(a.usporedi, putanje)

    profili = [analiziraj(p) for p in putanje]
    if a.json:
        json.dump({
            "profil": [sazetak(p) for p in profili],
            "nalazi": [nal.__dict__ for p in profili for nal in p.nalazi],
        }, sys.stdout, ensure_ascii=False, indent=1)
        print()
    elif a.nacrt:
        for p in profili:
            ispisi_nacrt(p)
    elif a.nalazi:
        ispisi_nalaze(profili)
    else:
        ispisi_profil(profili)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
