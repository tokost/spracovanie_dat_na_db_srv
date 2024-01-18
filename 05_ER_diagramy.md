>## Entitno-relačné diagramy – modelovanie entít a relácií 

Základ konceptuálneho modelovania relačných databáz je vyjadrenie modelov databáz pomocou grafických symbolov. Entitno-relačné diagramy (E-R diagramy) sa využívajú na modelovanie entít (Entities) a vzťahov (Relationships) pomocou príslušných grafických symbolov. K uvedeným dvom základným konštrukciám sa často pridáva tretia – atribút (Attribute). V tom prípade sa používa aj pomenovanie ERA diagram.   V E-R diagramoch entity vyjadrujú množiny entít (ich názvy sa uvádzajú v pluráli), atribúty vyjadrujú vlastnosti entít a relácie ich vzájomné vzťahy (spojenia). E-R diagramy opisujú entity, ktoré v modeli vystupujú a tiež ako spolu súvisia, avšak neobsahujú žiadne operácie, t. j. neopisujú, ako sa veci menia (napr. ako vznikajú a zanikajú).  Nevýhoda E-R diagramov je, že na ich vytváranie neexistuje jednotná (štandardná) notácia. Jedným z najznámejších a v súčasnosti ešte stále používaným formátom E-R diagramov je Chenov formát, ktorý zaviedol Peter Chen v roku 1976 so snahou o zjednotenie dovtedy používaných formátov. Jeho nevýhody eliminuje tzv. relačný formát diagramov, avšak ani jeho notácia nie je jednotná. 

### Chenov formát E-R diagramov 

V Chenovom formáte (Chenovej notácii) E-R diagramov sa označujú entity (alebo entitné množiny) symbolom obdĺžnik, na označenie ich atribútov sa používa symbol elipsa               a na znázornenie vzájomných vzťahov symbol kosoštvorec (Obr. 5.1 a Obr. 5.2). Podčiarknuté názvy atribútov v E-R diagrame zodpovedajú primárnym kľúčom.  Pri znázorňovaní relácií medzi entitami možno zobraziť aj počet výskytov jednej entity voči druhej v rámci ich vzájomného vzťahu, t. j. násobnosť (kardinalitu relácie (multiplicity)). Napríklad na diagrame na Obr. 5.2 je znázornený vzťah, v rámci ktorého osoba môže vlastniť M parciel, ale aj parcela môže mať N vlastníkov (vzťah typu M:N). 

![](./obrazky/erdiag01.png)

Násobnosť vzťahov najčastejšie vyjadruje jednu z nasledujúcich situácií (Obr. 5.3):



• MANY - MANY (M - M); napr. osoba môže vlastniť viac parciel, ale aj parcela môže mať viac vlastníkov, vzťah M:N

• MANY - ONE (M - O); napr. katastrálne územie obsahuje viac parciel, ale parcela patrí len do jedného katastrálneho územia, vzťah 1:N, 

• ONE - ONE (O - O); napr. fyzická osoba má práve jedno rodné číslo a zároveň rodné číslo patrí práve jednej fyzickej osobe, vzťah 1:1. 

![](./obrazky/erdiag02.png)

Ďalšie možnosti znázornenia násobnosti relácií znázornené na Obr. 5.3 odpovedajú situáciám, v ktorých relácia môže, ale nemusí mať zastúpenie vo vzťahu (napr. osoba vlastní nula alebo viac budov). Ide o tzv. povinné alebo nepovinné členstvo vo vzťahu. 

### Relačný formát diagramov

Chenov formát diagramov je pri zložitých modeloch nevyhovujúci, pretože jeho grafické symboly sú priestorovo veľmi rozsiahle. Množstvo atribútov potom robí model nečitateľným a z pohľadu priestoru neefektívnym. Z uvedeného dôvodu bol neskôr vyvinutý tzv. relačný formát diagramov. Upravené E-R diagramy (relačný formát) využívajú zápis atribútov priamo do symbolov entít a tým zároveň umožňujú presnejšie špecifikovať ich atribúty napr. označením primárnych a cudzích kľúčov a definovaním ich dátového typu alebo domény. Nevýhodou relačného formátu znázornenia je, že syntax symbolov sa v jednotlivých spôsoboch vyjadrenia diagramov líši, čo platí aj o softvéroch na ich vytváranie. Príklad relačného formátu diagramu vytvoreného v rôznych softvérových prostrediach je uvedený na Obr. 5.4.  

Všeobecné vlastnosti E-R diagramov v relačnom formáte možno charakterizovať nasledovne: 

• entity (entitné množiny) reprezentujú obdĺžniky a ich atribúty sú textovo opísané vo vnútri týchto obdĺžnikov, 

• násobnosť (kardinalita) vzťahov môže byť vyjadrená symbolmi prevzatými z E-R diagramov (Obr. 5.4a), ale napr. aj symbolmi 1 a ∞ (Obr. 5.4b) alebo šípkami, ktoré smerujú od entitnej množiny s hodnotou MANY (viac) k entitnej množine s hodnotou ONE (jeden) (Obr. 5.4c). 

• primárny kľúč je označený skratkou „PK“ (Primary Key) pri názve atribútu, prípadne tučným alebo podčiarknutým písmom, 

• cudzí kľúč je označený skratkou „FK“ (Foreign Key) pri názve atribútu. 

![](./obrazky/erdiag03.png)
