"""EURING place codes -- see scripts/generate_region_choices.py, which
generates this file (and country.py's Country class) wholesale from
EURING's own place-code list. Don't hand-edit; re-run that script when
EURING publishes an update.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Region(models.TextChoices):
    """Every current EURING place code, country-level and finer sub-regions alike."""

    ARCTIC_OCEAN = "+A00", _("Arctic Ocean")
    BEAR_ISLAND = "+ABI", _("Bear Island")
    JAN_MAYEN = "+AJM", _("Jan Mayen")
    SVALBARD = "+ASV", _("Svalbard")
    NORTH_SEA_ISLANDS = "+B00", _("North Sea islands")
    ENGLISH_CHANNEL_IRISH_SEA_ISLANDS = "+C00", _("English Channel/Irish Sea islands")
    BAY_OF_BISCAY_ISLANDS = "+D00", _("Bay of Biscay islands")
    BALTIC_SEA_ISLANDS = "+E00", _("Baltic Sea islands")
    MEDITERRANEAN_SEA_ISLANDS = "+F00", _("Mediterranean Sea islands")
    BLACK_AND_CASPIAN_SEA_ISLANDS = "+G00", _("Black and Caspian Sea islands")
    NORTH_ATLANTIC_OCEAN_ISLANDS = "+H00", _("North Atlantic Ocean islands")
    BERMUDA = "+HBE", _("Bermuda")
    CAPE_VERDE_ISLANDS = "+HCV", _("Cape Verde Islands")
    ISLANDS_IN_OTHER_OCEANS = "+I00", _("Islands in other oceans")
    INDIAN_OCEAN_ISLANDS = "+J00", _("Indian Ocean islands")
    NORTH_SEA = "-B00", _("North Sea")
    ENGLISH_CHANNEL_AND_IRISH_SEA = "-C00", _("English Channel and Irish Sea")
    BAY_OF_BISCAY = "-D00", _("Bay of Biscay")
    BALTIC_SEA = "-E00", _("Baltic Sea")
    MEDITERRANEAN_SEA = "-F00", _("Mediterranean Sea")
    BLACK_AND_CASPIAN_SEAS = "-G00", _("Black and Caspian Seas")
    NORTH_ATLANTIC_OCEAN_OTHER_PARTS = "-H00", _("North Atlantic Ocean (other parts)")
    OTHER_OCEANS = "-I00", _("Other Oceans")
    INDIAN_OCEAN = "-J00", _("Indian Ocean")
    AUSTRALIA = "AA--", _("Australia")
    NEW_SOUTH_WALES = "AANS", _("New South Wales")
    NORTHERN_TERRITORY = "AANT", _("Northern Territory")
    QUEENSLAND = "AAQU", _("Queensland")
    SOUTH_AUSTRALIA = "AASA", _("South Australia")
    TASMANIA = "AATA", _("Tasmania")
    VICTORIA = "AAVI", _("Victoria")
    WESTERN_AUSTRALIA = "AAWA", _("Western Australia")
    ALBANIA = "AB00", _("Albania")
    ARMENIA = "AE00", _("Armenia")
    ALGERIA = "AG--", _("Algeria")
    ALGER = "AGAL", _("Alger")
    CONSTANTINE = "AGCO", _("Constantine")
    ORAN = "AGOR", _("Oran")
    OTHER_PROVINCES = "AGTS", _("Other provinces")
    ADEN = "AI00", _("Aden")
    NEW_ZEALAND = "AJ--", _("New Zealand")
    NORTH_ISLAND = "AJNI", _("North Island")
    SOUTH_ISLAND = "AJSI", _("South Island")
    AZERBAIJAN = "AK--", _("Azerbaijan")
    NAGORNYY_KARABAKH = "AK01", _("Nagornyy Karabakh")
    ANGOLA = "AL00", _("Angola")
    LIECHTENSTEIN = "AM00", _("Liechtenstein")
    ANTARCTICA = "AN00", _("Antarctica")
    SAUDI_ARABIA = "AR00", _("Saudi Arabia")
    AUSTRIA = "AU--", _("Austria")
    BURGENLAND = "AU00", _("Burgenland")
    K_RNTEN = "AU01", _("K?rnten")
    NIEDER_STERREICH = "AU02", _("Nieder?sterreich")
    OBER_STERREICH = "AU03", _("Ober?sterreich")
    SALZBURG = "AU04", _("Salzburg")
    STEIERMARK = "AU05", _("Steiermark")
    TIROL = "AU06", _("Tirol")
    VORARLBERG = "AU07", _("Vorarlberg")
    WIEN = "AU08", _("Wien")
    BAHRAIN_QATAR = "AZ00", _("Bahrain & Qatar")
    BRAZIL = "BA00", _("Brazil")
    BULGARIA = "BG--", _("Bulgaria")
    BLAGOEVGRAD = "BG01", _("Blagoevgrad")
    BURGAS = "BG02", _("Burgas")
    VARNA = "BG03", _("Varna")
    VELIKO_TURNOVO = "BG04", _("Veliko Turnovo")
    VIDIN = "BG05", _("Vidin")
    VRATSA = "BG06", _("Vratsa")
    GABROVO = "BG07", _("Gabrovo")
    DOBRICH = "BG08", _("Dobrich")
    KURDZHALI = "BG09", _("Kurdzhali")
    KYUSTENDIL = "BG10", _("Kyustendil")
    LOVECH = "BG11", _("Lovech")
    MONTANA = "BG12", _("Montana")
    PAZARDZHIK = "BG13", _("Pazardzhik")
    PERNIK = "BG14", _("Pernik")
    PLEVEN = "BG15", _("Pleven")
    PLOVDIV = "BG16", _("Plovdiv")
    RAZGRAD = "BG17", _("Razgrad")
    RUSE = "BG18", _("Ruse")
    SILISTRA = "BG19", _("Silistra")
    SLIVEN = "BG20", _("Sliven")
    SMOLYAN = "BG21", _("Smolyan")
    SOFIA_PROVINCE = "BG22", _("Sofia province")
    SOFIA_CITY = "BG23", _("Sofia City")
    STARA_ZAGORA = "BG24", _("Stara Zagora")
    TURGOVISHTE = "BG25", _("Turgovishte")
    HASKOVO = "BG26", _("Haskovo")
    SHUMEN = "BG27", _("Shumen")
    YAMBOL = "BG28", _("Yambol")
    BOSNIA_AND_HERZEGOVINA = "BH00", _("Bosnia and Herzegovina")
    ARGENTINA = "BJ00", _("Argentina")
    BELGIUM = "BL--", _("Belgium")
    BRUXELLES = "BL19", _("Bruxelles")
    ANTWERPEN = "BL20", _("Antwerpen")
    BRABANT = "BL21", _("Brabant")
    HAINAUT = "BL22", _("Hainaut")
    LIMBURG = "BL23", _("Limburg")
    LI_GE = "BL24", _("Li?ge")
    LUXEMBOURG = "BL25", _("Luxembourg")
    NAMUR = "BL26", _("Namur")
    OOST_VLAANDEREN = "BL27", _("Oost-Vlaanderen")
    WEST_VLAANDEREN = "BL28", _("West-Vlaanderen")
    BRABANT_WALLON = "BL29", _("Brabant wallon")
    VLAAMS_BRABANT = "BL30", _("Vlaams Brabant")
    BELARUS = "BY--", _("Belarus")
    BREST_O = "BY20", _("Brest O.")
    GOMEL_O = "BY22", _("Gomel O.")
    GRODNO_O = "BY23", _("Grodno O.")
    MINSK_O = "BY25", _("Minsk O.")
    MOGILEV_O = "BY26", _("Mogilev O.")
    VITEBSK_O = "BY28", _("Vitebsk O.")
    CENTRAL_AMERICA = "CA--", _("Central America")
    BELIZE = "CABA", _("Belize")
    COSTA_RICA = "CACA", _("Costa Rica")
    EL_SALVADOR = "CAEA", _("El Salvador")
    GUATEMALA = "CAGA", _("Guatemala")
    HONDURAS = "CAHA", _("Honduras")
    NICARAGUA = "CANA", _("Nicaragua")
    PANAMA = "CAPA", _("Panama")
    HONG_KONG = "CG00", _("Hong Kong")
    CHANNEL_ISLANDS = "CI00", _("Channel Islands")
    ALDERNEY = "CIAL", _("Alderney")
    GUERNSEY = "CIGU", _("Guernsey")
    HERM = "CIHE", _("Herm")
    JERSEY = "CIJE", _("Jersey")
    SARK = "CISA", _("Sark")
    CUBA = "CJCA", _("Cuba")
    JAMAICA = "CJJA", _("Jamaica")
    CHINA = "CP--", _("China")
    ANHWEI = "CPAN", _("Anhwei")
    CHEKIANG = "CPCH", _("Chekiang")
    FUKIEN = "CPFU", _("Fukien")
    HUPEI = "CPHI", _("Hupei")
    HEILUNGKIANG = "CPHK", _("Heilungkiang")
    HONAN = "CPHO", _("Honan")
    HOPEI = "CPHP", _("Hopei")
    HUNAN = "CPHU", _("Hunan")
    INNER_MONGOLIA_AR = "CPIM", _("Inner Mongolia (AR)")
    KANSU = "CPKA", _("Kansu")
    KWANGTUNG = "CPKG", _("Kwangtung")
    KIANGSI = "CPKI", _("Kiangsi")
    KIRIN = "CPKR", _("Kirin")
    KWANGSI_CHUANG_AR = "CPKS", _("Kwangsi(Chuang AR)")
    KIANGSU = "CPKU", _("Kiangsu")
    KWEICHOW = "CPKW", _("Kweichow")
    LIAONING = "CPLI", _("Liaoning")
    NINGHSIA_HUI_AR = "CPNH", _("Ninghsia (Hui AR)")
    PEKING_MUNICIPALITY = "CPPK", _("Peking (Municipality)")
    SHANSI = "CPSA", _("Shansi")
    SHANTUNG = "CPSG", _("Shantung")
    SHANGHAI_MUNICIPALITY = "CPSH", _("Shanghai (Municipality)")
    SHENSI = "CPSI", _("Shensi")
    SINKIANG_UIGHUR_AR = "CPSK", _("Sinkiang (Uighur AR)")
    SZECHUAN = "CPSZ", _("Szechuan")
    CHINGHAI = "CPTS", _("Chinghai")
    TIENTSIN_MUNICIPALITY = "CPTT", _("Tientsin (Municipality)")
    YUNNAN = "CPYU", _("Yunnan")
    TAIWAN = "CX00", _("Taiwan")
    CYPRUS = "CY00", _("Cyprus")
    UN_BUFFER_ZONE = "CYB-", _("UN Buffer Zone")
    NORTHERN_REGIONS = "CYN-", _("Northern Regions")
    SOUTHERN_REGIONS = "CYS-", _("Southern Regions")
    CZECH_REPUBLIC = "CZ--", _("Czech Republic")
    JIHO_ESK = "CZ10", _("Jiho?esk?")
    KR_LOV_HRADECK = "CZ11", _("Kr?lov?hradeck?")
    VYSO_INA = "CZ12", _("Vyso?ina")
    KARLOVARSK = "CZ13", _("Karlovarsk?")
    LIBERECK = "CZ14", _("Libereck?")
    PARDUBICK = "CZ15", _("Pardubick?")
    PLZE_SK = "CZ16", _("Plze?sk?")
    STREDO_ESK_A_PRAHA = "CZ17", _("Stredo?esk? a Praha")
    STECK = "CZ18", _("?steck?")
    JIHOMORAVSK = "CZ22", _("Jihomoravsk?")
    ZL_NSK = "CZ23", _("Zl?nsk?")
    OLOMOUCK = "CZ26", _("Olomouck?")
    MORAVSKOSLEZSK = "CZ27", _("Moravskoslezsk?")
    CEUTA = "DA00", _("Ceuta")
    GERMANY = "DE--", _("Germany")
    BAVARIA = "DEA-", _("Bavaria")
    OBERBAYERN = "DEAB", _("Oberbayern")
    OBERFRANKEN = "DEAF", _("Oberfranken")
    MITTELFRANKEN = "DEAM", _("Mittelfranken")
    NIEDERBAYERN = "DEAN", _("Niederbayern")
    OBERPFALZ = "DEAP", _("Oberpfalz")
    SCHWABEN = "DEAS", _("Schwaben")
    UNTERFRANKEN = "DEAU", _("Unterfranken")
    BADEN_W_RTTEMBERG = "DEB-", _("Baden-W?rttemberg")
    BRANDENBURG = "DEBB", _("Brandenburg")
    BERLIN = "DEBE", _("Berlin")
    S_DBADEN = "DEBF", _("S?dbaden")
    NORDBADEN = "DEBK", _("Nordbaden")
    NORDW_RTTEMBERG = "DEBS", _("Nordw?rttemberg")
    S_DW_RTTEMBERG = "DEBT", _("S?dw?rttemberg")
    RHEINLAND_PFALZ = "DEC-", _("Rheinland-Pfalz")
    KOBLENZ = "DECK", _("Koblenz")
    RHEINHESSEN_PFALZ = "DECR", _("Rheinhessen-Pfalz")
    TRIER = "DECT", _("Trier")
    SAARLAND = "DEDO", _("Saarland")
    HESSEN = "DEE-", _("Hessen")
    DARMSTADT = "DEED", _("Darmstadt")
    GIE_EN = "DEEG", _("Gie?en")
    KASSEL = "DEEK", _("Kassel")
    NORDRHEIN_WESTFALEN = "DEF-", _("Nordrhein-Westfalen")
    ARNSBERG = "DEFA", _("Arnsberg")
    D_SSELDORF = "DEFD", _("D?sseldorf")
    K_LN = "DEFK", _("K?ln")
    DETMOLD = "DEFL", _("Detmold")
    M_NSTER = "DEFM", _("M?nster")
    NIEDERSACHSEN = "DEG-", _("Niedersachsen")
    BRAUNSCHWEIG = "DEGB", _("Braunschweig")
    OSTFRIESISCHE_INSELN = "DEGF", _("Ostfriesische Inseln")
    HANNOVER = "DEGH", _("Hannover")
    L_NEBURG = "DEGL", _("L?neburg")
    NEUWERK_AND_SCHARH_RN_ISLANDS = "DEGN", _("Neuwerk and Scharh?rn Islands")
    WESER_EMS = "DEGW", _("Weser-Ems")
    HAMBURG = "DEHH", _("Hamburg")
    MECKLENBURG_VORPOMMERN = "DEMV", _("Mecklenburg - Vorpommern")
    SCHLESWIG_HOLSTEIN = "DEQ-", _("Schleswig-Holstein")
    HELGOLAND = "DEQH", _("Helgoland")
    NORDFRIESISCHE_INSELN = "DEQN", _("Nordfriesische Inseln")
    SCHLESWIG_HOLSTEIN_MAINLAND = "DEQS", _("Schleswig-Holstein (mainland)")
    ISLAND_TRISCHEN = "DEQT", _("Island Trischen")
    SACHSEN_ANHALT = "DERA", _("Sachsen Anhalt")
    HALLE = "DERH", _("Halle")
    MAGDEBURG = "DERM", _("Magdeburg")
    DESSAU = "DERS", _("Dessau")
    CHEMNITZ = "DESC", _("Chemnitz")
    DRESDEN = "DESD", _("Dresden")
    LEIPZIG = "DESL", _("Leipzig")
    SACHSEN = "DESN", _("Sachsen")
    TH_RINGEN = "DETH", _("Th?ringen")
    BREMEN = "DEXB", _("Bremen")
    GERMANY_2 = "DF--", _("Germany")
    DENMARK = "DK--", _("Denmark")
    HOVEDSTADEN = "DKHS", _("HovedStaden")
    MIDTJYLLAND = "DKMJ", _("MidtJylland")
    NORDJYLLAND = "DKNJ", _("NordJylland")
    SYDDANMARK = "DKSD", _("SydDanmark")
    SJ_LLAND = "DKSL", _("Sj?lLand")
    CANADA = "EA--", _("Canada")
    ALBERTA = "EAAL", _("Alberta")
    BRITISH_COLUMBIA = "EABC", _("British Columbia")
    LABRADOR = "EALA", _("Labrador")
    MANITOBA = "EAMA", _("Manitoba")
    NEW_BRUNSWICK = "EANB", _("New Brunswick")
    NEWFOUNDLAND = "EANF", _("Newfoundland")
    NOVA_SCOTIA = "EANS", _("Nova Scotia")
    NORTH_WEST_TERRITORIES = "EANW", _("North West Territories")
    ONTARIO = "EAON", _("Ontario")
    PRINCE_EDWARD_ISLAND = "EAPE", _("Prince Edward Island")
    QUEBEC = "EAQU", _("Quebec")
    SASKATCHEWAN = "EASA", _("Saskatchewan")
    EGYPT = "EG00", _("Egypt")
    ANDORRA = "EK00", _("Andorra")
    MALI = "EM00", _("Mali")
    ETHIOPIA = "EQ00", _("Ethiopia")
    IRELAND = "ER--", _("Ireland")
    CORK = "ERCK", _("Cork")
    CLARE = "ERCL", _("Clare")
    CAVAN = "ERCV", _("Cavan")
    CARLOW = "ERCW", _("Carlow")
    DONEGAL = "ERDO", _("Donegal")
    DUBLIN = "ERDU", _("Dublin")
    GALWAY = "ERGA", _("Galway")
    KILDARE = "ERKD", _("Kildare")
    KERRY = "ERKE", _("Kerry")
    KILKENNY = "ERKK", _("Kilkenny")
    LONGFORD = "ERLG", _("Longford")
    LIMERICK = "ERLK", _("Limerick")
    LEITRIM = "ERLM", _("Leitrim")
    LOUTH = "ERLU", _("Louth")
    LAOIS = "ERLX", _("Laois")
    MAYO = "ERMA", _("Mayo")
    MEATH = "ERME", _("Meath")
    MONAGHAN = "ERMO", _("Monaghan")
    OFFALY = "EROF", _("Offaly")
    ROSCOMMON = "ERRO", _("Roscommon")
    SLIGO = "ERSL", _("Sligo")
    TIPPERARY = "ERTP", _("Tipperary")
    WATERFORD = "ERWA", _("Waterford")
    WICKLOW = "ERWI", _("Wicklow")
    WESTMEATH = "ERWM", _("Westmeath")
    WEXFORD = "ERWX", _("Wexford")
    SPAIN = "ES--", _("Spain")
    ATLANTIC_COAST = "ES0-", _("Atlantic coast")
    LAVA = "ES00", _("?lava")
    LA_CORU_A = "ES01", _("La Coru?a")
    GUIP_ZCOA = "ES02", _("Guip?zcoa")
    LUGO = "ES03", _("Lugo")
    ORENSE = "ES04", _("Orense")
    ASTURIAS = "ES05", _("Asturias")
    PONTEVEDRA = "ES06", _("Pontevedra")
    CANTABRIA = "ES07", _("Cantabria")
    VIZCAYA = "ES08", _("Vizcaya")
    CENTRA_NORTH_WEST = "ES1-", _("Centra; north-west")
    AVILA = "ES10", _("Avila")
    BURGOS = "ES11", _("Burgos")
    LE_N = "ES12", _("Le?n")
    LA_RIOJA_LOGRO_O = "ES13", _("La Rioja (Logro?o)")
    PALENCIA = "ES14", _("Palencia")
    SALAMANCA = "ES15", _("Salamanca")
    SEGOVIA = "ES16", _("Segovia")
    SORIA = "ES17", _("Soria")
    VALLADOLID = "ES18", _("Valladolid")
    ZAMORA = "ES19", _("Zamora")
    CENTRAL_NORTH_EAST = "ES2-", _("Central; north-east")
    CUENCA = "ES20", _("Cuenca")
    GUADALAJARA = "ES21", _("Guadalajara")
    HUESCA = "ES22", _("Huesca")
    L_RIDA = "ES23", _("L?rida")
    NAVARRA = "ES24", _("Navarra")
    TERUEL = "ES25", _("Teruel")
    ZARAGOZA = "ES26", _("Zaragoza")
    NORTH_EAST_COAST = "ES3-", _("North-east coast")
    BARCELONA = "ES30", _("Barcelona")
    CASTELL_N = "ES31", _("Castell?n")
    GIRONA = "ES32", _("Girona")
    TARRAGONA = "ES33", _("Tarragona")
    SOUTH_EAST_COAST = "ES4-", _("South-east coast")
    ALBACETE = "ES40", _("Albacete")
    ALICANTE = "ES41", _("Alicante")
    ALMERIA = "ES42", _("Almeria")
    MURCIA = "ES43", _("Murcia")
    VALENCIA = "ES44", _("Valencia")
    CENTRAL_SOUTH = "ES5-", _("Central; south")
    BADAJOZ = "ES50", _("Badajoz")
    C_CERES = "ES51", _("C?ceres")
    CIUDAD_REAL = "ES52", _("Ciudad Real")
    MADRID = "ES53", _("Madrid")
    TOLEDO = "ES54", _("Toledo")
    SOUTH = "ES6-", _("South")
    C_DIZ = "ES60", _("C?diz")
    C_RDOBA = "ES61", _("C?rdoba")
    GRANADA = "ES62", _("Granada")
    HUELVA = "ES63", _("Huelva")
    JA_N = "ES64", _("Ja?n")
    M_LAGA = "ES65", _("M?laga")
    SEVILLA = "ES66", _("Sevilla")
    BALEARES = "ES7-", _("Baleares")
    EIVISSA = "ES70", _("Eivissa")
    MALLORCA = "ES71", _("Mallorca")
    MENORCA = "ES72", _("Menorca")
    ISLAS_CANARIAS = "ES8-", _("Islas Canarias")
    ISLA_DE_TENERIFE = "ES80", _("Isla de Tenerife")
    ISLA_DE_LA_PALMA = "ES81", _("Isla de La Palma")
    ISLA_DE_LA_GOMERA = "ES82", _("Isla de La Gomera")
    ISLA_EL_HIERRO = "ES83", _("Isla el Hierro")
    ISLA_DE_GRAN_CANARIA = "ES84", _("Isla de Gran Canaria")
    ISLA_DE_FUERTEVENTURA = "ES85", _("Isla de Fuerteventura")
    ISLA_DE_LANZAROTE = "ES86", _("Isla de Lanzarote")
    ESTONIA = "ET00", _("Estonia")
    ERITREA = "EV00", _("Eritrea")
    DJIBOUTI = "EY00", _("Djibouti")
    FAROE_ISLANDS = "FA--", _("Faroe Islands")
    NORDOYAR = "FA01", _("Nordoyar")
    EYSTUROYA = "FA02", _("Eysturoya")
    STREYMOY = "FA03", _("Streymoy")
    V_GA = "FA04", _("V?ga")
    SANDOY = "FA05", _("Sandoy")
    SUDUROY_NORDARI = "FA06", _("Suduroy Nordari")
    SUDUROY_SUNNARI = "FA07", _("Suduroy Sunnari")
    MYANMAR = "FE00", _("Myanmar")
    LESOTHO = "FG00", _("Lesotho")
    FALKLAND_ISLANDS = "FK00", _("Falkland Islands")
    NAMIBIA = "FM00", _("Namibia")
    CAMBODIA = "FNCA", _("Cambodia")
    LAOS = "FNLA", _("Laos")
    THAILAND = "FNTA", _("Thailand")
    VIETNAM = "FNVA", _("Vietnam")
    SOUTH_AFRICA = "FP--", _("South Africa")
    WESTERN_CAPE_CAPE_PROVINCE = "FPCG", _("Western Cape (Cape Province)")
    KWAZULU_NATAL = "FPNA", _("Kwazulu-Natal")
    FREE_STATE_ORANGE_FREE_STATE = "FPOF", _("Free State (Orange Free State)")
    NORTHERN_MPUMALANGA_TRANSVAAL = "FPTV", _("Northern Mpumalanga (Transvaal)")
    FRANCE = "FR--", _("France")
    FRANCE_NORTH_WEST = "FR0-", _("France; north-west")
    CALVADOS = "FR01", _("Calvados")
    EURE = "FR02", _("Eure")
    MANCHE = "FR03", _("Manche")
    MAYENNE = "FR04", _("Mayenne")
    NORD = "FR05", _("Nord")
    ORNE = "FR06", _("Orne")
    PAS_DE_CALAIS = "FR07", _("Pas-de-Calais")
    SEINE_MARITIME = "FR08", _("Seine-Maritime")
    SOMME = "FR09", _("Somme")
    FRANCE_NORTH_EAST = "FR1-", _("France; north east")
    AISNE = "FR10", _("Aisne")
    ARDENNES = "FR11", _("Ardennes")
    BAS_RHIN = "FR12", _("Bas-Rhin")
    HAUTE_MARNE = "FR13", _("Haute-Marne")
    HAUT_RHIN_TERRITOIRE_DE_BELFORT = "FR14", _("Haut-Rhin & Territoire de Belfort")
    MARNE = "FR15", _("Marne")
    MEURTHE_ET_MOSELLE = "FR16", _("Meurthe-et-Moselle")
    MEUSE = "FR17", _("Meuse")
    MOSELLE = "FR18", _("Moselle")
    VOSGES = "FR19", _("Vosges")
    FRANCE_CENTRAL_NORTH = "FR2-", _("France; central north")
    AUBE = "FR20", _("Aube")
    C_TE_D_OR = "FR21", _("C?te-d'Or")
    EURE_ET_LOIR = "FR22", _("Eure-et-Loir")
    LOIR_ET_CHER = "FR23", _("Loir-et-Cher")
    LOIRET = "FR24", _("Loiret")
    OISE = "FR25", _("Oise")
    SARTHE = "FR26", _("Sarthe")
    SEINE_ET_MARNE = "FR27", _("Seine-et-Marne")
    SEINE_ET_OISE_SEINE = "FR28", _("Seine-et-Oise? & Seine")
    YONNE = "FR29", _("Yonne")
    FRANCE_ATLANTIC_COAST = "FR3-", _("France; Atlantic coast")
    PYR_N_ES_ATLANTIQUES = "FR30", _("Pyr?n?es-Atlantiques")
    CHARENTE_MARITIME = "FR31", _("Charente-Maritime")
    C_TES_D_ARMOR = "FR32", _("C?tes-d?Armor")
    FINIST_RE = "FR33", _("Finist?re")
    GIRONDE = "FR34", _("Gironde")
    ILLE_ET_VILAINE = "FR35", _("Ille-et-Vilaine")
    LANDES = "FR36", _("Landes")
    LOIRE_ATLANTIQUE = "FR37", _("Loire-Atlantique")
    MORBIHAN = "FR38", _("Morbihan")
    VEND_E = "FR39", _("Vend?e")
    FRANCE_CENTRAL_WEST = "FR4-", _("France; central west")
    CHARENTE = "FR40", _("Charente")
    CORR_ZE = "FR41", _("Corr?ze")
    CREUSE = "FR42", _("Creuse")
    DEUX_S_VRES = "FR43", _("Deux-S?vres")
    DORDOGNE = "FR44", _("Dordogne")
    HAUTE_VIENNE = "FR45", _("Haute-Vienne")
    INDRE = "FR46", _("Indre")
    INDRE_ET_LOIRE = "FR47", _("Indre-et-Loire")
    MAINE_ET_LOIRE = "FR48", _("Maine-et-Loire")
    VIENNE = "FR49", _("Vienne")
    FRANCE_CENTRAL_EAST = "FR5-", _("France; central east")
    ALLIER = "FR50", _("Allier")
    ARD_CHE = "FR51", _("Ard?che")
    CANTAL = "FR52", _("Cantal")
    CHER = "FR53", _("Cher")
    HAUTE_LOIRE = "FR54", _("Haute-Loire")
    LOIRE = "FR55", _("Loire")
    NI_VRE = "FR56", _("Ni?vre")
    PUY_DE_D_ME = "FR57", _("Puy-de-D?me")
    RH_NE = "FR58", _("Rh?ne")
    SA_NE_ET_LOIRE = "FR59", _("Sa?ne-et-Loire")
    FRANCE_EAST = "FR6-", _("France; east")
    AIN = "FR60", _("Ain")
    ALPES_DE_HAUTE_PROVENCE = "FR61", _("Alpes-de-Haute-Provence")
    DOUBS = "FR62", _("Doubs")
    DR_ME = "FR63", _("Dr?me")
    HAUTES_ALPES = "FR64", _("Hautes-Alpes")
    HAUTE_SA_NE = "FR65", _("Haute-Sa?ne")
    HAUTE_SAVOIE = "FR66", _("Haute-Savoie")
    IS_RE = "FR67", _("Is?re")
    JURA = "FR68", _("Jura")
    SAVOIE = "FR69", _("Savoie")
    FRANCE_CENTRAL_SOUTH = "FR7-", _("France; central south")
    ARI_GE = "FR70", _("Ari?ge")
    AVEYRON = "FR71", _("Aveyron")
    GERS = "FR72", _("Gers")
    HAUTE_GARONNE = "FR73", _("Haute-Garonne")
    HAUTES_PYR_N_ES = "FR74", _("Hautes-Pyr?n?es")
    LOT = "FR75", _("Lot")
    LOT_ET_GARONNE = "FR76", _("Lot-et-Garonne")
    LOZ_RE = "FR77", _("Loz?re")
    TARN = "FR78", _("Tarn")
    TARN_ET_GARONNE = "FR79", _("Tarn-et-Garonne")
    FRANCE_MEDITERRANEAN = "FR8-", _("France; Mediterranean")
    ALPES_MARITIMES = "FR80", _("Alpes-Maritimes")
    AUDE = "FR81", _("Aude")
    BOUCHES_DU_RH_NE = "FR82", _("Bouches-du-Rh?ne")
    GARD = "FR83", _("Gard")
    H_RAULT = "FR84", _("H?rault")
    PYR_N_ES_ORIENTALES = "FR85", _("Pyr?n?es-Orientales")
    VAR = "FR86", _("Var")
    VAUCLUSE = "FR87", _("Vaucluse")
    CORSE = "FR90", _("Corse")
    CHAD = "FT00", _("Chad")
    MALAYSIA = "FVMA", _("Malaysia")
    SINGAPORE = "FVSA", _("Singapore")
    GREAT_BRITAIN = "GB--", _("Great Britain")
    ABERDEEN = "GBAB", _("Aberdeen")
    ANGUS = "GBAG", _("Angus")
    ISLE_OF_ANGLESEY = "GBAN", _("Isle of Anglesey")
    ARGYLL_AND_BUTE = "GBAR", _("Argyll and Bute")
    ABERDEENSHIRE = "GBAS", _("Aberdeenshire")
    SOUTH_AYRSHIRE = "GBAY", _("South Ayrshire")
    BATH_AND_N_E_SOMERSET = "GBBA", _("Bath and N. E. Somerset")
    BLACKBURN_WITH_DARWEN = "GBBB", _("Blackburn with Darwen")
    BEDFORDSHIRE = "GBBE", _("Bedfordshire")
    BRACKNELL_FOREST = "GBBF", _("Bracknell Forest")
    BRIDGEND = "GBBG", _("Bridgend")
    BOURNEMOUTH = "GBBH", _("Bournemouth")
    BRIGHTON_HOVE = "GBBN", _("Brighton & Hove")
    BLACKPOOL = "GBBP", _("Blackpool")
    SCOTTISH_BORDERS = "GBBR", _("Scottish Borders")
    BRISTOL = "GBBS", _("Bristol")
    BUCKINGHAMSHIRE = "GBBU", _("Buckinghamshire")
    BLAENAU_GWENT = "GBBW", _("Blaenau Gwent")
    CAMBRIDGESHIRE = "GBCB", _("Cambridgeshire")
    CEREDIGION = "GBCE", _("Ceredigion")
    CARDIFF = "GBCF", _("Cardiff")
    CLACKMANNANSHIRE = "GBCK", _("Clackmannanshire")
    CARMARTHENSHIRE = "GBCM", _("Carmarthenshire")
    CONWY = "GBCN", _("Conwy")
    CORNWALL = "GBCO", _("Cornwall")
    CAERPHILLY = "GBCP", _("Caerphilly")
    CHESHIRE = "GBCS", _("Cheshire")
    CUMBRIA = "GBCU", _("Cumbria")
    DUNDEE = "GBDD", _("Dundee")
    DERBY = "GBDE", _("Derby")
    DURHAM = "GBDH", _("Durham")
    DENBIGHSHIRE = "GBDI", _("Denbighshire")
    DARLINGTON = "GBDL", _("Darlington")
    DEVON = "GBDN", _("Devon")
    DUMFRIES_GALLOWAY = "GBDR", _("Dumfries & Galloway")
    DERBYSHIRE = "GBDS", _("Derbyshire")
    DORSET = "GBDT", _("Dorset")
    ENGLAND = "GBE-", _("England")
    EAST_AYRSHIRE = "GBEA", _("East Ayrshire")
    EAST_DUNBARTONSHIRE = "GBED", _("East Dunbartonshire")
    EDINBURGH = "GBEH", _("Edinburgh")
    EAST_LOTHIAN = "GBEL", _("East Lothian")
    EAST_RENFREWSHIRE = "GBER", _("East Renfrewshire")
    ESSEX = "GBEX", _("Essex")
    EAST_RIDING_OF_YORKSHIRE = "GBEY", _("East Riding of Yorkshire")
    FALKIRK = "GBFK", _("Falkirk")
    FLINTSHIRE = "GBFL", _("Flintshire")
    FIFE = "GBFR", _("Fife")
    GLASGOW = "GBGG", _("Glasgow")
    GLOUCESTERSHIRE = "GBGL", _("Gloucestershire")
    SOUTH_GLOUCESTERSHIRE = "GBGS", _("South Gloucestershire")
    GWYNEDD = "GBGW", _("Gwynedd")
    HEREFORDSHIRE = "GBHE", _("Herefordshire")
    HALTON = "GBHL", _("Halton")
    HAMPSHIRE = "GBHM", _("Hampshire")
    HARTLEPOOL = "GBHP", _("Hartlepool")
    HIGHLAND = "GBHR", _("Highland")
    HERTFORDSHIRE = "GBHT", _("Hertfordshire")
    INVERCLYDE = "GBIC", _("Inverclyde")
    ISLE_OF_MAN = "GBIM", _("Isle of Man")
    ISLE_OF_WIGHT = "GBIW", _("Isle of Wight")
    KINGSTON_UPON_HULL = "GBKH", _("Kingston upon Hull")
    KENT = "GBKN", _("Kent")
    LANCASHIRE = "GBLC", _("Lancashire")
    SOUTH_LANARKSHIRE = "GBLH", _("South Lanarkshire")
    LINCOLNSHIRE = "GBLI", _("Lincolnshire")
    NORTH_LANARKSHIRE = "GBLK", _("North Lanarkshire")
    NORTH_LINCOLNSHIRE = "GBLN", _("North Lincolnshire")
    GREATER_LONDON = "GBLO", _("Greater London")
    LEICESTERSHIRE = "GBLS", _("Leicestershire")
    LEICESTER = "GBLT", _("Leicester")
    LUTON = "GBLU", _("Luton")
    GREATER_MANCHESTER = "GBMA", _("Greater Manchester")
    MIDDLESBROUGH = "GBMB", _("Middlesbrough")
    MERSEYSIDE = "GBME", _("Merseyside")
    MILTON_KEYNES = "GBMK", _("Milton Keynes")
    MIDLOTHIAN = "GBML", _("Midlothian")
    MONMOUTHSHIRE = "GBMN", _("Monmouthshire")
    MORAY = "GBMO", _("Moray")
    MERTHYR_TYDFIL = "GBMT", _("Merthyr Tydfil")
    MEDWAY = "GBMW", _("Medway")
    NORTH_AYRSHIRE = "GBNA", _("North Ayrshire")
    NORTH_EAST_LINCOLNSHIRE = "GBNE", _("North East Lincolnshire")
    NOTTINGHAM = "GBNG", _("Nottingham")
    NORTHAMPTONSHIRE = "GBNH", _("Northamptonshire")
    NORFOLK = "GBNK", _("Norfolk")
    NORTHUMBERLAND = "GBNL", _("Northumberland")
    NORTH_YORKSHIRE = "GBNO", _("North Yorkshire")
    NEWPORT = "GBNP", _("Newport")
    NORTH_SOMERSET = "GBNR", _("North Somerset")
    NOTTINGHAMSHIRE = "GBNS", _("Nottinghamshire")
    ORKNEY = "GBOR", _("Orkney")
    OXFORDSHIRE = "GBOX", _("Oxfordshire")
    PEMBROKESHIRE = "GBPB", _("Pembrokeshire")
    PETERBOROUGH = "GBPE", _("Peterborough")
    PERTH_KINROSS = "GBPH", _("Perth & Kinross")
    PLYMOUTH = "GBPL", _("Plymouth")
    PORTSMOUTH = "GBPM", _("Portsmouth")
    POOLE = "GBPP", _("Poole")
    NEATH_AND_PORT_TALBOT = "GBPT", _("Neath and Port Talbot")
    POWYS = "GBPW", _("Powys")
    REDCAR_CLEVELAND = "GBRC", _("Redcar & Cleveland")
    RENFREWSHIRE = "GBRE", _("Renfrewshire")
    READING = "GBRG", _("Reading")
    RHONDDA_CYNON_TAFF = "GBRH", _("Rhondda Cynon Taff")
    RUTLAND = "GBRU", _("Rutland")
    SCOTLAND = "GBS-", _("Scotland")
    STOKE_ON_TRENT = "GBSE", _("Stoke-on-Trent")
    STAFFORDSHIRE = "GBSF", _("Staffordshire")
    STIRLING = "GBSG", _("Stirling")
    SHETLAND = "GBSH", _("Shetland")
    ISLES_OF_SCILLY = "GBSI", _("Isles of Scilly")
    SUFFOLK = "GBSK", _("Suffolk")
    SLOUGH = "GBSL", _("Slough")
    SWINDON = "GBSN", _("Swindon")
    SOMERSET = "GBSO", _("Somerset")
    SHROPSHIRE = "GBSP", _("Shropshire")
    SURREY = "GBSR", _("Surrey")
    SOUTHEND = "GBSS", _("Southend")
    SOUTHAMPTON = "GBSU", _("Southampton")
    SWANSEA = "GBSW", _("Swansea")
    SOUTH_YORKSHIRE = "GBSY", _("South Yorkshire")
    TELFORD_AND_WREKIN = "GBTF", _("Telford and Wrekin")
    THURROCK = "GBTH", _("Thurrock")
    TORFAEN = "GBTN", _("Torfaen")
    TORBAY = "GBTQ", _("Torbay")
    STOCKTON_ON_TEES = "GBTS", _("Stockton-on-Tees")
    TYNE_AND_WEAR = "GBTY", _("Tyne and Wear")
    NORTHERN_IRELAND = "GBU-", _("Northern Ireland")
    ANTRIM = "GBUA", _("Antrim")
    BELFAST = "GBUB", _("Belfast")
    FERMANAGH = "GBUF", _("Fermanagh")
    LONDONDERRY = "GBUL", _("Londonderry")
    ARMAGH = "GBUR", _("Armagh")
    TYRONE = "GBUT", _("Tyrone")
    DOWN = "GBUW", _("Down")
    VALE_OF_GLAMORGAN = "GBVG", _("Vale of Glamorgan")
    WALES = "GBW-", _("Wales")
    WARRINGTON = "GBWA", _("Warrington")
    WEST_BERKSHIRE = "GBWB", _("West Berkshire")
    WEST_DUNBARTONSHIRE = "GBWD", _("West Dunbartonshire")
    WESTERN_ISLES = "GBWI", _("Western Isles")
    WARWICKSHIRE = "GBWK", _("Warwickshire")
    WEST_LOTHIAN = "GBWL", _("West Lothian")
    WEST_MIDLANDS = "GBWM", _("West Midlands")
    WINDSOR_AND_MAIDENHEAD = "GBWN", _("Windsor and Maidenhead")
    WOKINGHAM = "GBWO", _("Wokingham")
    WORCESTERSHIRE = "GBWR", _("Worcestershire")
    WILTSHIRE = "GBWS", _("Wiltshire")
    WREXHAM = "GBWX", _("Wrexham")
    WEST_YORKSHIRE = "GBWY", _("West Yorkshire")
    EAST_SUSSEX = "GBXE", _("East Sussex")
    WEST_SUSSEX = "GBXW", _("West Sussex")
    YORK = "GBYO", _("York")
    GREENLAND = "GD--", _("Greenland")
    QASIGIANNQUIT = "GD01", _("Qasigiannquit")
    AASIAAT = "GD03", _("Aasiaat")
    PAAMIUT = "GD05", _("Paamiut")
    QEQERTARSUAQ = "GD07", _("Qeqertarsuaq")
    NUUK = "GD09", _("Nuuk")
    SISIMIUT = "GD11", _("Sisimiut")
    IVITTUUT = "GD13", _("Ivittuut")
    ILULISSAT = "GD15", _("Ilulissat")
    QAQORTOQ = "GD17", _("Qaqortoq")
    KANGAATSIAQ = "GD19", _("Kangaatsiaq")
    NANORTALIK = "GD21", _("Nanortalik")
    NARSAQ = "GD23", _("Narsaq")
    MANIITSOQ = "GD25", _("Maniitsoq")
    UUMMANNAQ = "GD27", _("Uummannaq")
    UPERNAVIK = "GD29", _("Upernavik")
    AVANERSUQ = "GD41", _("Avanersuq")
    TASIILAQ = "GD51", _("Tasiilaq")
    ILLOQQORTOORMIUT = "GD53", _("Illoqqortoormiut")
    KOMMUNEGARFIIT_AVATAANNI = "GD61", _("Kommunegarfiit avataanni")
    GEORGIA = "GE--", _("Georgia")
    ADZHARIA = "GE01", _("Adzharia")
    YUZHNAYA_OSETIA = "GE02", _("Yuzhnaya Osetia")
    ABKHAZIYA = "GE03", _("Abkhaziya")
    FRENCH_GUIANA = "GF00", _("French Guiana")
    UGANDA = "GG00", _("Uganda")
    GHANA = "GH00", _("Ghana")
    AFGHANISTAN = "GN00", _("Afghanistan")
    KENYA = "GP00", _("Kenya")
    GUINEA_BISSAU = "GQ00", _("Guinea Bissau")
    GREECE = "GR--", _("Greece")
    AEGEAN_ISLANDS = "GR80", _("Aegean Islands")
    IONIAN_ISLANDS = "GR81", _("Ionian Islands")
    KRITI_CRETE = "GR82", _("Kriti (Crete)")
    MAKEDONIA = "GR83", _("Makedonia")
    PELOPONNISOS = "GR84", _("Peloponnisos")
    IPEIROS = "GR85", _("Ipeiros")
    STEREA_ELLAS = "GR86", _("Sterea Ellas")
    THESSALIA = "GR87", _("Thessalia")
    THRAKI = "GR88", _("Thraki")
    GAZA_STRIP = "GS00", _("Gaza Strip")
    GUINEA = "GY00", _("Guinea")
    TIBET = "HA00", _("Tibet")
    SWITZERLAND = "HE--", _("Switzerland")
    AARGAU = "HEAG", _("Aargau")
    APPENZELL_INNERRHODEN = "HEAI", _("Appenzell Innerrhoden")
    APPENZELL_AUSSERRHODEN = "HEAR", _("Appenzell Ausserrhoden")
    BERN_BERNE = "HEBE", _("Bern/Berne")
    BASSELLAND = "HEBL", _("Basselland")
    BASELSTADT = "HEBS", _("Baselstadt")
    FRIBOURG_FREIBURG = "HEFR", _("Fribourg/Freiburg")
    GEN_VE = "HEGE", _("Gen?ve")
    GLARUS = "HEGL", _("Glarus")
    GRAUB_NDEN = "HEGR", _("Graub?nden")
    JURA_2 = "HEJU", _("Jura")
    LUZERN = "HELU", _("Luzern")
    NEUCH_TEL = "HENE", _("Neuch?tel")
    NIDWALDEN = "HENW", _("Nidwalden")
    OBWALDEN = "HEOW", _("Obwalden")
    ST_GALLEN = "HESG", _("St. Gallen")
    SCHAFFHAUSEN = "HESH", _("Schaffhausen")
    SOLOTHURN = "HESO", _("Solothurn")
    SCHWYZ = "HESZ", _("Schwyz")
    THURGAU = "HETG", _("Thurgau")
    TICINO = "HETI", _("Ticino")
    URI = "HEUR", _("Uri")
    VAUD = "HEVD", _("Vaud")
    VALAIS = "HEVS", _("Valais")
    ZUG = "HEZG", _("Zug")
    Z_RICH = "HEZH", _("Z?rich")
    HUNGARY = "HG--", _("Hungary")
    HUNGARY_WEST = "HG3-", _("Hungary West")
    BARANYA = "HG30", _("Baranya")
    FEJ_R = "HG31", _("Fej?r")
    GY_R_MOSIN_SOPRON = "HG32", _("Gy?r-Mosin-Sopron")
    KOM_ROM_ESZTERGOM = "HG33", _("Kom?rom-Esztergom")
    SOMOGY = "HG34", _("Somogy")
    TOLNA = "HG35", _("Tolna")
    VAS = "HG36", _("Vas")
    VESZPR_M = "HG37", _("Veszpr?m")
    ZALA = "HG38", _("Zala")
    HUNGARY_EAST = "HG4-", _("Hungary East")
    B_CS_KISKUN = "HG40", _("B?cs-Kiskun")
    B_K_S = "HG41", _("B?k?s")
    BORSOD_ABA_J_ZEMPL_N = "HG42", _("Borsod-Aba?j-Zempl?n")
    CSONGR_D = "HG43", _("Csongr?d")
    HAJDU_BIHAR = "HG44", _("Hajdu-Bihar")
    HEVES = "HG45", _("Heves")
    J_SZ_NAGYKUN_SZOLNOK = "HG46", _("J?sz-Nagykun-Szolnok")
    N_GR_D = "HG47", _("N?gr?d")
    PEST = "HG48", _("Pest")
    SZABOLCS_SZATM_R_BEREG = "HG49", _("Szabolcs-Szatm?r-Bereg")
    GUINEA_ISLANDS = "HH00", _("Guinea Islands")
    NEPAL = "HJ00", _("Nepal")
    CROATIA = "HR--", _("Croatia")
    CENTRAL_CROATIA = "HR01", _("Central Croatia")
    EASTERN_CROATIA = "HR02", _("Eastern Croatia")
    MOUNTAIN_CROATIA = "HR03", _("Mountain Croatia")
    NORTHERN_CROATIAN_COAST = "HR04", _("Northern Croatian Coast")
    SOUTHERN_CROATIAN_COAST = "HR05", _("Southern Croatian Coast")
    TANZANIA = "HT00", _("Tanzania")
    ITALY = "IA--", _("Italy")
    ALPINE_AREA = "IA0-", _("Alpine area")
    BELLUNO = "IA00", _("Belluno")
    BERGAMO = "IA01", _("Bergamo")
    BOLZANO = "IA02", _("Bolzano")
    BRESCIA = "IA03", _("Brescia")
    COMO_SONDRIO_VARESE = "IA04", _("Como & Sondrio & Varese")
    CUNEO = "IA05", _("Cuneo")
    NOVARA_VERCELLI = "IA06", _("Novara & Vercelli")
    TORINO = "IA07", _("Torino")
    TRENTO = "IA08", _("Trento")
    VALLE_D_AOSTA = "IA09", _("Valle d'Aosta")
    PO_AREA = "IA1-", _("Po area")
    ALESSANDRIA_ASTI = "IA10", _("Alessandria & Asti")
    BOLOGNA = "IA11", _("Bologna")
    CREMONA_MANTOVA = "IA12", _("Cremona & Mantova")
    MILANO = "IA13", _("Milano")
    MODENA = "IA14", _("Modena")
    PARMA_REGGIO_N_EMILIA = "IA15", _("Parma & Reggio n.Emilia")
    PAVIA = "IA16", _("Pavia")
    PIACENZA = "IA17", _("Piacenza")
    VERONA = "IA18", _("Verona")
    VICENZA = "IA19", _("Vicenza")
    NORTH_TYRRHENIAN = "IA2-", _("North Tyrrhenian")
    AREZZO = "IA20", _("Arezzo")
    FIRENZE = "IA21", _("Firenze")
    GENOVA_MASSA_CARRARA_LA_SPEZIA = "IA22", _("Genova & Massa; Carrara & La Spezia")
    GROSSETO = "IA23", _("Grosseto")
    IMPERIA_SAVONA = "IA24", _("Imperia & Savona")
    LIVORNO_PISA = "IA25", _("Livorno & Pisa")
    LUCCA_PISTOIA = "IA26", _("Lucca & Pistoia")
    SIENA = "IA27", _("Siena")
    TERNI = "IA28", _("Terni")
    VITERBO = "IA29", _("Viterbo")
    NORTH_ADRIATIC = "IA3-", _("North Adriatic")
    ANCONA_PESARO_E_URBINO = "IA30", _("Ancona & Pesaro e Urbino")
    ASCOLI_PICENO_MACERATA = "IA31", _("Ascoli Piceno & Macerata")
    FERRARA_ROVIGO = "IA32", _("Ferrara & Rovigo")
    FORLI = "IA33", _("Forli")
    GORIZIA_UDINE = "IA34", _("Gorizia & Udine")
    PADOVA = "IA35", _("Padova")
    PERUGIA = "IA36", _("Perugia")
    RAVENNA = "IA37", _("Ravenna")
    TREVISO = "IA38", _("Treviso")
    VENEZIA = "IA39", _("Venezia")
    SOUTH_TYRRHENIAN = "IA4-", _("South Tyrrhenian")
    AVELLINO = "IA40", _("Avellino")
    BENEVENTO = "IA41", _("Benevento")
    CASERTA_NAPOLI = "IA42", _("Caserta & Napoli")
    CATANZARO = "IA43", _("Catanzaro")
    COSENZA = "IA44", _("Cosenza")
    FROSINONE_LATINA = "IA45", _("Frosinone & Latina")
    POTENZA = "IA46", _("Potenza")
    REGGIO_DI_CALABRIA = "IA47", _("Reggio di Calabria")
    ROMA = "IA48", _("Roma")
    SALERNO = "IA49", _("Salerno")
    SOUTH_ADRIATIC = "IA5-", _("South Adriatic")
    L_AQUILA_D_ABRUZZI = "IA50", _("L?Aquila d.Abruzzi")
    BARI = "IA51", _("Bari")
    BRINDISI_LECCE = "IA52", _("Brindisi & Lecce")
    CAMPOBASSO = "IA53", _("Campobasso")
    CHIETI = "IA54", _("Chieti")
    FOGGIA = "IA55", _("Foggia")
    MATERA = "IA56", _("Matera")
    PESCARA_TERAMO = "IA57", _("Pescara & Teramo")
    RIETI = "IA58", _("Rieti")
    TARANTO_IONIO = "IA59", _("Taranto (Ionio)")
    ITALIAN_ISLANDS = "IA6-", _("Italian Islands")
    ELBA = "IA61", _("Elba")
    SARDEGNA_SARDINIA = "IA62", _("Sardegna (Sardinia)")
    SICILIA_INCLUDING_ISLANDS_TO_W_N = "IA63", _("Sicilia (including islands to W & N)")
    NOT_USED = "IA64", _("not used")
    PANTELLERIA = "IA65", _("Pantelleria")
    ISOLE_PELAGIE = "IA66", _("Isole Pelagie")
    TRIESTE = "IA76", _("Trieste")
    ISRAEL = "IL00", _("Israel")
    INDIA = "IN--", _("India")
    ANDHRA_PRADESH = "INAP", _("Andhra Pradesh")
    ASSAM = "INAS", _("Assam")
    BIHAR = "INBI", _("Bihar")
    MAHARASHTRA = "INBO", _("Maharashtra")
    DELHI = "INDE", _("Delhi")
    HIMACHAL_PRADESH = "INHP", _("Himachal Pradesh")
    JAMMU_AND_KASHMIR = "INJK", _("Jammu and Kashmir")
    KERALA = "INKE", _("Kerala")
    MADHYA_PRADESH = "INMP", _("Madhya Pradesh")
    MANIPUR = "INMR", _("Manipur")
    TAMIL_NADU = "INMS", _("Tamil Nadu")
    KARNATAKA = "INMY", _("Karnataka")
    ORISSA = "INOR", _("Orissa")
    PONDICHERRY = "INPO", _("Pondicherry")
    PUNJAB = "INPU", _("Punjab")
    RAJASTHAN = "INRA", _("Rajasthan")
    TRIPURA = "INTR", _("Tripura")
    UTTAR_PRADESH = "INUP", _("Uttar Pradesh")
    WEST_BENGAL = "INWB", _("West Bengal")
    BRITISH_INDIAN_OCEAN_TERRITORIES = "IO00", _("British Indian Ocean Territories")
    IRAN = "IP00", _("Iran")
    IRAQ = "IQ00", _("Iraq")
    ICELAND = "IS--", _("Iceland")
    REYKJAV_K = "IS01", _("Reykjav?k")
    KJ_SARS_SLA = "IS02", _("Kj?sars?sla")
    BORGARFJAR_ARS_SLA = "IS03", _("Borgarfjar?ars?sla")
    M_RAS_SLA = "IS04", _("M?ras?sla")
    HNAPPADALSS_SLA = "IS05", _("Hnappadalss?sla")
    SN_FELLSNESS_SLA = "IS06", _("Sn?fellsness?sla")
    DALAS_SLA = "IS07", _("Dalas?sla")
    AUSTUR_BAR_ASTRANDAS_SLA = "IS08", _("Austur-Bar?astrandas?sla")
    VESTUR_BAR_ASTRANDAS_SLA = "IS09", _("Vestur-Bar?astrandas?sla")
    VESTUR_SAFJAR_ARS_SLA = "IS10", _("Vestur-?safjar?ars?sla")
    NOR_UR_SAFJAR_ARS_SLA = "IS11", _("Nor?ur-?safjar?ars?sla")
    STRANDAS_SLA = "IS12", _("Strandas?sla")
    VESTUR_H_NAVATNSS_SLA = "IS13", _("Vestur-H?navatnss?sla")
    AUSTUR_H_NAVATNSS_SLA = "IS14", _("Austur-H?navatnss?sla")
    SKAGAFJAR_ARS_SLA = "IS15", _("Skagafjar?ars?sla")
    EYJAFJAR_ARS_SLA = "IS16", _("Eyjafjar?ars?sla")
    SU_UR_INGEYJARS_SLA = "IS17", _("Su?ur-?ingeyjars?sla")
    NOR_UR_INGEYJARS_SLA = "IS18", _("Nor?ur-?ingeyjars?sla")
    NOR_UR_M_LAS_SLA = "IS19", _("Nor?ur-M?las?sla")
    SU_UR_M_LAS_SLA = "IS20", _("Su?ur-M?las?sla")
    AUSTUR_SKAFTAFELLSS_SLA = "IS21", _("Austur-Skaftafellss?sla")
    VESTUR_SKAFTAFELLSS_SLA = "IS22", _("Vestur-Skaftafellss?sla")
    RANG_RVALLAS_SLA = "IS23", _("Rang?rvallas?sla")
    RNESS_SLA = "IS24", _("?rness?sla")
    GULLBRINGUS_SLA = "IS25", _("Gullbringus?sla")
    VESTMANNAEYJAR = "IS26", _("Vestmannaeyjar")
    MI_H_LENDI = "IS27", _("Mi?h?lendi")
    JAPAN = "JH00", _("Japan")
    KUWAIT = "JI00", _("Kuwait")
    JORDAN = "JO00", _("Jordan")
    UNITED_ARAB_EMIRATES = "JR00", _("United Arab Emirates")
    YEMEN = "JZ00", _("Yemen")
    CHILE = "KA00", _("Chile")
    KYRGYZSTAN = "KI--", _("Kyrgyzstan")
    ISSYK_KUL_O_PRZHEVALSK = "KI01", _("Issyk-Kul'O. Przhevalsk")
    NARYN_O = "KI02", _("Naryn O.")
    TALAS_O = "KI03", _("Talas O.")
    PERU = "KJ00", _("Peru")
    COMOROS = "KM00", _("Comoros")
    LUXEMBOURG_2 = "KN00", _("Luxembourg")
    KAZAKHSTAN = "KZ--", _("Kazakhstan")
    AKTYUBINSK_O = "KZ00", _("Aktyubinsk O.")
    ALMA_ATA_O = "KZ01", _("Alma-Ata O.")
    CHIMKENT_O = "KZ03", _("Chimkent O.")
    DZHAMBUL_O = "KZ04", _("Dzhambul O.")
    GUR_YEV_O = "KZ06", _("Gur'yev O.")
    KARAGANDA_O = "KZ07", _("Karaganda O.")
    TURGAISK_O = "KZ09", _("Turgaisk O.")
    KZYL_ORDA_O = "KZ10", _("Kzyl-Orda O.")
    PAVLODAR_O = "KZ11", _("Pavlodar O.")
    SEVERO_KAZAKHSTAN_O = "KZ12", _("Severo-Kazakhstan O.")
    SEMIPALATINSK_O = "KZ13", _("Semipalatinsk O.")
    TALDY_KURGAN_O = "KZ14", _("Taldy-Kurgan O.")
    AKMOLINSK_O = "KZ15", _("Akmolinsk O.")
    URAL_SK_O = "KZ16", _("Ural'sk O.")
    VOSTOCHNO_KAZAKHSTAN_O = "KZ17", _("Vostochno-Kazakhstan O.")
    LESSER_ANTILLES = "LA00", _("Lesser Antilles")
    LEBANON = "LE00", _("Lebanon")
    LITHUANIA = "LI00", _("Lithuania")
    DOMINICAN_REPUBLIC = "LJDA", _("Dominican Republic")
    HAITI = "LJHA", _("Haiti")
    PUERTO_RICO = "LJPA", _("Puerto Rico")
    LIBYA = "LT00", _("Libya")
    LATVIA = "LV00", _("Latvia")
    MOROCCO = "MA00", _("Morocco")
    B_NI_MELLAL_KH_NIFRA = "MABM", _("Béni Mellal-Khénifra")
    CASABLANCA_SETTAT = "MACS", _("Casablanca-Settat")
    DAKHLA_OUED_ED_DAHAB = "MADO", _("Dakhla-Oued Ed-Dahab")
    DR_A_TAFILALET = "MADT", _("Drâa-Tafilalet")
    F_Z_MEKN_S = "MAFM", _("Féz-Meknès")
    GUELMIM_OUED_NOUN = "MAGO", _("Guelmim-Oued Noun")
    L_ORIENTAL = "MALO", _("L'Oriental")
    LA_YOUNE_SAKIA_EL_HAMRA = "MALS", _("Laâyoune-Sakia El Hamra")
    MARRAKECH_SAFI = "MAMS", _("Marrakech-Safi")
    RABAT_SAL_K_NITRA = "MARS", _("Rabat-Salé-Kénitra")
    SOUSS_MASSA = "MASM", _("Souss-Massa")
    TANGER_T_TOUAN_AL_HOCE_MA = "MATT", _("Tanger-Tétouan-aL Hoceïma")
    MOLDOVA = "MD00", _("Moldova")
    MONTENEGRO = "ME00", _("Montenegro")
    MADAGASCAR = "MG00", _("Madagascar")
    MELILLA = "MJ00", _("Melilla")
    MACEDONIA = "MK00", _("Macedonia")
    MALTA = "ML00", _("Malta")
    MONGOLIA = "MN00", _("Mongolia")
    MOZAMBIQUE = "MQ00", _("Mozambique")
    MAURITIUS = "MU00", _("Mauritius")
    MALDIVES = "MV00", _("Maldives")
    MALAWI = "MY00", _("Malawi")
    UNITED_STATES_OF_AMERICA = "NA--", _("United States of America")
    ARKANSAS = "NAAK", _("Arkansas")
    ALABAMA = "NAAL", _("Alabama")
    ARIZONA = "NAAZ", _("Arizona")
    CALIFORNIA = "NACA", _("California")
    COLORADO = "NACL", _("Colorado")
    CONNECTICUT = "NACN", _("Connecticut")
    DISTRICT_OF_COLUMBIA = "NADC", _("District of Columbia")
    DELAWARE = "NADE", _("Delaware")
    FLORIDA = "NAFL", _("Florida")
    GEORGIA_2 = "NAGE", _("Georgia")
    IDAHO = "NAID", _("Idaho")
    ILLINOIS = "NAIL", _("Illinois")
    INDIANA = "NAIN", _("Indiana")
    IOWA = "NAIO", _("Iowa")
    KANSAS = "NAKA", _("Kansas")
    KENTUCKY = "NAKE", _("Kentucky")
    LOUISIANA = "NALO", _("Louisiana")
    MAINE = "NAMA", _("Maine")
    MICHIGAN = "NAMC", _("Michigan")
    MINNESOTA = "NAMN", _("Minnesota")
    MONTANA_2 = "NAMO", _("Montana")
    MISSISSIPPI = "NAMP", _("Mississippi")
    MISSOURI = "NAMR", _("Missouri")
    MASSACHUSETTS = "NAMS", _("Massachusetts")
    MARYLAND = "NAMY", _("Maryland")
    NEBRASKA = "NANA", _("Nebraska")
    NORTH_CAROLINA = "NANC", _("North Carolina")
    NORTH_DAKOTA = "NAND", _("North Dakota")
    NEW_HAMPSHIRE = "NANH", _("New Hampshire")
    NEW_JERSEY = "NANJ", _("New Jersey")
    NEVADA = "NANV", _("Nevada")
    NEW_YORK = "NANY", _("New York")
    OHIO = "NAOH", _("Ohio")
    OKLAHOMA = "NAOK", _("Oklahoma")
    OREGON = "NAOR", _("Oregon")
    PENNSYLVANIA = "NAPE", _("Pennsylvania")
    RHODE_ISLAND = "NARI", _("Rhode Island")
    SOUTH_CAROLINA = "NASC", _("South Carolina")
    SOUTH_DAKOTA = "NASD", _("South Dakota")
    TENNESSEE = "NATN", _("Tennessee")
    TEXAS = "NATX", _("Texas")
    UTAH = "NAUT", _("Utah")
    VERMONT = "NAVE", _("Vermont")
    VIRGINIA = "NAVI", _("Virginia")
    WASHINGTON = "NAWA", _("Washington")
    WISCONSIN = "NAWI", _("Wisconsin")
    WEST_VIRGINIA = "NAWV", _("West Virginia")
    WYOMING = "NAWY", _("Wyoming")
    GIBRALTAR = "NB00", _("Gibraltar")
    NEW_CALEDONIA = "NC00", _("New Caledonia")
    WESTERN_SAHARA = "ND00", _("Western Sahara")
    NIGER = "NE00", _("Niger")
    THE_NETHERLANDS = "NL--", _("The Netherlands")
    TEXEL = "NL00", _("Texel")
    VLIELAND = "NL01", _("Vlieland")
    GRIEND = "NL02", _("Griend")
    TERSCHELLING = "NL03", _("Terschelling")
    DRENTHE = "NL04", _("Drenthe")
    FRIESLAND = "NL05", _("Friesland")
    GELDERLAND = "NL06", _("Gelderland")
    GRONINGEN = "NL07", _("Groningen")
    LIMBURG_2 = "NL08", _("Limburg")
    NOORD_BRABANT = "NL09", _("Noord-Brabant")
    AMELAND = "NL11", _("Ameland")
    SCHIERMONNIKOOG = "NL12", _("Schiermonnikoog")
    ROTTUMEROOG = "NL13", _("Rottumeroog")
    NOORD_HOLLAND = "NL14", _("Noord-Holland")
    OVERIJSSEL = "NL15", _("Overijssel")
    UTRECHT = "NL16", _("Utrecht")
    IJSSELMEERPOLDERS = "NL17", _("IJsselmeerpolders")
    ZEELAND = "NL18", _("Zeeland")
    ZUID_HOLLAND = "NL19", _("Zuid-Holland")
    MAURITANIA = "NM00", _("Mauritania")
    HODH_ECH_CHARGUI = "NM01", _("Hodh ech Chargui")
    HODH_EL_GHARBI = "NM02", _("Hodh el Gharbi")
    ASSABA = "NM03", _("Assaba")
    GORGOL = "NM04", _("Gorgol")
    BRAKNA = "NM05", _("Brakna")
    TRARZA = "NM06", _("Trarza")
    ADRAR = "NM07", _("Adrar")
    DAKHLET_NOU_DHIBOU = "NM08", _("Dakhlet Nou?dhibou")
    TAGANT = "NM09", _("Tagant")
    GUIDIMAKA = "NM10", _("Guidimaka")
    TIRIS_ZEMMOUR = "NM11", _("Tiris Zemmour")
    INCHIRI = "NM12", _("Inchiri")
    NOUAKCHOTT = "NMNK", _("Nouakchott")
    NORWAY = "NO--", _("Norway")
    AKERSHUS_OSLO_INCLUDED = "NO20", _("Akershus (Oslo included)")
    AUST_AGDER = "NO21", _("Aust-Agder")
    BUSKERUD = "NO22", _("Buskerud")
    FINNMARK = "NO23", _("Finnmark")
    HEDMARK = "NO24", _("Hedmark")
    HORDALAND_BERGEN_INCLUDED = "NO25", _("Hordaland (Bergen included)")
    M_RE_OG_ROMSDAL = "NO26", _("M?re og Romsdal")
    NORDLAND = "NO27", _("Nordland")
    NORD_TR0NDELAG = "NO28", _("Nord-Tr0ndelag")
    OPLAND = "NO29", _("Opland")
    STFOLD = "NO30", _("?stfold")
    ROGALAND = "NO31", _("Rogaland")
    SOGN_OG_FJORDANE = "NO32", _("Sogn og Fjordane")
    S_R_TR_NDELAG = "NO33", _("S?r-Tr?ndelag")
    TELEMARK = "NO34", _("Telemark")
    TROMS = "NO35", _("Troms")
    VEST_AGDER = "NO36", _("Vest-Agder")
    VESTFOLD = "NO37", _("Vestfold")
    SENEGAL = "NU00", _("Senegal")
    NIGERIA = "NV00", _("Nigeria")
    PHILIPPINES = "OE00", _("Philippines")
    OMAN = "OM00", _("Oman")
    INDONESIA = "ON00", _("Indonesia")
    BORNEO_ISLAND = "OV00", _("Borneo Island")
    BRUNEI = "OVB0", _("Brunei")
    INDONESIAN_PART = "OVI0", _("Indonesian part")
    MALAYSIAN_PART = "OVM0", _("Malaysian part")
    SIERRA_LEONE = "PH00", _("Sierra Leone")
    PACIFIC_ISLANDS = "PI00", _("Pacific Islands")
    POLAND = "PL--", _("Poland")
    LUBELSKIE = "PLBE", _("Lubelskie")
    LUBUSKIE = "PLBU", _("Lubuskie")
    DOLNOSLASKIE = "PLDO", _("Dolnoslaskie")
    KUJAWSKO_POMORSKIE = "PLKP", _("Kujawsko-Pomorskie")
    L_DZKIE = "PLLO", _("L?dzkie")
    MALOPOLSKIE = "PLMP", _("Malopolskie")
    MAZOWIECKIE = "PLMZ", _("Mazowieckie")
    OPOLSKIE = "PLOE", _("Opolskie")
    PODKARPACKIE = "PLPC", _("Podkarpackie")
    POMORSKIE = "PLPM", _("Pomorskie")
    PODLASKIE = "PLPS", _("Podlaskie")
    SLASKIE = "PLSL", _("Slaskie")
    SWIETOKRZYSKIE = "PLSW", _("Swietokrzyskie")
    WIELKOPOLSKIE = "PLWI", _("Wielkopolskie")
    WARMINSKO_MAZURSKIE = "PLWM", _("Warminsko-Mazurskie")
    ZACHODNIO_POMORSKIE = "PLZP", _("Zachodnio-Pomorskie")
    PAKISTAN = "PN00", _("Pakistan")
    PORTUGAL = "PO--", _("Portugal")
    AVEIRO = "PO01", _("Aveiro")
    BEJA = "PO02", _("Beja")
    BRAGA = "PO03", _("Braga")
    BRAGAN_A = "PO04", _("Bragan?a")
    CASTELO_BRANCO = "PO05", _("Castelo Branco")
    COIMBRA = "PO06", _("Coimbra")
    VORA = "PO07", _("?vora")
    FARO = "PO08", _("Faro")
    GUARDA = "PO09", _("Guarda")
    LEIRIA = "PO10", _("Leiria")
    LISBOA = "PO11", _("Lisboa")
    PORTALEGRE = "PO12", _("Portalegre")
    PORTO = "PO13", _("Porto")
    SANTAR_M = "PO14", _("Santar?m")
    SET_BAL = "PO15", _("Set?bal")
    VIANA_DO_CASTELO = "PO16", _("Viana do Castelo")
    VILA_REAL = "PO17", _("Vila Real")
    VISEU = "PO18", _("Viseu")
    ILHA_DA_TERCEIRA_AZORES = "PO19", _("Ilha da Terceira, Azores")
    ILHA_DO_FAIAL_AZORES = "PO20", _("Ilha do Faial, Azores")
    ILHA_DE_S_O_MIGUEL_AZORES = "PO21", _("Ilha de S?o Miguel, Azores")
    ILHA_DA_MADEIRA_MADEIRA = "PO22", _("Ilha da Madeira, Madeira")
    ILHA_DE_SANTA_MARIA_AZORES = "PO23", _("Ilha de Santa Maria, Azores")
    ILHA_GRACIOSA_AZORES = "PO24", _("Ilha Graciosa, Azores")
    ILHA_DE_S_O_JORGE_AZORES = "PO25", _("Ilha de S?o Jorge, Azores")
    ILHA_DO_PICO_AZORES = "PO26", _("Ilha do Pico, Azores")
    ILHA_DAS_FLORES_AZORES = "PO27", _("Ilha das Flores, Azores")
    ILHA_DO_CORVO_AZORES = "PO28", _("Ilha do Corvo, Azores")
    ILHA_DE_PORTO_SANTO_MADEIRA = "PO29", _("Ilha de Porto Santo, Madeira")
    RWANDA = "PP00", _("Rwanda")
    LIBERIA = "PQ00", _("Liberia")
    GAZA_STRIP_2 = "PSGZ", _("Gaza Strip")
    WEST_BANK = "PSWB", _("West Bank")
    BURUNDI = "PX00", _("Burundi")
    C_TE_D_IVOIRE = "PY00", _("C?te d`Ivoire")
    BHUTAN = "QA00", _("Bhutan")
    ZANZIBAR_PEMBA = "QC00", _("Zanzibar & Pemba")
    CENTRAL_AFRICAN_REPUBLIC = "QH00", _("Central African Republic")
    SIKKIM = "QJ00", _("Sikkim")
    CAMEROON = "QQ00", _("Cameroon")
    GABON = "QY00", _("Gabon")
    VATICAN_CITY = "RA48", _("Vatican City")
    REUNION = "RE00", _("Reunion")
    BANGLADESH = "RN00", _("Bangladesh")
    ROMANIA = "RO--", _("Romania")
    ALBA = "ROAB", _("Alba")
    ARGES = "ROAG", _("Arges")
    ARAD = "ROAR", _("Arad")
    BUCURESTI = "ROB-", _("Bucuresti")
    BACAU = "ROBC", _("Bacau")
    BIHOR = "ROBH", _("Bihor")
    BISTRITA_NASAUD = "ROBN", _("Bistrita-Nasaud")
    BRAILA = "ROBR", _("Braila")
    BOTOSANI = "ROBT", _("Botosani")
    BRASOV = "ROBV", _("Brasov")
    BUZAU = "ROBZ", _("Buzau")
    CLUJ = "ROCJ", _("Cluj")
    CALARASI = "ROCL", _("Calarasi")
    CARAS_SEVERIN = "ROCS", _("Caras-Severin")
    CONSTANTA = "ROCT", _("Constanta")
    COVASNA = "ROCV", _("Covasna")
    DAMBOVITA = "RODB", _("Dambovita")
    DOLJ = "RODJ", _("Dolj")
    GORJ = "ROGJ", _("Gorj")
    GALATI = "ROGL", _("Galati")
    GIURGIU = "ROGR", _("Giurgiu")
    HUNEDOARA = "ROHD", _("Hunedoara")
    HARGHITA = "ROHR", _("Harghita")
    ILFOV = "ROIF", _("Ilfov")
    IALOMITA = "ROIL", _("Ialomita")
    IASI = "ROIS", _("Iasi")
    MEHEDINTI = "ROMH", _("Mehedinti")
    MARAMURES = "ROMM", _("Maramures")
    MURES = "ROMS", _("Mures")
    NEAMT = "RONT", _("Neamt")
    OLT = "ROOT", _("Olt")
    PRAHOVA = "ROPH", _("Prahova")
    SIBIU = "ROSB", _("Sibiu")
    SALAJ = "ROSJ", _("Salaj")
    SATU_MARE = "ROSM", _("Satu Mare")
    SUCEAVA = "ROSV", _("Suceava")
    TULCEA = "ROTL", _("Tulcea")
    TIMIS = "ROTM", _("Timis")
    TELEORMAN = "ROTR", _("Teleorman")
    VALCEA = "ROVL", _("Valcea")
    VRANCEA = "ROVN", _("Vrancea")
    VASLUI = "ROVS", _("Vaslui")
    REPUBLIC_OF_SERBIA = "RS--", _("Republic of Serbia")
    KOSOVO = "RS74", _("Kosovo")
    SERBIA = "RS77", _("Serbia")
    VOJVODINA = "RS78", _("Vojvodina")
    RUSSIAN_FEDERATION = "RU--", _("Russian Federation")
    MURMANSK_O = "RU01", _("Murmansk O.")
    KARELIA = "RU02", _("Karelia")
    LENINGRAD_O = "RU03", _("Leningrad O.")
    KALININGRAD_O = "RU04", _("Kaliningrad O.")
    PSKOV_O = "RU05", _("Pskov O.")
    NOVGOROD_O = "RU06", _("Novgorod O.")
    ARKHANGELSK_O = "RU07", _("Arkhangelsk O.")
    NENETS_A_O = "RU08", _("Nenets A.O.")
    KOMI = "RU09", _("Komi")
    FRANZ_JOSEF_LAND = "RU10", _("Franz Josef Land")
    NOVAYA_ZEMLYA = "RU11", _("Novaya Zemlya")
    VOLOGDA_O = "RU12", _("Vologda O.")
    YAROSLAVL_O = "RU13", _("Yaroslavl' O.")
    TVER_O = "RU14", _("Tver' O.")
    KOSTROMA_O = "RU15", _("Kostroma O.")
    IVANOVO_O = "RU16", _("Ivanovo O.")
    MOSCOW_O = "RU17", _("Moscow O.")
    VLADIMIR_O = "RU18", _("Vladimir O.")
    SMOLENSK_O = "RU19", _("Smolensk O.")
    KALUGA_O = "RU20", _("Kaluga O.")
    TULA_O = "RU21", _("Tula O.")
    RYAZAN_O = "RU22", _("Ryazan' O.")
    KIROV_O = "RU23", _("Kirov O.")
    PERM_O = "RU24", _("Perm' O.")
    UDMURTIA = "RU25", _("Udmurtia")
    NIZHNIY_NOVGOROD_O = "RU26", _("Nizhniy Novgorod O.")
    MARIY_EL = "RU27", _("Mariy El")
    CHUVASHIA = "RU28", _("Chuvashia")
    MORDOVIA_O = "RU29", _("Mordovia O.")
    TATARIA = "RU30", _("Tataria")
    UL_YANOVSK_O = "RU31", _("Ul'yanovsk O.")
    PENZA_O = "RU32", _("Penza O.")
    SAMARA_O = "RU33", _("Samara O.")
    SARATOV_O = "RU34", _("Saratov O.")
    BRYANSK_O = "RU35", _("Bryansk O.")
    OREL_O = "RU36", _("Orel O.")
    KURSK_O = "RU37", _("Kursk O.")
    LIPETSK_O = "RU38", _("Lipetsk O.")
    TAMBOV_O = "RU39", _("Tambov O.")
    VORONEZH_O = "RU40", _("Voronezh O.")
    BELGOROD_O = "RU41", _("Belgorod O.")
    VOLGOGRAD_O = "RU42", _("Volgograd O.")
    ROSTOV_O = "RU43", _("Rostov O.")
    ASTRAKHAN_O = "RU44", _("Astrakhan' O.")
    KALMYKIA = "RU45", _("Kalmykia")
    KRASNODAR = "RU46", _("Krasnodar")
    STAVROPOL_O = "RU47", _("Stavropol' O.")
    KARACHAYEVO_CHERKESSIA = "RU48", _("Karachayevo-Cherkessia")
    KABARDINO_BALKARIA = "RU49", _("Kabardino-Balkaria")
    SEVERNAYA_OSETIA = "RU50", _("Severnaya Osetia")
    INGUSHETIA = "RU51", _("Ingushetia")
    CHECHNYA = "RU52", _("Chechnya")
    DAGESTAN = "RU53", _("Dagestan")
    SVERDLOVSK_O = "RU54", _("SVERDLOVSK O.")
    KURGAN_O = "RU55", _("Kurgan O.")
    CHELYABINSK_O = "RU56", _("Chelyabinsk O.")
    BASHKIRIA = "RU57", _("Bashkiria")
    ORENBURG_O = "RU58", _("Orenburg O.")
    YAMAL_NENETS_A_O = "RU60", _("Yamal-Nenets A.O.")
    KHANTY_MANSI_A_O = "RU61", _("Khanty-Mansi A.O.")
    TYUMEN_O = "RU62", _("Tyumen' O.")
    OMSK_O = "RU63", _("Omsk O.")
    TOMSK_O = "RU64", _("Tomsk O.")
    NOVOSIBIRSK_O = "RU65", _("Novosibirsk O.")
    KEMEROVO_O = "RU66", _("Kemerovo O.")
    ALTAY_INCL_GORNO_ALTAYSK = "RU67", _("Altay (incl. Gorno-Altaysk)")
    SEVERNAYA_ZEMLYA_ISLANDS = "RU68", _("Severnaya Zemlya Islands")
    TAYMYR_A_O = "RU69", _("Taymyr A.O.")
    EVENKIY_A_O = "RU70", _("Evenkiy A.O.")
    KRASNOYARSK = "RU71", _("Krasnoyarsk")
    KHAKASSIA = "RU72", _("Khakassia")
    TUVA = "RU73", _("Tuva")
    IRKUTSK_O = "RU74", _("Irkutsk O.")
    BURYATIA = "RU75", _("Buryatia")
    CHITA_O = "RU76", _("Chita O.")
    NOVOSIBIRSKIYE_ISLANDS = "RU77", _("Novosibirskiye Islands")
    YAKUTIA_SAKHA = "RU78", _("Yakutia-Sakha")
    WRANGEL_ISLAND = "RU79", _("Wrangel Island")
    CHUKOTKA = "RU80", _("Chukotka")
    MAGADAN_O = "RU81", _("Magadan O.")
    KAMCHATKA_O = "RU82", _("Kamchatka O.")
    AMUR_O = "RU83", _("Amur O.")
    KHABAROVSK = "RU84", _("Khabarovsk")
    PRIMORSKIY = "RU85", _("Primorskiy")
    SAKHALIN_O = "RU86", _("Sakhalin O.")
    KURIL_ISLANDS = "RU87", _("Kuril Islands")
    BAIKAL_REGION = "RUBS", _("Baikal Region")
    CENTRAL_BLACKSOIL_REGION = "RUCB", _("Central Blacksoil Region")
    CENTRE_OF_EUROPEAN_RUSSIA = "RUCE", _("Centre of European Russia")
    CENTRAL_SIBERIA = "RUCS", _("Central Siberia")
    FAR_EAST = "RUFE", _("Far East")
    MIDDLE_VOLGA = "RUMV", _("Middle Volga")
    NORTH_CAUCASUS = "RUNC", _("North Caucasus")
    NORTH_EAST = "RUNE", _("North-East")
    NORTH_OF_EUROPEAN_RUSSIA = "RUNR", _("North of European Russia")
    NORTH_WEST_EUROPEAN_RUSSIA = "RUNW", _("North-West European Russia")
    SOUTH_WESTERN_SIBERIA = "RUSS", _("South-Western Siberia")
    SOUTHERN_URAL = "RUSU", _("Southern Ural")
    VOLGO_DON_REGION = "RUVD", _("Volgo-Don Region")
    VOLGO_VYATKA_REGION = "RUVV", _("Volgo-Vyatka Region")
    WESTERN_SIBERIA = "RUWS", _("Western Siberia")
    YAKUTIA = "RUYS", _("Yakutia")
    BOLIVIA = "SABA", _("Bolivia")
    COLOMBIA = "SACA", _("Colombia")
    ECUADOR = "SAEA", _("Ecuador")
    GUYANA = "SAGA", _("Guyana")
    PARAGUAY = "SAPA", _("Paraguay")
    URUGUAY = "SAUA", _("Uruguay")
    SEYCHELLES = "SC00", _("Seychelles")
    FINLAND = "SF--", _("Finland")
    H_ME = "SF80", _("H?me")
    KUOPIO = "SF81", _("Kuopio")
    KYMI = "SF82", _("Kymi")
    LAPPI = "SF83", _("Lappi")
    MIKKELI = "SF84", _("Mikkeli")
    OULU = "SF85", _("Oulu")
    TURKU_PORI = "SF86", _("Turku-Pori")
    UUSIMAA = "SF87", _("Uusimaa")
    VAASA = "SF88", _("Vaasa")
    AHVENANMAA = "SF90", _("Ahvenanmaa")
    VENEZUELA = "SJ00", _("Venezuela")
    SLOVAKIA = "SK--", _("Slovakia")
    BRATISLAVA_I_II_III_IV_V = "SKBA", _("Bratislava I; II; III; IV; V")
    BANSKA_BYSTRICA = "SKBB", _("Banska Bystrica")
    BARDEJOV = "SKBJ", _("Bardejov")
    BANOVCE_NAD_BEBRAVOU = "SKBN", _("Banovce nad Bebravou")
    BREZNO = "SKBR", _("Brezno")
    BANSKA_TIAVNICA = "SKBS", _("Banska ?tiavnica")
    BYTCA = "SKBY", _("Bytca")
    CADCA = "SKCA", _("Cadca")
    DOLNY_KUBIN = "SKDK", _("Dolny Kubin")
    DUNAJSKA_STREDA = "SKDS", _("Dunajska Streda")
    DETVA = "SKDT", _("Detva")
    GALANTA = "SKGA", _("Galanta")
    GELNICA = "SKGL", _("Gelnica")
    HLOHOVEC = "SKHC", _("Hlohovec")
    HUMENNE = "SKHE", _("Humenne")
    ILAVA = "SKIL", _("Ilava")
    KRUPINA = "SKKA", _("Krupina")
    KOSICE_I_II_III_IV = "SKKE", _("Kosice I; II; III; IV")
    KEZMAROK = "SKKK", _("Kezmarok")
    KYSUCKE_NOVE_MESTO = "SKKM", _("Kysucke Nove Mesto")
    KOMARNA = "SKKN", _("Komarna")
    KOSICE_OKOLIE = "SKKS", _("Kosice;okolie")
    LUCENEC = "SKLC", _("Lucenec")
    LEVOCA = "SKLE", _("Levoca")
    LIPTOVSKY_MIKULAS = "SKLM", _("Liptovsky Mikulas")
    LEVICE = "SKLV", _("Levice")
    MALACKY = "SKMA", _("Malacky")
    MICHALOVCE = "SKMI", _("Michalovce")
    MEDZILABORCE = "SKML", _("Medzilaborce")
    MARTIN = "SKMT", _("Martin")
    MYJAVA = "SKMY", _("Myjava")
    NOVE_MESTO_NAD_VAHOM = "SKNM", _("Nove Mesto nad Vahom")
    NAMESTOVO = "SKNO", _("Namestovo")
    NITRA = "SKNR", _("Nitra")
    NOVE_ZAMKY = "SKNZ", _("Nove Zamky")
    POVAZSKA_BYSTRICA = "SKPB", _("Povazska Bystrica")
    PRIEVIDZA = "SKPD", _("Prievidza")
    PARTIZANSKE = "SKPE", _("Partizanske")
    PIESTANY = "SKPI", _("Piestany")
    PEZINOK = "SKPK", _("Pezinok")
    PRESOV = "SKPO", _("Presov")
    POPRAD = "SKPP", _("Poprad")
    POLTAR = "SKPT", _("Poltar")
    PUCHOV = "SKPU", _("Puchov")
    REVUCA = "SKRA", _("Revuca")
    RUZOMBEROK = "SKRK", _("Ruzomberok")
    RIMAVSKA_SOBOTA = "SKRS", _("Rimavska Sobota")
    ROZNAVA = "SKRV", _("Roznava")
    SALA = "SKSA", _("Sala")
    SABINOV = "SKSB", _("Sabinov")
    SENEC = "SKSC", _("Senec")
    SENICA = "SKSE", _("Senica")
    SKALICA = "SKSI", _("Skalica")
    SVIDNIK = "SKSK", _("Svidnik")
    STARA_LUBOVNA = "SKSL", _("Stara Lubovna")
    SPISSKA_NOVA_VES = "SKSN", _("Spisska Nova Ves")
    SOBRANCE = "SKSO", _("Sobrance")
    STROPKOV = "SKSP", _("Stropkov")
    SNINA = "SKSV", _("Snina")
    TRENCIN = "SKTN", _("Trencin")
    TOPOLCANY = "SKTO", _("Topolcany")
    TURCIANSKE_TEPLICE = "SKTR", _("Turcianske Teplice")
    TVRDOSIN = "SKTS", _("Tvrdosin")
    TRNAVA = "SKTT", _("Trnava")
    TREBISOV = "SKTV", _("Trebisov")
    VELKY_KRTIS = "SKVK", _("Velky Krtis")
    VRANOV_NAD_TOPLOU = "SKVT", _("Vranov nad Toplou")
    ZILINA = "SKZA", _("Zilina")
    ZARNOVICA = "SKZC", _("Zarnovica")
    ZIAR_NAD_HRONOM = "SKZH", _("Ziar nad Hronom")
    ZLATE_MORAVCE = "SKZM", _("Zlate Moravce")
    ZVOLEN = "SKZV", _("Zvolen")
    SLOVENIA = "SL00", _("Slovenia")
    SURINAME = "SR00", _("Suriname")
    SUDAN = "SS00", _("Sudan")
    ALVSBORG = "SV40", _("Alvsborg")
    BLEKINGE = "SV41", _("Blekinge")
    G_VLEBORG = "SV42", _("G?vleborg")
    G_TEBORG_OCH_BOHUS = "SV43", _("G?teborg och Bohus")
    HALLAND = "SV44", _("Halland")
    J_MTLAND = "SV45", _("J?mtland")
    J_NK_PING = "SV46", _("J?nk?ping")
    KALMAR = "SV47", _("Kalmar")
    KOPPARBERG = "SV48", _("Kopparberg")
    KRISTIANSTAD = "SV49", _("Kristianstad")
    KRONOBERG = "SV50", _("Kronoberg")
    MALM_HUS = "SV51", _("Malm?hus")
    NORRBOTTEN = "SV52", _("Norrbotten")
    REBRO = "SV53", _("?rebro")
    STERG_TLAND = "SV54", _("?sterg?tland")
    SKARABORG = "SV55", _("Skaraborg")
    S_DERMANLAND = "SV56", _("S?dermanland")
    STOCKHOLM = "SV57", _("Stockholm")
    UPPSALA = "SV58", _("Uppsala")
    V_RMLAND = "SV59", _("V?rmland")
    V_STERBOTTEN = "SV60", _("V?sterbotten")
    V_STERNORRLAND = "SV61", _("V?sternorrland")
    V_STMANLAND = "SV62", _("V?stmanland")
    SK_NE = "SV63", _("Sk?ne")
    V_STRA_G_TALAND = "SV64", _("V?stra G?taland")
    GOTLAND = "SV70", _("Gotland")
    LAND = "SV71", _("?land")
    SYRIA = "SY00", _("Syria")
    MEXICO = "TA00", _("Mexico")
    TAJIKISTAN = "TD--", _("Tajikistan")
    GORNO_BADAKHSHAN = "TD01", _("Gorno-Badakhshan")
    KHATLON_OBLAST = "TD02", _("Khatlon Oblast")
    DUSHANBE_OBLAST = "TD03", _("Dushanbe Oblast")
    SOGDI_OBLAST = "TD04", _("Sogdi Oblast")
    FRENCH_SOUTHERN_TERRITORIES = "TF00", _("French Southern Territories")
    BAHAMAS = "TJ00", _("Bahamas")
    TURKMENISTAN = "TM--", _("Turkmenistan")
    BALKAN_VELAYAT = "TM01", _("Balkan Velayat")
    DASHOGUS_VELAYAT = "TM02", _("Dashogus Velayat")
    AKHAL_VELAYAT = "TM03", _("Akhal Velayat")
    LEBAP_VELAYAT = "TM04", _("Lebap Velayat")
    MARY_VELAYAT = "TM05", _("Mary Velayat")
    TUNISIA = "TO00", _("Tunisia")
    NORTH_KOREA = "TP00", _("North Korea")
    TURKEY = "TU00", _("Turkey")
    SOUTH_KOREA = "TX00", _("South Korea")
    UKRAINE = "UK--", _("Ukraine")
    CHERKASSY_O = "UK50", _("Cherkassy O.")
    CHERNIGIV_O = "UK51", _("Chernigiv O.")
    CHERNIVTSY_O = "UK52", _("Chernivtsy O.")
    DNIPROPETROVSK_O = "UK53", _("Dnipropetrovsk O.")
    DONETSK_O = "UK54", _("Donetsk O.")
    KHARKIV_O = "UK55", _("Kharkiv O.")
    KHERSON_O = "UK56", _("Kherson O.")
    KHMEL_NITSKIY_O = "UK57", _("Khmel'nitskiy O.")
    KIROVOGRAD_O = "UK58", _("Kirovograd O.")
    KYIV_O = "UK59", _("Kyiv O.")
    KRYM = "UK60", _("Krym")
    LUGANSK_O = "UK61", _("Lugansk O.")
    VOLYNSKA_O = "UK62", _("Volynska O.")
    LVIV_O = "UK63", _("Lviv O.")
    MIKOLAYIV_O = "UK65", _("Mikolayiv O.")
    ODESA_O = "UK66", _("Odesa O.")
    POLTAVA_O = "UK67", _("Poltava O.")
    RIVNE_O = "UK68", _("Rivne O.")
    IVANO_FRANKIVSK_O = "UK69", _("Ivano-Frankivsk O.")
    SUMY_O = "UK70", _("Sumy O.")
    TERNOPIL_O = "UK71", _("Ternopil' O.")
    ZAKARPATSKA_O = "UK72", _("Zakarpatska O.")
    VINNITSA_O = "UK73", _("Vinnitsa O.")
    ZAPORIZHZHYA_O = "UK74", _("Zaporizhzhya O.")
    ZHITOMIR_O = "UK75", _("Zhitomir O.")
    UZBEKISTAN = "UZ--", _("Uzbekistan")
    ANDIZHAN_O = "UZ01", _("Andizhan O.")
    BUKHARA_O = "UZ02", _("Bukhara O.")
    DZHIZAK_O = "UZ03", _("Dzhizak O.")
    FERGANA_O = "UZ04", _("Fergana O.")
    KARA_KALPAK = "UZ05", _("Kara-Kalpak")
    KASHKADAR_IN_O = "UZ06", _("Kashkadar'in O.")
    KHOREZM_O = "UZ07", _("Khorezm O.")
    NAMANGAN_O = "UZ08", _("Namangan O.")
    NAVOI_O = "UZ09", _("Navoi O.")
    SAMARKAND_O = "UZ10", _("Samarkand O.")
    SURKHANDAR_IN_O = "UZ11", _("Surkhandar'in O.")
    SYRDAR_IN_O = "UZ12", _("Syrdar'in O.")
    TASHKENT_O = "UZ13", _("Tashkent O.")
    ALASKA = "VA00", _("Alaska")
    VIRGIN_ISLANDS = "VI00", _("Virgin Islands")
    VIRGIN_ISLANDS_BRITISH = "VIGB", _("Virgin Islands - British")
    VIRGIN_ISLANDS_AMERICAN = "VINA", _("Virgin Islands - American")
    THE_GAMBIA = "VM00", _("The Gambia")
    BURKINA_FASO = "VU00", _("Burkina Faso")
    NEW_GUINEA = "WE00", _("New Guinea")
    BOTSWANA = "WG00", _("Botswana")
    SWAZILAND = "WP00", _("Swaziland")
    MONACO = "WR80", _("Monaco")
    ZIMBABWE = "WS00", _("Zimbabwe")
    TOGO = "XH00", _("Togo")
    BENIN = "XY00", _("Benin")
    SUQUTR = "YB00", _("Suqutr?")
    BIOCO = "YH00", _("Bioco")
    EQUATORIAL_GUINEA = "YQ00", _("Equatorial Guinea")
    SOMALIA = "YS00", _("Somalia")
    MAYOTTE = "YT00", _("Mayotte")
    CONGO = "YY00", _("Congo")
    SAN_MARINO = "ZA33", _("San Marino")
    SRI_LANKA = "ZE00", _("Sri Lanka")
    DEMOCRATIC_REPUBLIC_OF_CONGO = "ZI00", _("Democratic Republic of Congo")
    ZAMBIA = "ZM00", _("Zambia")


PLACE_TO_COUNTRY: dict[str, str] = {
    "+A00": "+A00",
    "+ABI": "+ABI",
    "+AJM": "+AJM",
    "+ASV": "+ASV",
    "+B00": "+B00",
    "+C00": "+C00",
    "+D00": "+D00",
    "+E00": "+E00",
    "+F00": "+F00",
    "+G00": "+G00",
    "+H00": "+H00",
    "+HBE": "+HBE",
    "+HCV": "+HCV",
    "+I00": "+I00",
    "+J00": "+J00",
    "-B00": "-B00",
    "-C00": "-B00",
    "-D00": "-B00",
    "-E00": "-B00",
    "-F00": "-B00",
    "-G00": "-B00",
    "-H00": "-B00",
    "-I00": "-B00",
    "-J00": "-B00",
    "AA--": "AA--",
    "AANS": "AA--",
    "AANT": "AA--",
    "AAQU": "AA--",
    "AASA": "AA--",
    "AATA": "AA--",
    "AAVI": "AA--",
    "AAWA": "AA--",
    "AB00": "AB00",
    "AE00": "AE00",
    "AG--": "AG--",
    "AGAL": "AG--",
    "AGCO": "AG--",
    "AGOR": "AG--",
    "AGTS": "AG--",
    "AI00": "AI00",
    "AJ--": "AJ--",
    "AJNI": "AJ--",
    "AJSI": "AJ--",
    "AK--": "AK--",
    "AK01": "AK--",
    "AL00": "AL00",
    "AM00": "AM00",
    "AN00": "AN00",
    "AR00": "AR00",
    "AU--": "AU--",
    "AU00": "AU--",
    "AU01": "AU--",
    "AU02": "AU--",
    "AU03": "AU--",
    "AU04": "AU--",
    "AU05": "AU--",
    "AU06": "AU--",
    "AU07": "AU--",
    "AU08": "AU--",
    "AZ00": "AZ00",
    "BA00": "BA00",
    "BG--": "BG--",
    "BG01": "BG--",
    "BG02": "BG--",
    "BG03": "BG--",
    "BG04": "BG--",
    "BG05": "BG--",
    "BG06": "BG--",
    "BG07": "BG--",
    "BG08": "BG--",
    "BG09": "BG--",
    "BG10": "BG--",
    "BG11": "BG--",
    "BG12": "BG--",
    "BG13": "BG--",
    "BG14": "BG--",
    "BG15": "BG--",
    "BG16": "BG--",
    "BG17": "BG--",
    "BG18": "BG--",
    "BG19": "BG--",
    "BG20": "BG--",
    "BG21": "BG--",
    "BG22": "BG--",
    "BG23": "BG--",
    "BG24": "BG--",
    "BG25": "BG--",
    "BG26": "BG--",
    "BG27": "BG--",
    "BG28": "BG--",
    "BH00": "BH00",
    "BJ00": "BJ00",
    "BL--": "BL--",
    "BL19": "BL--",
    "BL20": "BL--",
    "BL21": "BL--",
    "BL22": "BL--",
    "BL23": "BL--",
    "BL24": "BL--",
    "BL25": "BL--",
    "BL26": "BL--",
    "BL27": "BL--",
    "BL28": "BL--",
    "BL29": "BL--",
    "BL30": "BL--",
    "BY--": "BY--",
    "BY20": "BY--",
    "BY22": "BY--",
    "BY23": "BY--",
    "BY25": "BY--",
    "BY26": "BY--",
    "BY28": "BY--",
    "CA--": "CA--",
    "CABA": "CABA",
    "CACA": "CACA",
    "CAEA": "CAEA",
    "CAGA": "CAGA",
    "CAHA": "CAHA",
    "CANA": "CANA",
    "CAPA": "CAPA",
    "CG00": "CG00",
    "CI00": "CI00",
    "CIAL": "CI00",
    "CIGU": "CI00",
    "CIHE": "CI00",
    "CIJE": "CI00",
    "CISA": "CI00",
    "CJCA": "CJCA",
    "CJJA": "CJJA",
    "CP--": "CP--",
    "CPAN": "CP--",
    "CPCH": "CP--",
    "CPFU": "CP--",
    "CPHI": "CP--",
    "CPHK": "CP--",
    "CPHO": "CP--",
    "CPHP": "CP--",
    "CPHU": "CP--",
    "CPIM": "CP--",
    "CPKA": "CP--",
    "CPKG": "CP--",
    "CPKI": "CP--",
    "CPKR": "CP--",
    "CPKS": "CP--",
    "CPKU": "CP--",
    "CPKW": "CP--",
    "CPLI": "CP--",
    "CPNH": "CP--",
    "CPPK": "CP--",
    "CPSA": "CP--",
    "CPSG": "CP--",
    "CPSH": "CP--",
    "CPSI": "CP--",
    "CPSK": "CP--",
    "CPSZ": "CP--",
    "CPTS": "CP--",
    "CPTT": "CP--",
    "CPYU": "CP--",
    "CX00": "CX00",
    "CY00": "CY00",
    "CYB-": "CY00",
    "CYN-": "CY00",
    "CYS-": "CY00",
    "CZ--": "CZ--",
    "CZ10": "CZ--",
    "CZ11": "CZ--",
    "CZ12": "CZ--",
    "CZ13": "CZ--",
    "CZ14": "CZ--",
    "CZ15": "CZ--",
    "CZ16": "CZ--",
    "CZ17": "CZ--",
    "CZ18": "CZ--",
    "CZ22": "CZ--",
    "CZ23": "CZ--",
    "CZ26": "CZ--",
    "CZ27": "CZ--",
    "DA00": "DA00",
    "DE--": "DE--",
    "DEA-": "DE--",
    "DEAB": "DE--",
    "DEAF": "DE--",
    "DEAM": "DE--",
    "DEAN": "DE--",
    "DEAP": "DE--",
    "DEAS": "DE--",
    "DEAU": "DE--",
    "DEB-": "DE--",
    "DEBB": "DE--",
    "DEBE": "DE--",
    "DEBF": "DE--",
    "DEBK": "DE--",
    "DEBS": "DE--",
    "DEBT": "DE--",
    "DEC-": "DE--",
    "DECK": "DE--",
    "DECR": "DE--",
    "DECT": "DE--",
    "DEDO": "DE--",
    "DEE-": "DE--",
    "DEED": "DE--",
    "DEEG": "DE--",
    "DEEK": "DE--",
    "DEF-": "DE--",
    "DEFA": "DE--",
    "DEFD": "DE--",
    "DEFK": "DE--",
    "DEFL": "DE--",
    "DEFM": "DE--",
    "DEG-": "DE--",
    "DEGB": "DE--",
    "DEGF": "DE--",
    "DEGH": "DE--",
    "DEGL": "DE--",
    "DEGN": "DE--",
    "DEGW": "DE--",
    "DEHH": "DE--",
    "DEMV": "DE--",
    "DEQ-": "DE--",
    "DEQH": "DE--",
    "DEQN": "DE--",
    "DEQS": "DE--",
    "DEQT": "DE--",
    "DERA": "DE--",
    "DERH": "DE--",
    "DERM": "DE--",
    "DERS": "DE--",
    "DESC": "DE--",
    "DESD": "DE--",
    "DESL": "DE--",
    "DESN": "DE--",
    "DETH": "DE--",
    "DEXB": "DE--",
    "DF--": "DF--",
    "DK--": "DK--",
    "DKHS": "DK--",
    "DKMJ": "DK--",
    "DKNJ": "DK--",
    "DKSD": "DK--",
    "DKSL": "DK--",
    "EA--": "EA--",
    "EAAL": "EA--",
    "EABC": "EA--",
    "EALA": "EA--",
    "EAMA": "EA--",
    "EANB": "EA--",
    "EANF": "EA--",
    "EANS": "EA--",
    "EANW": "EA--",
    "EAON": "EA--",
    "EAPE": "EA--",
    "EAQU": "EA--",
    "EASA": "EA--",
    "EG00": "EG00",
    "EK00": "EK00",
    "EM00": "EM00",
    "EQ00": "EQ00",
    "ER--": "ER--",
    "ERCK": "ER--",
    "ERCL": "ER--",
    "ERCV": "ER--",
    "ERCW": "ER--",
    "ERDO": "ER--",
    "ERDU": "ER--",
    "ERGA": "ER--",
    "ERKD": "ER--",
    "ERKE": "ER--",
    "ERKK": "ER--",
    "ERLG": "ER--",
    "ERLK": "ER--",
    "ERLM": "ER--",
    "ERLU": "ER--",
    "ERLX": "ER--",
    "ERMA": "ER--",
    "ERME": "ER--",
    "ERMO": "ER--",
    "EROF": "ER--",
    "ERRO": "ER--",
    "ERSL": "ER--",
    "ERTP": "ER--",
    "ERWA": "ER--",
    "ERWI": "ER--",
    "ERWM": "ER--",
    "ERWX": "ER--",
    "ES--": "ES--",
    "ES0-": "ES--",
    "ES00": "ES--",
    "ES01": "ES--",
    "ES02": "ES--",
    "ES03": "ES--",
    "ES04": "ES--",
    "ES05": "ES--",
    "ES06": "ES--",
    "ES07": "ES--",
    "ES08": "ES--",
    "ES1-": "ES--",
    "ES10": "ES--",
    "ES11": "ES--",
    "ES12": "ES--",
    "ES13": "ES--",
    "ES14": "ES--",
    "ES15": "ES--",
    "ES16": "ES--",
    "ES17": "ES--",
    "ES18": "ES--",
    "ES19": "ES--",
    "ES2-": "ES--",
    "ES20": "ES--",
    "ES21": "ES--",
    "ES22": "ES--",
    "ES23": "ES--",
    "ES24": "ES--",
    "ES25": "ES--",
    "ES26": "ES--",
    "ES3-": "ES--",
    "ES30": "ES--",
    "ES31": "ES--",
    "ES32": "ES--",
    "ES33": "ES--",
    "ES4-": "ES--",
    "ES40": "ES--",
    "ES41": "ES--",
    "ES42": "ES--",
    "ES43": "ES--",
    "ES44": "ES--",
    "ES5-": "ES--",
    "ES50": "ES--",
    "ES51": "ES--",
    "ES52": "ES--",
    "ES53": "ES--",
    "ES54": "ES--",
    "ES6-": "ES--",
    "ES60": "ES--",
    "ES61": "ES--",
    "ES62": "ES--",
    "ES63": "ES--",
    "ES64": "ES--",
    "ES65": "ES--",
    "ES66": "ES--",
    "ES7-": "ES--",
    "ES70": "ES--",
    "ES71": "ES--",
    "ES72": "ES--",
    "ES8-": "ES--",
    "ES80": "ES--",
    "ES81": "ES--",
    "ES82": "ES--",
    "ES83": "ES--",
    "ES84": "ES--",
    "ES85": "ES--",
    "ES86": "ES--",
    "ET00": "ET00",
    "EV00": "EV00",
    "EY00": "EY00",
    "FA--": "FA--",
    "FA01": "FA--",
    "FA02": "FA--",
    "FA03": "FA--",
    "FA04": "FA--",
    "FA05": "FA--",
    "FA06": "FA--",
    "FA07": "FA--",
    "FE00": "FE00",
    "FG00": "FG00",
    "FK00": "FK00",
    "FM00": "FM00",
    "FNCA": "FNCA",
    "FNLA": "FNLA",
    "FNTA": "FNTA",
    "FNVA": "FNVA",
    "FP--": "FP--",
    "FPCG": "FP--",
    "FPNA": "FP--",
    "FPOF": "FP--",
    "FPTV": "FP--",
    "FR--": "FR--",
    "FR0-": "FR--",
    "FR01": "FR--",
    "FR02": "FR--",
    "FR03": "FR--",
    "FR04": "FR--",
    "FR05": "FR--",
    "FR06": "FR--",
    "FR07": "FR--",
    "FR08": "FR--",
    "FR09": "FR--",
    "FR1-": "FR--",
    "FR10": "FR--",
    "FR11": "FR--",
    "FR12": "FR--",
    "FR13": "FR--",
    "FR14": "FR--",
    "FR15": "FR--",
    "FR16": "FR--",
    "FR17": "FR--",
    "FR18": "FR--",
    "FR19": "FR--",
    "FR2-": "FR--",
    "FR20": "FR--",
    "FR21": "FR--",
    "FR22": "FR--",
    "FR23": "FR--",
    "FR24": "FR--",
    "FR25": "FR--",
    "FR26": "FR--",
    "FR27": "FR--",
    "FR28": "FR--",
    "FR29": "FR--",
    "FR3-": "FR--",
    "FR30": "FR--",
    "FR31": "FR--",
    "FR32": "FR--",
    "FR33": "FR--",
    "FR34": "FR--",
    "FR35": "FR--",
    "FR36": "FR--",
    "FR37": "FR--",
    "FR38": "FR--",
    "FR39": "FR--",
    "FR4-": "FR--",
    "FR40": "FR--",
    "FR41": "FR--",
    "FR42": "FR--",
    "FR43": "FR--",
    "FR44": "FR--",
    "FR45": "FR--",
    "FR46": "FR--",
    "FR47": "FR--",
    "FR48": "FR--",
    "FR49": "FR--",
    "FR5-": "FR--",
    "FR50": "FR--",
    "FR51": "FR--",
    "FR52": "FR--",
    "FR53": "FR--",
    "FR54": "FR--",
    "FR55": "FR--",
    "FR56": "FR--",
    "FR57": "FR--",
    "FR58": "FR--",
    "FR59": "FR--",
    "FR6-": "FR--",
    "FR60": "FR--",
    "FR61": "FR--",
    "FR62": "FR--",
    "FR63": "FR--",
    "FR64": "FR--",
    "FR65": "FR--",
    "FR66": "FR--",
    "FR67": "FR--",
    "FR68": "FR--",
    "FR69": "FR--",
    "FR7-": "FR--",
    "FR70": "FR--",
    "FR71": "FR--",
    "FR72": "FR--",
    "FR73": "FR--",
    "FR74": "FR--",
    "FR75": "FR--",
    "FR76": "FR--",
    "FR77": "FR--",
    "FR78": "FR--",
    "FR79": "FR--",
    "FR8-": "FR--",
    "FR80": "FR--",
    "FR81": "FR--",
    "FR82": "FR--",
    "FR83": "FR--",
    "FR84": "FR--",
    "FR85": "FR--",
    "FR86": "FR--",
    "FR87": "FR--",
    "FR90": "FR--",
    "FT00": "FT00",
    "FVMA": "FVMA",
    "FVSA": "FVSA",
    "GB--": "GB--",
    "GBAB": "GB--",
    "GBAG": "GB--",
    "GBAN": "GB--",
    "GBAR": "GB--",
    "GBAS": "GB--",
    "GBAY": "GB--",
    "GBBA": "GB--",
    "GBBB": "GB--",
    "GBBE": "GB--",
    "GBBF": "GB--",
    "GBBG": "GB--",
    "GBBH": "GB--",
    "GBBN": "GB--",
    "GBBP": "GB--",
    "GBBR": "GB--",
    "GBBS": "GB--",
    "GBBU": "GB--",
    "GBBW": "GB--",
    "GBCB": "GB--",
    "GBCE": "GB--",
    "GBCF": "GB--",
    "GBCK": "GB--",
    "GBCM": "GB--",
    "GBCN": "GB--",
    "GBCO": "GB--",
    "GBCP": "GB--",
    "GBCS": "GB--",
    "GBCU": "GB--",
    "GBDD": "GB--",
    "GBDE": "GB--",
    "GBDH": "GB--",
    "GBDI": "GB--",
    "GBDL": "GB--",
    "GBDN": "GB--",
    "GBDR": "GB--",
    "GBDS": "GB--",
    "GBDT": "GB--",
    "GBE-": "GB--",
    "GBEA": "GB--",
    "GBED": "GB--",
    "GBEH": "GB--",
    "GBEL": "GB--",
    "GBER": "GB--",
    "GBEX": "GB--",
    "GBEY": "GB--",
    "GBFK": "GB--",
    "GBFL": "GB--",
    "GBFR": "GB--",
    "GBGG": "GB--",
    "GBGL": "GB--",
    "GBGS": "GB--",
    "GBGW": "GB--",
    "GBHE": "GB--",
    "GBHL": "GB--",
    "GBHM": "GB--",
    "GBHP": "GB--",
    "GBHR": "GB--",
    "GBHT": "GB--",
    "GBIC": "GB--",
    "GBIM": "GB--",
    "GBIW": "GB--",
    "GBKH": "GB--",
    "GBKN": "GB--",
    "GBLC": "GB--",
    "GBLH": "GB--",
    "GBLI": "GB--",
    "GBLK": "GB--",
    "GBLN": "GB--",
    "GBLO": "GB--",
    "GBLS": "GB--",
    "GBLT": "GB--",
    "GBLU": "GB--",
    "GBMA": "GB--",
    "GBMB": "GB--",
    "GBME": "GB--",
    "GBMK": "GB--",
    "GBML": "GB--",
    "GBMN": "GB--",
    "GBMO": "GB--",
    "GBMT": "GB--",
    "GBMW": "GB--",
    "GBNA": "GB--",
    "GBNE": "GB--",
    "GBNG": "GB--",
    "GBNH": "GB--",
    "GBNK": "GB--",
    "GBNL": "GB--",
    "GBNO": "GB--",
    "GBNP": "GB--",
    "GBNR": "GB--",
    "GBNS": "GB--",
    "GBOR": "GB--",
    "GBOX": "GB--",
    "GBPB": "GB--",
    "GBPE": "GB--",
    "GBPH": "GB--",
    "GBPL": "GB--",
    "GBPM": "GB--",
    "GBPP": "GB--",
    "GBPT": "GB--",
    "GBPW": "GB--",
    "GBRC": "GB--",
    "GBRE": "GB--",
    "GBRG": "GB--",
    "GBRH": "GB--",
    "GBRU": "GB--",
    "GBS-": "GB--",
    "GBSE": "GB--",
    "GBSF": "GB--",
    "GBSG": "GB--",
    "GBSH": "GB--",
    "GBSI": "GB--",
    "GBSK": "GB--",
    "GBSL": "GB--",
    "GBSN": "GB--",
    "GBSO": "GB--",
    "GBSP": "GB--",
    "GBSR": "GB--",
    "GBSS": "GB--",
    "GBSU": "GB--",
    "GBSW": "GB--",
    "GBSY": "GB--",
    "GBTF": "GB--",
    "GBTH": "GB--",
    "GBTN": "GB--",
    "GBTQ": "GB--",
    "GBTS": "GB--",
    "GBTY": "GB--",
    "GBU-": "GB--",
    "GBUA": "GB--",
    "GBUB": "GB--",
    "GBUF": "GB--",
    "GBUL": "GB--",
    "GBUR": "GB--",
    "GBUT": "GB--",
    "GBUW": "GB--",
    "GBVG": "GB--",
    "GBW-": "GB--",
    "GBWA": "GB--",
    "GBWB": "GB--",
    "GBWD": "GB--",
    "GBWI": "GB--",
    "GBWK": "GB--",
    "GBWL": "GB--",
    "GBWM": "GB--",
    "GBWN": "GB--",
    "GBWO": "GB--",
    "GBWR": "GB--",
    "GBWS": "GB--",
    "GBWX": "GB--",
    "GBWY": "GB--",
    "GBXE": "GB--",
    "GBXW": "GB--",
    "GBYO": "GB--",
    "GD--": "GD--",
    "GD01": "GD--",
    "GD03": "GD--",
    "GD05": "GD--",
    "GD07": "GD--",
    "GD09": "GD--",
    "GD11": "GD--",
    "GD13": "GD--",
    "GD15": "GD--",
    "GD17": "GD--",
    "GD19": "GD--",
    "GD21": "GD--",
    "GD23": "GD--",
    "GD25": "GD--",
    "GD27": "GD--",
    "GD29": "GD--",
    "GD41": "GD--",
    "GD51": "GD--",
    "GD53": "GD--",
    "GD61": "GD--",
    "GE--": "GE--",
    "GE01": "GE--",
    "GE02": "GE--",
    "GE03": "GE--",
    "GF00": "GF00",
    "GG00": "GG00",
    "GH00": "GH00",
    "GN00": "GN00",
    "GP00": "GP00",
    "GQ00": "GQ00",
    "GR--": "GR--",
    "GR80": "GR--",
    "GR81": "GR--",
    "GR82": "GR--",
    "GR83": "GR--",
    "GR84": "GR--",
    "GR85": "GR--",
    "GR86": "GR--",
    "GR87": "GR--",
    "GR88": "GR--",
    "GS00": "GS00",
    "GY00": "GY00",
    "HA00": "HA00",
    "HE--": "HE--",
    "HEAG": "HE--",
    "HEAI": "HE--",
    "HEAR": "HE--",
    "HEBE": "HE--",
    "HEBL": "HE--",
    "HEBS": "HE--",
    "HEFR": "HE--",
    "HEGE": "HE--",
    "HEGL": "HE--",
    "HEGR": "HE--",
    "HEJU": "HE--",
    "HELU": "HE--",
    "HENE": "HE--",
    "HENW": "HE--",
    "HEOW": "HE--",
    "HESG": "HE--",
    "HESH": "HE--",
    "HESO": "HE--",
    "HESZ": "HE--",
    "HETG": "HE--",
    "HETI": "HE--",
    "HEUR": "HE--",
    "HEVD": "HE--",
    "HEVS": "HE--",
    "HEZG": "HE--",
    "HEZH": "HE--",
    "HG--": "HG--",
    "HG3-": "HG--",
    "HG30": "HG--",
    "HG31": "HG--",
    "HG32": "HG--",
    "HG33": "HG--",
    "HG34": "HG--",
    "HG35": "HG--",
    "HG36": "HG--",
    "HG37": "HG--",
    "HG38": "HG--",
    "HG4-": "HG--",
    "HG40": "HG--",
    "HG41": "HG--",
    "HG42": "HG--",
    "HG43": "HG--",
    "HG44": "HG--",
    "HG45": "HG--",
    "HG46": "HG--",
    "HG47": "HG--",
    "HG48": "HG--",
    "HG49": "HG--",
    "HH00": "HH00",
    "HJ00": "HJ00",
    "HR--": "HR--",
    "HR01": "HR--",
    "HR02": "HR--",
    "HR03": "HR--",
    "HR04": "HR--",
    "HR05": "HR--",
    "HT00": "HT00",
    "IA--": "IA--",
    "IA0-": "IA--",
    "IA00": "IA--",
    "IA01": "IA--",
    "IA02": "IA--",
    "IA03": "IA--",
    "IA04": "IA--",
    "IA05": "IA--",
    "IA06": "IA--",
    "IA07": "IA--",
    "IA08": "IA--",
    "IA09": "IA--",
    "IA1-": "IA--",
    "IA10": "IA--",
    "IA11": "IA--",
    "IA12": "IA--",
    "IA13": "IA--",
    "IA14": "IA--",
    "IA15": "IA--",
    "IA16": "IA--",
    "IA17": "IA--",
    "IA18": "IA--",
    "IA19": "IA--",
    "IA2-": "IA--",
    "IA20": "IA--",
    "IA21": "IA--",
    "IA22": "IA--",
    "IA23": "IA--",
    "IA24": "IA--",
    "IA25": "IA--",
    "IA26": "IA--",
    "IA27": "IA--",
    "IA28": "IA--",
    "IA29": "IA--",
    "IA3-": "IA--",
    "IA30": "IA--",
    "IA31": "IA--",
    "IA32": "IA--",
    "IA33": "IA--",
    "IA34": "IA--",
    "IA35": "IA--",
    "IA36": "IA--",
    "IA37": "IA--",
    "IA38": "IA--",
    "IA39": "IA--",
    "IA4-": "IA--",
    "IA40": "IA--",
    "IA41": "IA--",
    "IA42": "IA--",
    "IA43": "IA--",
    "IA44": "IA--",
    "IA45": "IA--",
    "IA46": "IA--",
    "IA47": "IA--",
    "IA48": "IA--",
    "IA49": "IA--",
    "IA5-": "IA--",
    "IA50": "IA--",
    "IA51": "IA--",
    "IA52": "IA--",
    "IA53": "IA--",
    "IA54": "IA--",
    "IA55": "IA--",
    "IA56": "IA--",
    "IA57": "IA--",
    "IA58": "IA--",
    "IA59": "IA--",
    "IA6-": "IA--",
    "IA61": "IA--",
    "IA62": "IA--",
    "IA63": "IA--",
    "IA64": "IA--",
    "IA65": "IA--",
    "IA66": "IA--",
    "IA76": "IA--",
    "IL00": "IL00",
    "IN--": "IN--",
    "INAP": "IN--",
    "INAS": "IN--",
    "INBI": "IN--",
    "INBO": "IN--",
    "INDE": "IN--",
    "INHP": "IN--",
    "INJK": "IN--",
    "INKE": "IN--",
    "INMP": "IN--",
    "INMR": "IN--",
    "INMS": "IN--",
    "INMY": "IN--",
    "INOR": "IN--",
    "INPO": "IN--",
    "INPU": "IN--",
    "INRA": "IN--",
    "INTR": "IN--",
    "INUP": "IN--",
    "INWB": "IN--",
    "IO00": "IO00",
    "IP00": "IP00",
    "IQ00": "IQ00",
    "IS--": "IS--",
    "IS01": "IS--",
    "IS02": "IS--",
    "IS03": "IS--",
    "IS04": "IS--",
    "IS05": "IS--",
    "IS06": "IS--",
    "IS07": "IS--",
    "IS08": "IS--",
    "IS09": "IS--",
    "IS10": "IS--",
    "IS11": "IS--",
    "IS12": "IS--",
    "IS13": "IS--",
    "IS14": "IS--",
    "IS15": "IS--",
    "IS16": "IS--",
    "IS17": "IS--",
    "IS18": "IS--",
    "IS19": "IS--",
    "IS20": "IS--",
    "IS21": "IS--",
    "IS22": "IS--",
    "IS23": "IS--",
    "IS24": "IS--",
    "IS25": "IS--",
    "IS26": "IS--",
    "IS27": "IS--",
    "JH00": "JH00",
    "JI00": "JI00",
    "JO00": "JO00",
    "JR00": "JR00",
    "JZ00": "JZ00",
    "KA00": "KA00",
    "KI--": "KI--",
    "KI01": "KI--",
    "KI02": "KI--",
    "KI03": "KI--",
    "KJ00": "KJ00",
    "KM00": "KM00",
    "KN00": "KN00",
    "KZ--": "KZ--",
    "KZ00": "KZ--",
    "KZ01": "KZ--",
    "KZ03": "KZ--",
    "KZ04": "KZ--",
    "KZ06": "KZ--",
    "KZ07": "KZ--",
    "KZ09": "KZ--",
    "KZ10": "KZ--",
    "KZ11": "KZ--",
    "KZ12": "KZ--",
    "KZ13": "KZ--",
    "KZ14": "KZ--",
    "KZ15": "KZ--",
    "KZ16": "KZ--",
    "KZ17": "KZ--",
    "LA00": "LA00",
    "LE00": "LE00",
    "LI00": "LI00",
    "LJDA": "LJDA",
    "LJHA": "LJHA",
    "LJPA": "LJPA",
    "LT00": "LT00",
    "LV00": "LV00",
    "MA00": "MA00",
    "MABM": "MA00",
    "MACS": "MA00",
    "MADO": "MA00",
    "MADT": "MA00",
    "MAFM": "MA00",
    "MAGO": "MA00",
    "MALO": "MA00",
    "MALS": "MA00",
    "MAMS": "MA00",
    "MARS": "MA00",
    "MASM": "MA00",
    "MATT": "MA00",
    "MD00": "MD00",
    "ME00": "ME00",
    "MG00": "MG00",
    "MJ00": "MJ00",
    "MK00": "MK00",
    "ML00": "ML00",
    "MN00": "MN00",
    "MQ00": "MQ00",
    "MU00": "MU00",
    "MV00": "MV00",
    "MY00": "MY00",
    "NA--": "NA--",
    "NAAK": "NA--",
    "NAAL": "NA--",
    "NAAZ": "NA--",
    "NACA": "NA--",
    "NACL": "NA--",
    "NACN": "NA--",
    "NADC": "NA--",
    "NADE": "NA--",
    "NAFL": "NA--",
    "NAGE": "NA--",
    "NAID": "NA--",
    "NAIL": "NA--",
    "NAIN": "NA--",
    "NAIO": "NA--",
    "NAKA": "NA--",
    "NAKE": "NA--",
    "NALO": "NA--",
    "NAMA": "NA--",
    "NAMC": "NA--",
    "NAMN": "NA--",
    "NAMO": "NA--",
    "NAMP": "NA--",
    "NAMR": "NA--",
    "NAMS": "NA--",
    "NAMY": "NA--",
    "NANA": "NA--",
    "NANC": "NA--",
    "NAND": "NA--",
    "NANH": "NA--",
    "NANJ": "NA--",
    "NANV": "NA--",
    "NANY": "NA--",
    "NAOH": "NA--",
    "NAOK": "NA--",
    "NAOR": "NA--",
    "NAPE": "NA--",
    "NARI": "NA--",
    "NASC": "NA--",
    "NASD": "NA--",
    "NATN": "NA--",
    "NATX": "NA--",
    "NAUT": "NA--",
    "NAVE": "NA--",
    "NAVI": "NA--",
    "NAWA": "NA--",
    "NAWI": "NA--",
    "NAWV": "NA--",
    "NAWY": "NA--",
    "NB00": "NB00",
    "NC00": "NC00",
    "ND00": "ND00",
    "NE00": "NE00",
    "NL--": "NL--",
    "NL00": "NL--",
    "NL01": "NL--",
    "NL02": "NL--",
    "NL03": "NL--",
    "NL04": "NL--",
    "NL05": "NL--",
    "NL06": "NL--",
    "NL07": "NL--",
    "NL08": "NL--",
    "NL09": "NL--",
    "NL11": "NL--",
    "NL12": "NL--",
    "NL13": "NL--",
    "NL14": "NL--",
    "NL15": "NL--",
    "NL16": "NL--",
    "NL17": "NL--",
    "NL18": "NL--",
    "NL19": "NL--",
    "NM00": "NM00",
    "NM01": "NM00",
    "NM02": "NM00",
    "NM03": "NM00",
    "NM04": "NM00",
    "NM05": "NM00",
    "NM06": "NM00",
    "NM07": "NM00",
    "NM08": "NM00",
    "NM09": "NM00",
    "NM10": "NM00",
    "NM11": "NM00",
    "NM12": "NM00",
    "NMNK": "NM00",
    "NO--": "NO--",
    "NO20": "NO--",
    "NO21": "NO--",
    "NO22": "NO--",
    "NO23": "NO--",
    "NO24": "NO--",
    "NO25": "NO--",
    "NO26": "NO--",
    "NO27": "NO--",
    "NO28": "NO--",
    "NO29": "NO--",
    "NO30": "NO--",
    "NO31": "NO--",
    "NO32": "NO--",
    "NO33": "NO--",
    "NO34": "NO--",
    "NO35": "NO--",
    "NO36": "NO--",
    "NO37": "NO--",
    "NU00": "NU00",
    "NV00": "NV00",
    "OE00": "OE00",
    "OM00": "OM00",
    "ON00": "ON00",
    "OV00": "OV00",
    "OVB0": "OVB0",
    "OVI0": "OVB0",
    "OVM0": "OVB0",
    "PH00": "PH00",
    "PI00": "PI00",
    "PL--": "PL--",
    "PLBE": "PL--",
    "PLBU": "PL--",
    "PLDO": "PL--",
    "PLKP": "PL--",
    "PLLO": "PL--",
    "PLMP": "PL--",
    "PLMZ": "PL--",
    "PLOE": "PL--",
    "PLPC": "PL--",
    "PLPM": "PL--",
    "PLPS": "PL--",
    "PLSL": "PL--",
    "PLSW": "PL--",
    "PLWI": "PL--",
    "PLWM": "PL--",
    "PLZP": "PL--",
    "PN00": "PN00",
    "PO--": "PO--",
    "PO01": "PO--",
    "PO02": "PO--",
    "PO03": "PO--",
    "PO04": "PO--",
    "PO05": "PO--",
    "PO06": "PO--",
    "PO07": "PO--",
    "PO08": "PO--",
    "PO09": "PO--",
    "PO10": "PO--",
    "PO11": "PO--",
    "PO12": "PO--",
    "PO13": "PO--",
    "PO14": "PO--",
    "PO15": "PO--",
    "PO16": "PO--",
    "PO17": "PO--",
    "PO18": "PO--",
    "PO19": "PO--",
    "PO20": "PO--",
    "PO21": "PO--",
    "PO22": "PO--",
    "PO23": "PO--",
    "PO24": "PO--",
    "PO25": "PO--",
    "PO26": "PO--",
    "PO27": "PO--",
    "PO28": "PO--",
    "PO29": "PO--",
    "PP00": "PP00",
    "PQ00": "PQ00",
    "PSGZ": "PSGZ",
    "PSWB": "PSGZ",
    "PX00": "PX00",
    "PY00": "PY00",
    "QA00": "QA00",
    "QC00": "QC00",
    "QH00": "QH00",
    "QJ00": "QJ00",
    "QQ00": "QQ00",
    "QY00": "QY00",
    "RA48": "IA--",
    "RE00": "RE00",
    "RN00": "RN00",
    "RO--": "RO--",
    "ROAB": "RO--",
    "ROAG": "RO--",
    "ROAR": "RO--",
    "ROB-": "RO--",
    "ROBC": "RO--",
    "ROBH": "RO--",
    "ROBN": "RO--",
    "ROBR": "RO--",
    "ROBT": "RO--",
    "ROBV": "RO--",
    "ROBZ": "RO--",
    "ROCJ": "RO--",
    "ROCL": "RO--",
    "ROCS": "RO--",
    "ROCT": "RO--",
    "ROCV": "RO--",
    "RODB": "RO--",
    "RODJ": "RO--",
    "ROGJ": "RO--",
    "ROGL": "RO--",
    "ROGR": "RO--",
    "ROHD": "RO--",
    "ROHR": "RO--",
    "ROIF": "RO--",
    "ROIL": "RO--",
    "ROIS": "RO--",
    "ROMH": "RO--",
    "ROMM": "RO--",
    "ROMS": "RO--",
    "RONT": "RO--",
    "ROOT": "RO--",
    "ROPH": "RO--",
    "ROSB": "RO--",
    "ROSJ": "RO--",
    "ROSM": "RO--",
    "ROSV": "RO--",
    "ROTL": "RO--",
    "ROTM": "RO--",
    "ROTR": "RO--",
    "ROVL": "RO--",
    "ROVN": "RO--",
    "ROVS": "RO--",
    "RS--": "RS--",
    "RS74": "RS--",
    "RS77": "RS--",
    "RS78": "RS--",
    "RU--": "RU--",
    "RU01": "RU--",
    "RU02": "RU--",
    "RU03": "RU--",
    "RU04": "RU--",
    "RU05": "RU--",
    "RU06": "RU--",
    "RU07": "RU--",
    "RU08": "RU--",
    "RU09": "RU--",
    "RU10": "RU--",
    "RU11": "RU--",
    "RU12": "RU--",
    "RU13": "RU--",
    "RU14": "RU--",
    "RU15": "RU--",
    "RU16": "RU--",
    "RU17": "RU--",
    "RU18": "RU--",
    "RU19": "RU--",
    "RU20": "RU--",
    "RU21": "RU--",
    "RU22": "RU--",
    "RU23": "RU--",
    "RU24": "RU--",
    "RU25": "RU--",
    "RU26": "RU--",
    "RU27": "RU--",
    "RU28": "RU--",
    "RU29": "RU--",
    "RU30": "RU--",
    "RU31": "RU--",
    "RU32": "RU--",
    "RU33": "RU--",
    "RU34": "RU--",
    "RU35": "RU--",
    "RU36": "RU--",
    "RU37": "RU--",
    "RU38": "RU--",
    "RU39": "RU--",
    "RU40": "RU--",
    "RU41": "RU--",
    "RU42": "RU--",
    "RU43": "RU--",
    "RU44": "RU--",
    "RU45": "RU--",
    "RU46": "RU--",
    "RU47": "RU--",
    "RU48": "RU--",
    "RU49": "RU--",
    "RU50": "RU--",
    "RU51": "RU--",
    "RU52": "RU--",
    "RU53": "RU--",
    "RU54": "RU--",
    "RU55": "RU--",
    "RU56": "RU--",
    "RU57": "RU--",
    "RU58": "RU--",
    "RU60": "RU--",
    "RU61": "RU--",
    "RU62": "RU--",
    "RU63": "RU--",
    "RU64": "RU--",
    "RU65": "RU--",
    "RU66": "RU--",
    "RU67": "RU--",
    "RU68": "RU--",
    "RU69": "RU--",
    "RU70": "RU--",
    "RU71": "RU--",
    "RU72": "RU--",
    "RU73": "RU--",
    "RU74": "RU--",
    "RU75": "RU--",
    "RU76": "RU--",
    "RU77": "RU--",
    "RU78": "RU--",
    "RU79": "RU--",
    "RU80": "RU--",
    "RU81": "RU--",
    "RU82": "RU--",
    "RU83": "RU--",
    "RU84": "RU--",
    "RU85": "RU--",
    "RU86": "RU--",
    "RU87": "RU--",
    "RUBS": "RU--",
    "RUCB": "RU--",
    "RUCE": "RU--",
    "RUCS": "RU--",
    "RUFE": "RU--",
    "RUMV": "RU--",
    "RUNC": "RU--",
    "RUNE": "RU--",
    "RUNR": "RU--",
    "RUNW": "RU--",
    "RUSS": "RU--",
    "RUSU": "RU--",
    "RUVD": "RU--",
    "RUVV": "RU--",
    "RUWS": "RU--",
    "RUYS": "RU--",
    "SABA": "SABA",
    "SACA": "SACA",
    "SAEA": "SAEA",
    "SAGA": "SAGA",
    "SAPA": "SAPA",
    "SAUA": "SAUA",
    "SC00": "SC00",
    "SF--": "SF--",
    "SF80": "SF--",
    "SF81": "SF--",
    "SF82": "SF--",
    "SF83": "SF--",
    "SF84": "SF--",
    "SF85": "SF--",
    "SF86": "SF--",
    "SF87": "SF--",
    "SF88": "SF--",
    "SF90": "SF--",
    "SJ00": "SJ00",
    "SK--": "SK--",
    "SKBA": "SK--",
    "SKBB": "SK--",
    "SKBJ": "SK--",
    "SKBN": "SK--",
    "SKBR": "SK--",
    "SKBS": "SK--",
    "SKBY": "SK--",
    "SKCA": "SK--",
    "SKDK": "SK--",
    "SKDS": "SK--",
    "SKDT": "SK--",
    "SKGA": "SK--",
    "SKGL": "SK--",
    "SKHC": "SK--",
    "SKHE": "SK--",
    "SKIL": "SK--",
    "SKKA": "SK--",
    "SKKE": "SK--",
    "SKKK": "SK--",
    "SKKM": "SK--",
    "SKKN": "SK--",
    "SKKS": "SK--",
    "SKLC": "SK--",
    "SKLE": "SK--",
    "SKLM": "SK--",
    "SKLV": "SK--",
    "SKMA": "SK--",
    "SKMI": "SK--",
    "SKML": "SK--",
    "SKMT": "SK--",
    "SKMY": "SK--",
    "SKNM": "SK--",
    "SKNO": "SK--",
    "SKNR": "SK--",
    "SKNZ": "SK--",
    "SKPB": "SK--",
    "SKPD": "SK--",
    "SKPE": "SK--",
    "SKPI": "SK--",
    "SKPK": "SK--",
    "SKPO": "SK--",
    "SKPP": "SK--",
    "SKPT": "SK--",
    "SKPU": "SK--",
    "SKRA": "SK--",
    "SKRK": "SK--",
    "SKRS": "SK--",
    "SKRV": "SK--",
    "SKSA": "SK--",
    "SKSB": "SK--",
    "SKSC": "SK--",
    "SKSE": "SK--",
    "SKSI": "SK--",
    "SKSK": "SK--",
    "SKSL": "SK--",
    "SKSN": "SK--",
    "SKSO": "SK--",
    "SKSP": "SK--",
    "SKSV": "SK--",
    "SKTN": "SK--",
    "SKTO": "SK--",
    "SKTR": "SK--",
    "SKTS": "SK--",
    "SKTT": "SK--",
    "SKTV": "SK--",
    "SKVK": "SK--",
    "SKVT": "SK--",
    "SKZA": "SK--",
    "SKZC": "SK--",
    "SKZH": "SK--",
    "SKZM": "SK--",
    "SKZV": "SK--",
    "SL00": "SL00",
    "SR00": "SR00",
    "SS00": "SS00",
    "SV40": "SV40",
    "SV41": "SV40",
    "SV42": "SV40",
    "SV43": "SV40",
    "SV44": "SV40",
    "SV45": "SV40",
    "SV46": "SV40",
    "SV47": "SV40",
    "SV48": "SV40",
    "SV49": "SV40",
    "SV50": "SV40",
    "SV51": "SV40",
    "SV52": "SV40",
    "SV53": "SV40",
    "SV54": "SV40",
    "SV55": "SV40",
    "SV56": "SV40",
    "SV57": "SV40",
    "SV58": "SV40",
    "SV59": "SV40",
    "SV60": "SV40",
    "SV61": "SV40",
    "SV62": "SV40",
    "SV63": "SV40",
    "SV64": "SV40",
    "SV70": "SV40",
    "SV71": "SV40",
    "SY00": "SY00",
    "TA00": "TA00",
    "TD--": "TD--",
    "TD01": "TD--",
    "TD02": "TD--",
    "TD03": "TD--",
    "TD04": "TD--",
    "TF00": "TF00",
    "TJ00": "TJ00",
    "TM--": "TM--",
    "TM01": "TM--",
    "TM02": "TM--",
    "TM03": "TM--",
    "TM04": "TM--",
    "TM05": "TM--",
    "TO00": "TO00",
    "TP00": "TP00",
    "TU00": "TU00",
    "TX00": "TX00",
    "UK--": "UK--",
    "UK50": "UK--",
    "UK51": "UK--",
    "UK52": "UK--",
    "UK53": "UK--",
    "UK54": "UK--",
    "UK55": "UK--",
    "UK56": "UK--",
    "UK57": "UK--",
    "UK58": "UK--",
    "UK59": "UK--",
    "UK60": "UK--",
    "UK61": "UK--",
    "UK62": "UK--",
    "UK63": "UK--",
    "UK65": "UK--",
    "UK66": "UK--",
    "UK67": "UK--",
    "UK68": "UK--",
    "UK69": "UK--",
    "UK70": "UK--",
    "UK71": "UK--",
    "UK72": "UK--",
    "UK73": "UK--",
    "UK74": "UK--",
    "UK75": "UK--",
    "UZ--": "UZ--",
    "UZ01": "UZ--",
    "UZ02": "UZ--",
    "UZ03": "UZ--",
    "UZ04": "UZ--",
    "UZ05": "UZ--",
    "UZ06": "UZ--",
    "UZ07": "UZ--",
    "UZ08": "UZ--",
    "UZ09": "UZ--",
    "UZ10": "UZ--",
    "UZ11": "UZ--",
    "UZ12": "UZ--",
    "UZ13": "UZ--",
    "VA00": "NA--",
    "VI00": "VI00",
    "VIGB": "VIGB",
    "VINA": "VINA",
    "VM00": "VM00",
    "VU00": "VU00",
    "WE00": "WE00",
    "WG00": "WG00",
    "WP00": "WP00",
    "WR80": "WR80",
    "WS00": "WS00",
    "XH00": "XH00",
    "XY00": "XY00",
    "YB00": "YB00",
    "YH00": "YH00",
    "YQ00": "YQ00",
    "YS00": "YS00",
    "YT00": "YT00",
    "YY00": "YY00",
    "ZA33": "ZA33",
    "ZE00": "ZE00",
    "ZI00": "ZI00",
    "ZM00": "ZM00",
}
