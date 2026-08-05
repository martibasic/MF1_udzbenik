# Protokol neovisne stručne recenzije

Ovaj dokument pretvara završnu stručnu provjeru u ponovljiv release-gate. Ne
predstavlja recenziju niti potpis autora; ispunjavaju ga dvije osobe koje nisu
provodile predmetnu reviziju rukopisa.

## Opseg i evidencija

Za svaku recenziju zabilježiti:

- oznaku izdanja, Git commit i datum preuzimanja artefakta;
- ime, ustanovu i stručnu ulogu recenzenta;
- pregledani HTML i PDF artefakt;
- svaki nalaz uz stabilni ID poglavlja, jednadžbe, primjera, zadatka ili slike;
- težinu nalaza: `P0` (pogrešan ili opasan zaključak), `P1` (znanstveno ili
  pedagoški bitna pogreška), `P2` (jasnoća, stil ili manji tehnički nedostatak).

## Recenzent mehanike fluida

Recenzent provjerava najmanje:

- konzistentnost sustava, osi, normala, referentnih tlakova i predznaka;
- očuvanje mase, energije, količine i momenta količine gibanja;
- pretpostavke materijalnog modela, steady/unsteady razliku i granične slučajeve;
- dimenzijsku homogenost te red veličine ključnih rezultata;
- znanstvenu opravdanost empirijskih pragova i lokalnih citata;
- podudaranje teksta, zadataka, odgovora, slika, notebookova i verifikatora.

## Primjenski recenzent

Odvojeni recenzent iz strojarstva ili brodogradnje provjerava najmanje:

- fizikalnu vjerodostojnost dimenzija, opterećenja i radnih točaka;
- jasno razdvajanje nastavnog modela od konstrukcijske, sigurnosne i normativne
  ocjene;
- primjerenost pomorskih, energetskih, procesnih i građevinskih primjera;
- čitljivost skica i mogućnost jednoznačnog postavljanja svakog zadatka.

## Odluka

Izdanje može prijeći iz release-candidate statusa u `v1.0` tek kada:

1. oba recenzenta potpišu svoju provjeru;
2. nema otvorenih nalaza `P0` ni `P1`;
3. svaki prihvaćeni ispravak ima zapis u `CHANGELOG.md` i, ako mijenja već
   objavljeni rezultat, u `docs/errata.md`;
4. nakon ispravaka ponovno prolazi cijeli automatizirani paket provjera.

Potpis uključuje ime, ulogu, datum, pregledani commit i izričitu odluku
`prihvaćeno`, `prihvaćeno uz ispravke` ili `nije prihvaćeno`.
