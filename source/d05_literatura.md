## Literatura i izvori

Citat uz tvrdnju upućuje na izvor modela, podatka ili područja valjanosti. Za daljnje učenje izvori su ovdje razvrstani po temama.

## Temelji i integralne bilance

Za opći uvodni kolegij te za hidrostatiku, kontrolne volumene, Bernoullijevu jednadžbu i cjevovode korisni su White [@white2011], Munson i suradnici [@munson2009] te Çengel i Cimbala [@cengel2014]. Streeter, Wylie i Bedford [@streeter] daju klasičan inženjerski prikaz, a Virag [@virag] dodatni oslonac na hrvatskom jeziku.

## Kompresibilni, viskozni i turbulentni tok

Kompresibilni idealni tok, sapnice i udarni valovi u poglavlju 9 slijede standardni prikaz Andersona [@anderson2021]. Gradivo o graničnom sloju i odvajanju iz poglavlja 12 može se produbiti uz Schlichtinga i Gerstena [@schlichting2017], a o turbulenciji uz Popea [@pope2000].

## Cjevovodi i otvoreni tokovi

Moodyjev dijagram potječe iz rada [@moody1944], a implicitna veza za turbulentni koeficijent trenja iz rada [@colebrook1939]. Za otvorene tokove, specifičnu energiju, postupno promjenjiv tok i hidraulički skok referentni je izvor Chow [@chow1959]. Empirijske koeficijente uvijek treba uzeti iz izvora koji odgovara geometriji, hrapavosti i rasponu Reynoldsova broja konkretnog problema.

## Brodogradnja, stabilitet i modelska ispitivanja

Analiza početnog stabiliteta preko metacentarske visine u poglavlju 6 nastavni je model i ne zamjenjuje obveznu provjeru intaktnog ili oštećenog stabiliteta. Za kriterije intaktnog stabiliteta mjerodavan je IMO-ov IS Code [@imo-is-code-2008], a za aktualni okvir oštećenog stabiliteta i zahtjeve konvencije SOLAS IMO-ova dokumentacija [@imo-damage-stability]. Modelska ispitivanja, analizu nesigurnosti i ekstrapolaciju treba provoditi prema odgovarajućem aktualnom postupku ITTC-a [@ittc].

## Numerička mehanika fluida

Prijelaz od zakona očuvanja do metode konačnih volumena, rubnih uvjeta i turbulencijskih modela pokriva otvoreno dostupna knjiga Greenshieldsa i Wellera [@greenshieldsweller2022]. CFD odlomci u poglavljima kratko primjenjuju tu vezu. Definiciju izdvojenog hidrostatičkog tlaka ilustrira dokumentacija OpenFOAM-a [@openfoam-hydrostatic], a vezu rubnih podataka sa širenjem poremećaja NASA-in vodič za Wind-US [@nasa-wind-boundaries].

U dodatku D pojmovi verifikacije i validacije slijede NASA-in vodič [@nasa-cfd-vv] i ASME V&V 20 [@asme-vv20-2009]. Nastavni skup podataka za aeroprofil povezuje Ladsonov eksperiment [@ladson1988] s referentnim slučajem NASA TMR [@nasa-tmr-naca0012]. Mjerenja strujanja iza stepenice Drivera i Seegmillera [@driver-seegmiller1985] te objavljeni CFD rezultati [@tmr-backstep] omogućuju izravnu usporedbu u primjeru [-@ex-stepenica-mjerenje-cfd]. Postotno slaganje bez procjene eksperimentalne, iteracijske, diskretizacijske i modelske nesigurnosti nije opći kriterij valjanosti.

::: {.mf1-mini-summary}
<p class="mf1-box-label">Pravilo korištenja izvora</p>

Priručnik je dovoljan za praćenje kolegija, ali svojstva fluida, empirijski koeficijenti, normativni kriteriji i softverski postupci moraju se provjeriti u izdanju izvora koje odgovara godini i namjeni projekta.
:::

## Bibliografski zapisi

::: {#refs}
:::
