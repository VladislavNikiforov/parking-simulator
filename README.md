# Parking-simulator
University project on python which idea is to parse car models in real size and try to park them

#  Automašīnu parkošanas simulators
## Projekta uzdevums/ideja
 Šī programma ir domāta kā automašīnu parkošanas simulēšanas spēle, kas var būt noderīga gan izklaidējošām aktivitātēm, gan arī mācību nolūkiem. 
Šī programma ir domāta kā automašīnu parkošanas simulēšanas spēle, kas var būt noderīga gan izklaidējošām aktivitātēm, gan arī mācību nolūkiem. 
Šī ideja radās pec secinājuma, ka viena no grūtākām lietām, lai nokārtotu mašīnas braukšanas eksāmenu ir tieši parkošanās. 
Bieži cilvēks nav pieradis parkoties tieši ar eksāmena masīnas izmēriem, jo trenēšanas laikā parkojās ar cita izmēra mašīnām un tādejādi bieži eksāmenā kļūdās.
 Ar šo programmas palīdzību persona var ievadīt specifisku mašīnas modeli- pat to, kuru lieto eksāmena kārtošanas laikā. 
Persona var attīstīt parkošanas prasmi ar tieši eksāmena izmantoto mašīnu un rezultātā nekļūdīties parkošanā eksāmena laikā. 
Spēlētājs ir novietots virtuālā vidē, kur viņam jāvada automašīna un jāmēģina veiksmīgi ieparkoties uz noteiktajām parkošanas vietām.
 Spēles sākumā ir iespēja ievadīt specifisku mašīnas modeli un programma pati automātiski atradīs mašīnas izmērus, kas ir svarīgi priekš spēles spēlēšanas- vēlamie auto modeļi ir jāņem no izmantotās auto mājas lapas, un to nosaukumi jāievada pilnā apmērā, pretējā gadījumā programma nedarbosies. Kā arī ir iespēja ievadīt mašīnu skaita daudzumu, kuras jau būs aizņēmušas parkošanas vietas, kas arī ir svarīgi priekš spēles spēlēšanas.
Tad, kad dati ir ievadīti uz ekrāna parādās parkošanas stāvvieta, mašīnas, kuru skaits ir vienāds ar daudzumu, ko persona ievadīja un pati mašina, kuru var kontrolēt persona kura spēlē šo simulātoru. Ir vērts precizēt, ka programma neiesākas ātri un cilvēkam ir mazliet jāpagaida. Jo vairāk stāvošu automašīnu cilvēks ir norādījis, jo ilgāks laiks būs nepieciešams, lai programma tiktu iedarbināta.
Spēles uzdevums ir ieparkot precīzi mašīnu brīvajā parkošanas vietā nepieskaroties līnijām vai citām mašīnām.
Ļoti svarīga piezīme spēlētājam- ja avarējat, neuztraucieties, vienkārši ieslēdziet pārnesumu atpakaļgaitā un turiet nospiestu gāzi (poga W). 
Programma nodrošina lietotājiem iespēju izklaidēties, vienlaikus trenējot savas reakcijas un koordināciju. Šāds simulācijas rīks var būt noderīgs tiem, kuri vēlas uzlabot savas automašīnu parkošanas prasmes, sniedzot iespēju praktizēt bez reālas riska. 
Tāpat kā braukšanas skolās tiek izmantotas automašīnu simulācijas, šī programma var būt noderīgs līdzeklis transportlīdzekļu apmācībā un pārbaudē.
 Projekts izmanto Python programmēšanas valodu, un tāpēc to var izmantot kā resursu sākotnējām prasmēm izstrādātājiem, kas interesējas par spēļu izstrādi un vizualizāciju. 
Izstrādātāji var izmantot šo projektu kā piemēru Python valodā rakstītas spēles izveidei un attīstīt savas programmēšanas prasmes.

## Izmantotās bibliotēkas
1. pygame
Pygame ir bibliotēka Python valodā, kas piedāvā iespējas spēļu izstrādei un multimediju lietojumprogrammu veidošanai. 
Šajā projektā pygame tiek izmantots visaptveroši, nodrošinot spēles logiku, grafiku, un vadības atpazīšanu.
Detalizēts izmantojums:
Pygame ļauj izveidot spēles logiku un izstrādāt vizualizāciju, kā arī kontrolēt spēles notikumus un vadību.
Tieši šī bibliotēka nodrošina iespēju attēlot attēlus, animācijas un interaktīvus elementus uz ekrāna.
Pygame tiek izmantots automašīnu un parkošanas vietu attēlošanai, spēles notikumu apstrādei un lietotāja ievades uztveršanai (piemēram, taustiņu nospiešana).

2. selenium
selenium ir bibliotēka Python valodā, kas piedāvā automatizācijas iespējas darbā ar tīmekļa pārlūkiem. 
Tas ir īpaši noderīgs tīmekļa lietojumprogrammu testēšanai un datu iegūšanai no tīmekļa vietnēm.
Detalizēts izmantojums:
selenium tiek izmantots, lai automātiski apmeklētu tīmekļa vietni /"https://www.automobiledimension.com" un iegūtu informāciju par automašīnu izmēriem.
Ar šo bibliotēku tiek kontrolēts tīmekļa pārlūks (Chrome), un programmatiski tiek veiktas darbības, piemēram, noklusējuma iestatījumu maiņa vai elementu meklēšana pēc CSS selektoriem.
selenium nodrošina iespēju iegūt konkrētas informācijas vietnes elementu vērtības, kā arī navigēt starp lapām.

3. Math
math ir iebūvēta Python bibliotēka, kas piedāvā matemātiskās funkcijas un operācijas. Tā ir noderīga, veicot sarežģītus matemātiskus aprēķinus.
Detalizēts izmantojums:
math tiek izmantots, lai veiktu dažādus matemātiskus aprēķinus, kas saistīti ar automašīnas kustību un pagriezienu, piemēram, trigonometriskos aprēķinus un leņķu pārveidošanu.

4. os un random
os un random ir iebūvētas Python bibliotēkas, kas nodrošina funkcijas operēšanai ar operētājsistēmu un ģenerējot gadījuma skaitļus.
Detalizēts izmantojums:
os tiek izmantots, lai apstrādātu attēlus, konkrēti, lai izveidotu sarakstu ar automašīnu attēliem no noteiktā direktorijas (./cars).
random tiek izmantots, lai izvēlētos automašīnas attēlu gadījuma secībā, piedāvājot dažādu automašīnu vizuālo dažādību.

Šīs bibliotēkas kopā nodrošina plašu funkcionalitāti, lai izveidotu spēli ar interaktīvu lietotāja pieredzi un automatizētu datu iegūšanu no tīmekļa.
 Katra no tām sniedz savas unikālās iespējas, lai pilnveidotu projektu un nodrošinātu labu lietotāja pieredzi.

## Programmatūras izmantošanas metodes
Lai izmantotu šo programmatūru, ir nepieciešams Python v3.7 vai jaunāka versija, kā arī instalētas šīs bibliotēkas: pip install pygame; pip install selenium .

Progrāmmā ir daudz dažādas metodes, kuras tika izmantotas:

### Mantotāja Saskarsme:
Lietotājam ir nepieciešams izpildīt programmu, palaistot to no Python vides vai citiem atbilstošiem izpildes apstākļiem.
Programma iesāk ar lietotāja interaktīvu ievadu, kur lietotājs norāda vēlamās automašīnas skaitu un specifisku mašīnas modeli.

### Spēles Galvenā Logika:
Lietotājam ir jākontrolē virtuālā automašīna, izmantojot atslēgas W (paātrināšana), B (bremzēšana), Q (pagriešana pa kreisi) un E (pagriešana pa labi), R (braukšana aizmuguriski).
Galvenais mērķis ir izvairīties no sadursmēm ar citām automašīnām un veiksmīgi ieparkoties uz norādītajām parkošanas vietām.

### Parkošanas Vietu Izvietošana:
Programma izveido statisko vizuālo fonu, kas reprezentē parkošanas vietu izkārtojumu.
Parkošanas vietas tiek attēlotas kā griesti un iekrāsotas pelēkā krāsā, bet centrālais rāmis ir atstāts brīvs transportlīdzekļu kustībai.

### Automobiļu Kustība un Sadursmju Pārbaude:
Katrs automobilis (gan lietotāja vadītā, gan autonomais) tiek attēlots ar savu attēlu, kas tiek parādīts uz ekrāna, pārvietojoties pa parkošanas vietām.
Programma regulāri pārbauda sadursmes starp lietotāja vadīto automašīnu un citiem transportlīdzekļiem. Ja sadursme notiek, lietotāja vadītajai automašīnai tiek izslēgta kustība.

### Informācijas Parādīšana Uz Ekrāna:
Programma parāda informāciju par lietotāja vadīto automašīnu, tās ātrumu, stāvokli un režīmu (priekšējais vai aizmugurējais) uz ekrāna.
Lietotājam ir iespēja sekot līdzi šai informācijai, lai labāk saprastu automašīnas stāvokli un darbību.

### Automašīnu Izvietošana:
Programma automātiski izvēlas un izvieto automašīnas uz parkošanas vietām, piedāvājot izklaides iespējas lietotājam.
Gadījuma izvēle un izvietošana nodrošina atšķirīgu spēles pieredzi katru reizi, kad tiek palaidīta programma.

### Sadalīta izstrāde un Kļūdu Pārvaldība:
Programma ir sadalīta dažādos moduļos, katrs atbildēt par konkrētām funkcionalitātēm (piemēram, automašīnas vadība, datu iegūšana).
Izmantotas kļūdu apstrādes metodes un izņēmumi, lai nodrošinātu, ka programma var apstrādāt neparedzētas situācijas un kļūdas.
Šīs izmantotās metodes un funkcijas kopumā nodrošina lietotājam iespēju izbaudīt spēli, piedāvāt interaktīvu pieredzi un piedalīties virtuālajā parkošanas simulācijā, kurā var veicināt savas prasmes un izklaidēties.

## Programmas metodes
Pašā programmā ir izmantotas vairākas metodes, kas nodrošina programmas pareizu darbību un spēles loģiku. 
Šeit ir apskats par galvenajām metodēm un to funkcionalitāti:

### scrapParameters(autoFullName)
Šī metode tiek izmantota, lai iegūtu informāciju par automašīnas izmēriem, izmantojot tīmekļa skrapošanu ar selenium.
Pārlūks tiek konfigurēts ar webdriver.Chrome un tiek apmeklēta tīmekļa vietne "https://www.automobiledimension.com".
Automobiļa nosaukums tiek izmantots, lai izveidotu CSS selektoru, un pēc tam tiek iegūta informācija par automašīnas izmēriem.

### class Cars un class Player
Abas šīs klases piedāvā metodes draw un update, kas atbild par attēlošanu un stāvokļa atjaunošanu attiecīgi.
draw metode izmanto pygame bibliotēku, lai attēlotu automašīnas attēlu uz ekrāna.
update metode atjauno automašīnas stāvokli, tostarp tās atrašanās vietu un rotāciju.

### class ParkingScreen
Šī klase ir atbildīga par spēles vizuālo daļu, tostarp parkošanas vietu izveidi un attēlošanu uz ekrāna.
Metodes draw_parking_lot un create_cars veic attiecīgi parkošanas vietu izveidi un automašīnu izvietošanu uz ekrāna.

### main()
Galvenā izpildes metode, kas ir atbildīga par spēles pamata darbību.
Lietotājs tiek uzrunāts, lai ievadītu vēlamo automašīnu skaitu.
Tiek izveidots Player objekts, ievietots spēles vidē (ParkingScreen), un izveidotas autonomās automašīnas.
Notiek galvenais spēles cikls, kurā tiek atjauninātas un attēlotas automašīnas, pārbaudītas sadursmes un veiktas citas spēles darbības.

Daudz citas mazākas palīgmetodes un funkcijas
Piemēram, checkBorder, updateAlignment, updateAngleAndVelocity utt., kas nodrošina automašīnas pareizu kustību un reakciju uz lietotāja ievadi.

Šīs metodes kopā veido spēles loģiku, kontrolē automašīnas kustību, veic sadursmju pārbaudes un nodrošina pareizu attēlošanu uz ekrāna.
 Koda organizācija ar dažādām klasēm un metodēm palīdz uzturēt skaidrību un ērtu izstrādi.

