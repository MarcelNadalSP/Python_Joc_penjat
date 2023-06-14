#Aquest és el Joc del Penjat d'en Marcel Nadal. Fet per a l'assignatura de PTD I. 
import sys

color = sys.stdout.shell #assigna color com funció (necessari per a posar text de colors)

Historial = {}
Valors = {}
Preguntes = {}
Partides,Millor = 0,0
FiFinal = False

#opertura de variables no reiniciades a cada partida

Valors = {
    #fàcil
    1:"Quina és la classe de programació?",
    2:"Quin és l'apòstol que dona nom al col·legi?",
    3:"Quin és el nom del professor de Robòtica?",
    4:"A quina hora comencen les classes a l'escola?",
    5:"Com s'anomena aquest llenguatge de programació?",
    6:"Quina és l'aula de robòtica?",
    7:"Quantes taules hi ha a l'aula de robòtica?",
    8:"Quines són les sigles que donen nom a l'actual llei d'educació?",
    9:"A quin pis es troben les aules de batxillerat?",
    10:"Quantes línies hi ha de batxillerat a l'escola?",
    11:"Quants de banys hi ha al pis de batxillerat?",
    12:"Quantes classes hi ha d'ESO?",
    13:"Quants alumnes caben a l'aula Gal·làxia 3.1?",
    14:"Quantes hores de PTD hi ha per setmana?",
    15:"Quin és el nom habitual del dispositiu que ens dona connexió Wi-fi a casa?",
    16:"Quines són les sigles de \"Programació i Tractament de Dades\"?",
    17:"Quina és la primera funció que s'ensenya a Python?",
    18:"Quina és la primera frase que s'escriu en aprendre un nou llenguatge de programació?",
    19:"En quin idioma es dona l'assignatura de Programació i Tractament de Dades?",
    20:"Quina és la màxima nota obtenible al sistema educatiu espanyol?",
    #mitjà
    21:"Quina classe té com a aula principal la C21?",
    22:"Quants punts donava la missió M10 - Central Elèctrica com a màxim?",
    23:"Segueix la frase: Sense maqueta no sortireu...",
    24:"Quina és la nova modalitat de batxillerat introduïda aquest curs?",
    25:"Quina empresa dona a l'escola els dominis per a pàgines web com la de Robosapiens?",
    26:"Quin any va començar la robòtica a l'escola?",
    27:"Quina funció s'ha d'importar per fer un cronòmetre a Python?",
    28:"Anomena un llenguatge de programació amb un nom d'una sola lletra:",
    29:"De quin país ve en Carlos Bayés?",
    30:"A quin carrer es troba l'escola?",
    31:"Quina és la nacionalitat de'n David Guetta?",
    32:"Quina ha estat la seu de la darrera FLL Gran Final Nacional?",
    33:"Quina coneguda web de pel·lícules i sèries en \"streaming\" ha estat programada amb Python?",
    34:"Quin tipus d'ordinadors s'empren a l'hora de PTD?",
    35:"Anomena un sistema operatiu per a ordinadors de codi obert:",
    36:"Què s'ha de fer abans de crear un programa informàtic?", 
    37:"Quin és el nom de la temporada actual de FLL (sense espais)?",
    38:"On va ser la primera nacional que hi va participar l'escola?",
    39:"Com és el nom de la solució innovadora de Robosapiens Superpowered?",
    40:"Quin és l'element característic que porten els equips als estands a les FLL Gran Final Nacional?", 
    #difícil
    41:"Quin és el nom de la temporada 2018-2019 de FLL?",
    42:"Quin element vam passar per l'aeroport d'una manera poc legítima?",
    43:"Quina funció s'ha d'importar per fer \"randoms\" a Python?",
    44:"Com es refereixen els alumnes a l'assignatura de Programació i Tractament de Dades?",
    45:"Quina és la beguda preferida de'n Mateo i que és molt dolenta?",
    46:"Quina ha estat l'única temporada des dels inicis de la FLL a l'escola que no s'hi ha participat (nom)?",
    47:"Com és conegut el robot de l'equip Robosapiens Superpowered?",
    48:"A quina temporada van coincidir Robosapiens i ICASP (nom)?",
    49:"Com en Joan Rotger anomena a les pistoles de silicona?", 
    50:"Com estava en Marcel a la seva primera FLL Gran Final presencial?", 
    51:"Quina és la tecnologia en què es basava el projecte d'ICASP el 2020 i va investigar Robosapiens pel 2023?", 
    52:"Quin és el contacte de Robosapiens que va introduir l'hidrogen?",
    53:"Quina és la fase mai obtinguda fins ara per cap equip de l'escola a la FLL?", 
    54:"Com s'anomena el nou model de brick de robots lego", 
    55:"De quin material estan fetes les bateries dels dispositius mòbils actuals?", 
    56:"Quin element de la part de Valors FIRST® es va retirar després de City Shaper?", 
    57:"Quin concepte es va introduir a la temporada City Shaper a la taula del robot?", 
    58:"Quin és el nom del color oficial de Robosapiens?", 
    59:"Quin alumne present ara a PTD formava part del Robosapiens original (nom i cognom)?", 
    60:"Quina és la localitat de procedència de'n Pep Garau?", 
    61:"Quina és la localitat més lletja de tota Mallorca?", 
    62:"Quina és la segona localitat més lletja de tota Mallorca?", 
    63:"Què hi ha per fer a Múrcia?", 
    64:"Quin era el col·laborador principal que donava nom al Premi al Guanyador fins al 2021?", 
    65:"És possible fer tots els punts en els 2:30 min de la ronda del robot?", 
    66:"Qui va guanyar en l'únic enfrontament directe entre Robosapiens i ICASP a un torneig classificatori?", 
    67:"A quina categoria ICASP va guanyar un 2n premi a la Gran Final Nacional 2018?", 
    68:"La presència d'un ... a la nostra habitació va destorbar en Monserrat i el va treure", 
    69:"El 1r Premi als Valors FIRST donava la classificació a la internacional celebrada a..:", 
    70:"Quina és la distribució de teclats més comú a Espanya?", 
    71:"Quina enginyeria s'ha d'estodiar per treballar a la F1?", 
    72:"Quants nivells té aquest joc?", 
    73:"Quin element de Robosapiens va quedar a l'escola pel viatge a la FLL Gran Final Nacional?", 
    74:"Quin càrrec de l'ajuntament ha vingut 2 vegades a l'escola en les darreres 3 temporades?",
    75:"Quina és la data d'entrega d'aquest joc (dd/mm)?", 
    #extrem
    76:"Quants punts màxims es podien fer a la temporada 2018-2019 de FLL: Into Orbit?",
    77:"Quants d'anys té la flauta de'n Damià, de primària?",
    78:"Quin dia va ser la primera competició de FLL de l'escola local (dd/mm/aaaa)?",
    79:"Com és coneguda Marta Pons pels membres de Robosapiens?", 
    80:"Amb quina part de Palma es pot comparar Torremolinos? (Sense article salat)",
    81:"De quina localitat navarra ve l'equip FSIngenium?",
    82:"Quin va ser el màxim de punts obtingut a Cargo Connect per un equip espanyol?",
    83:"Aproximant a les desenes de millar, quina és la superfície de l'escola?",
    84:"El Spike Prime incorpora quantes possibles lectures de girosensor?",
    85:"Amb quin paràmetre estava relacionat el primer problema amb el robot que va sorgir a la FLL Gran Final Nacional?",
    86:"Quina és la duració en hores aproximada d'una FLL Gran Final Nacional?",
    87:"Quants de punts van servir per guanyar el joc del robot a la FLL Hidrodinamics local?",
    88:"Amb quin software es programen actualment els robots Mindstorms EV3 a l'escola?", 
    89:"Què signifiquen les sigles FIRST?", 
    90:"A quin mes es llancen les noves temporades de FLL?",
    91:"Quina va ser la primera temporada on la FLL va tenir lloc a Balears?", 
    92:"Quin és el nom de les connexions proporcionades per la FLL per assegurar les missions?", 
    93:"Quina va ser la primera temporada que va introduir una missió de \"batalla\" entre dos equips?",
    94:"Quina era l'empresa que regentava abans la que és ara la central d'hidrogen de Lloseta?", 
    95:"Quina era l'entitat organitzadora de la I Jornada de Transició Energètica de les Illes Balears?",
    96:"Quina va ser la primera comunitat autònoma d'Espanya on es va celebrar la FLL?", 
    97:"Quina va ser la pitjor puntuació de Robosapiens a la FLL Gran Final Nacional Superpowered?", 
    98:"Quin és el meu gènere musical preferit?", 
    99:"Quin fitxatge per a Robosapiens Superpowered va ser un fracàs i s'ha convertit en broma?", 
    100:"Quina és la quantitat monetària en € que demanàvem a les empreses que visitàvem?", 
    101:"Construint amb Enginy és una olimpiada en l'...", 
    102:"A quin torneig classificatori participa l'equip FSIngenium?",
    103:"Quina és la fundació que suporta els equips Legotronic Beavers, Robotronic Bulls i Electronic Falcons?",
    104:"De quina professora és un fill apassionat per la Robòtica i Robosapiens (nom)?", 
    105:"Quin premi va guanyar Robosapiens a RoboticACTS?", 
    106:"Quina era l'anterior nomenclatura per al Projecte d'Innovació?", 
    107:"Com s'anomena la zona de pràctiques del joc del robot als tornejos FLL presencials?", 
    108:"Quin és el temps en minuts post-presentació que tenen estipulat els jutges per discutir les puntuacions?", 
    109:"Abans de City Shaper, què passava quan es tocava el robot fora de la base (verb infinitiu i nom)?",
    110:"A quin edifici del Parc Bit es troben les oficines de Wireless DNA?", 
    111:"Com s'anomenava el robot de Robosapiens a la temporada Cargo Connect?", 
    112:"Robosapiens és millor que quin equip?", 
    113:"D'on venen les sigles ICASP?", 
    114:"Quants alumnes formaven part d'ICASP a la seva primera temporada?", 
    115:"Amb quin equip José Arambarri va guanyar el Primer Premi al Disseny del Robot a la FLL Gran Final Online City Shaper?", 
    116:"Quin alumne de PTD també és de Santa Maria (nom)?", 
    117:"Quin va ser el resultat del partit on el Mallorca va aconseguir la salvació la temporada 2021-2022 (x a y)?",
    118:"Quin nom té la competició de FLL internacional celebrada a Arkansas?", 
    119:"Què va fer en Mateo a la classe de PTD del divendres 31/03?", 
    120:"Quin és el país actualment amb millors resultats a les competicions FLL Internacionals?", 
} #nombre de la llista-pregunta

#Es fan dos diccionaris: un nombre-pregunta i l'altre pregunta-resposta. En el primer entra un nombre aleatori i treu una pregunta i
#del segon a partir de la pregunta treu la resposta. Sinó, no es podria fer aleatori ja que els diccionaris no estan indexats.

Preguntes = {
    #fàcil
    "Quina és la classe de programació?":"C21",
    "Quin és l'apòstol que dona nom al col·legi?":"Sant Pere",
    "Quin és el nom del professor de Robòtica?":"Monserrat",
    "A quina hora comencen les classes a l'escola?":"8",
    "Com s'anomena aquest llenguatge de programació?":"Python",
    "Quina és l'aula de robòtica?":"C20",
    "Quantes taules hi ha a l'aula de robòtica?":"4",
    "Quines són les sigles que donen nom a l'actual llei d'educació?":"LOMLOE",
    "A quin pis es troben les aules de batxillerat?":"1r",
    "Quantes línies hi ha de batxillerat a l'escola?":"5",
    "Quants de banys hi ha al pis de batxillerat?":"2",
    "Quantes classes hi ha d'ESO?":"12",
    "Quants alumnes caben a l'aula Gal·làxia 3.1?":"90",
    "Quantes hores de PTD hi ha per setmana?":"3",
    "Quin és el nom habitual del dispositiu que ens dona connexió Wi-fi a casa?":"Router",
    "Quines són les sigles de \"Programació i Tractament de Dades\"?":"PTD",
    "Quina és la primera funció que s'ensenya a Python?":"Print",
    "Quina és la primera frase que s'escriu en aprendre un nou llenguatge de programació?":"Hola món",
    "En quin idioma es dona l'assignatura de Programació i Tractament de Dades?":"Català",
    "Quina és la màxima nota obtenible al sistema educatiu espanyol?":"10",
    #mitjà
    "Quina classe té com a aula principal la C21?":"1E",
    "Quants punts donava la missió M10 - Central Elèctrica com a màxim?":"25",
    "Segueix la frase: Sense maqueta no sortireu...":"Ni de ca vostra",
    "Quina és la nova modalitat de batxillerat introduïda aquest curs?":"General",
    "Quina empresa dona a l'escola els dominis per a pàgines web com la de Robosapiens?":"Dinahosting",
    "Quin any va començar la robòtica a l'escola?":"2017",
    "Quina funció s'ha d'importar per fer un cronòmetre a Python?":"Time",
    "Anomena un llenguatge de programació amb un nom d'una sola lletra:":"C",
    "De quin país ve en Carlos Bayés?":"Cuba",
    "A quin carrer es troba l'escola?":"Baltasar Valentí",
    "Quina és la nacionalitat de'n David Guetta?":"Francesa",
    "Quina ha estat la seu de la darrera FLL Gran Final Nacional?":"Cartagena",
    "Quina coneguda web de pel·lícules i sèries en \"streaming\" ha estat programada amb Python?":"Netflix",
    "Quin tipus d'ordinadors s'empren a l'hora de PTD?":"Chromebook",
    "Anomena un sistema operatiu per a ordinadors de codi obert:":"Linux",
    "Què s'ha de fer abans de crear un programa informàtic?":"Diagrama de flux de control",
    "Quin és el nom de la temporada actual de FLL (sense espais)?":"Superpowered",
    "On va ser la primera nacional que hi va participar l'escola?":"Logronyo",
    "Com és el nom de la solució innovadora de Robosapiens Superpowered?":"H2Vault",
    "Quin és l'element característic que porten els equips als estands a les FLL Gran Final Nacional?":"Xapes",
    #difícil
    "Quin és el nom de la temporada 2018-2019 de FLL?":"Into orbit",
    "Quin element vam passar per l'aeroport d'una manera poc legítima?":"El Tub",
    "Quina funció s'ha d'importar per fer \"randoms\" a Python?":"Random",
    "Com es refereixen els alumnes a l'assignatura de Programació i Tractament de Dades?":"Tic",
    "Quina és la beguda preferida de'n Mateo i que és molt dolenta?":"Monster",
    "Quina ha estat l'única temporada des dels inicis de la FLL a l'escola que no s'hi ha participat (nom)?":"Replay",
    "Com és conegut el robot de l'equip Robosapiens Superpowered?":"Rabot",
    "A quina temporada van coincidir Robosapiens i ICASP (nom)?":"City shaper",
    "Com en Joan Rotger anomena a les pistoles de silicona?":"Pistola termofusible",
    "Com estava en Marcel a la seva primera FLL Gran Final presencial?":"Coix",
    "Quina és la tecnologia en què es basava el projecte d'ICASP el 2020 i va investigar Robosapiens pel 2023?":"Harvesting",
    "Quin és el contacte de Robosapiens que va introduir l'hidrogen?":"Marta Pons",
    "Quina és la fase mai obtinguda fins ara per cap equip de l'escola a la FLL?":"Internacional",
    "Com s'anomena el nou model de brick de robots lego":"Spike prime",
    "De quin material estan fetes les bateries dels dispositius mòbils actuals?":"Liti",
    "Quin element de la part de Valors FIRST® es va retirar després de City Shaper?":"Poster de valors",
    "Quin concepte es va introduir a la temporada City Shaper a la taula del robot?":"Inspecció menor",
    "Quin és el nom del color oficial de Robosapiens?":"Rojo vino 405",
    "Quin alumne present ara a PTD formava part del Robosapiens original (nom i cognom)?":"Alberto Coba",
    "Quina és la localitat de procedència de'n Pep Garau?":"Santa Maria",
    "Quina és la localitat més lletja de tota Mallorca?":"Inca",
    "Quina és la segona localitat més lletja de tota Mallorca?":"Sa Pobla",
    "Què hi ha per fer a Múrcia?":"Res",
    "Quin era el col·laborador principal que donava nom al Premi al Guanyador fins al 2021?":"Fundació Scientia",
    "És possible fer tots els punts en els 2:30 min de la ronda del robot?":"Sí",
    "Qui va guanyar en l'únic enfrontament directe entre Robosapiens i ICASP a un torneig classificatori?":"Robosapiens",
    "A quina categoria ICASP va guanyar un 2n premi a la Gran Final Nacional 2018?":"Disseny mecànic",
    "La presència d'un ... a la nostra habitació va destorbar en Monserrat i el va treure":"Vasc",
    "El 1r Premi als Valors FIRST donava la classificació a la internacional celebrada a..:":"Marrakech",
    "Quina és la distribució de teclats més comú a Espanya?":"Qwerty",
    "Quina enginyeria s'ha d'estodiar per treballar a la F1?":"Enginyeria aeroespacial",
    "Quants nivells té aquest joc?":"4",
    "Quin element de Robosapiens va quedar a l'escola pel viatge a la FLL Gran Final Nacional?":"Disfressa lego",
    "Quin càrrec de l'ajuntament ha vingut 2 vegades a l'escola en les darreres 3 temporades?":"Ramon Perpinyà",
    "Quina és la data d'entrega d'aquest joc (dd/mm)?":"16/04",
    #extrem
    "Quants punts màxims es podien fer a la temporada 2018-2019 de FLL: Into Orbit?":"400",
    "Quants d'anys té la flauta de'n Damià, de primària?":"38",
    "Quin dia va ser la primera competició de FLL de l'escola local (dd/mm/aaaa)?":"17/02/2018",
    "Com és coneguda Marta Pons pels membres de Robosapiens?":"La amiguita de Marcel",
    "Amb quina part de Palma es pot comparar Torremolinos? (Sense article salat)":"Arenal",
    "De quina localitat navarra ve l'equip FSIngenium?":"Sagurrien",
    "Quin va ser el màxim de punts obtingut a Cargo Connect per un equip espanyol?":"710",
    "Aproximant a les desenes de millar, quina és la superfície de l'escola?":"60000",
    "El Spike Prime incorpora quantes possibles lectures de girosensor?":"3",
    "Amb quin paràmetre estava relacionat el primer problema amb el robot que va sorgir a la FLL Gran Final Nacional?":"Rotacions",
    "Quina és la duració en hores aproximada d'una FLL Gran Final Nacional?":"12",
    "Quants de punts van servir per guanyar el joc del robot a la FLL Hidrodinamics local?":"155",
    "Amb quin software es programen actualment els robots Mindstorms EV3 a l'escola?":"Lego mindstorms education",
    "Què signifiquen les sigles FIRST?":"For inspiration and recognition of science and technology",
    "A quin mes es llancen les noves temporades de FLL?":"Agost",
    "Quina va ser la primera temporada on la FLL va tenir lloc a Balears?":"Animal allies",
    "Quin és el nom de les connexions proporcionades per la FLL per assegurar les missions?":"Dual lock",
    "Quina va ser la primera temporada que va introduir una missió de \"batalla\" entre dos equips?":"City shaper",
    "Quina era l'empresa que regentava abans la que és ara la central d'hidrogen de Lloseta?":"Cemex",
    "Quina era l'entitat organitzadora de la I Jornada de Transició Energètica de les Illes Balears?":"Cluster TEIB",
    "Quina va ser la primera comunitat autònoma d'Espanya on es va celebrar la FLL?":"Catalunya",
    "Quina va ser la pitjor puntuació de Robosapiens a la FLL Gran Final Nacional Superpowered?":"170",
    "Quin és el meu gènere musical preferit?":"Música electrònica",
    "Quin fitxatge per a Robosapiens Superpowered va ser un fracàs i s'ha convertit en broma?":"Alex",
    "Quina és la quantitat monetària en € que demanàvem a les empreses que visitàvem?":"5000",
    "Construint amb Enginy és una olimpiada en l'...":"Edificació",
    "A quin torneig classificatori participa l'equip FSIngenium?":"Madrid UPM",
    "Quina és la fundació que suporta els equips Legotronic Beavers, Robotronic Bulls i Electronic Falcons?":"MTorres",
    "De quina professora és un fill apassionat per la Robòtica i Robosapiens (nom)?":"Joana",
    "Quin premi va guanyar Robosapiens a RoboticACTS?":"Millor execució de les proves de camp",
    "Quina era l'anterior nomenclatura per al Projecte d'Innovació?":"Projecte científic",
    "Com s'anomena la zona de pràctiques del joc del robot als tornejos FLL presencials?":"Pit",
    "Quin és el temps en minuts post-presentació que tenen estipulat els jutges per discutir les puntuacions?":"10",
    "Abans de City Shaper, què passava quan es tocava el robot fora de la base (verb infinitiu i nom)?":"Restar punts",
    "A quin edifici del Parc Bit es troben les oficines de Wireless DNA?":"Lleret",
    "Com s'anomenava el robot de Robosapiens a la temporada Cargo Connect?":"Botijo",
    "Robosapiens és millor que quin equip?":"ICASP",
    "D'on venen les sigles ICASP?":"Ingenieros científicos alumnos del sant pere",
    "Quants alumnes formaven part d'ICASP a la seva primera temporada?":"10",
    "Amb quin equip José Arambarri va guanyar el Primer Premi al Disseny del Robot a la FLL Gran Final Online City Shaper?":"Construcciones y demoliciones", 
    "Quin alumne de PTD també és de Santa Maria (nom)?":"Manel",
    "Quin va ser el resultat del partit on el Mallorca va aconseguir la salvació la temporada 2021-2022 (x a y)?":"0 a 2",
    "Quin nom té la competició de FLL internacional celebrada a Arkansas?":"Razorback",
    "Què va fer en Mateo a la classe de PTD del divendres 31/03?":"Dormir",
    "Quin és el país actualment amb millors resultats a les competicions FLL Internacionals?":"Espanya",
} #pregunta-resposta


while FiFinal == False: #bucle partides

    Partides += 1
    Correctes,Ttotal,Intents,Vp,Punts,Puntp,Tf,Tp,Ti,segons,Temps,Inici1,Vt,Vd,Ratxa,Vr,PNivell,minuts,hores,FinalIn,Jugades,Difp,Nivell,PTotals= 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 #assignacions0
    Vides = 7 #vides per defecte
    Nom = "n/a" #nom per defecte
    Dif = "n/a" #dificultat per defecte
    TipusP = "n/a" #partida llarga/curta
    #imports
    import time
    import random
    #obertura de variables
    Temps_R = {} 
    Llista = []

    Correctes #Respostes correctes (int)
    Ttotal #temps total a totes les preguntes (float)
    Intents #Total de respostes (int)
    Vp #Valor de punts d'una pregunta segons el nivell (int)
    Punts #Punts del jugador (int)
    Ti, Tf #Moment del llançament d'una pregunta i de la resposta. Serveix per fer un cronòmetre (int)
    Tp #Temps emprat per respondre una pregunta (int)
    segons #comptador de segons emprat per donar format a Temps (str)
    minuts #comptador de minuts emprat per donar format a Temps (str)
    hores #comptador d'hores emprat per donar format a Temps (str)
    Temps #Temps total en format de cronòmetre hores-minuts-segons (str)
    Inici1 #Emmagatzemador d'inici o no del joc (boolean)
    Vt #Valor de puntuació d'una pregunta en relació al temps tardat (int)
    Vd #Valor de puntuació d'una pregunta en relació a la dificultat (int)
    Vr #Valor de puntuació d'una pregunta en relació a la ratxa d'encerts (int)
    Ratxa #Comptador de ratxa d'encerts (int)
    PNivell #Valor de respostes correctes a partir del que es puja el nivell de dificultat. (int)
    #Es separa de Correctes per poder anar des de l'inici del joc a un nivell concret sense sortir com a encertades totes les preguntes anteriors. 
    Puntp #valor de puntuació final per a una pregunta (int)
    Llista #Acumulador de possibles valors per a la funció random que pot treure per no repetir preguntes (list)
    Valors #Diccionari index (int) - pregunta (str)
    Preguntes #Diccionari pregunta (str) - resposta (str)
    Nom #Nom del jugador (str)
    Vides #Vides del jugador (int)
    Dif #dificultat del joc (str)
    Temps_R #Diccionari acumulatiu pregunta (str) - temps (str)
    Historial #Diccinari acumulatiu nom jugador (str) - puntuació i temps (str) no ordenat
    FiFinal #Emmagatzemador si es vol repetir la partida (boolean)
    Partides #Recompte de partides totals jugades
    FinalIn #Emmagatzemador resposta si es vol reiniciar la partida o no (str)
    Jugades #Acumulador de les puntuacions de totes les partides (llista)
    Millor #Major puntuació obtinguda entre totes les partides (int)
    Nivell #Emmagatzemador de la 
    PTotals #nombre de preguntes total (variable) amb les que s'acabarà el joc (int)
    Difp #Dificultat de les preguntes que es mostraran que canvia segons el mode de joc (int)

    class c: #classe amb els diferents colors per als strings
        negre = "SYNC"
        lila = "BUILTIN"
        verd = "STRING"
        vermell = "COMMENT"
        blau = "stdout"
        groc = "KEYWORD"

    def T_Pregunta(Ttotal, Vp): #funció calcular temps pregunta
        Tf = time.monotonic() #atura cronòmetre
        Tp = round((Tf - Ti), 2) #calcula temps
        Temps_R[f"Pregunta {Intents}"] = f"{round(Tp, 2)}s" #llista acumulativa temps
        Ttotal += Tp #suma temps
        round(Ttotal, 2) #redonejar 2 decimals
        Vt = int(400*((20-Tp)/20)) #Valor total = 400 * multiplicador per temps de pregunta
        return [Ttotal, Vt] #la sortida és el temps total i el valor de la pregunta sense multiplicadors externs   

    def T_Format(Ttotal): #la variable d'entrada és el temps total (obtingut a T_Pregunta)
        segons = round(Ttotal,2) #temps en segons
        minuts,hores = 0,0
        while segons >= 60: #minuts?
            segons -= 60
            minuts += 1
        while minuts >=  60: #hores?
            minuts -= 60
            hores += 1
        return f"{hores} h : {minuts} min : {segons} s" #la sortida és el cronòmetre total

    Nl = 1
    Llista = [Nl]
    while len(Llista) < 120: #fer una llista amb 120 nombres per anar llevant a mesura que es respongui
        Nl += 1
        Llista.append(Nl)

    #benvinguda al joc
    color.write("Benvinguts al joc del penjat!\n",c.negre)
    time.sleep(1)
    color.write(f"""
Aquesta és la vostra partida nombre {Partides}.
Aquests són els resultats de les anteriors: {Historial}. Sereu capaços de millorar les marques?\n""",c.negre)
    time.sleep(1.2)
    
    Inici1 = False 
    while Inici1 == False: #dona opció a obrir instruccions, o passar-les directament
        if input("\nVoleu veure les instruccions? Sí (S) | No (N):").upper() == "S":
            
            color.write("""\nEl Joc del Penjat és un joc de pregunta-resposta oberta sobre l’escola.
Hi ha 100 preguntes sobre l’escola que haureu de respondre correctament amb un nombre limitat de vides. Se us mostrarà una al atzar i haureu de respondre correctament.

Hi ha 4 nivells de preguntes: de la pregunta 1 a la 15, amb preguntes senzilles; de la 16 a la 30, amb preguntes mitjanes; de la 31 a la 60, amb preguntes difícils; i de la 61 a la 100, amb preguntes insanes.
*Tant podeu jugar a totes les preguntes com un nivell en concret.

Si encertau la pregunta, se us donarà una puntuació basada en el nivell de la pregunta, la dificultat introduïda pel joc, la ratxa d’encerts i el temps trigat en respondre. Si fallau, se us restarà 1⁄4 del seu valor original.
*A l’hora de respondre, teniu cura amb les faltes d’ortografia. Les majúscules són negligibles.

Al principi del joc se us demanarà un pseudònim que pot ser el vostre nom real per poder competir amb altres jugadors dins la mateixa partida; haureu de sel·leccionar la dificultat del joc, que es basa en la quantitat de vides que tendreu; i si voleu jugar al joc complet o parcial, i si és parcial, quin nivell de preguntes jugar.

També podeu introduir diverses entrades clau durant la resposta:
- S: Passa a la següent pregunta.
- P: Mostra una pista (la primera lletra de la resposta correcta) a canvi d’obtenir la
meitat de la puntuació si s’encerta la pregunta.
- F: Passa al fi del joc.
*Si la resposta correcta és de només 1 caràcter, la entrada “P” es donarà com a invàlida. Si voleu tornar a jugar, o competir amb altres amics, se us donarà l’opció en acabar el joc. Molta sort!\n""",c.negre)
            time.sleep(1)
            
            if input("\nHo heu entès? Si és així, per continuar, introduïu qualsevol caràcter:"): #crea una interacció per a l'inici del joc
                Inici1 = True
        else:
            Inici1 = True

    time.sleep(0.5)
        
    color.write("\nPareix que ja us sabeu les instruccions!\n",c.negre)
    time.sleep(1.5)

    #introducció al joc

    Inici1 = False
    if input("\nSi esteu llestos per començar, introduïu qualsevol caràcter:"):  #inicia quan el jugador vol
        Inici1 = True
    time.sleep(1)
    
    while Nom == "n/a":
        Nom = input("\nIntroduiu el vostre nom:") #demana el nom per fer registre millors jugadors
    time.sleep(0.5)
    
    Inici1 = False
    while Inici1 == False:
        Nivell = input("\nIntroduiu la duració de la partida Completa (C) [100 preguntes] | Parcial (P) [15-40 preugntes]:") #demana la llargada del joc
        if Nivell.upper() == "C": #es vol jugar complet
            PTotals = 100 #les preguntes per acabar són totes
            Inici1 = True
        if Nivell.upper() == "P": #es vol jugar només 1 nivell
            Difp = int(input("\nQuina és la dificultat de les preguntes que voleu jugar? (1-4):")) #demana el nivell concret
            if Difp == 1: #depenent del nivell, les preguntes totals a jugar són les d'aquell nivell
                PTotals = 15
                Inici1 = True
            if Difp == 2:
                PTotals = 15
                Inici1 = True
            if Difp == 3:
                PTotals = 30
                Inici1 = True
            if Difp == 4:
                PTotals = 40
                Inici1 = True
                
    time.sleep(1)
    Inici1 = False #variable que dona inici al joc
    while Inici1 == False:
        Dif = input("\nIntroduiu la dificultat [vides disponibles] Fàcil (F) | Mitjà (M) | Difícil (D) | Extrem (E):") #input dificultat, no permet faltes ortogràfiques
        if Dif.upper() == "F": #segons el nivell canvia la quantitat de vides i el multiplicador de dificultat
            if Nivell.upper() == "C":
                Vides = 10 #si es juga complet
            else:
                Vides = 5 #si es juga parcial
            Vd = 0.75
            Inici1 = True
        elif Dif.upper() == "M":
            if Nivell.upper() == "C":
                Vides = 7
            else:
                Vides = 4
            Vd = 1
            Inici1 = True
        elif Dif.upper() == "D":
            if Nivell.upper() == "C":
                Vides = 4
            else:
                Vides = 2
            Vd = 1.3
            Inici1 = True
        elif Dif.upper() == "E":
            Vides = 1 #al nivell extrem les vides sempre són 1
            Vd = 1.6
            Inici1 = True
            
    time.sleep(0.3)
    color.write(f"\nBon dia, {Nom}, avui jugareu mode {Nivell} al nivell {Difp} en dificultat {Dif}, així que disposau de {Vides} vides.\n",c.groc) #Missatge d'inici del joc confirmant les dades introduïdes
    time.sleep(2)

    while Intents < PTotals and Vides > 0: #mentres no es guanyi, mostrar preguntes
        
        Ti,Tf,Tp,Vp,Nm=0,0,0,0,0 #reinici de variables a cada intent
        Intents += 1 #bucle limitat
    
        if Nivell.upper() == "C": #en cas de jugar en complet, Difp dependrà de les respostes i intents
            if PNivell <= 15 and Intents <= 20:
                Difp = 1
            elif PNivell <= 30 and Intents <= 40:
                Difp = 2
            elif PNivell <= 60 and Intents <= 75:
                Difp = 3
            elif PNivell <= 100 and Intents <= 120:
                Difp = 4

        #Difp s'assigna al principi del joc si s'elegeix el mode Parcial
        
        while Nm not in Llista: #identifica quina pregunta es farà segons nivell o la puntuació donada
            if Difp == 1:
                Nm = random.randrange(1,20)
                Vp = 200
            elif Difp == 2:
                Nm = random.randrange(21,40)
                Vp = 300
            elif Difp == 3:
                Nm = random.randrange(41,75)
                Vp = 400
            elif Difp == 4:
                Nm = random.randrange(76,120)
                Vp = 500
                    
            if Ratxa < 3: #multiplicador ratxa
                Vr = 1
            elif Ratxa < 6:
                Vr = 1.1
            elif Ratxa < 9:
                Vr = 1.2
            elif Ratxa < 12:
                Vr = 1.3
            elif Ratxa < 15:
                Vr = 1.4
            else:
                Vr = 1.5
            
        Llista.remove(Nm) #lleva la pregunta de la llista de possibles nombres aleatoris, així no es repeteix
        P = Valors.get(Nm) #asigna la pregunta 
        Rc = Preguntes.get(Valors.get(Nm)) #assigna solució
        time.sleep(1)
        color.write(f"\nLa pregunta és: {P}\n",c.lila) #mostra pregunta
        time.sleep(0.4) #compte enrere
        color.write("\n3",c.vermell)
        time.sleep(0.4)
        color.write("\n2",c.groc)
        time.sleep(0.4)
        color.write("\n1\n",c.verd)
        time.sleep(0.4)
        Ti = time.monotonic() #inicia cronòmetre
        Rj = input("\nIntroduiu la vostra resposta:\n") #demana solució
        
        if Rj.upper() == "P":#el jugador demana pista
            if len(Rc) > 1:
                time.sleep(0.5)
                Vp = Vp*0.5 #dona el valor en cas d'encertar a la meitat
                color.write("La primera lletra de la resposta és:",Rc[0],c.lila) #mostra la primera lletra
                Rj = input("Introduiu de nou la vostra resposta:\n") #dona opció per tornar-ho a escriure
            
        if Rj.upper() == "F": #el jugador demana el final de la partida
            time.sleep(2)
            Vides = 0 #lleva vides per acabar el joc
            
        elif Rj.upper() == "S": #el jugador demana nova pregunta
            time.sleep(0.5)
            color.write("Es mostrarà una nova pregunta",c.lila) #segueix amb una nova pregunta
            PNivell += 1 #fa recompte com a intent
            Ratxa = 0 #es reinicia la ratxa d'encerts
            T_Pregunta(Ttotal,Vt) #compta temps però no mostra
            time.sleep(2)
            
        elif Rj.upper() == Rc.upper(): #el jugador és bo
            time.sleep(0.5) #intriga
            color.write("\nHeu encertat la pregunta, enhorabona!\n",c.verd) #missatge enhorabona
            Ttotal,Vt = T_Pregunta(Ttotal,Vt)[0],T_Pregunta(Ttotal,Vt)[1] #acumulador temps i multiplicador temps
            Puntp = int((Vt + Vp)*Vd*Vr) #variables puntuació ((puntuació joc + valor pregunta original)*valor dificultat*valor ratxa)
            color.write(f"\n+{Puntp} punts\n",c.verd) #mostra la puntuació que sumarà
            PNivell += 1 #acumulació de variables
            Correctes += 1
            Punts += Puntp
            Ratxa += 1
            Temps = T_Format(Ttotal) #temps amb format
            time.sleep(1)
            color.write(f"\nUs queden {Vides} vides, duis {Punts} punts i {Correctes}/{Intents} encertades, ja són {Ratxa} seguides, en {Temps}\n",c.groc) #missatge sortida
            time.sleep(1)
            if Intents < PTotals: #si no ha acabat, mostra per seguir
                color.write("\nSegüent pregunta:\n",c.negre)
                time.sleep(1)
            else: #si ha acabat, determina que aquesta era la darrera pregunta
                color.write("\nJoc finalitzat: heu acabat totes les preguntes.\n",c.lila)
                time.sleep(1)
            
        else: #el jugador és un magre
            time.sleep(0.5) #intriga
            color.write("\nHeu introduit una resposta incorrecta!\n",c.vermell) #missatge penós
            Ttotal,Vt = T_Pregunta(Ttotal,Vt)[0],T_Pregunta(Ttotal,Vt)[1] #acumulador temps i multiplicador temps
            Puntp = int((Vt + Vp)*Vd*Vr) #variables puntuació ((puntuació joc + valor pregunta original)*valor dificultat*valor ratxa)
            PNivell += 1 #acumulació de variables
            Vides -= 1
            Punts -= int(Puntp/4) #resta 1/4 de la puntuació que hagués obtingut si encertava
            color.write(f"\n-{int(Puntp/4)} punts\n",c.vermell)
            Ratxa = 0 #lleva la ratxa d'encerts
            Temps = T_Format(Ttotal) #temps format
            time.sleep(1)
            color.write(f"\nLa resposta correcta és: {Rc}\n",c.negre) #mostra la que era la resposta correcta
            time.sleep(1)
            color.write(f"\nUs queden {Vides} vides, duis {Punts} punts i {Correctes}/{Intents} encertades en {Temps}\n",c.groc) #missatge sortida
            time.sleep(1)
            if Vides > 0: #si no ha acabat, mostra per seguir
                color.write("\nSegüent pregunta:\n",c.negre)
                time.sleep(1)
            else: #si ha acabat, determina que aquesta era la darrera pregunta
                color.write("\nJoc finalitzat: heu perdut totes les vides.\n",c.lila)
                time.sleep(1)

    time.sleep(1)
    color.write(f"""
\nLa vostra puntuació final és de {Punts} punts en un temps de {Temps}, havent encertat {Correctes} de {Intents} intentades.\n
    """,c.groc
    ) #missatge final del joc
    time.sleep(2)
    Historial[Punts] = Nom #afegeix el registre nom-puntuació
    color.write(f"\nAquest és el registre de partides (punts-jugador):{Historial}\n",c.negre) #mostra el registre total
    time.sleep(1.5)
    Jugades = list(Historial.keys()) #extreu les puntuacions i les fa llista
    Millor = max(Jugades) #extreu la millor puntuació
    color.write(f"\nLa millor marca per ara és de {Historial[Millor]}, amb {Millor} punts.\n",c.groc) #mostra el millor resultat i qui l'ha obtingut
    time.sleep(1.5)
    FinalIn = input("\nVoleu millorar aquestes puntuacions? Si és així, escriviu \"S\", si escriviu una altra cosa, aquí s'acabarà la partida:")#demana al jugador si vol tornar a jugar 
    

    if FinalIn.upper() == "S": #el jugador vol continuar
        FiFinal = False
        time.sleep(0.5)
        color.write("\nTornareu a jugar una nova partida, podreu millorar la vostra puntuació?\n\n\n",c.negre) #nova partida cap a les instruccions
        time.sleep(1)
    else:
        FiFinal = True
        time.sleep(0.5)
        color.write(f"\nEl joc ha acabat definitivament, la taula de puntuacions és aquesta:\n{Historial}",c.negre) #mostra de nou l'historial i acaba

