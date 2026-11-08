# Odgovor na recenziju

Kad Povjerenstvo zatraži izmjene prema mišljenju recenzenta, autorica ih
provodi u 90 dana, a recenzent u 60 dana pisano potvrđuje jesu li provedene
(čl. 12(3)–(4) Pravilnika, vidi [fesb_postupak.md](fesb_postupak.md)). Odgovor
zato mora recenzentu omogućiti da svaku primjedbu provjeri brzo.

## Postupak

1. Prepiši svaku primjedbu doslovno i daj joj broj (R1-3 = recenzent 1,
   primjedba 3). Primjedbu s više zahtjeva podijeli.
2. Za svaku zabilježi odluku autorice: **prihvaćeno**, **djelomično
   prihvaćeno** ili **nije prihvaćeno**. Odluku donosi autorica; agent
   predlaže i obrazlaže.
3. Prihvaćenu primjedbu provedi prema `AGENTS.md`: izvor u `source/`,
   generatori, verifikator, D06, skice, puni CI. Nakon izmjene napravi korak 6
   skilla (provjera značenja).
4. Za svaku primjedbu navedi gdje je izmjena u novom PDF-u (poglavlje,
   stranica, oznaka) i citiraj novi tekst ako je kratak.
5. Uz neprihvaćenu primjedbu napiši kratko stručno obrazloženje bez
   polemike: što djelo tvrdi, zašto je to ispravno ili namjerno, i što je
   eventualno pojašnjeno u tekstu da se nesporazum ne ponovi.
6. Ispravke koji mijenjaju već objavljeni rezultat zapiši u `CHANGELOG.md` i
   `docs/errata.md`.

## Oblik

| Br. | Primjedba (doslovno) | Odluka | Izmjena i mjesto u novoj verziji |
| --- | --- | --- | --- |
| R1-1 | | prihvaćeno | pog. 5, str. 112, Z2: … |

Na početku odgovora jedna rečenica zahvale recenzentu i oznaka verzije
(commit, datum PDF-a) na koju se odgovor odnosi. Bez ponavljanja primjedbi u
uvodu i bez općenitih obećanja.

## Nikad

- Ne tvrdi da je izmjena provedena ako nije u predanom PDF-u.
- Ne mijenjaj nepovezani sadržaj „usput” u verziji za recenzenta; svaka
  izmjena mora biti vidljiva u tablici.
- Ne piši odgovor u ime autorice bez njezine odluke o svakoj primjedbi.
