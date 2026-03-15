"""EURING species codes -- see scripts/generate_species_choices.py,
which generates this file wholesale from EURING's own species-code
list. Don't hand-edit; re-run that script when EURING publishes an
update.

Translations of the common names below come from
scripts/generate_species_translations.py, which writes them straight
into the locale .po files from IOC's own multilingual names -- there's
nothing for a translator (or an administrator) to do by hand.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Species(models.TextChoices):
    """Every current EURING species code -- see
    scripts/generate_species_choices.py.
    """

    ABDIM_S_STORK = "01320", _("Abdim's Stork")
    ABERRANT_BUSH_WARBLER = "12170", _("Aberrant Bush Warbler")
    ABERT_S_TOWHEE = "18000", _("Abert's Towhee")
    ABYSSINIAN_GROUND_HORNBILL = "30770", _("Abyssinian Ground Hornbill")
    ABYSSINIAN_ROLLER = "08420", _("Abyssinian Roller")
    ABYSSINIAN_SUNBIRD = "14940", _("Abyssinian Sunbird")
    ABYSSINIAN_WHEATEAR = "11542", _("Abyssinian Wheatear")
    ABYSSINIAN_WHITE_EYE = "15040", _("Abyssinian White-eye")
    ACADIAN_FLYCATCHER = "09140", _("Acadian Flycatcher")
    ACANTHIS_FLAMMEA_FLAMMEA_SENSU_LATO = "16630", _("Acanthis flammea flammea sensu lato")
    ACANTHIS_FLAMMEA_FLAMMEA_SENSU_LATO_2 = "16633", _("Acanthis flammea flammea sensu lato")
    ACANTHIS_FLAMMEA_HORNEMANNI_SENSU_LATO = "16640", _("Acanthis flammea hornemanni sensu lato")
    ACCIPITER_ASTUR_TACHYSPIZA_AEROSPIZA_SP = (
        "02749",
        _("Accipiter; Astur; Tachyspiza; Aerospiza sp."),
    )
    ACORN_WOODPECKER = "08700", _("Acorn Woodpecker")
    ACROCEPHALUS_HYBRID = "90700", _("Acrocephalus hybrid")
    ACROCEPHALUS_PALUSTRIS_X_ACROCEPHALUS_DUMETORUM = (
        "90340",
        _("Acrocephalus palustris x Acrocephalus dumetorum"),
    )
    ACROCEPHALUS_PALUSTRIS_X_ACROCEPHALUS_SCIRPACEUS = (
        "90300",
        _("Acrocephalus palustris x Acrocephalus scirpaceus"),
    )
    ACROCEPHALUS_PALUSTRIS_X_ACROCEPHALUS_SCIRPACEUS_2 = (
        "90301",
        _("Acrocephalus palustris x Acrocephalus scirpaceus"),
    )
    ACROCEPHALUS_PALUSTRIS_X_ACROCEPHALUS_SCIRPACEUS_3 = (
        "90302",
        _("Acrocephalus palustris x Acrocephalus scirpaceus"),
    )
    ACROCEPHALUS_SCIRPACEUS_BAETICATUS_SENSU_LATO = (
        "20900",
        _("Acrocephalus scirpaceus baeticatus sensu lato"),
    )
    ACROCEPHALUS_SCIRPACEUS_X_ACROCEPHALUS_ARUNDINACEUS = (
        "90120",
        _("Acrocephalus scirpaceus x Acrocephalus arundinaceus"),
    )
    ACROCEPHALUS_SCIRPACEUS_X_ACROCEPHALUS_ARUNDINACEUS_2 = (
        "90121",
        _("Acrocephalus scirpaceus x Acrocephalus arundinaceus"),
    )
    ACROCEPHALUS_SCIRPACEUS_X_ACROCEPHALUS_ARUNDINACEUS_3 = (
        "90122",
        _("Acrocephalus scirpaceus x Acrocephalus arundinaceus"),
    )
    ACROCEPHALUS_SP = "12549", _("Acrocephalus sp.")
    ADAMAWA_TURTLE_DOVE = "35010", _("Adamawa Turtle Dove")
    ADELIE_PENGUIN = "20200", _("Adelie Penguin")
    AFEP_PIGEON = "31430", _("Afep Pigeon")
    AFGHAN_SNOWFINCH = "16050", _("Afghan Snowfinch")
    AFRICAN_BLACK_DUCK = "30200", _("African Black Duck")
    AFRICAN_BLACK_SWIFT = "30500", _("African Black Swift")
    AFRICAN_BLUE_FLYCATCHER = "21700", _("African Blue Flycatcher")
    AFRICAN_BLUE_TIT = "14625", _("African Blue Tit")
    AFRICAN_BROADBILL = "34900", _("African Broadbill")
    AFRICAN_CHAFFINCH = "16367", _("African Chaffinch")
    AFRICAN_COLLARED_DOVE = "06830", _("African Collared Dove")
    AFRICAN_CRAKE = "31570", _("African Crake")
    AFRICAN_CUCKOO = "31620", _("African Cuckoo")
    AFRICAN_CUCKOO_HAWK = "30570", _("African Cuckoo-Hawk")
    AFRICAN_DARTER = "30280", _("African Darter")
    AFRICAN_DESERT_WARBLER = "12701", _("African Desert Warbler")
    AFRICAN_DUSKY_FLYCATCHER = "33320", _("African Dusky Flycatcher")
    AFRICAN_DWARF_KINGFISHER = "32580", _("African Dwarf Kingfisher")
    AFRICAN_EMERALD_CUCKOO = "31180", _("African Emerald Cuckoo")
    AFRICAN_FINFOOT = "34310", _("African Finfoot")
    AFRICAN_FIREFINCH = "32680", _("African Firefinch")
    AFRICAN_FISH_EAGLE = "02410", _("African Fish Eagle")
    AFRICAN_GOLDEN_ORIOLE = "33830", _("African Golden Oriole")
    AFRICAN_GOSHAWK = "23200", _("African Goshawk")
    AFRICAN_GREEN_PIGEON = "35260", _("African Green Pigeon")
    AFRICAN_GREY_HORNBILL = "08470", _("African Grey Hornbill")
    AFRICAN_GREY_WOODPECKER = "31690", _("African Grey Woodpecker")
    AFRICAN_HARRIER_HAWK = "34450", _("African Harrier-Hawk")
    AFRICAN_HAWK_EAGLE = "32360", _("African Hawk-Eagle")
    AFRICAN_HILL_BABBLER = "34560", _("African Hill Babbler")
    AFRICAN_HOBBY = "32130", _("African Hobby")
    AFRICAN_HOUBARA = "04440", _("African Houbara")
    AFRICAN_JACANA = "30070", _("African Jacana")
    AFRICAN_OLIVE_PIGEON = "31400", _("African Olive Pigeon")
    AFRICAN_OPENBILL = "30220", _("African Openbill")
    AFRICAN_OYSTERCATCHER = "04530", _("African Oystercatcher")
    AFRICAN_PALM_SWIFT = "08020", _("African Palm Swift")
    AFRICAN_PARADISE_FLYCATCHER = "13530", _("African Paradise Flycatcher")
    AFRICAN_PIED_WAGTAIL = "10230", _("African Pied Wagtail")
    AFRICAN_PIPIT = "30380", _("African Pipit")
    AFRICAN_PITTA = "34120", _("African Pitta")
    AFRICAN_PYGMY_GOOSE = "26590", _("African Pygmy Goose")
    AFRICAN_PYGMY_KINGFISHER = "32590", _("African Pygmy Kingfisher")
    AFRICAN_RED_RUMPED_SWALLOW = "09953", _("African Red-rumped Swallow")
    AFRICAN_SACRED_IBIS = "01420", _("African Sacred Ibis")
    AFRICAN_SCOPS_OWL = "33890", _("African Scops Owl")
    AFRICAN_SHRIKE_FLYCATCHER = "30630", _("African Shrike-flycatcher")
    AFRICAN_SILVERBILL = "16190", _("African Silverbill")
    AFRICAN_SKIMMER = "06330", _("African Skimmer")
    AFRICAN_SPOONBILL = "34130", _("African Spoonbill")
    AFRICAN_SPOTTED_CREEPER = "34762", _("African Spotted Creeper")
    AFRICAN_STONECHAT = "11391", _("African Stonechat")
    AFRICAN_SWAMPHEN = "04272", _("African Swamphen")
    AFRICAN_THRUSH = "26530", _("African Thrush")
    AFRICAN_WATTLED_LAPWING = "35430", _("African Wattled Lapwing")
    AFRICAN_WOOD_OWL = "35020", _("African Wood Owl")
    AFRICAN_YELLOW_WARBLER = "31170", _("African Yellow Warbler")
    AHANTA_SPURFOWL = "34580", _("Ahanta Spurfowl")
    ALAUDALA_RUFESCENS_S_LATO = "09700", _("Alaudala rufescens s. lato")
    ALAUDIDAE_SP = "09799", _("Alaudidae sp.")
    ALDER_FLYCATCHER = "09230", _("Alder Flycatcher")
    ALEUTIAN_TERN = "06170", _("Aleutian Tern")
    ALEXANDRINE_PARAKEET = "26610", _("Alexandrine Parakeet")
    ALGERIAN_NUTHATCH = "14710", _("Algerian Nuthatch")
    ALLEN_S_GALLINULE = "04250", _("Allen's Gallinule")
    ALLEN_S_HUMMINGBIRD = "08230", _("Allen's Hummingbird")
    ALPINE_ACCENTOR = "10940", _("Alpine Accentor")
    ALPINE_CHOUGH = "15580", _("Alpine Chough")
    ALPINE_SWIFT = "07980", _("Alpine Swift")
    ALPINE_THRUSH = "11680", _("Alpine Thrush")
    ALTAI_ACCENTOR = "10930", _("Altai Accentor")
    ALTAI_SNOWCOCK = "03540", _("Altai Snowcock")
    ALTAMIRA_ORIOLE = "19200", _("Altamira Oriole")
    AMAMI_WOODCOCK = "05300", _("Amami Woodcock")
    AMAZON_KINGFISHER = "26830", _("Amazon Kingfisher")
    AMAZONIAN_MOTMOT = "27211", _("Amazonian Motmot")
    AMERICAN_AVOCET = "04570", _("American Avocet")
    AMERICAN_BITTERN = "00960", _("American Bittern")
    AMERICAN_BLACK_DUCK = "01870", _("American Black Duck")
    AMERICAN_BLACK_SWIFT = "07880", _("American Black Swift")
    AMERICAN_BUSHTIT = "14310", _("American Bushtit")
    AMERICAN_CLIFF_SWALLOW = "09980", _("American Cliff Swallow")
    AMERICAN_COOT = "04300", _("American Coot")
    AMERICAN_CROW = "15640", _("American Crow")
    AMERICAN_DIPPER = "10520", _("American Dipper")
    AMERICAN_DUSKY_FLYCATCHER = "09170", _("American Dusky Flycatcher")
    AMERICAN_FLAMINGO = "01471", _("American Flamingo")
    AMERICAN_GOLDEN_PLOVER = "04841", _("American Golden Plover")
    AMERICAN_GOLDFINCH = "16570", _("American Goldfinch")
    AMERICAN_GREY_FLYCATCHER = "09180", _("American Grey Flycatcher")
    AMERICAN_HERRING_GULL = "26632", _("American Herring Gull")
    AMERICAN_KESTREL = "03050", _("American Kestrel")
    AMERICAN_OYSTERCATCHER = "04510", _("American Oystercatcher")
    AMERICAN_PIPIT = "10144", _("American Pipit")
    AMERICAN_REDSTART = "17550", _("American Redstart")
    AMERICAN_ROBIN = "12030", _("American Robin")
    AMERICAN_TREE_SPARROW = "18170", _("American Tree Sparrow")
    AMERICAN_WHITE_IBIS = "01380", _("American White Ibis")
    AMERICAN_WHITE_PELICAN = "00870", _("American White Pelican")
    AMERICAN_WIGEON = "01800", _("American Wigeon")
    AMERICAN_WOODCOCK = "05310", _("American Woodcock")
    AMERICAN_YELLOW_WARBLER = "17331", _("American Yellow Warbler")
    AMUR_FALCON = "03080", _("Amur Falcon")
    AMUR_STONECHAT = "11392", _("Amur Stonechat")
    ANAMBRA_WAXBILL = "31990", _("Anambra Waxbill")
    ANAS_PLATYRHYNCHOS_HYBRID = "90710", _("Anas platyrhynchos hybrid")
    ANAS_PLATYRHYNCHOS_VAR_DOMESTICA = "01863", _("Anas platyrhynchos var. domestica")
    ANAS_PLATYRHYNCHOS_X_ANAS_ACUTA = "90480", _("Anas platyrhynchos x Anas acuta")
    ANAS_PLATYRHYNCHOS_X_ANAS_ACUTA_2 = "90481", _("Anas platyrhynchos x Anas acuta")
    ANAS_PLATYRHYNCHOS_X_ANAS_ACUTA_3 = "90482", _("Anas platyrhynchos x Anas acuta")
    ANAS_PLATYRHYNCHOS_X_ANAS_PLATYRHYNCHOS_VAR_DOMESTICA = (
        "90050",
        _("Anas platyrhynchos x Anas platyrhynchos var. domestica"),
    )
    ANAS_PLATYRHYNCHOS_X_ANAS_PLATYRHYNCHOS_VAR_DOMESTICA_2 = (
        "90051",
        _("Anas platyrhynchos x Anas platyrhynchos var. domestica"),
    )
    ANAS_PLATYRHYNCHOS_X_ANAS_PLATYRHYNCHOS_VAR_DOMESTICA_3 = (
        "90052",
        _("Anas platyrhynchos x Anas platyrhynchos var. domestica"),
    )
    ANAS_PLATYRHYNCHOS_X_AYTHYA_FERINA = "90770", _("Anas platyrhynchos x Aythya ferina")
    ANAS_SP = "01949", _("Anas sp.")
    ANCIENT_MURRELET = "06450", _("Ancient Murrelet")
    ANHINGA = "00850", _("Anhinga")
    ANNA_S_HUMMINGBIRD = "08180", _("Anna's Hummingbird")
    ANSER_ALBIFRONS_X_ANSER_ERYTHROPUS = "90660", _("Anser albifrons x Anser erythropus")
    ANSER_ALBIFRONS_X_ANSER_INDICUS = "90750", _("Anser albifrons x Anser indicus")
    ANSER_ALBIFRONS_X_BRANTA_LEUCOPSIS = "90640", _("Anser albifrons x Branta leucopsis")
    ANSER_ANSER_VAR_DOMESTICA = "01613", _("Anser anser var. domestica")
    ANSER_ANSER_X_ANSER_ALBIFRONS = "90570", _("Anser anser x Anser albifrons")
    ANSER_ANSER_X_ANSER_CYGNOIDES = "90580", _("Anser anser x Anser cygnoides")
    ANSER_ANSER_X_ANSER_INDICUS = "90590", _("Anser anser x Anser indicus")
    ANSER_ANSER_X_BRANTA_CANADENSIS = "90020", _("Anser anser x Branta canadensis")
    ANSER_ANSER_X_BRANTA_CANADENSIS_2 = "90021", _("Anser anser x Branta canadensis")
    ANSER_ANSER_X_BRANTA_CANADENSIS_3 = "90022", _("Anser anser x Branta canadensis")
    ANSER_ANSER_X_BRANTA_LEUCOPSIS = "90680", _("Anser anser x Branta leucopsis")
    ANSER_CAERULESCENS_X_BRANTA_CANADENSIS = "90630", _("Anser caerulescens x Branta canadensis")
    ANSER_CAERULESCENS_X_BRANTA_LEUCOPSIS = "90650", _("Anser caerulescens x Branta leucopsis")
    ANSER_CYGNOIDES_X_BRANTA_CANADENSIS = "90620", _("Anser cygnoides x Branta canadensis")
    ANSER_ERYTHROPUS_X_BRANTA_LEUCOPSIS = "90010", _("Anser erythropus x Branta leucopsis")
    ANSER_ERYTHROPUS_X_BRANTA_LEUCOPSIS_2 = "90011", _("Anser erythropus x Branta leucopsis")
    ANSER_ERYTHROPUS_X_BRANTA_LEUCOPSIS_3 = "90012", _("Anser erythropus x Branta leucopsis")
    ANSER_FABALIS_SENSU_LATO = "01570", _("Anser fabalis sensu lato")
    ANSER_INDICUS_X_ANSER_CAERULESCENS = "90600", _("Anser indicus x Anser caerulescens")
    ANSER_INDICUS_X_ANSER_CYGNOIDES = "90610", _("Anser indicus x Anser cygnoides")
    ANSER_INDICUS_X_BRANTA_CANADENSIS = "90690", _("Anser indicus x Branta canadensis")
    ANSER_INDICUS_X_BRANTA_LEUCOPSIS = "90030", _("Anser indicus x Branta leucopsis")
    ANSER_INDICUS_X_BRANTA_LEUCOPSIS_2 = "90031", _("Anser indicus x Branta leucopsis")
    ANSER_INDICUS_X_BRANTA_LEUCOPSIS_3 = "90032", _("Anser indicus x Branta leucopsis")
    ANSER_SP = "01659", _("Anser sp.")
    ANSER_SP_X_BRANTA_SP = "90670", _("Anser sp. x Branta sp.")
    ANSERINAE_SP = "01569", _("Anserinae sp.")
    ANSORGE_S_GREENBUL = "30230", _("Ansorge's Greenbul")
    ANTARCTIC_PETREL = "20020", _("Antarctic Petrel")
    ANTARCTIC_PRION = "20320", _("Antarctic Prion")
    ANTARCTIC_TERN = "20700", _("Antarctic Tern")
    ANTEATER_CHAT = "11430", _("Anteater Chat")
    ANTHUS_PETROSUS_SPINOLETTA = "10140", _("Anthus petrosus/spinoletta")
    ANTHUS_SP = "10159", _("Anthus sp.")
    APLOMADO_FALCON = "03130", _("Aplomado Falcon")
    APUS_SP = "08009", _("Apus sp.")
    AQUATIC_WARBLER = "12420", _("Aquatic Warbler")
    AQUILA_RAPAX_SENSU_LATO = "02940", _("Aquila rapax sensu lato")
    AQUILA_SP = "02979", _("Aquila sp.")
    ARABIAN_BABBLER = "13790", _("Arabian Babbler")
    ARABIAN_BUSTARD = "04450", _("Arabian Bustard")
    ARABIAN_GOLDEN_SPARROW = "16000", _("Arabian Golden Sparrow")
    ARABIAN_GREEN_BEE_EATER = "08381", _("Arabian Green Bee-eater")
    ARABIAN_LARK = "36330", _("Arabian Lark")
    ARABIAN_PARTRIDGE = "03610", _("Arabian Partridge")
    ARABIAN_SCOPS_OWL = "33891", _("Arabian Scops Owl")
    ARABIAN_SERIN = "16450", _("Arabian Serin")
    ARABIAN_WARBLER = "12710", _("Arabian Warbler")
    ARABIAN_WAXBILL = "16160", _("Arabian Waxbill")
    ARABIAN_WHEATEAR = "11541", _("Arabian Wheatear")
    ARABIAN_WOODPECKER = "08900", _("Arabian Woodpecker")
    ARCTIC_TERN = "06160", _("Arctic Tern")
    ARCTIC_WARBLER = "12950", _("Arctic Warbler")
    ARDEA_ALBA_X_ARDEA_CINEREA = "90460", _("Ardea alba x Ardea cinerea")
    ARDEA_CINEREA_X_ARDEA_PURPUREA = "90240", _("Ardea cinerea x Ardea purpurea")
    ARDEA_CINEREA_X_ARDEA_PURPUREA_2 = "90241", _("Ardea cinerea x Ardea purpurea")
    ARDEA_CINEREA_X_ARDEA_PURPUREA_3 = "90242", _("Ardea cinerea x Ardea purpurea")
    ARDEA_SP = "01259", _("Ardea sp.")
    ARIZONA_WOODPECKER = "08950", _("Arizona Woodpecker")
    ARMENIAN_GULL = "35980", _("Armenian Gull")
    ARREMON_TORQUATUS_SENSU_LATO = "17950", _("Arremon torquatus sensu lato")
    ASH_THROATED_FLYCATCHER = "09340", _("Ash-throated Flycatcher")
    ASHY_DRONGO = "15260", _("Ashy Drongo")
    ASHY_FLYCATCHER = "22100", _("Ashy Flycatcher")
    ASHY_MINIVET = "10290", _("Ashy Minivet")
    ASHY_STORM_PETREL = "00570", _("Ashy Storm Petrel")
    ASHY_WOOD_PIGEON = "06750", _("Ashy Wood Pigeon")
    ASHY_BREASTED_FLYCATCHER = "13340", _("Ashy-breasted Flycatcher")
    ASHY_THROATED_PARROTBILL = "13705", _("Ashy-throated Parrotbill")
    ASHY_THROATED_WARBLER = "12970", _("Ashy-throated Warbler")
    ASIAN_BARRED_OWLET = "35810", _("Asian Barred Owlet")
    ASIAN_DESERT_WARBLER = "12702", _("Asian Desert Warbler")
    ASIAN_DOWITCHER = "05280", _("Asian Dowitcher")
    ASIAN_EMERALD_CUCKOO = "07190", _("Asian Emerald Cuckoo")
    ASIAN_HOUBARA = "04442", _("Asian Houbara")
    ASIAN_HOUSE_MARTIN = "10000", _("Asian House Martin")
    ASIAN_KOEL = "35590", _("Asian Koel")
    ASIAN_OPENBILL = "01300", _("Asian Openbill")
    ASIAN_ROSY_FINCH = "16710", _("Asian Rosy Finch")
    ASIAN_SHORT_TOED_LARK = "09702", _("Asian Short-toed Lark")
    ASIAN_STUBTAIL = "12130", _("Asian Stubtail")
    ASIAN_WOOLLY_NECKED_STORK = "01330", _("Asian Woolly-necked Stork")
    ATLANTIC_CANARY = "16420", _("Atlantic Canary")
    ATLANTIC_PETREL = "20330", _("Atlantic Petrel")
    ATLANTIC_PUFFIN = "06540", _("Atlantic Puffin")
    ATLANTIC_YELLOW_NOSED_ALBATROSS = "00151", _("Atlantic Yellow-nosed Albatross")
    ATLAS_PIED_FLYCATCHER = "13493", _("Atlas Pied Flycatcher")
    ATLAS_WHEATEAR = "11463", _("Atlas Wheatear")
    AUDOUIN_S_GULL = "05880", _("Audouin's Gull")
    AUDUBON_S_ORIOLE = "19130", _("Audubon's Oriole")
    AUSTRALIAN_SHELDUCK = "26670", _("Australian Shelduck")
    AUSTRALIAN_ZEBRA_FINCH = "20442", _("Australian Zebra Finch")
    AYRES_S_HAWK_EAGLE = "32350", _("Ayres's Hawk-Eagle")
    AYTHA_HYBRID = "90780", _("Aytha hybrid")
    AYTHYA_FERINA_X_AYTHYA_NYROCA = "90470", _("Aythya ferina x Aythya nyroca")
    AYTHYA_FERINA_X_AYTHYA_NYROCA_2 = "90471", _("Aythya ferina x Aythya nyroca")
    AYTHYA_FERINA_X_AYTHYA_NYROCA_3 = "90472", _("Aythya ferina x Aythya nyroca")
    AYTHYA_NYROCA_X_ANAS_PLATYRHYNCHOS = "90250", _("Aythya nyroca x Anas platyrhynchos")
    AYTHYA_NYROCA_X_ANAS_PLATYRHYNCHOS_2 = "90251", _("Aythya nyroca x Anas platyrhynchos")
    AYTHYA_NYROCA_X_ANAS_PLATYRHYNCHOS_3 = "90252", _("Aythya nyroca x Anas platyrhynchos")
    AYTHYA_SP = "02059", _("Aythya sp.")
    AZORES_BULLFINCH = "17105", _("Azores Bullfinch")
    AZORES_CHAFFINCH = "16366", _("Azores Chaffinch")
    AZTEC_THRUSH = "11730", _("Aztec Thrush")
    AZURE_GALLINULE = "20150", _("Azure Gallinule")
    AZURE_TIT = "14630", _("Azure Tit")
    BACHMAN_S_SPARROW = "18110", _("Bachman's Sparrow")
    BACHMAN_S_WARBLER = "17210", _("Bachman's Warbler")
    BAER_S_POCHARD = "02010", _("Baer's Pochard")
    BAGLAFECHT_WEAVER = "34200", _("Baglafecht Weaver")
    BAHAMA_MOCKINGBIRD = "10680", _("Bahama Mockingbird")
    BAHAMA_SWALLOW = "09860", _("Bahama Swallow")
    BAHAMA_WOODSTAR = "08130", _("Bahama Woodstar")
    BAHAMA_YELLOWTHROAT = "17630", _("Bahama Yellowthroat")
    BAIKAL_TEAL = "01830", _("Baikal Teal")
    BAILLON_S_CRAKE = "04110", _("Baillon's Crake")
    BAIRD_S_SANDPIPER = "05060", _("Baird's Sandpiper")
    BAIRD_S_SPARROW = "18270", _("Baird's Sparrow")
    BALD_EAGLE = "02440", _("Bald Eagle")
    BALEARIC_SHEARWATER = "00463", _("Balearic Shearwater")
    BALEARIC_WARBLER = "12612", _("Balearic Warbler")
    BALTIMORE_ORIOLE = "19180", _("Baltimore Oriole")
    BANANAQUIT = "17830", _("Bananaquit")
    BAND_BELLIED_CRAKE = "04150", _("Band-bellied Crake")
    BAND_RUMPED_STORM_PETREL = "00582", _("Band-rumped Storm Petrel")
    BAND_TAILED_MANAKIN = "27350", _("Band-tailed Manakin")
    BAND_TAILED_PIGEON = "06810", _("Band-tailed Pigeon")
    BANDED_MARTIN = "34740", _("Banded Martin")
    BANDED_QUAIL = "03440", _("Banded Quail")
    BANGWA_FOREST_WARBLER = "30720", _("Bangwa Forest Warbler")
    BANK_MYNA = "15880", _("Bank Myna")
    BANNERMAN_S_SHEARWATER = "00485", _("Bannerman's Shearwater")
    BANNERMAN_S_WEAVER = "34210", _("Bannerman's Weaver")
    BAR_BREASTED_FIREFINCH = "32690", _("Bar-breasted Firefinch")
    BAR_HEADED_GOOSE = "01620", _("Bar-headed Goose")
    BAR_TAILED_GODWIT = "05340", _("Bar-tailed Godwit")
    BAR_TAILED_LARK = "09550", _("Bar-tailed Lark")
    BAR_TAILED_TREECREEPER = "14840", _("Bar-tailed Treecreeper")
    BAR_TAILED_TROGON = "30480", _("Bar-tailed Trogon")
    BAR_THROATED_MINLA = "14140", _("Bar-throated Minla")
    BAR_WINGED_WREN_BABBLER = "13600", _("Bar-winged Wren-Babbler")
    BARBARY_PARTRIDGE = "03590", _("Barbary Partridge")
    BARE_CHEEKED_TROGON = "30460", _("Bare-cheeked Trogon")
    BARKA_INDIGOBIRD = "35490", _("Barka Indigobird")
    BARN_SWALLOW = "09920", _("Barn Swallow")
    BARNACLE_GOOSE = "01670", _("Barnacle Goose")
    BAROLO_SHEARWATER = "00482", _("Barolo Shearwater")
    BARRED_ANTSHRIKE = "27540", _("Barred Antshrike")
    BARRED_BUTTONQUAIL = "04020", _("Barred Buttonquail")
    BARRED_LAUGHINGTHRUSH = "13930", _("Barred Laughingthrush")
    BARRED_OWL = "07630", _("Barred Owl")
    BARRED_WARBLER = "12730", _("Barred Warbler")
    BARROW_S_GOLDENEYE = "02170", _("Barrow's Goldeneye")
    BASRA_REED_WARBLER = "12532", _("Basra Reed Warbler")
    BAT_HAWK = "32980", _("Bat Hawk")
    BATELEUR = "02570", _("Bateleur")
    BATES_S_SUNBIRD = "33480", _("Bates's Sunbird")
    BAUMANN_S_OLIVE_GREENBUL = "34030", _("Baumann's Olive Greenbul")
    BAY_BACKED_SHRIKE = "15160", _("Bay-backed Shrike")
    BAY_BREASTED_WARBLER = "17540", _("Bay-breasted Warbler")
    BAYA_WEAVER = "36580", _("Baya Weaver")
    BEARDED_BARBET = "26550", _("Bearded Barbet")
    BEARDED_REEDLING = "13640", _("Bearded Reedling")
    BEARDED_VULTURE = "02460", _("Bearded Vulture")
    BEAUTIFUL_SIBIA = "14260", _("Beautiful Sibia")
    BEAUTIFUL_SUNBIRD = "22400", _("Beautiful Sunbird")
    BEIJING_BABBLER = "12320", _("Beijing Babbler")
    BELCHER_S_GULL = "26300", _("Belcher's Gull")
    BELL_S_SPARROW = "18070", _("Bell's Sparrow")
    BELL_S_VIREO = "16250", _("Bell's Vireo")
    BELTED_KINGFISHER = "08340", _("Belted Kingfisher")
    BENDIRE_S_THRASHER = "10710", _("Bendire's Thrasher")
    BERMUDA_PETREL = "20490", _("Bermuda Petrel")
    BERNIER_S_TEAL = "28030", _("Bernier's Teal")
    BERTHELOT_S_PIPIT = "10060", _("Berthelot's Pipit")
    BERYLLINE_HUMMINGBIRD = "08070", _("Berylline Hummingbird")
    BESRA = "02681", _("Besra")
    BEWICK_S_WREN = "10600", _("Bewick's Wren")
    BICKNELL_S_THRUSH = "11782", _("Bicknell's Thrush")
    BIMACULATED_LARK = "09620", _("Bimaculated Lark")
    BLACK_BEE_EATER = "33200", _("Black Bee-eater")
    BLACK_COUCAL = "30990", _("Black Coucal")
    BLACK_CRAKE = "04200", _("Black Crake")
    BLACK_CROWNED_CRANE = "30600", _("Black Crowned Crane")
    BLACK_CUCKOO = "31610", _("Black Cuckoo")
    BLACK_DRONGO = "15250", _("Black Drongo")
    BLACK_FRANCOLIN = "03640", _("Black Francolin")
    BLACK_GROUSE = "03320", _("Black Grouse")
    BLACK_GUILLEMOT = "06380", _("Black Guillemot")
    BLACK_GUINEAFOWL = "30100", _("Black Guineafowl")
    BLACK_HERON = "31820", _("Black Heron")
    BLACK_KITE = "02380", _("Black Kite")
    BLACK_LARK = "09660", _("Black Lark")
    BLACK_NODDY = "30300", _("Black Noddy")
    BLACK_OYSTERCATCHER = "04520", _("Black Oystercatcher")
    BLACK_PARADISE_FLYCATCHER = "13550", _("Black Paradise Flycatcher")
    BLACK_PETREL = "27810", _("Black Petrel")
    BLACK_PHOEBE = "09100", _("Black Phoebe")
    BLACK_RAIL = "04190", _("Black Rail")
    BLACK_REDSTART = "11210", _("Black Redstart")
    BLACK_SCIMITARBILL = "34720", _("Black Scimitarbill")
    BLACK_SCOTER = "02132", _("Black Scoter")
    BLACK_SCRUB_ROBIN = "10960", _("Black Scrub Robin")
    BLACK_SHAMA = "27980", _("Black Shama")
    BLACK_SKIMMER = "06320", _("Black Skimmer")
    BLACK_SPARROWHAWK = "30030", _("Black Sparrowhawk")
    BLACK_SPINETAIL = "35100", _("Black Spinetail")
    BLACK_STORK = "01310", _("Black Stork")
    BLACK_STORM_PETREL = "00600", _("Black Storm Petrel")
    BLACK_SWAN = "20800", _("Black Swan")
    BLACK_TERN = "06270", _("Black Tern")
    BLACK_TURNSTONE = "05620", _("Black Turnstone")
    BLACK_VULTURE = "02280", _("Black Vulture")
    BLACK_WHEATEAR = "11580", _("Black Wheatear")
    BLACK_WOOD_PIGEON = "06760", _("Black Wood Pigeon")
    BLACK_WOODPECKER = "08630", _("Black Woodpecker")
    BLACK_AND_WHITE_MANNIKIN = "34930", _("Black-and-white Mannikin")
    BLACK_AND_WHITE_SHRIKE_FLYCATCHER = "30640", _("Black-and-white Shrike-flycatcher")
    BLACK_AND_WHITE_WARBLER = "17200", _("Black-and-white Warbler")
    BLACK_AND_WHITE_CASQUED_HORNBILL = "31070", _("Black-and-white-casqued Hornbill")
    BLACK_AND_YELLOW_GROSBEAK = "17110", _("Black-and-yellow Grosbeak")
    BLACK_BACKED_BARBET = "36550", _("Black-backed Barbet")
    BLACK_BACKED_CISTICOLA = "31300", _("Black-backed Cisticola")
    BLACK_BACKED_WOODPECKER = "08990", _("Black-backed Woodpecker")
    BLACK_BELLIED_BUSTARD = "32060", _("Black-bellied Bustard")
    BLACK_BELLIED_FIREFINCH = "32670", _("Black-bellied Firefinch")
    BLACK_BELLIED_SANDGROUSE = "06610", _("Black-bellied Sandgrouse")
    BLACK_BELLIED_SEEDCRACKER = "34660", _("Black-bellied Seedcracker")
    BLACK_BELLIED_STORM_PETREL = "27730", _("Black-bellied Storm Petrel")
    BLACK_BELLIED_WHISTLING_DUCK = "01510", _("Black-bellied Whistling Duck")
    BLACK_BILLED_CAPERCAILLIE = "03340", _("Black-billed Capercaillie")
    BLACK_BILLED_CUCKOO = "07270", _("Black-billed Cuckoo")
    BLACK_BILLED_WEAVER = "36490", _("Black-billed Weaver")
    BLACK_BILLED_WOOD_DOVE = "35340", _("Black-billed Wood Dove")
    BLACK_BREASTED_PARROTBILL = "13680", _("Black-breasted Parrotbill")
    BLACK_BROWED_ALBATROSS = "00140", _("Black-browed Albatross")
    BLACK_BROWED_REED_WARBLER = "12450", _("Black-browed Reed Warbler")
    BLACK_CAPPED_APALIS = "30430", _("Black-capped Apalis")
    BLACK_CAPPED_CHICKADEE = "14430", _("Black-capped Chickadee")
    BLACK_CAPPED_DONACOBIUS = "26930", _("Black-capped Donacobius")
    BLACK_CAPPED_GNATCATCHER = "13200", _("Black-capped Gnatcatcher")
    BLACK_CAPPED_KINGFISHER = "08280", _("Black-capped Kingfisher")
    BLACK_CAPPED_PETREL = "00290", _("Black-capped Petrel")
    BLACK_CAPPED_VIREO = "16210", _("Black-capped Vireo")
    BLACK_CAPPED_WOODLAND_WARBLER = "34090", _("Black-capped Woodland Warbler")
    BLACK_CASQUED_HORNBILL = "31030", _("Black-casqued Hornbill")
    BLACK_CHINNED_HUMMINGBIRD = "08160", _("Black-chinned Hummingbird")
    BLACK_CHINNED_SPARROW = "18230", _("Black-chinned Sparrow")
    BLACK_CHINNED_YUHINA = "14300", _("Black-chinned Yuhina")
    BLACK_COLLARED_APALIS = "30440", _("Black-collared Apalis")
    BLACK_CROWNED_NIGHT_HERON = "01040", _("Black-crowned Night Heron")
    BLACK_CROWNED_SPARROW_LARK = "09530", _("Black-crowned Sparrow-Lark")
    BLACK_CROWNED_TCHAGRA = "15090", _("Black-crowned Tchagra")
    BLACK_CROWNED_WAXBILL = "31970", _("Black-crowned Waxbill")
    BLACK_FACED_BUNTING = "18530", _("Black-faced Bunting")
    BLACK_FACED_FIREFINCH = "32660", _("Black-faced Firefinch")
    BLACK_FACED_GRASSQUIT = "18030", _("Black-faced Grassquit")
    BLACK_FACED_LAUGHINGTHRUSH = "14030", _("Black-faced Laughingthrush")
    BLACK_FACED_SPOONBILL = "01450", _("Black-faced Spoonbill")
    BLACK_FACED_TANAGER = "27420", _("Black-faced Tanager")
    BLACK_FACED_WARBLER = "12800", _("Black-faced Warbler")
    BLACK_FOOTED_ALBATROSS = "00170", _("Black-footed Albatross")
    BLACK_FRONTED_NUNBIRD = "27220", _("Black-fronted Nunbird")
    BLACK_HEADED_BEE_EATER = "33180", _("Black-headed Bee-eater")
    BLACK_HEADED_BUNTING = "18810", _("Black-headed Bunting")
    BLACK_HEADED_GONOLEK = "32820", _("Black-headed Gonolek")
    BLACK_HEADED_GREENFINCH = "16510", _("Black-headed Greenfinch")
    BLACK_HEADED_GROSBEAK = "18860", _("Black-headed Grosbeak")
    BLACK_HEADED_GULL = "05820", _("Black-headed Gull")
    BLACK_HEADED_HERON = "20310", _("Black-headed Heron")
    BLACK_HEADED_IBIS = "01430", _("Black-headed Ibis")
    BLACK_HEADED_JAY = "15400", _("Black-headed Jay")
    BLACK_HEADED_LAPWING = "04880", _("Black-headed Lapwing")
    BLACK_HEADED_PENDULINE_TIT = "14903", _("Black-headed Penduline Tit")
    BLACK_HEADED_SISKIN = "16560", _("Black-headed Siskin")
    BLACK_HEADED_WEAVER = "20410", _("Black-headed Weaver")
    BLACK_LEGGED_KITTIWAKE = "06020", _("Black-legged Kittiwake")
    BLACK_MASKED_FINCH = "26870", _("Black-masked Finch")
    BLACK_NAPED_ORIOLE = "15070", _("Black-naped Oriole")
    BLACK_NAPED_TERN = "06130", _("Black-naped Tern")
    BLACK_NECKED_CRANE = "04340", _("Black-necked Crane")
    BLACK_NECKED_GREBE = "00120", _("Black-necked Grebe")
    BLACK_POLLED_YELLOWTHROAT = "17640", _("Black-polled Yellowthroat")
    BLACK_RUMPED_BUTTONQUAIL = "35330", _("Black-rumped Buttonquail")
    BLACK_RUMPED_FLAMEBACK = "08610", _("Black-rumped Flameback")
    BLACK_RUMPED_WAXBILL = "20270", _("Black-rumped Waxbill")
    BLACK_SHOULDERED_KITE = "31830", _("Black-shouldered Kite")
    BLACK_TAILED_CRAKE = "04160", _("Black-tailed Crake")
    BLACK_TAILED_GNATCATCHER = "13190", _("Black-tailed Gnatcatcher")
    BLACK_TAILED_GODWIT = "05320", _("Black-tailed Godwit")
    BLACK_TAILED_GULL = "05870", _("Black-tailed Gull")
    BLACK_TAILED_TROGON = "27640", _("Black-tailed Trogon")
    BLACK_THROATED_ACCENTOR = "10900", _("Black-throated Accentor")
    BLACK_THROATED_APALIS = "30420", _("Black-throated Apalis")
    BLACK_THROATED_BLUE_WARBLER = "17360", _("Black-throated Blue Warbler")
    BLACK_THROATED_BUSHTIT = "14360", _("Black-throated Bushtit")
    BLACK_THROATED_COUCAL = "31000", _("Black-throated Coucal")
    BLACK_THROATED_GREEN_WARBLER = "17450", _("Black-throated Green Warbler")
    BLACK_THROATED_GREY_WARBLER = "17420", _("Black-throated Grey Warbler")
    BLACK_THROATED_LOON = "00030", _("Black-throated Loon")
    BLACK_THROATED_PARROTBILL = "13740", _("Black-throated Parrotbill")
    BLACK_THROATED_PRINIA = "12300", _("Black-throated Prinia")
    BLACK_THROATED_SPARROW = "18060", _("Black-throated Sparrow")
    BLACK_THROATED_THRUSH = "11972", _("Black-throated Thrush")
    BLACK_VENTED_ORIOLE = "19140", _("Black-vented Oriole")
    BLACK_WHISKERED_VIREO = "16340", _("Black-whiskered Vireo")
    BLACK_WINGED_CUCKOOSHRIKE = "10250", _("Black-winged Cuckooshrike")
    BLACK_WINGED_KITE = "02350", _("Black-winged Kite")
    BLACK_WINGED_ORIOLE = "33850", _("Black-winged Oriole")
    BLACK_WINGED_PRATINCOLE = "04670", _("Black-winged Pratincole")
    BLACK_WINGED_RED_BISHOP = "32040", _("Black-winged Red Bishop")
    BLACK_WINGED_SNOWFINCH = "16100", _("Black-winged Snowfinch")
    BLACK_WINGED_STILT = "04550", _("Black-winged Stilt")
    BLACKBURNIAN_WARBLER = "17470", _("Blackburnian Warbler")
    BLACKCAP_BABBLER = "35320", _("Blackcap Babbler")
    BLACKCAP_ILLADOPSIS = "32500", _("Blackcap Illadopsis")
    BLACKPOLL_WARBLER = "17530", _("Blackpoll Warbler")
    BLACKSTART = "11350", _("Blackstart")
    BLACKTHROAT = "11090", _("Blackthroat")
    BLAKISTON_S_FISH_OWL = "07460", _("Blakiston's Fish Owl")
    BLANFORD_S_ROSEFINCH = "16770", _("Blanford's Rosefinch")
    BLANFORD_S_SNOWFINCH = "16060", _("Blanford's Snowfinch")
    BLOOD_PHEASANT = "03770", _("Blood Pheasant")
    BLUE_CUCKOOSHRIKE = "31460", _("Blue Cuckooshrike")
    BLUE_EARED_PHEASANT = "03900", _("Blue Eared Pheasant")
    BLUE_GROSBEAK = "18910", _("Blue Grosbeak")
    BLUE_JAY = "15350", _("Blue Jay")
    BLUE_MALKOHA = "31120", _("Blue Malkoha")
    BLUE_MOCKINGBIRD = "10810", _("Blue Mockingbird")
    BLUE_PETREL = "20160", _("Blue Petrel")
    BLUE_QUAIL = "31560", _("Blue Quail")
    BLUE_ROCK_THRUSH = "11660", _("Blue Rock Thrush")
    BLUE_WHISTLING_THRUSH = "11670", _("Blue Whistling Thrush")
    BLUE_AND_WHITE_FLYCATCHER = "13270", _("Blue-and-white Flycatcher")
    BLUE_BELLIED_ROLLER = "31440", _("Blue-bellied Roller")
    BLUE_BILLED_MALIMBE = "25400", _("Blue-billed Malimbe")
    BLUE_BILLED_TEAL = "30190", _("Blue-billed Teal")
    BLUE_BLACK_GRASSQUIT = "18050", _("Blue-black Grassquit")
    BLUE_BREASTED_BEE_EATER = "33260", _("Blue-breasted Bee-eater")
    BLUE_BREASTED_KINGFISHER = "32310", _("Blue-breasted Kingfisher")
    BLUE_CAPPED_MOTMOT = "27212", _("Blue-capped Motmot")
    BLUE_CAPPED_REDSTART = "11200", _("Blue-capped Redstart")
    BLUE_CAPPED_ROCK_THRUSH = "11630", _("Blue-capped Rock Thrush")
    BLUE_CHEEKED_BEE_EATER = "36430", _("Blue-cheeked Bee-eater")
    BLUE_CROWNED_PARAKEET = "35680", _("Blue-crowned Parakeet")
    BLUE_FOOTED_BOOBY = "00690", _("Blue-footed Booby")
    BLUE_FRONTED_REDSTART = "11240", _("Blue-fronted Redstart")
    BLUE_GREY_GNATCATCHER = "13210", _("Blue-grey Gnatcatcher")
    BLUE_HEADED_BEE_EATER = "33230", _("Blue-headed Bee-eater")
    BLUE_HEADED_COUCAL = "31010", _("Blue-headed Coucal")
    BLUE_HEADED_CRESTED_FLYCATCHER = "35290", _("Blue-headed Crested Flycatcher")
    BLUE_HEADED_VIREO = "16270", _("Blue-headed Vireo")
    BLUE_HEADED_WOOD_DOVE = "35350", _("Blue-headed Wood Dove")
    BLUE_MANTLED_CRESTED_FLYCATCHER = "23100", _("Blue-mantled Crested Flycatcher")
    BLUE_NAPED_MOUSEBIRD = "35380", _("Blue-naped Mousebird")
    BLUE_SHOULDERED_ROBIN_CHAT = "31520", _("Blue-shouldered Robin-Chat")
    BLUE_SPOTTED_WOOD_DOVE = "20010", _("Blue-spotted Wood Dove")
    BLUE_THROATED_BLUE_FLYCATCHER = "13260", _("Blue-throated Blue Flycatcher")
    BLUE_THROATED_BROWN_SUNBIRD = "33530", _("Blue-throated Brown Sunbird")
    BLUE_THROATED_MOUNTAINGEM = "08110", _("Blue-throated Mountaingem")
    BLUE_THROATED_ROLLER = "32090", _("Blue-throated Roller")
    BLUE_WINGED_MINLA = "14130", _("Blue-winged Minla")
    BLUE_WINGED_TEAL = "01920", _("Blue-winged Teal")
    BLUE_WINGED_WARBLER = "17230", _("Blue-winged Warbler")
    BLUETHROAT = "11060", _("Bluethroat")
    BLUNT_WINGED_WARBLER = "12460", _("Blunt-winged Warbler")
    BLYTH_S_LEAF_WARBLER = "12850", _("Blyth's Leaf Warbler")
    BLYTH_S_PIPIT = "10040", _("Blyth's Pipit")
    BLYTH_S_REED_WARBLER = "12480", _("Blyth's Reed Warbler")
    BLYTH_S_ROSEFINCH = "16940", _("Blyth's Rosefinch")
    BLYTH_S_TRAGOPAN = "03800", _("Blyth's Tragopan")
    BOAT_TAILED_GRACKLE = "19040", _("Boat-tailed Grackle")
    BOBOLINK = "18970", _("Bobolink")
    BOHEMIAN_WAXWING = "10480", _("Bohemian Waxwing")
    BOLLE_S_PIGEON = "06720", _("Bolle's Pigeon")
    BONAPARTE_S_GULL = "05810", _("Bonaparte's Gull")
    BONELLI_S_EAGLE = "02990", _("Bonelli's Eagle")
    BONIN_GROSBEAK = "17010", _("Bonin Grosbeak")
    BONIN_PETREL = "00300", _("Bonin Petrel")
    BONIN_THRUSH = "11740", _("Bonin Thrush")
    BONIN_WHITE_EYE = "15050", _("Bonin White-eye")
    BONIN_WOOD_PIGEON = "06770", _("Bonin Wood Pigeon")
    BOOTED_EAGLE = "02980", _("Booted Eagle")
    BOOTED_WARBLER = "12561", _("Booted Warbler")
    BOREAL_CHICKADEE = "14490", _("Boreal Chickadee")
    BOREAL_OWL = "07700", _("Boreal Owl")
    BOTTERI_S_SPARROW = "18090", _("Botteri's Sparrow")
    BOUCARD_S_WREN = "10530", _("Boucard's Wren")
    BOYD_S_SHEARWATER = "00483", _("Boyd's Shearwater")
    BRACHYRAMPHUS_MARMORATUS_SENSU_LATO = "06410", _("Brachyramphus marmoratus sensu lato")
    BRACHYRAMPHUS_SP = "06429", _("Brachyramphus sp.")
    BRAHMINY_KITE = "02400", _("Brahminy Kite")
    BRAHMINY_STARLING = "15770", _("Brahminy Starling")
    BRAMBLING = "16380", _("Brambling")
    BRAN_COLORED_FLYCATCHER = "27250", _("Bran-colored Flycatcher")
    BRANDT_S_CORMORANT = "00770", _("Brandt's Cormorant")
    BRANDT_S_MOUNTAIN_FINCH = "16700", _("Brandt's Mountain Finch")
    BRANT_GOOSE = "01680", _("Brant Goose")
    BRANTA_CANADENSIS_X_BRANTA_LEUCOPSIS = "90040", _("Branta canadensis x Branta leucopsis")
    BRANTA_CANADENSIS_X_BRANTA_LEUCOPSIS_2 = "90041", _("Branta canadensis x Branta leucopsis")
    BRANTA_CANADENSIS_X_BRANTA_LEUCOPSIS_3 = "90042", _("Branta canadensis x Branta leucopsis")
    BRANTA_LEUCOPSIS_X_BRANTA_RUFICOLLIS = "90490", _("Branta leucopsis x Branta ruficollis")
    BRANTA_LEUCOPSIS_X_BRANTA_RUFICOLLIS_2 = "90491", _("Branta leucopsis x Branta ruficollis")
    BRANTA_LEUCOPSIS_X_BRANTA_RUFICOLLIS_3 = "90492", _("Branta leucopsis x Branta ruficollis")
    BRANTA_SP = "01699", _("Branta sp.")
    BREWER_S_BLACKBIRD = "19000", _("Brewer's Blackbird")
    BREWER_S_SPARROW = "18200", _("Brewer's Sparrow")
    BRIDLED_SPARROW = "18080", _("Bridled Sparrow")
    BRIDLED_TERN = "06220", _("Bridled Tern")
    BRIDLED_TITMOUSE = "14470", _("Bridled Titmouse")
    BRISTLE_NOSED_BARBET = "32250", _("Bristle-nosed Barbet")
    BRISTLE_THIGHED_CURLEW = "05390", _("Bristle-thighed Curlew")
    BROAD_BILLED_HUMMINGBIRD = "08040", _("Broad-billed Hummingbird")
    BROAD_BILLED_PRION = "35900", _("Broad-billed Prion")
    BROAD_BILLED_ROLLER = "08440", _("Broad-billed Roller")
    BROAD_BILLED_SANDPIPER = "05140", _("Broad-billed Sandpiper")
    BROAD_TAILED_HUMMINGBIRD = "08210", _("Broad-tailed Hummingbird")
    BROAD_WINGED_HAWK = "02800", _("Broad-winged Hawk")
    BRONZE_MANNIKIN = "34940", _("Bronze Mannikin")
    BRONZE_TAILED_STARLING = "32720", _("Bronze-tailed Starling")
    BRONZE_WINGED_COURSER = "34730", _("Bronze-winged Courser")
    BRONZED_COWBIRD = "18980", _("Bronzed Cowbird")
    BROOKS_S_LEAF_WARBLER = "12990", _("Brooks's Leaf Warbler")
    BROWN_ACCENTOR = "10870", _("Brown Accentor")
    BROWN_BABBLER = "35310", _("Brown Babbler")
    BROWN_BOOBOOK = "07560", _("Brown Boobook")
    BROWN_BOOBY = "00700", _("Brown Booby")
    BROWN_BULLFINCH = "17060", _("Brown Bullfinch")
    BROWN_BUSH_WARBLER = "12240", _("Brown Bush Warbler")
    BROWN_CRAKE = "04220", _("Brown Crake")
    BROWN_DIPPER = "10510", _("Brown Dipper")
    BROWN_EARED_PHEASANT = "03890", _("Brown Eared Pheasant")
    BROWN_FISH_OWL = "07470", _("Brown Fish Owl")
    BROWN_ILLADOPSIS = "32510", _("Brown Illadopsis")
    BROWN_JAY = "15310", _("Brown Jay")
    BROWN_NODDY = "06300", _("Brown Noddy")
    BROWN_PARROTBILL = "13670", _("Brown Parrotbill")
    BROWN_PELICAN = "00910", _("Brown Pelican")
    BROWN_SHRIKE = "15130", _("Brown Shrike")
    BROWN_SKUA = "05693", _("Brown Skua")
    BROWN_SNAKE_EAGLE = "31210", _("Brown Snake Eagle")
    BROWN_THRASHER = "10690", _("Brown Thrasher")
    BROWN_TWINSPOT = "31380", _("Brown Twinspot")
    BROWN_WOOD_OWL = "07600", _("Brown Wood Owl")
    BROWN_WOODLAND_WARBLER = "12810", _("Brown Woodland Warbler")
    BROWN_BACKED_HONEYBIRD = "34500", _("Brown-backed Honeybird")
    BROWN_BACKED_SCRUB_ROBIN = "31110", _("Brown-backed Scrub Robin")
    BROWN_BACKED_WOODPECKER = "31700", _("Brown-backed Woodpecker")
    BROWN_BREASTED_BULBUL = "10330", _("Brown-breasted Bulbul")
    BROWN_BREASTED_FLYCATCHER = "13330", _("Brown-breasted Flycatcher")
    BROWN_CAPPED_WEAVER = "34240", _("Brown-capped Weaver")
    BROWN_CHEEKED_LAUGHINGTHRUSH = "14020", _("Brown-cheeked Laughingthrush")
    BROWN_CHESTED_ALETHE = "36530", _("Brown-chested Alethe")
    BROWN_CHESTED_LAPWING = "35440", _("Brown-chested Lapwing")
    BROWN_CRESTED_FLYCATCHER = "09360", _("Brown-crested Flycatcher")
    BROWN_CROWNED_TCHAGRA = "35080", _("Brown-crowned Tchagra")
    BROWN_EARED_BULBUL = "10390", _("Brown-eared Bulbul")
    BROWN_EARED_WOODPECKER = "30910", _("Brown-eared Woodpecker")
    BROWN_FLANKED_BUSH_WARBLER = "12150", _("Brown-flanked Bush Warbler")
    BROWN_FRONTED_WOODPECKER = "08860", _("Brown-fronted Woodpecker")
    BROWN_HEADED_COWBIRD = "18990", _("Brown-headed Cowbird")
    BROWN_HEADED_GULL = "05830", _("Brown-headed Gull")
    BROWN_HEADED_NUTHATCH = "14740", _("Brown-headed Nuthatch")
    BROWN_HEADED_THRUSH = "11900", _("Brown-headed Thrush")
    BROWN_HOODED_GULL = "20360", _("Brown-hooded Gull")
    BROWN_HOODED_KINGFISHER = "36440", _("Brown-hooded Kingfisher")
    BROWN_NECKED_RAVEN = "15710", _("Brown-necked Raven")
    BROWN_RUMPED_BUNTING = "31860", _("Brown-rumped Bunting")
    BROWN_THROATED_MARTIN = "09800", _("Brown-throated Martin")
    BROWN_THROATED_WATTLE_EYE = "22700", _("Brown-throated Wattle-eye")
    BROWN_WINGED_SCHIFFORNIS = "27410", _("Brown-winged Schiffornis")
    BRUBRU = "33780", _("Brubru")
    BRUCE_S_GREEN_PIGEON = "07030", _("Bruce's Green Pigeon")
    BUFF_BARRED_WARBLER = "12960", _("Buff-barred Warbler")
    BUFF_BELLIED_HUMMINGBIRD = "08080", _("Buff-bellied Hummingbird")
    BUFF_BELLIED_WARBLER = "34080", _("Buff-bellied Warbler")
    BUFF_BREASTED_FLYCATCHER = "09240", _("Buff-breasted Flycatcher")
    BUFF_BREASTED_SANDPIPER = "05160", _("Buff-breasted Sandpiper")
    BUFF_BREASTED_WHEATEAR = "11450", _("Buff-breasted Wheatear")
    BUFF_SPOTTED_FLUFFTAIL = "34790", _("Buff-spotted Flufftail")
    BUFF_SPOTTED_WOODPECKER = "30920", _("Buff-spotted Woodpecker")
    BUFF_THROATED_APALIS = "30450", _("Buff-throated Apalis")
    BUFF_THROATED_MONAL_PARTRIDGE = "03490", _("Buff-throated Monal-Partridge")
    BUFF_THROATED_SALTATOR = "27390", _("Buff-throated Saltator")
    BUFF_THROATED_SUNBIRD = "33470", _("Buff-throated Sunbird")
    BUFF_THROATED_WOODCREEPER = "27690", _("Buff-throated Woodcreeper")
    BUFFLEHEAD = "02160", _("Bufflehead")
    BULL_HEADED_SHRIKE = "15120", _("Bull-headed Shrike")
    BULLER_S_SHEARWATER = "00420", _("Buller's Shearwater")
    BULWER_S_PETREL = "00340", _("Bulwer's Petrel")
    BUMBLEBEE_HUMMINGBIRD = "08200", _("Bumblebee Hummingbird")
    BURCHELL_S_COUCAL = "26714", _("Burchell's Coucal")
    BURROWING_OWL = "07590", _("Burrowing Owl")
    BURROWING_PARROT = "26200", _("Burrowing Parrot")
    BUTEO_BUTEO_X_BUTEO_LAGOPUS = "90850", _("Buteo buteo x Buteo lagopus")
    BUTEO_BUTEO_X_BUTEO_RUFINUS = "90260", _("Buteo buteo x Buteo rufinus")
    BUTEO_BUTEO_X_BUTEO_RUFINUS_2 = "90261", _("Buteo buteo x Buteo rufinus")
    BUTEO_BUTEO_X_BUTEO_RUFINUS_3 = "90262", _("Buteo buteo x Buteo rufinus")
    BUTEO_SPP = "02919", _("Buteo spp.")
    BUTORIDES_VIRESCENS_SENSU_LATO = "01070", _("Butorides virescens sensu lato")
    CABANIS_S_BUNTING = "31870", _("Cabanis's Bunting")
    CABOT_S_TERN = "06111", _("Cabot's Tern")
    CACKLING_GOOSE = "01666", _("Cackling Goose")
    CACTUS_WREN = "10550", _("Cactus Wren")
    CAGE_EXOTIC_BIRDS = "24997", _("Cage & exotic birds")
    CALANDRA_LARK = "09610", _("Calandra Lark")
    CALIDRIS_ALPINA_SCHINZII_ARCTICA = "05128", _("Calidris alpina schinzii/arctica")
    CALIDRIS_SP = "05129", _("Calidris sp.")
    CALIFORNIA_CONDOR = "02290", _("California Condor")
    CALIFORNIA_GULL = "05930", _("California Gull")
    CALIFORNIA_QUAIL = "03410", _("California Quail")
    CALIFORNIA_THRASHER = "10770", _("California Thrasher")
    CALLIOPE_HUMMINGBIRD = "08190", _("Calliope Hummingbird")
    CALONECTRIS_DIOMEDEA_SENSU_LATO = "00360", _("Calonectris diomedea sensu lato")
    CAMEROON_MOUNTAIN_GREENBUL = "30260", _("Cameroon Mountain Greenbul")
    CAMEROON_OLIVE_GREENBUL = "34050", _("Cameroon Olive Greenbul")
    CAMEROON_SUNBIRD = "33580", _("Cameroon Sunbird")
    CAMPO_FLICKER = "26850", _("Campo Flicker")
    CANADA_GOOSE = "01660", _("Canada Goose")
    CANADA_JAY = "15420", _("Canada Jay")
    CANADA_WARBLER = "17730", _("Canada Warbler")
    CANARY_ISLANDS_CHIFFCHAFF = "13117", _("Canary Islands Chiffchaff")
    CANARY_ISLANDS_STONECHAT = "11380", _("Canary Islands Stonechat")
    CANVASBACK = "01970", _("Canvasback")
    CANYON_TOWHEE = "17990", _("Canyon Towhee")
    CANYON_WREN = "10570", _("Canyon Wren")
    CAPE_BARREN_GOOSE = "35620", _("Cape Barren Goose")
    CAPE_CORMORANT = "20040", _("Cape Cormorant")
    CAPE_GANNET = "00712", _("Cape Gannet")
    CAPE_MAY_WARBLER = "17490", _("Cape May Warbler")
    CAPE_PARROT = "34410", _("Cape Parrot")
    CAPE_TEAL = "01850", _("Cape Teal")
    CAPE_VERDE_SHEARWATER = "00362", _("Cape Verde Shearwater")
    CAPE_VERDE_SWIFT = "07930", _("Cape Verde Swift")
    CAPE_VERDE_WARBLER = "12490", _("Cape Verde Warbler")
    CAPRIMULGIDAE_SP = "07839", _("Caprimulgidae sp.")
    CAPUCHIN_BABBLER = "34020", _("Capuchin Babbler")
    CARDINAL_WOODPECKER = "31670", _("Cardinal Woodpecker")
    CARDUELIS_CITRINELLA_SENSU_LATO = "16440", _("Carduelis citrinella sensu lato")
    CARDUELIS_CHLORIS_ACANTHIS_LINARIA_SPINUS_SP = (
        "16649",
        _("Carduelis/Chloris/Acanthis/Linaria/Spinus sp."),
    )
    CARIBBEAN_ELAENIA = "09070", _("Caribbean Elaenia")
    CARIBBEAN_MARTIN = "09880", _("Caribbean Martin")
    CARMELITE_SUNBIRD = "33540", _("Carmelite Sunbird")
    CAROLINA_CHICKADEE = "14440", _("Carolina Chickadee")
    CAROLINA_PARAKEET = "07080", _("Carolina Parakeet")
    CAROLINA_WREN = "10630", _("Carolina Wren")
    CARRION_CROW = "15671", _("Carrion Crow")
    CASPIAN_GULL = "05927", _("Caspian Gull")
    CASPIAN_PLOVER = "04800", _("Caspian Plover")
    CASPIAN_SNOWCOCK = "03510", _("Caspian Snowcock")
    CASPIAN_TERN = "06060", _("Caspian Tern")
    CASPIAN_TIT = "36070", _("Caspian Tit")
    CASSIN_S_AUKLET = "06480", _("Cassin's Auklet")
    CASSIN_S_FINCH = "16810", _("Cassin's Finch")
    CASSIN_S_FLYCATCHER = "33340", _("Cassin's Flycatcher")
    CASSIN_S_HAWK_EAGLE = "34970", _("Cassin's Hawk-Eagle")
    CASSIN_S_HONEYBIRD = "34490", _("Cassin's Honeybird")
    CASSIN_S_KINGBIRD = "09410", _("Cassin's Kingbird")
    CASSIN_S_SPARROW = "18100", _("Cassin's Sparrow")
    CASSIN_S_SPINETAIL = "33460", _("Cassin's Spinetail")
    CATHARUS_MINIMUS_SENSU_LATO = "11780", _("Catharus minimus sensu lato")
    CAUCASIAN_GROUSE = "03330", _("Caucasian Grouse")
    CAUCASIAN_SNOWCOCK = "03500", _("Caucasian Snowcock")
    CAVE_SWALLOW = "09970", _("Cave Swallow")
    CEDAR_WAXWING = "10460", _("Cedar Waxwing")
    CEPPHUS_SP = "06409", _("Cepphus sp.")
    CERTHIA_SP = "14879", _("Certhia sp.")
    CERULEAN_KINGFISHER = "30110", _("Cerulean Kingfisher")
    CERULEAN_WARBLER = "17350", _("Cerulean Warbler")
    CETTI_S_WARBLER = "12200", _("Cetti's Warbler")
    CHACO_EAGLE = "32330", _("Chaco Eagle")
    CHALK_BROWED_MOCKINGBIRD = "27200", _("Chalk-browed Mockingbird")
    CHARADRIIFORMES = "05659", _("Charadriiformes")
    CHARADRIUS_SP = "04839", _("Charadrius sp.")
    CHATTERING_CISTICOLA = "31220", _("Chattering Cisticola")
    CHEER_PHEASANT = "03910", _("Cheer Pheasant")
    CHESTNUT_BUNTING = "18750", _("Chestnut Bunting")
    CHESTNUT_MUNIA = "20293", _("Chestnut Munia")
    CHESTNUT_THRUSH = "11880", _("Chestnut Thrush")
    CHESTNUT_WATTLE_EYE = "24700", _("Chestnut Wattle-eye")
    CHESTNUT_BACKED_CHICKADEE = "14500", _("Chestnut-backed Chickadee")
    CHESTNUT_BACKED_SPARROW_LARK = "31940", _("Chestnut-backed Sparrow-Lark")
    CHESTNUT_BELLIED_ROCK_THRUSH = "11650", _("Chestnut-bellied Rock Thrush")
    CHESTNUT_BELLIED_SANDGROUSE = "06600", _("Chestnut-bellied Sandgrouse")
    CHESTNUT_BELLIED_SEED_FINCH = "27310", _("Chestnut-bellied Seed Finch")
    CHESTNUT_BELLIED_STARLING = "32750", _("Chestnut-bellied Starling")
    CHESTNUT_BREASTED_NIGRITA = "33740", _("Chestnut-breasted Nigrita")
    CHESTNUT_CAPPED_FLYCATCHER = "31950", _("Chestnut-capped Flycatcher")
    CHESTNUT_CHEEKED_STARLING = "15800", _("Chestnut-cheeked Starling")
    CHESTNUT_COLLARED_LONGSPUR = "18480", _("Chestnut-collared Longspur")
    CHESTNUT_CROWNED_BUSH_WARBLER = "12160", _("Chestnut-crowned Bush Warbler")
    CHESTNUT_CROWNED_LAUGHINGTHRUSH = "14040", _("Chestnut-crowned Laughingthrush")
    CHESTNUT_CROWNED_SPARROW_WEAVER = "34170", _("Chestnut-crowned Sparrow-Weaver")
    CHESTNUT_EARED_BUNTING = "18690", _("Chestnut-eared Bunting")
    CHESTNUT_FLANKED_SPARROWHAWK = "30010", _("Chestnut-flanked Sparrowhawk")
    CHESTNUT_FLANKED_WHITE_EYE = "15020", _("Chestnut-flanked White-eye")
    CHESTNUT_HEADED_TESIA = "12120", _("Chestnut-headed Tesia")
    CHESTNUT_SIDED_WARBLER = "17340", _("Chestnut-sided Warbler")
    CHESTNUT_THROATED_MONAL_PARTRIDGE = "03480", _("Chestnut-throated Monal-Partridge")
    CHESTNUT_WINGED_STARLING = "33800", _("Chestnut-winged Starling")
    CHIHUAHUAN_RAVEN = "15730", _("Chihuahuan Raven")
    CHILEAN_FLAMINGO = "20230", _("Chilean Flamingo")
    CHILOE_WIGEON = "25800", _("Chiloe Wigeon")
    CHIMNEY_SWIFT = "07900", _("Chimney Swift")
    CHINESE_BABAX = "13810", _("Chinese Babax")
    CHINESE_BAMBOO_PARTRIDGE = "03760", _("Chinese Bamboo Partridge")
    CHINESE_BUSH_WARBLER = "12230", _("Chinese Bush Warbler")
    CHINESE_CRESTED_TERN = "06100", _("Chinese Crested Tern")
    CHINESE_EGRET = "01160", _("Chinese Egret")
    CHINESE_FULVETTA = "14200", _("Chinese Fulvetta")
    CHINESE_GREY_SHRIKE = "15210", _("Chinese Grey Shrike")
    CHINESE_GROSBEAK = "17150", _("Chinese Grosbeak")
    CHINESE_GROUSE = "03270", _("Chinese Grouse")
    CHINESE_HWAMEI = "13970", _("Chinese Hwamei")
    CHINESE_MONAL = "03850", _("Chinese Monal")
    CHINESE_NUTHATCH = "14680", _("Chinese Nuthatch")
    CHINESE_POND_HERON = "01100", _("Chinese Pond Heron")
    CHINESE_SPARROWHAWK = "02710", _("Chinese Sparrowhawk")
    CHINESE_THRUSH = "11990", _("Chinese Thrush")
    CHINSTRAP_PENGUIN = "20210", _("Chinstrap Penguin")
    CHIPPING_SPARROW = "18180", _("Chipping Sparrow")
    CHLIDONIAS_SP = "06289", _("Chlidonias sp.")
    CHLORIS_CHLORIS_X_SPINUS_SPINUS = "90161", _("Chloris chloris x Spinus spinus")
    CHOCOLATE_BACKED_KINGFISHER = "32280", _("Chocolate-backed Kingfisher")
    CHRISTMAS_SHEARWATER = "00450", _("Christmas Shearwater")
    CHROICOCEPHALUS_RIDIBUNDUS_X_ICHTHYAETUS_MELANOCEPHALUS = (
        "90530",
        _("Chroicocephalus ridibundus x Ichthyaetus melanocephalus"),
    )
    CHROICOCEPHALUS_RIDIBUNDUS_X_ICHTHYAETUS_MELANOCEPHALUS_2 = (
        "90531",
        _("Chroicocephalus ridibundus x Ichthyaetus melanocephalus"),
    )
    CHROICOCEPHALUS_RIDIBUNDUS_X_ICHTHYAETUS_MELANOCEPHALUS_3 = (
        "90532",
        _("Chroicocephalus ridibundus x Ichthyaetus melanocephalus"),
    )
    CHUBB_S_CISTICOLA = "31260", _("Chubb's Cisticola")
    CHUCK_WILL_S_WIDOW = "07820", _("Chuck-will's-widow")
    CHUKAR_PARTRIDGE = "03550", _("Chukar Partridge")
    CICONIA_SP = "01349", _("Ciconia sp.")
    CINEREOUS_BUNTING = "18650", _("Cinereous Bunting")
    CINEREOUS_VULTURE = "02550", _("Cinereous Vulture")
    CINEREOUS_BREASTED_SPINETAIL = "27510", _("Cinereous-breasted Spinetail")
    CINNAMON_BITTERN = "01010", _("Cinnamon Bittern")
    CINNAMON_TEAL = "01930", _("Cinnamon Teal")
    CINNAMON_BELLIED_FLOWERPIERCER = "17930", _("Cinnamon-bellied Flowerpiercer")
    CINNAMON_BREASTED_BUNTING = "18641", _("Cinnamon-breasted Bunting")
    CIRCUS_CYANEUS_X_CIRCUS_MACROURUS = "90350", _("Circus cyaneus x Circus macrourus")
    CIRCUS_MACROURUS_X_CIRCUS_PYGARGUS = "90390", _("Circus macrourus x Circus pygargus")
    CIRCUS_SP = "02649", _("Circus sp.")
    CIRL_BUNTING = "18580", _("Cirl Bunting")
    CISTICOLA_ABERRANS_EMINI_SENSU_LATO = "31280", _("Cisticola aberrans emini sensu lato")
    CISTOTHORUS_PLATENSIS_SENSU_LATO = "10580", _("Cistothorus platensis sensu lato")
    CITRIL_FINCH = "16441", _("Citril Finch")
    CITRINE_WAGTAIL = "10180", _("Citrine Wagtail")
    CLAMOROUS_REED_WARBLER = "12520", _("Clamorous Reed Warbler")
    CLANGA_POMARINA_X_CLANGA_CLANGA = "90180", _("Clanga pomarina x Clanga clanga")
    CLANGA_POMARINA_X_CLANGA_CLANGA_2 = "90181", _("Clanga pomarina x Clanga clanga")
    CLANGA_POMARINA_X_CLANGA_CLANGA_3 = "90182", _("Clanga pomarina x Clanga clanga")
    CLAPPERTON_S_SPURFOWL = "34600", _("Clapperton's Spurfowl")
    CLARK_S_NUTCRACKER = "15560", _("Clark's Nutcracker")
    CLAY_COLORED_SPARROW = "18190", _("Clay-colored Sparrow")
    CLAY_COLORED_THRUSH = "12050", _("Clay-colored Thrush")
    COAL_TIT = "14610", _("Coal Tit")
    COLIMA_WARBLER = "17280", _("Colima Warbler")
    COLLARED_CROW = "15690", _("Collared Crow")
    COLLARED_FINCHBILL = "10320", _("Collared Finchbill")
    COLLARED_FLYCATCHER = "13480", _("Collared Flycatcher")
    COLLARED_GROSBEAK = "17120", _("Collared Grosbeak")
    COLLARED_OWLET = "07540", _("Collared Owlet")
    COLLARED_PRATINCOLE = "04650", _("Collared Pratincole")
    COLLARED_SUNBIRD = "25100", _("Collared Sunbird")
    COLUMBA_LIVIA_VAR_DOMESTICA = "06657", _("Columba livia var. domestica")
    COLUMBIFORMES_SP = "06829", _("Columbiformes sp.")
    COMMON_BABBLER = "13780", _("Common Babbler")
    COMMON_BLACK_HAWK = "02770", _("Common Black Hawk")
    COMMON_BLACKBIRD = "11870", _("Common Blackbird")
    COMMON_BULBUL = "10370", _("Common Bulbul")
    COMMON_BUTTONQUAIL = "04000", _("Common Buttonquail")
    COMMON_BUZZARD = "02870", _("Common Buzzard")
    COMMON_CHIFFCHAFF = "13118", _("Common Chiffchaff")
    COMMON_CRANE = "04330", _("Common Crane")
    COMMON_CUCKOO = "07240", _("Common Cuckoo")
    COMMON_DIVING_PETREL = "20170", _("Common Diving Petrel")
    COMMON_EIDER = "02060", _("Common Eider")
    COMMON_EMERALD_DOVE = "06930", _("Common Emerald Dove")
    COMMON_FIRECREST = "13150", _("Common Firecrest")
    COMMON_GOLDENEYE = "02180", _("Common Goldeneye")
    COMMON_GRACKLE = "19050", _("Common Grackle")
    COMMON_GRASSHOPPER_WARBLER = "12360", _("Common Grasshopper Warbler")
    COMMON_GREENSHANK = "05480", _("Common Greenshank")
    COMMON_GROUND_DOVE = "06980", _("Common Ground Dove")
    COMMON_GULL = "05900", _("Common Gull")
    COMMON_KESTREL = "03040", _("Common Kestrel")
    COMMON_KINGFISHER = "08310", _("Common Kingfisher")
    COMMON_LINNET = "16600", _("Common Linnet")
    COMMON_LOON = "00040", _("Common Loon")
    COMMON_MERGANSER = "02230", _("Common Merganser")
    COMMON_MOORHEN = "04240", _("Common Moorhen")
    COMMON_MURRE = "06340", _("Common Murre")
    COMMON_MYNA = "15870", _("Common Myna")
    COMMON_NIGHTHAWK = "07860", _("Common Nighthawk")
    COMMON_NIGHTINGALE = "11040", _("Common Nightingale")
    COMMON_OSTRICH = "00010", _("Common Ostrich")
    COMMON_PHEASANT = "03940", _("Common Pheasant")
    COMMON_POCHARD = "01980", _("Common Pochard")
    COMMON_POORWILL = "07840", _("Common Poorwill")
    COMMON_QUAIL = "03700", _("Common Quail")
    COMMON_REDSHANK = "05460", _("Common Redshank")
    COMMON_REDSTART = "11220", _("Common Redstart")
    COMMON_REED_BUNTING = "18770", _("Common Reed Bunting")
    COMMON_REED_WARBLER = "12510", _("Common Reed Warbler")
    COMMON_RINGED_PLOVER = "04700", _("Common Ringed Plover")
    COMMON_ROCK_THRUSH = "11620", _("Common Rock Thrush")
    COMMON_ROSEFINCH = "16790", _("Common Rosefinch")
    COMMON_SANDPIPER = "05560", _("Common Sandpiper")
    COMMON_SCOTER = "02130", _("Common Scoter")
    COMMON_SHELDUCK = "01730", _("Common Shelduck")
    COMMON_SNIPE = "05190", _("Common Snipe")
    COMMON_STARLING = "15820", _("Common Starling")
    COMMON_SWIFT = "07950", _("Common Swift")
    COMMON_TERN = "06150", _("Common Tern")
    COMMON_WAXBILL = "16150", _("Common Waxbill")
    COMMON_WHITETHROAT = "12750", _("Common Whitethroat")
    COMMON_WOOD_PIGEON = "06700", _("Common Wood Pigeon")
    COMMON_WOODSHRIKE = "10240", _("Common Woodshrike")
    COMMON_YELLOWTHROAT = "17620", _("Common Yellowthroat")
    COMPACT_WEAVER = "33910", _("Compact Weaver")
    CONGO_PIED_HORNBILL = "35221", _("Congo Pied Hornbill")
    CONGO_SERPENT_EAGLE = "31810", _("Congo Serpent Eagle")
    CONNECTICUT_WARBLER = "17680", _("Connecticut Warbler")
    COOK_S_PETREL = "00310", _("Cook's Petrel")
    COOPER_S_HAWK = "02740", _("Cooper's Hawk")
    COPPER_PHEASANT = "03920", _("Copper Pheasant")
    COPPER_SUNBIRD = "33520", _("Copper Sunbird")
    COQUI_FRANCOLIN = "33960", _("Coqui Francolin")
    CORN_BUNTING = "18820", _("Corn Bunting")
    CORN_CRAKE = "04210", _("Corn Crake")
    CORSICAN_FINCH = "16442", _("Corsican Finch")
    CORSICAN_NUTHATCH = "14700", _("Corsican Nuthatch")
    CORVUS_CORNIX_X_CORVUS_CORONE = "90200", _("Corvus cornix x Corvus corone")
    CORVUS_CORNIX_X_CORVUS_CORONE_2 = "90201", _("Corvus cornix x Corvus corone")
    CORVUS_CORNIX_X_CORVUS_CORONE_3 = "90202", _("Corvus cornix x Corvus corone")
    CORVUS_CORONE_SENSU_LATO = "15670", _("Corvus corone sensu lato")
    CORVUS_SP = "15749", _("Corvus sp.")
    CORY_S_SHEARWATER = "00361", _("Cory's Shearwater")
    COSTA_S_HUMMINGBIRD = "08170", _("Costa's Hummingbird")
    COTTON_PYGMY_GOOSE = "01760", _("Cotton Pygmy Goose")
    COUCH_S_KINGBIRD = "09440", _("Couch's Kingbird")
    CRAB_PLOVER = "04580", _("Crab-plover")
    CRANE_HAWK = "02590", _("Crane Hawk")
    CRAVERI_S_MURRELET = "06440", _("Craveri's Murrelet")
    CREAM_COLORED_COURSER = "04640", _("Cream-colored Courser")
    CREAMY_BELLIED_THRUSH = "27650", _("Creamy-bellied Thrush")
    CRESCENT_CHESTED_WARBLER = "17300", _("Crescent-chested Warbler")
    CRESTED_AUKLET = "06490", _("Crested Auklet")
    CRESTED_BUNTING = "18830", _("Crested Bunting")
    CRESTED_CARACARA = "03020", _("Crested Caracara")
    CRESTED_DORADITO = "27370", _("Crested Doradito")
    CRESTED_DUCK = "36170", _("Crested Duck")
    CRESTED_FINCHBILL = "10310", _("Crested Finchbill")
    CRESTED_HONEY_BUZZARD = "02320", _("Crested Honey Buzzard")
    CRESTED_IBIS = "01410", _("Crested Ibis")
    CRESTED_KINGFISHER = "08360", _("Crested Kingfisher")
    CRESTED_LARK = "09720", _("Crested Lark")
    CRESTED_MALIMBE = "33090", _("Crested Malimbe")
    CRESTED_MYNA = "15890", _("Crested Myna")
    CRESTED_SERPENT_EAGLE = "02580", _("Crested Serpent Eagle")
    CRESTED_SHELDUCK = "01720", _("Crested Shelduck")
    CRESTED_TIT = "14540", _("Crested Tit")
    CRESTED_TIT_WARBLER = "13180", _("Crested Tit-warbler")
    CRETZSCHMAR_S_BUNTING = "18680", _("Cretzschmar's Bunting")
    CRICKET_WARBLER = "34960", _("Cricket Warbler")
    CRIMSON_SEEDCRACKER = "36110", _("Crimson Seedcracker")
    CRIMSON_BREASTED_SHRIKE = "32790", _("Crimson-breasted Shrike")
    CRIMSON_BROWED_FINCH = "17000", _("Crimson-browed Finch")
    CRIMSON_COLLARED_GROSBEAK = "18900", _("Crimson-collared Grosbeak")
    CRIMSON_NAPED_WOODPECKER = "08820", _("Crimson-naped Woodpecker")
    CRIMSON_RUMPED_WAXBILL = "26450", _("Crimson-rumped Waxbill")
    CRIMSON_WINGED_FINCH = "16730", _("Crimson-winged Finch")
    CRISSAL_THRASHER = "10760", _("Crissal Thrasher")
    CROAKING_CISTICOLA = "31330", _("Croaking Cisticola")
    CROSSLEY_S_GROUND_THRUSH = "35550", _("Crossley's Ground Thrush")
    CROWNED_SANDGROUSE = "06580", _("Crowned Sandgrouse")
    CUBAN_AMAZON = "07110", _("Cuban Amazon")
    CUBAN_EMERALD = "08030", _("Cuban Emerald")
    CUBAN_GRASSQUIT = "18020", _("Cuban Grassquit")
    CUBAN_PEWEE = "09270", _("Cuban Pewee")
    CUCKOO_FINCH = "30290", _("Cuckoo-finch")
    CURLEW_SANDPIPER = "05090", _("Curlew Sandpiper")
    CURRUCA_CANTILLANS_SENSU_LATO = "12650", _("Curruca cantillans sensu lato")
    CURRUCA_CURRUCA_MINULA_SENSU_LATO = "26580", _("Curruca curruca minula sensu lato")
    CURRUCA_HORTENSIS_SENSU_LATO = "12720", _("Curruca hortensis sensu lato")
    CURRUCA_NANA_SENSU_LATO = "12700", _("Curruca nana sensu lato")
    CURRUCA_SARDA_SENSU_LATO = "12610", _("Curruca sarda sensu lato")
    CURVE_BILLED_THRASHER = "10740", _("Curve-billed Thrasher")
    CUT_THROAT_FINCH = "30160", _("Cut-throat Finch")
    CYANISTES_CAERULEUS_X_CYANISTES_CYANUS = "90150", _("Cyanistes caeruleus x Cyanistes cyanus")
    CYANISTES_CAERULEUS_X_CYANISTES_CYANUS_2 = "90151", _("Cyanistes caeruleus x Cyanistes cyanus")
    CYANISTES_CAERULEUS_X_CYANISTES_CYANUS_3 = "90152", _("Cyanistes caeruleus x Cyanistes cyanus")
    CYGNUS_SP = "01559", _("Cygnus sp.")
    CYPRUS_SCOPS_OWL = "36360", _("Cyprus Scops Owl")
    CYPRUS_WARBLER = "12680", _("Cyprus Warbler")
    CYPRUS_WHEATEAR = "11471", _("Cyprus Wheatear")
    DALMATIAN_PELICAN = "00890", _("Dalmatian Pelican")
    DAMARA_TERN = "34990", _("Damara Tern")
    DARJEELING_WOODPECKER = "08810", _("Darjeeling Woodpecker")
    DARK_CHANTING_GOSHAWK = "02650", _("Dark Chanting Goshawk")
    DARK_BACKED_WEAVER = "34220", _("Dark-backed Weaver")
    DARK_BREASTED_ROSEFINCH = "16780", _("Dark-breasted Rosefinch")
    DARK_EYED_JUNCO = "18420", _("Dark-eyed Junco")
    DARK_RUMPED_ROSEFINCH = "16870", _("Dark-rumped Rosefinch")
    DARK_SIDED_FLYCATCHER = "13300", _("Dark-sided Flycatcher")
    DARK_THROATED_SEEDEATER = "27480", _("Dark-throated Seedeater")
    DARTFORD_WARBLER = "12620", _("Dartford Warbler")
    DAURIAN_JACKDAW = "15610", _("Daurian Jackdaw")
    DAURIAN_PARTRIDGE = "03680", _("Daurian Partridge")
    DAURIAN_REDSTART = "11260", _("Daurian Redstart")
    DAURIAN_STARLING = "15790", _("Daurian Starling")
    DAVISON_S_LEAF_WARBLER = "12840", _("Davison's Leaf Warbler")
    DEAD_SEA_SPARROW = "15950", _("Dead Sea Sparrow")
    DELICHON_URBICUM_X_RIPARIA_RIPARIA = "90280", _("Delichon urbicum x Riparia riparia")
    DELICHON_URBICUM_X_RIPARIA_RIPARIA_2 = "90281", _("Delichon urbicum x Riparia riparia")
    DELICHON_URBICUM_X_RIPARIA_RIPARIA_3 = "90282", _("Delichon urbicum x Riparia riparia")
    DEMOISELLE_CRANE = "04410", _("Demoiselle Crane")
    DENDROCOPOS_MAJOR_X_DENDROCOPOS_LEUCOTOS = (
        "90400",
        _("Dendrocopos major x Dendrocopos leucotos"),
    )
    DENDROCOPOS_MAJOR_X_DENDROCOPOS_SYRIACUS = (
        "90760",
        _("Dendrocopos major x Dendrocopos syriacus"),
    )
    DENDROCOPOS_SP = "08979", _("Dendrocopos sp.")
    DENHAM_S_BUSTARD = "04430", _("Denham's Bustard")
    DESERT_CISTICOLA = "31230", _("Desert Cisticola")
    DESERT_FINCH = "16740", _("Desert Finch")
    DESERT_LARK = "09570", _("Desert Lark")
    DESERT_OWL = "07621", _("Desert Owl")
    DESERT_SPARROW = "15970", _("Desert Sparrow")
    DESERT_WHEATEAR = "11490", _("Desert Wheatear")
    DESERTAS_PETREL = "35990", _("Desertas Petrel")
    DICKCISSEL = "18840", _("Dickcissel")
    DIEDERIK_CUCKOO = "07200", _("Diederik Cuckoo")
    DIOMEDEA_EXULANS_SENSU_LATO = "00200", _("Diomedea exulans sensu lato")
    DORST_S_CISTICOLA = "31270", _("Dorst's Cisticola")
    DOUBLE_COLLARED_SEEDEATER = "27450", _("Double-collared Seedeater")
    DOUBLE_CRESTED_CORMORANT = "00780", _("Double-crested Cormorant")
    DOUBLE_SPURRED_SPURFOWL = "03660", _("Double-spurred Spurfowl")
    DOUBLE_TOOTHED_BARBET = "32950", _("Double-toothed Barbet")
    DOWNY_WOODPECKER = "08930", _("Downy Woodpecker")
    DUNLIN = "05120", _("Dunlin")
    DUNN_S_LARK = "09540", _("Dunn's Lark")
    DUNNOCK = "10840", _("Dunnock")
    DUPONT_S_LARK = "09590", _("Dupont's Lark")
    DUSKY_CRESTED_FLYCATCHER = "31850", _("Dusky Crested Flycatcher")
    DUSKY_FULVETTA = "14230", _("Dusky Fulvetta")
    DUSKY_GROUSE = "03250", _("Dusky Grouse")
    DUSKY_INDIGOBIRD = "35470", _("Dusky Indigobird")
    DUSKY_LONG_TAILED_CUCKOO = "31080", _("Dusky Long-tailed Cuckoo")
    DUSKY_THRUSH = "11962", _("Dusky Thrush")
    DUSKY_TURTLE_DOVE = "06880", _("Dusky Turtle Dove")
    DUSKY_WARBLER = "13030", _("Dusky Warbler")
    DUSKY_BLUE_FLYCATCHER = "33350", _("Dusky-blue Flycatcher")
    DUSKY_CAPPED_FLYCATCHER = "09320", _("Dusky-capped Flycatcher")
    DWARF_BITTERN = "01020", _("Dwarf Bittern")
    DYBOWSKI_S_TWINSPOT = "32100", _("Dybowski's Twinspot")
    EASTERN_BEARDED_GREENBUL = "31590", _("Eastern Bearded Greenbul")
    EASTERN_BLACK_EARED_WHEATEAR = "11482", _("Eastern Black-eared Wheatear")
    EASTERN_BLUEBIRD = "11340", _("Eastern Bluebird")
    EASTERN_BONELLI_S_WARBLER = "13072", _("Eastern Bonelli's Warbler")
    EASTERN_BRONZE_NAPED_PIGEON = "31410", _("Eastern Bronze-naped Pigeon")
    EASTERN_CRESTED_GUINEAFOWL = "32230", _("Eastern Crested Guineafowl")
    EASTERN_CROWNED_WARBLER = "12860", _("Eastern Crowned Warbler")
    EASTERN_IMPERIAL_EAGLE = "02950", _("Eastern Imperial Eagle")
    EASTERN_KINGBIRD = "09480", _("Eastern Kingbird")
    EASTERN_MEADOWLARK = "19070", _("Eastern Meadowlark")
    EASTERN_OLIVACEOUS_WARBLER = "12550", _("Eastern Olivaceous Warbler")
    EASTERN_ORPHEAN_WARBLER = "12725", _("Eastern Orphean Warbler")
    EASTERN_PHOEBE = "09090", _("Eastern Phoebe")
    EASTERN_RED_RUMPED_SWALLOW = "09951", _("Eastern Red-rumped Swallow")
    EASTERN_ROCK_NUTHATCH = "14800", _("Eastern Rock Nuthatch")
    EASTERN_SCREECH_OWL = "07410", _("Eastern Screech Owl")
    EASTERN_SUBALPINE_WARBLER = "12656", _("Eastern Subalpine Warbler")
    EASTERN_TOWHEE = "17980", _("Eastern Towhee")
    EASTERN_WATTLED_CUCKOOSHRIKE = "30850", _("Eastern Wattled Cuckooshrike")
    EASTERN_WHIP_POOR_WILL = "07830", _("Eastern Whip-poor-will")
    EASTERN_WOOD_PEWEE = "09300", _("Eastern Wood Pewee")
    EASTERN_YELLOW_WAGTAIL = "26643", _("Eastern Yellow Wagtail")
    EASTERN_YELLOW_BILLED_BARBET = "35250", _("Eastern Yellow-billed Barbet")
    EGRETTA_SP = "01219", _("Egretta sp.")
    EGYPTIAN_GOOSE = "01700", _("Egyptian Goose")
    EGYPTIAN_NIGHTJAR = "07810", _("Egyptian Nightjar")
    EGYPTIAN_PLOVER = "04630", _("Egyptian Plover")
    EGYPTIAN_VULTURE = "02470", _("Egyptian Vulture")
    EL_ORO_PARAKEET = "26000", _("El Oro Parakeet")
    ELEGANT_EUPHONIA = "17920", _("Elegant Euphonia")
    ELEGANT_QUAIL = "03430", _("Elegant Quail")
    ELEGANT_TERN = "06120", _("Elegant Tern")
    ELEGANT_TROGON = "08250", _("Elegant Trogon")
    ELEONORA_S_FALCON = "03110", _("Eleonora's Falcon")
    ELF_OWL = "07550", _("Elf Owl")
    ELLIOT_S_LAUGHINGTHRUSH = "14010", _("Elliot's Laughingthrush")
    ELLIOT_S_WOODPECKER = "31660", _("Elliot's Woodpecker")
    EMBERIZA_LEUCOCEPHALOS_X_EMBERIZA_CITRINELLA = (
        "90520",
        _("Emberiza leucocephalos x Emberiza citrinella"),
    )
    EMBERIZA_LEUCOCEPHALOS_X_EMBERIZA_CITRINELLA_2 = (
        "90521",
        _("Emberiza leucocephalos x Emberiza citrinella"),
    )
    EMBERIZA_LEUCOCEPHALOS_X_EMBERIZA_CITRINELLA_3 = (
        "90522",
        _("Emberiza leucocephalos x Emberiza citrinella"),
    )
    EMBERIZA_RUSTICA_X_EMBERIZA_PUSILLA = "90810", _("Emberiza rustica x Emberiza pusilla")
    EMBERIZA_SP = "18819", _("Emberiza sp.")
    EMBERIZA_STRIOLATA_SENSU_LATO = "18630", _("Emberiza striolata sensu lato")
    EMBERIZA_TAHAPISI_SENSU_LATO = "18640", _("Emberiza tahapisi sensu lato")
    EMERALD_SPOTTED_WOOD_DOVE = "36460", _("Emerald-spotted Wood Dove")
    EMIN_S_SHRIKE = "32890", _("Emin's Shrike")
    EMPEROR_GOOSE = "01650", _("Emperor Goose")
    EMPEROR_PENGUIN = "27760", _("Emperor Penguin")
    EMU = "35920", _("Emu")
    EPAULET_ORIOLE = "27100", _("Epaulet Oriole")
    ERCKEL_S_SPURFOWL = "28010", _("Erckel's Spurfowl")
    ESKIMO_CURLEW = "05370", _("Eskimo Curlew")
    ESTRILDA_SP = "20439", _("Estrilda sp.")
    ETHIOPIAN_BOUBOU = "25600", _("Ethiopian Boubou")
    ETHIOPIAN_SWALLOW = "32390", _("Ethiopian Swallow")
    EULER_S_FLYCATCHER = "27150", _("Euler's Flycatcher")
    EURASIAN_BITTERN = "00950", _("Eurasian Bittern")
    EURASIAN_BLACKCAP = "12770", _("Eurasian Blackcap")
    EURASIAN_BLUE_TIT = "14620", _("Eurasian Blue Tit")
    EURASIAN_BULLFINCH = "17100", _("Eurasian Bullfinch")
    EURASIAN_CHAFFINCH = "16360", _("Eurasian Chaffinch")
    EURASIAN_COLLARED_DOVE = "06840", _("Eurasian Collared Dove")
    EURASIAN_COOT = "04290", _("Eurasian Coot")
    EURASIAN_CRAG_MARTIN = "09910", _("Eurasian Crag Martin")
    EURASIAN_CURLEW = "05410", _("Eurasian Curlew")
    EURASIAN_DOTTEREL = "04820", _("Eurasian Dotterel")
    EURASIAN_EAGLE_OWL = "07440", _("Eurasian Eagle-Owl")
    EURASIAN_GOLDEN_ORIOLE = "15080", _("Eurasian Golden Oriole")
    EURASIAN_GOSHAWK = "02670", _("Eurasian Goshawk")
    EURASIAN_HOBBY = "03100", _("Eurasian Hobby")
    EURASIAN_HOOPOE = "08460", _("Eurasian Hoopoe")
    EURASIAN_JAY = "15390", _("Eurasian Jay")
    EURASIAN_MAGPIE = "15490", _("Eurasian Magpie")
    EURASIAN_NUTHATCH = "14790", _("Eurasian Nuthatch")
    EURASIAN_OYSTERCATCHER = "04500", _("Eurasian Oystercatcher")
    EURASIAN_PENDULINE_TIT = "14900", _("Eurasian Penduline Tit")
    EURASIAN_PYGMY_OWL = "07510", _("Eurasian Pygmy Owl")
    EURASIAN_SCOPS_OWL = "07390", _("Eurasian Scops Owl")
    EURASIAN_SISKIN = "16540", _("Eurasian Siskin")
    EURASIAN_SKYLARK = "09760", _("Eurasian Skylark")
    EURASIAN_SPARROWHAWK = "02690", _("Eurasian Sparrowhawk")
    EURASIAN_SPOONBILL = "01440", _("Eurasian Spoonbill")
    EURASIAN_STONE_CURLEW = "04590", _("Eurasian Stone-curlew")
    EURASIAN_TEAL = "01840", _("Eurasian Teal")
    EURASIAN_THREE_TOED_WOODPECKER = "08980", _("Eurasian Three-toed Woodpecker")
    EURASIAN_TREE_SPARROW = "15980", _("Eurasian Tree Sparrow")
    EURASIAN_TREECREEPER = "14860", _("Eurasian Treecreeper")
    EURASIAN_WHIMBREL = "05380", _("Eurasian Whimbrel")
    EURASIAN_WIGEON = "01790", _("Eurasian Wigeon")
    EURASIAN_WOODCOCK = "05290", _("Eurasian Woodcock")
    EURASIAN_WREN = "10660", _("Eurasian Wren")
    EURASIAN_WRYNECK = "08480", _("Eurasian Wryneck")
    EUROPEAN_BEE_EATER = "08400", _("European Bee-eater")
    EUROPEAN_GOLDEN_PLOVER = "04850", _("European Golden Plover")
    EUROPEAN_GOLDFINCH = "16530", _("European Goldfinch")
    EUROPEAN_GREEN_WOODPECKER = "08561", _("European Green Woodpecker")
    EUROPEAN_GREENFINCH = "16490", _("European Greenfinch")
    EUROPEAN_HERRING_GULL = "36380", _("European Herring Gull")
    EUROPEAN_HONEY_BUZZARD = "02310", _("European Honey Buzzard")
    EUROPEAN_NIGHTJAR = "07780", _("European Nightjar")
    EUROPEAN_PIED_FLYCATCHER = "13490", _("European Pied Flycatcher")
    EUROPEAN_RED_RUMPED_SWALLOW = "09950", _("European Red-rumped Swallow")
    EUROPEAN_ROBIN = "10990", _("European Robin")
    EUROPEAN_ROCK_PIPIT = "10145", _("European Rock Pipit")
    EUROPEAN_ROLLER = "08410", _("European Roller")
    EUROPEAN_SERIN = "16400", _("European Serin")
    EUROPEAN_SHAG = "00800", _("European Shag")
    EUROPEAN_STONECHAT = "11397", _("European Stonechat")
    EUROPEAN_STORM_PETREL = "00520", _("European Storm Petrel")
    EUROPEAN_TURTLE_DOVE = "06870", _("European Turtle Dove")
    EVENING_GROSBEAK = "17180", _("Evening Grosbeak")
    EVERSMANN_S_REDSTART = "11180", _("Eversmann's Redstart")
    EXCLAMATORY_PARADISE_WHYDAH = "35480", _("Exclamatory Paradise Whydah")
    EYEBROWED_THRUSH = "11950", _("Eyebrowed Thrush")
    FAIRY_PRION = "27740", _("Fairy Prion")
    FALCATED_DUCK = "01810", _("Falcated Duck")
    FALCO_PEREGRINUS_HYBRID = "90060", _("Falco peregrinus hybrid")
    FALCO_SP = "03219", _("Falco sp.")
    FAMILIAR_CHAT = "31100", _("Familiar Chat")
    FAN_TAILED_GRASSBIRD = "34820", _("Fan-tailed Grassbird")
    FAN_TAILED_RAVEN = "15740", _("Fan-tailed Raven")
    FAN_TAILED_WARBLER = "17780", _("Fan-tailed Warbler")
    FAN_TAILED_WIDOWBIRD = "32010", _("Fan-tailed Widowbird")
    FANTI_SAW_WING = "34540", _("Fanti Saw-wing")
    FAR_EASTERN_CURLEW = "05430", _("Far Eastern Curlew")
    FAWN_BREASTED_WAXBILL = "31980", _("Fawn-breasted Waxbill")
    FAWN_BREASTED_WREN = "27610", _("Fawn-breasted Wren")
    FEA_S_PETREL = "00264", _("Fea's Petrel")
    FERNANDO_PO_BATIS = "30620", _("Fernando Po Batis")
    FERNANDO_PO_SWIFT = "30520", _("Fernando Po Swift")
    FERRUGINOUS_DUCK = "02020", _("Ferruginous Duck")
    FERRUGINOUS_FLYCATCHER = "13290", _("Ferruginous Flycatcher")
    FERRUGINOUS_HAWK = "02910", _("Ferruginous Hawk")
    FERRUGINOUS_PYGMY_OWL = "07530", _("Ferruginous Pygmy Owl")
    FICEDULA_ALBICOLLIS_X_FICEDULA_HYPOLEUCA = (
        "90140",
        _("Ficedula albicollis x Ficedula hypoleuca"),
    )
    FICEDULA_ALBICOLLIS_X_FICEDULA_HYPOLEUCA_2 = (
        "90141",
        _("Ficedula albicollis x Ficedula hypoleuca"),
    )
    FICEDULA_ALBICOLLIS_X_FICEDULA_HYPOLEUCA_3 = (
        "90142",
        _("Ficedula albicollis x Ficedula hypoleuca"),
    )
    FICEDULA_PARVA_SENSU_LATO = "13430", _("Ficedula parva sensu lato")
    FICEDULA_SP = "13499", _("Ficedula sp.")
    FICEDULA_SP_HYBRID = "90130", _("Ficedula sp. Hybrid")
    FIELD_SPARROW = "18210", _("Field Sparrow")
    FIELDFARE = "11980", _("Fieldfare")
    FIERY_BREASTED_BUSHSHRIKE = "33040", _("Fiery-breasted Bushshrike")
    FIERY_NECKED_NIGHTJAR = "30970", _("Fiery-necked Nightjar")
    FINE_SPOTTED_WOODPECKER = "26520", _("Fine-spotted Woodpecker")
    FINSCH_S_RUFOUS_THRUSH = "33670", _("Finsch's Rufous Thrush")
    FINSCH_S_WHEATEAR = "11500", _("Finsch's Wheatear")
    FIRE_BELLIED_WOODPECKER = "31720", _("Fire-bellied Woodpecker")
    FIRE_BREASTED_FLOWERPECKER = "15000", _("Fire-breasted Flowerpecker")
    FIRE_CAPPED_TIT = "14880", _("Fire-capped Tit")
    FIRE_TAILED_MYZORNIS = "14080", _("Fire-tailed Myzornis")
    FIRE_TAILED_SUNBIRD = "14980", _("Fire-tailed Sunbird")
    FIRETHROAT = "11100", _("Firethroat")
    FIREWOOD_GATHERER = "28020", _("Firewood-gatherer")
    FISCHER_S_LOVEBIRD = "35710", _("Fischer's Lovebird")
    FISH_CROW = "15660", _("Fish Crow")
    FIVE_STRIPED_SPARROW = "18120", _("Five-striped Sparrow")
    FLAME_COLORED_TANAGER = "17840", _("Flame-colored Tanager")
    FLAMMULATED_BAMBOO_TYRANT = "27070", _("Flammulated Bamboo Tyrant")
    FLAMMULATED_OWL = "07400", _("Flammulated Owl")
    FLAPPET_LARK = "33290", _("Flappet Lark")
    FLESH_FOOTED_SHEARWATER = "00380", _("Flesh-footed Shearwater")
    FLIGHTLESS_CORMORANT = "36190", _("Flightless Cormorant")
    FLORIDA_SCRUB_JAY = "15370", _("Florida Scrub Jay")
    FORBES_S_PLOVER = "31130", _("Forbes's Plover")
    FOREST_PENDULINE_TIT = "30310", _("Forest Penduline Tit")
    FOREST_WAGTAIL = "10160", _("Forest Wagtail")
    FOREST_WOOD_HOOPOE = "33990", _("Forest Wood Hoopoe")
    FORK_TAILED_DRONGO = "21500", _("Fork-tailed Drongo")
    FORK_TAILED_STORM_PETREL = "00540", _("Fork-tailed Storm Petrel")
    FORSTER_S_TERN = "06180", _("Forster's Tern")
    FOUR_BANDED_SANDGROUSE = "34620", _("Four-banded Sandgrouse")
    FOX_KESTREL = "32110", _("Fox Kestrel")
    FRANKLIN_S_GULL = "05770", _("Franklin's Gull")
    FRASER_S_EAGLE_OWL = "30750", _("Fraser's Eagle-Owl")
    FRASER_S_FOREST_FLYCATCHER = "32140", _("Fraser's Forest Flycatcher")
    FRASER_S_RUFOUS_THRUSH = "33680", _("Fraser's Rufous Thrush")
    FRASER_S_SUNBIRD = "30340", _("Fraser's Sunbird")
    FRECKLED_NIGHTJAR = "30980", _("Freckled Nightjar")
    FRINGILLA_COELEBS_X_FRINGILLA_MONTIFRINGILLA = (
        "90220",
        _("Fringilla coelebs x Fringilla montifringilla"),
    )
    FRINGILLA_COELEBS_X_FRINGILLA_MONTIFRINGILLA_2 = (
        "90221",
        _("Fringilla coelebs x Fringilla montifringilla"),
    )
    FRINGILLA_COELEBS_X_FRINGILLA_MONTIFRINGILLA_3 = (
        "90222",
        _("Fringilla coelebs x Fringilla montifringilla"),
    )
    FRINGILLA_SP = "16389", _("Fringilla sp.")
    FRINGILLA_TEYDEA_SENSU_LATO = "16370", _("Fringilla teydea sensu lato")
    FUJIAN_NILTAVA = "13240", _("Fujian Niltava")
    FULVOUS_BABBLER = "13800", _("Fulvous Babbler")
    FULVOUS_PARROTBILL = "13730", _("Fulvous Parrotbill")
    FULVOUS_WHISTLING_DUCK = "01490", _("Fulvous Whistling Duck")
    FUSCOUS_FLYCATCHER = "26840", _("Fuscous Flycatcher")
    F_LLEBORN_S_BOUBOU = "32830", _("Fülleborn's Boubou")
    GABAR_GOSHAWK = "02660", _("Gabar Goshawk")
    GABON_WOODPECKER = "31680", _("Gabon Woodpecker")
    GADWALL = "01820", _("Gadwall")
    GALERIDA_SP = "09739", _("Galerida sp.")
    GALLINAGO_MEDIA_X_GALLINAGO_GALLINAGO = "90450", _("Gallinago media x Gallinago gallinago")
    GAMBAGA_FLYCATCHER = "13360", _("Gambaga Flycatcher")
    GAMBEL_S_QUAIL = "03420", _("Gambel's Quail")
    GARDEN_WARBLER = "12760", _("Garden Warbler")
    GARGANEY = "01910", _("Garganey")
    GAVIA_SP = "00059", _("Gavia sp.")
    GENTOO_PENGUIN = "20220", _("Gentoo Penguin")
    GEOTHLYPIS_AEQUINOCTIALIS_SENSU_LATO = "27060", _("Geothlypis aequinoctialis sensu lato")
    GIANT_BABAX = "13820", _("Giant Babax")
    GIANT_KINGBIRD = "09460", _("Giant Kingbird")
    GIANT_KINGFISHER = "33140", _("Giant Kingfisher")
    GIANT_LAUGHINGTHRUSH = "13940", _("Giant Laughingthrush")
    GILA_WOODPECKER = "08670", _("Gila Woodpecker")
    GILDED_FLICKER = "08520", _("Gilded Flicker")
    GLAREOLA_SP = "04689", _("Glareola sp.")
    GLAUCOUS_GULL = "05990", _("Glaucous Gull")
    GLAUCOUS_WINGED_GULL = "05960", _("Glaucous-winged Gull")
    GLOSSY_IBIS = "01360", _("Glossy Ibis")
    GODLEWSKI_S_BUNTING = "35770", _("Godlewski's Bunting")
    GOLDCREST = "13140", _("Goldcrest")
    GOLDEN_BUSH_ROBIN = "11140", _("Golden Bush Robin")
    GOLDEN_EAGLE = "02960", _("Golden Eagle")
    GOLDEN_GREENBUL = "30820", _("Golden Greenbul")
    GOLDEN_NIGHTJAR = "07800", _("Golden Nightjar")
    GOLDEN_PARROTBILL = "13750", _("Golden Parrotbill")
    GOLDEN_PHEASANT = "03960", _("Golden Pheasant")
    GOLDEN_VIREO = "16300", _("Golden Vireo")
    GOLDEN_BREASTED_BUNTING = "31880", _("Golden-breasted Bunting")
    GOLDEN_BREASTED_FULVETTA = "14160", _("Golden-breasted Fulvetta")
    GOLDEN_CHEEKED_WARBLER = "17460", _("Golden-cheeked Warbler")
    GOLDEN_CROWNED_KINGLET = "13160", _("Golden-crowned Kinglet")
    GOLDEN_CROWNED_SPARROW = "18410", _("Golden-crowned Sparrow")
    GOLDEN_CROWNED_WARBLER = "17790", _("Golden-crowned Warbler")
    GOLDEN_FRONTED_WOODPECKER = "08660", _("Golden-fronted Woodpecker")
    GOLDEN_HEADED_MANAKIN = "36200", _("Golden-headed Manakin")
    GOLDEN_NAPED_FINCH = "17030", _("Golden-naped Finch")
    GOLDEN_TAILED_WOODPECKER = "30890", _("Golden-tailed Woodpecker")
    GOLDEN_WINGED_WARBLER = "17220", _("Golden-winged Warbler")
    GOLIATH_HERON = "01250", _("Goliath Heron")
    GOSLING_S_BUNTING = "18642", _("Gosling's Bunting")
    GOUGH_FINCH = "36010", _("Gough Finch")
    GOULD_S_PETREL = "00330", _("Gould's Petrel")
    GOULD_S_SHORTWING = "10970", _("Gould's Shortwing")
    GRACE_S_WARBLER = "17380", _("Grace's Warbler")
    GRACEFUL_PRINIA = "12270", _("Graceful Prinia")
    GRAN_CANARIA_BLUE_CHAFFINCH = "16372", _("Gran Canaria Blue Chaffinch")
    GRANDALA = "11310", _("Grandala")
    GRASS_WREN = "10581", _("Grass Wren")
    GRASSHOPPER_BUZZARD = "30800", _("Grasshopper Buzzard")
    GRASSHOPPER_SPARROW = "18280", _("Grasshopper Sparrow")
    GRASSLAND_SPARROW = "26730", _("Grassland Sparrow")
    GRAY_S_GRASSHOPPER_WARBLER = "12390", _("Gray's Grasshopper Warbler")
    GREAT_ANTSHRIKE = "27530", _("Great Antshrike")
    GREAT_AUK = "06370", _("Great Auk")
    GREAT_BLACK_BACKED_GULL = "06000", _("Great Black-backed Gull")
    GREAT_BLUE_HERON = "01230", _("Great Blue Heron")
    GREAT_BLUE_TURACO = "31500", _("Great Blue Turaco")
    GREAT_BUSTARD = "04460", _("Great Bustard")
    GREAT_CORMORANT = "00720", _("Great Cormorant")
    GREAT_CRESTED_FLYCATCHER = "09370", _("Great Crested Flycatcher")
    GREAT_CRESTED_GREBE = "00090", _("Great Crested Grebe")
    GREAT_EGRET = "01210", _("Great Egret")
    GREAT_FRIGATEBIRD = "00920", _("Great Frigatebird")
    GREAT_GREY_OWL = "07660", _("Great Grey Owl")
    GREAT_GREY_SHRIKE = "15200", _("Great Grey Shrike")
    GREAT_HORNED_OWL = "07430", _("Great Horned Owl")
    GREAT_KISKADEE = "09400", _("Great Kiskadee")
    GREAT_KNOT = "04950", _("Great Knot")
    GREAT_LIZARD_CUCKOO = "07300", _("Great Lizard Cuckoo")
    GREAT_PARROTBILL = "13650", _("Great Parrotbill")
    GREAT_REED_WARBLER = "12530", _("Great Reed Warbler")
    GREAT_ROSEFINCH = "16960", _("Great Rosefinch")
    GREAT_SHEARWATER = "00400", _("Great Shearwater")
    GREAT_SKUA = "05690", _("Great Skua")
    GREAT_SNIPE = "05200", _("Great Snipe")
    GREAT_SPARROW = "22500", _("Great Sparrow")
    GREAT_SPOTTED_CUCKOO = "07160", _("Great Spotted Cuckoo")
    GREAT_SPOTTED_WOODPECKER = "08760", _("Great Spotted Woodpecker")
    GREAT_STONE_CURLEW = "04620", _("Great Stone-curlew")
    GREAT_TIT = "14640", _("Great Tit")
    GREAT_WHITE_PELICAN = "00880", _("Great White Pelican")
    GREAT_TAILED_GRACKLE = "19020", _("Great-tailed Grackle")
    GREATER_BLUE_EARED_STARLING = "32730", _("Greater Blue-eared Starling")
    GREATER_CRESTED_TERN = "06080", _("Greater Crested Tern")
    GREATER_FLAMINGO = "01472", _("Greater Flamingo")
    GREATER_HONEYGUIDE = "32540", _("Greater Honeyguide")
    GREATER_HOOPOE_LARK = "09580", _("Greater Hoopoe-Lark")
    GREATER_NECKLACED_LAUGHINGTHRUSH = "13860", _("Greater Necklaced Laughingthrush")
    GREATER_PAINTED_SNIPE = "04490", _("Greater Painted-snipe")
    GREATER_PEWEE = "09280", _("Greater Pewee")
    GREATER_PRAIRIE_CHICKEN = "03360", _("Greater Prairie Chicken")
    GREATER_RHEA = "35660", _("Greater Rhea")
    GREATER_ROADRUNNER = "07330", _("Greater Roadrunner")
    GREATER_SAND_PLOVER = "04790", _("Greater Sand Plover")
    GREATER_SCAUP = "02040", _("Greater Scaup")
    GREATER_SHORT_TOED_LARK = "09680", _("Greater Short-toed Lark")
    GREATER_SPOTTED_EAGLE = "02930", _("Greater Spotted Eagle")
    GREATER_SWAMP_WARBLER = "30060", _("Greater Swamp Warbler")
    GREATER_THORNBIRD = "27330", _("Greater Thornbird")
    GREATER_WHITE_FRONTED_GOOSE = "01590", _("Greater White-fronted Goose")
    GREATER_YELLOWLEGS = "05500", _("Greater Yellowlegs")
    GREATER_YELLOWNAPE = "08540", _("Greater Yellownape")
    GREEN_CROMBEC = "24400", _("Green Crombec")
    GREEN_HERON = "01071", _("Green Heron")
    GREEN_HYLIA = "24500", _("Green Hylia")
    GREEN_KINGFISHER = "08320", _("Green Kingfisher")
    GREEN_LONGTAIL = "35390", _("Green Longtail")
    GREEN_PARAKEET = "07070", _("Green Parakeet")
    GREEN_PHEASANT = "03950", _("Green Pheasant")
    GREEN_SANDPIPER = "05530", _("Green Sandpiper")
    GREEN_SHRIKE_BABBLER = "14110", _("Green Shrike-babbler")
    GREEN_TWINSPOT = "33130", _("Green Twinspot")
    GREEN_WARBLER = "12910", _("Green Warbler")
    GREEN_WOOD_HOOPOE = "34000", _("Green Wood Hoopoe")
    GREEN_BACKED_CAMAROPTERA = "21200", _("Green-backed Camaroptera")
    GREEN_BACKED_EREMOMELA = "31910", _("Green-backed Eremomela")
    GREEN_BACKED_TIT = "14660", _("Green-backed Tit")
    GREEN_BREASTED_BUSHSHRIKE = "33050", _("Green-breasted Bushshrike")
    GREEN_CROWNED_WARBLER = "12780", _("Green-crowned Warbler")
    GREEN_HEADED_SUNBIRD = "33660", _("Green-headed Sunbird")
    GREEN_TAILED_BRISTLEBILL = "30650", _("Green-tailed Bristlebill")
    GREEN_TAILED_SUNBIRD = "14970", _("Green-tailed Sunbird")
    GREEN_TAILED_TOWHEE = "17970", _("Green-tailed Towhee")
    GREEN_THROATED_SUNBIRD = "33610", _("Green-throated Sunbird")
    GREEN_WINGED_PYTILIA = "34690", _("Green-winged Pytilia")
    GREEN_WINGED_TEAL = "01842", _("Green-winged Teal")
    GREENISH_ELAENIA = "09060", _("Greenish Elaenia")
    GREENISH_WARBLER = "12930", _("Greenish Warbler")
    GREY_APALIS = "30400", _("Grey Apalis")
    GREY_BUNTING = "18520", _("Grey Bunting")
    GREY_BUSH_CHAT = "11420", _("Grey Bush Chat")
    GREY_CATBIRD = "10800", _("Grey Catbird")
    GREY_CROWNED_CRANE = "27990", _("Grey Crowned Crane")
    GREY_CUCKOOSHRIKE = "31470", _("Grey Cuckooshrike")
    GREY_FRANCOLIN = "03650", _("Grey Francolin")
    GREY_GROUND_THRUSH = "35560", _("Grey Ground Thrush")
    GREY_HERON = "01220", _("Grey Heron")
    GREY_HYPOCOLIUS = "10490", _("Grey Hypocolius")
    GREY_KESTREL = "32120", _("Grey Kestrel")
    GREY_KINGBIRD = "09450", _("Grey Kingbird")
    GREY_LAUGHINGTHRUSH = "13880", _("Grey Laughingthrush")
    GREY_LONGBILL = "36130", _("Grey Longbill")
    GREY_PARROT = "34570", _("Grey Parrot")
    GREY_PARTRIDGE = "03670", _("Grey Partridge")
    GREY_PETREL = "27790", _("Grey Petrel")
    GREY_PLOVER = "04860", _("Grey Plover")
    GREY_PRATINCOLE = "32170", _("Grey Pratincole")
    GREY_SILKY_FLYCATCHER = "10450", _("Grey Silky-flycatcher")
    GREY_SUNBIRD = "22310", _("Grey Sunbird")
    GREY_THRASHER = "10720", _("Grey Thrasher")
    GREY_TIT_FLYCATCHER = "22200", _("Grey Tit-Flycatcher")
    GREY_TREEPIE = "15480", _("Grey Treepie")
    GREY_VIREO = "16260", _("Grey Vireo")
    GREY_WAGTAIL = "10190", _("Grey Wagtail")
    GREY_WAXBILL = "26440", _("Grey Waxbill")
    GREY_BACKED_CAMAROPTERA = "24300", _("Grey-backed Camaroptera")
    GREY_BACKED_FISCAL = "32880", _("Grey-backed Fiscal")
    GREY_BACKED_SHRIKE = "15180", _("Grey-backed Shrike")
    GREY_BACKED_STORM_PETREL = "20140", _("Grey-backed Storm Petrel")
    GREY_BACKED_THRUSH = "11930", _("Grey-backed Thrush")
    GREY_BREASTED_MARTIN = "09870", _("Grey-breasted Martin")
    GREY_CAPPED_PYGMY_WOODPECKER = "08880", _("Grey-capped Pygmy Woodpecker")
    GREY_CHEEKED_FULVETTA = "14240", _("Grey-cheeked Fulvetta")
    GREY_CHEEKED_THRUSH = "11781", _("Grey-cheeked Thrush")
    GREY_CHESTED_BABBLER = "32630", _("Grey-chested Babbler")
    GREY_CRESTED_TIT = "14530", _("Grey-crested Tit")
    GREY_CROWNED_GOLDFINCH = "16532", _("Grey-crowned Goldfinch")
    GREY_CROWNED_ROSY_FINCH = "16720", _("Grey-crowned Rosy Finch")
    GREY_CROWNED_YELLOWTHROAT = "17660", _("Grey-crowned Yellowthroat")
    GREY_FACED_BUZZARD = "02760", _("Grey-faced Buzzard")
    GREY_FRONTED_DOVE = "27180", _("Grey-fronted Dove")
    GREY_HEADED_ALBATROSS = "20090", _("Grey-headed Albatross")
    GREY_HEADED_BATIS = "30610", _("Grey-headed Batis")
    GREY_HEADED_BRISTLEBILL = "23800", _("Grey-headed Bristlebill")
    GREY_HEADED_BROADBILL = "34920", _("Grey-headed Broadbill")
    GREY_HEADED_BULLFINCH = "17090", _("Grey-headed Bullfinch")
    GREY_HEADED_BUSHSHRIKE = "33030", _("Grey-headed Bushshrike")
    GREY_HEADED_CANARY_FLYCATCHER = "13500", _("Grey-headed Canary-flycatcher")
    GREY_HEADED_CHICKADEE = "14480", _("Grey-headed Chickadee")
    GREY_HEADED_GREENBUL = "34060", _("Grey-headed Greenbul")
    GREY_HEADED_GULL = "05840", _("Grey-headed Gull")
    GREY_HEADED_KINGFISHER = "08290", _("Grey-headed Kingfisher")
    GREY_HEADED_LAPWING = "04890", _("Grey-headed Lapwing")
    GREY_HEADED_NIGRITA = "33750", _("Grey-headed Nigrita")
    GREY_HEADED_OLIVEBACK = "33720", _("Grey-headed Oliveback")
    GREY_HEADED_SWAMPHEN = "04273", _("Grey-headed Swamphen")
    GREY_HEADED_TANAGER = "26990", _("Grey-headed Tanager")
    GREY_HEADED_WOODPECKER = "08550", _("Grey-headed Woodpecker")
    GREY_HOODED_FULVETTA = "14220", _("Grey-hooded Fulvetta")
    GREY_HOODED_PARROTBILL = "13710", _("Grey-hooded Parrotbill")
    GREY_LINED_HAWK = "02790", _("Grey-lined Hawk")
    GREY_NECKED_BUNTING = "18670", _("Grey-necked Bunting")
    GREY_NECKED_ROCKFOWL = "34100", _("Grey-necked Rockfowl")
    GREY_RUMPED_SWALLOW = "34550", _("Grey-rumped Swallow")
    GREY_SIDED_BUSH_WARBLER = "12190", _("Grey-sided Bush Warbler")
    GREY_SIDED_LAUGHINGTHRUSH = "13960", _("Grey-sided Laughingthrush")
    GREY_SIDED_THRUSH = "11920", _("Grey-sided Thrush")
    GREY_STREAKED_FLYCATCHER = "13310", _("Grey-streaked Flycatcher")
    GREY_TAILED_TATTLER = "05580", _("Grey-tailed Tattler")
    GREY_THROATED_LEAFTOSSER = "36210", _("Grey-throated Leaftosser")
    GREY_THROATED_RAIL = "30940", _("Grey-throated Rail")
    GREY_THROATED_TIT_FLYCATCHER = "33430", _("Grey-throated Tit-Flycatcher")
    GREY_WINGED_ROBIN_CHAT = "31540", _("Grey-winged Robin-Chat")
    GREYLAG_GOOSE = "01610", _("Greylag Goose")
    GRIFFON_VULTURE = "02510", _("Griffon Vulture")
    GROOVE_BILLED_ANI = "07320", _("Groove-billed Ani")
    GROUND_TIT = "15550", _("Ground Tit")
    GRUS_SP = "04409", _("Grus sp.")
    GUADALUPE_MURRELET = "06430", _("Guadalupe Murrelet")
    GUADALUPE_STORM_PETREL = "00620", _("Guadalupe Storm Petrel")
    GUAM_KINGFISHER = "08300", _("Guam Kingfisher")
    GUINEA_TURACO = "35070", _("Guinea Turaco")
    GULL_BILLED_TERN = "06050", _("Gull-billed Tern")
    GYRFALCON = "03180", _("Gyrfalcon")
    G_LDENST_DT_S_REDSTART = "11280", _("Güldenstädt's Redstart")
    HADADA_IBIS = "30670", _("Hadada Ibis")
    HAIR_CRESTED_DRONGO = "15270", _("Hair-crested Drongo")
    HAIRY_WOODPECKER = "08960", _("Hairy Woodpecker")
    HAIRY_BREASTED_BARBET = "35270", _("Hairy-breasted Barbet")
    HAMERKOP = "01260", _("Hamerkop")
    HAMMOND_S_FLYCATCHER = "09160", _("Hammond's Flycatcher")
    HAPPY_WREN = "10610", _("Happy Wren")
    HARLEQUIN_DUCK = "02110", _("Harlequin Duck")
    HARLEQUIN_QUAIL = "26600", _("Harlequin Quail")
    HARRIS_S_HAWK = "02780", _("Harris's Hawk")
    HARRIS_S_SPARROW = "18380", _("Harris's Sparrow")
    HARTLAUB_S_DUCK = "34630", _("Hartlaub's Duck")
    HAUXWELL_S_THRUSH = "27660", _("Hauxwell's Thrush")
    HAWFINCH = "17170", _("Hawfinch")
    HAZEL_GROUSE = "03260", _("Hazel Grouse")
    HEARD_ISLAND_SHAG = "20192", _("Heard Island Shag")
    HEERMANN_S_GULL = "05860", _("Heermann's Gull")
    HELLMAYR_S_PIPIT = "26740", _("Hellmayr's Pipit")
    HELMETED_GUINEAFOWL = "03980", _("Helmeted Guineafowl")
    HEN_HARRIER = "02610", _("Hen Harrier")
    HENSLOW_S_SPARROW = "18330", _("Henslow's Sparrow")
    HERMIT_THRUSH = "11760", _("Hermit Thrush")
    HERMIT_WARBLER = "17430", _("Hermit Warbler")
    HEUGLIN_S_MASKED_WEAVER = "34230", _("Heuglin's Masked Weaver")
    HEUGLIN_S_WHEATEAR = "33790", _("Heuglin's Wheatear")
    HILL_PARTRIDGE = "03730", _("Hill Partridge")
    HILL_PIGEON = "06660", _("Hill Pigeon")
    HIMALAYAN_BEAUTIFUL_ROSEFINCH = "16830", _("Himalayan Beautiful Rosefinch")
    HIMALAYAN_BULBUL = "10350", _("Himalayan Bulbul")
    HIMALAYAN_CUCKOO = "07250", _("Himalayan Cuckoo")
    HIMALAYAN_CUTIA = "14090", _("Himalayan Cutia")
    HIMALAYAN_MONAL = "03830", _("Himalayan Monal")
    HIMALAYAN_PRINIA = "12290", _("Himalayan Prinia")
    HIMALAYAN_RUBYTHROAT = "11070", _("Himalayan Rubythroat")
    HIMALAYAN_SNOWCOCK = "03520", _("Himalayan Snowcock")
    HIMALAYAN_SWIFTLET = "07890", _("Himalayan Swiftlet")
    HIMALAYAN_VULTURE = "02520", _("Himalayan Vulture")
    HIMALAYAN_WHITE_BROWED_ROSEFINCH = "16920", _("Himalayan White-browed Rosefinch")
    HIMALAYAN_WOODPECKER = "08800", _("Himalayan Woodpecker")
    HIPPOLAIS_ICTERINA_X_HIPPOLAIS_POLYGLOTTA = (
        "90170",
        _("Hippolais icterina x Hippolais polyglotta"),
    )
    HIPPOLAIS_ICTERINA_X_HIPPOLAIS_POLYGLOTTA_2 = (
        "90171",
        _("Hippolais icterina x Hippolais polyglotta"),
    )
    HIPPOLAIS_ICTERINA_X_HIPPOLAIS_POLYGLOTTA_3 = (
        "90172",
        _("Hippolais icterina x Hippolais polyglotta"),
    )
    HIPPOLAIS_IDUNA_SP = "12609", _("Hippolais/Iduna sp.")
    HIRUNDINIDAE_SP = "10019", _("Hirundinidae sp.")
    HIRUNDO_RUSTICA_X_CECROPSIS_DAURICA = "90510", _("Hirundo rustica x Cecropsis daurica")
    HIRUNDO_RUSTICA_X_CECROPSIS_DAURICA_2 = "90511", _("Hirundo rustica x Cecropsis daurica")
    HIRUNDO_RUSTICA_X_CECROPSIS_DAURICA_3 = "90512", _("Hirundo rustica x Cecropsis daurica")
    HIRUNDO_RUSTICA_X_DELICHON_URBICUM = "90100", _("Hirundo rustica x Delichon urbicum")
    HIRUNDO_RUSTICA_X_DELICHON_URBICUM_2 = "90101", _("Hirundo rustica x Delichon urbicum")
    HIRUNDO_RUSTICA_X_DELICHON_URBICUM_3 = "90102", _("Hirundo rustica x Delichon urbicum")
    HIRUNDO_RUSTICA_X_RIPARIA_RIPARIA = "90440", _("Hirundo rustica x Riparia riparia")
    HOARY_THROATED_BARWING = "14120", _("Hoary-throated Barwing")
    HODGSON_S_REDSTART = "11230", _("Hodgson's Redstart")
    HONEYGUIDE_GREENBUL = "30590", _("Honeyguide Greenbul")
    HOODED_CRANE = "04350", _("Hooded Crane")
    HOODED_CROW = "15673", _("Hooded Crow")
    HOODED_GROSBEAK = "17190", _("Hooded Grosbeak")
    HOODED_MERGANSER = "02190", _("Hooded Merganser")
    HOODED_ORIOLE = "19160", _("Hooded Oriole")
    HOODED_VULTURE = "02480", _("Hooded Vulture")
    HOODED_WARBLER = "17710", _("Hooded Warbler")
    HOODED_WHEATEAR = "11550", _("Hooded Wheatear")
    HOODED_YELLOWTHROAT = "17650", _("Hooded Yellowthroat")
    HOOK_BILLED_KITE = "02300", _("Hook-billed Kite")
    HORNED_GREBE = "00110", _("Horned Grebe")
    HORNED_LARK = "09780", _("Horned Lark")
    HORNED_PUFFIN = "06550", _("Horned Puffin")
    HORSFIELD_S_BRONZE_CUCKOO = "21300", _("Horsfield's Bronze Cuckoo")
    HORUS_SWIFT = "30510", _("Horus Swift")
    HOUSE_BUNTING = "35840", _("House Bunting")
    HOUSE_CROW = "15620", _("House Crow")
    HOUSE_FINCH = "16820", _("House Finch")
    HOUSE_SPARROW = "15910", _("House Sparrow")
    HUDSON_S_BLACK_TYRANT = "27130", _("Hudson's Black Tyrant")
    HUDSONIAN_GODWIT = "05330", _("Hudsonian Godwit")
    HUDSONIAN_WHIMBREL = "05381", _("Hudsonian Whimbrel")
    HUME_S_LEAF_WARBLER = "13002", _("Hume's Leaf Warbler")
    HUME_S_SHORT_TOED_LARK = "09690", _("Hume's Short-toed Lark")
    HUME_S_WHEATEAR = "11560", _("Hume's Wheatear")
    HUTTON_S_VIREO = "16290", _("Hutton's Vireo")
    HYDROBATES_CASTRO_SENSU_LATO = "00580", _("Hydrobates castro sensu lato")
    HYDROBATES_SP = "00639", _("Hydrobates sp.")
    IAGO_SPARROW = "15960", _("Iago Sparrow")
    IBADAN_MALIMBE = "33080", _("Ibadan Malimbe")
    IBERIAN_CHIFFCHAFF = "13115", _("Iberian Chiffchaff")
    IBERIAN_GREEN_WOODPECKER = "08562", _("Iberian Green Woodpecker")
    IBERIAN_GREY_SHRIKE = "15203", _("Iberian Grey Shrike")
    IBERIAN_MAGPIE = "15470", _("Iberian Magpie")
    IBISBILL = "04540", _("Ibisbill")
    ICELAND_GULL = "05980", _("Iceland Gull")
    ICTERINE_GREENBUL = "34040", _("Icterine Greenbul")
    ICTERINE_WARBLER = "12590", _("Icterine Warbler")
    ICTERUS_DOMINICENSIS_SENSU_LATO = "19150", _("Icterus dominicensis sensu lato")
    IDUNA_CALIGATA_SENSU_LATO = "12560", _("Iduna caligata sensu lato")
    IJIMA_S_LEAF_WARBLER = "12890", _("Ijima's Leaf Warbler")
    IMPERIAL_SHAG = "20190", _("Imperial Shag")
    IMPERIAL_WOODPECKER = "09010", _("Imperial Woodpecker")
    INCA_JAY = "15290", _("Inca Jay")
    INDIAN_BLUE_ROBIN = "11110", _("Indian Blue Robin")
    INDIAN_CUCKOO = "07230", _("Indian Cuckoo")
    INDIAN_NIGHTJAR = "07760", _("Indian Nightjar")
    INDIAN_NUTHATCH = "14780", _("Indian Nuthatch")
    INDIAN_PARADISE_FLYCATCHER = "13540", _("Indian Paradise Flycatcher")
    INDIAN_PEAFOWL = "35670", _("Indian Peafowl")
    INDIAN_PITTA = "09510", _("Indian Pitta")
    INDIAN_POND_HERON = "01090", _("Indian Pond Heron")
    INDIAN_ROBIN = "11600", _("Indian Robin")
    INDIAN_ROLLER = "08430", _("Indian Roller")
    INDIAN_SCOPS_OWL = "07360", _("Indian Scops Owl")
    INDIAN_SILVERBILL = "16180", _("Indian Silverbill")
    INDIAN_SPOT_BILLED_DUCK = "01880", _("Indian Spot-billed Duck")
    INDIAN_SPOTTED_CREEPER = "34761", _("Indian Spotted Creeper")
    INDIAN_VULTURE = "02500", _("Indian Vulture")
    INDIAN_WHITE_EYE = "15010", _("Indian White-eye")
    INDIAN_YELLOW_NOSED_ALBATROSS = "00152", _("Indian Yellow-nosed Albatross")
    INDIGO_BUNTING = "18920", _("Indigo Bunting")
    IRANIAN_GROUND_JAY = "15540", _("Iranian Ground Jay")
    IRAQ_BABBLER = "13770", _("Iraq Babbler")
    ISABELLINE_SHRIKE = "15141", _("Isabelline Shrike")
    ISABELLINE_WHEATEAR = "11440", _("Isabelline Wheatear")
    ITALIAN_SPARROW = "15912", _("Italian Sparrow")
    IVORY_GULL = "06040", _("Ivory Gull")
    IVORY_BILLED_WOODCREEPER = "09020", _("Ivory-billed Woodcreeper")
    IVORY_BILLED_WOODPECKER = "09000", _("Ivory-billed Woodpecker")
    IZU_THRUSH = "11910", _("Izu Thrush")
    JACK_SNIPE = "05180", _("Jack Snipe")
    JACOBIN_CUCKOO = "07150", _("Jacobin Cuckoo")
    JAMBANDU_INDIGOBIRD = "35530", _("Jambandu Indigobird")
    JANKOWSKI_S_BUNTING = "18620", _("Jankowski's Bunting")
    JAPANESE_ACCENTOR = "10830", _("Japanese Accentor")
    JAPANESE_BUSH_WARBLER = "12140", _("Japanese Bush Warbler")
    JAPANESE_CORMORANT = "00730", _("Japanese Cormorant")
    JAPANESE_GREEN_WOODPECKER = "08580", _("Japanese Green Woodpecker")
    JAPANESE_GROSBEAK = "17160", _("Japanese Grosbeak")
    JAPANESE_MURRELET = "06460", _("Japanese Murrelet")
    JAPANESE_NIGHT_HERON = "01030", _("Japanese Night Heron")
    JAPANESE_PYGMY_WOODPECKER = "08890", _("Japanese Pygmy Woodpecker")
    JAPANESE_QUAIL = "03710", _("Japanese Quail")
    JAPANESE_ROBIN = "11000", _("Japanese Robin")
    JAPANESE_SPARROWHAWK = "02682", _("Japanese Sparrowhawk")
    JAPANESE_THRUSH = "11840", _("Japanese Thrush")
    JAPANESE_WAGTAIL = "10210", _("Japanese Wagtail")
    JAPANESE_WAXWING = "10470", _("Japanese Waxwing")
    JAVAN_SHORTWING = "10980", _("Javan Shortwing")
    JOHANNA_S_SUNBIRD = "33550", _("Johanna's Sunbird")
    JOS_PLATEAU_INDIGOBIRD = "35500", _("Jos Plateau Indigobird")
    JOUANIN_S_PETREL = "00350", _("Jouanin's Petrel")
    JUNGLE_BUSH_QUAIL = "03720", _("Jungle Bush Quail")
    JUNGLE_NIGHTJAR = "07770", _("Jungle Nightjar")
    KALIJ_PHEASANT = "03870", _("Kalij Pheasant")
    KAMCHATKA_LEAF_WARBLER = "36320", _("Kamchatka Leaf Warbler")
    KELP_GULL = "20600", _("Kelp Gull")
    KEMP_S_LONGBILL = "33020", _("Kemp's Longbill")
    KENTISH_PLOVER = "04770", _("Kentish Plover")
    KENTUCKY_WARBLER = "17670", _("Kentucky Warbler")
    KERGUELEN_PETREL = "20120", _("Kerguelen Petrel")
    KERMADEC_PETREL = "00250", _("Kermadec Petrel")
    KEY_WEST_QUAIL_DOVE = "07010", _("Key West Quail-Dove")
    KILLDEER = "04740", _("Killdeer")
    KING_EIDER = "02070", _("King Eider")
    KING_PENGUIN = "27750", _("King Penguin")
    KING_RAIL = "04050", _("King Rail")
    KIRTLAND_S_WARBLER = "17410", _("Kirtland's Warbler")
    KITTLITZ_S_MURRELET = "06420", _("Kittlitz's Murrelet")
    KITTLITZ_S_PLOVER = "04760", _("Kittlitz's Plover")
    KLAAS_S_CUCKOO = "07210", _("Klaas's Cuckoo")
    KNOB_BILLED_DUCK = "34770", _("Knob-billed Duck")
    KOKLASS_PHEASANT = "03820", _("Koklass Pheasant")
    KOZLOV_S_ACCENTOR = "10910", _("Kozlov's Accentor")
    KR_PER_S_NUTHATCH = "14690", _("Krüper's Nuthatch")
    KURDISH_WHEATEAR = "11520", _("Kurdish Wheatear")
    LABRADOR_DUCK = "02100", _("Labrador Duck")
    LADDER_BACKED_WOODPECKER = "08910", _("Ladder-backed Woodpecker")
    LADY_AMHERST_S_PHEASANT = "03970", _("Lady Amherst's Pheasant")
    LAGGAR_FALCON = "03150", _("Laggar Falcon")
    LAGOPUS_LAGOPUS_SENSU_LATO = "03290", _("Lagopus lagopus sensu lato")
    LANCEOLATED_WARBLER = "12350", _("Lanceolated Warbler")
    LANIUS_COLLURIO_X_LANIUS_SENATOR = "90740", _("Lanius collurio x Lanius senator")
    LANIUS_ISABELLINUS_SENSU_LATO = "15140", _("Lanius isabellinus sensu lato")
    LANIUS_SP = "15249", _("Lanius sp.")
    LANNER_FALCON = "03140", _("Lanner Falcon")
    LAPLAND_LONGSPUR = "18470", _("Lapland Longspur")
    LAPPET_FACED_VULTURE = "02540", _("Lappet-faced Vulture")
    LARGE_HAWK_CUCKOO = "07180", _("Large Hawk-Cuckoo")
    LARGE_NILTAVA = "13220", _("Large Niltava")
    LARGE_BILLED_CROW = "15680", _("Large-billed Crow")
    LARGE_BILLED_LEAF_WARBLER = "12940", _("Large-billed Leaf Warbler")
    LARIDAE_SP = "06009", _("Laridae sp.")
    LARK_BUNTING = "18450", _("Lark Bunting")
    LARK_SPARROW = "18240", _("Lark Sparrow")
    LARUS_ARGENTATUS_SENSU_LATO = "05920", _("Larus argentatus sensu lato")
    LARUS_ARGENTATUS_X_LARUS_CACHINNANS = "90090", _("Larus argentatus x Larus cachinnans")
    LARUS_ARGENTATUS_X_LARUS_CACHINNANS_2 = "90091", _("Larus argentatus x Larus cachinnans")
    LARUS_ARGENTATUS_X_LARUS_CACHINNANS_3 = "90092", _("Larus argentatus x Larus cachinnans")
    LARUS_ARGENTATUS_X_LARUS_HYPERBOREUS = "90080", _("Larus argentatus x Larus hyperboreus")
    LARUS_ARGENTATUS_X_LARUS_HYPERBOREUS_2 = "90081", _("Larus argentatus x Larus hyperboreus")
    LARUS_ARGENTATUS_X_LARUS_HYPERBOREUS_3 = "90082", _("Larus argentatus x Larus hyperboreus")
    LARUS_ARGENTATUS_X_LARUS_MICHAHELLIS = "90330", _("Larus argentatus x Larus michahellis")
    LARUS_ARGENTATUS_X_LARUS_MICHAHELLIS_2 = "90331", _("Larus argentatus x Larus michahellis")
    LARUS_ARGENTATUS_X_LARUS_MICHAHELLIS_3 = "90332", _("Larus argentatus x Larus michahellis")
    LARUS_ARGENTATUS_CACHINNANS_MICHAHELLIS = "05929", _("Larus argentatus/cachinnans/michahellis")
    LARUS_FUSCUS_X_LARUS_ARGENTATUS = "90730", _("Larus fuscus x Larus argentatus")
    LARUS_FUSCUS_X_LARUS_CACHINNANS = "90720", _("Larus fuscus x Larus cachinnans")
    LARUS_FUSCUS_X_LARUS_MICHAHELLIS = "90320", _("Larus fuscus x Larus michahellis")
    LARUS_FUSCUS_X_LARUS_MICHAHELLIS_2 = "90321", _("Larus fuscus x Larus michahellis")
    LARUS_FUSCUS_X_LARUS_MICHAHELLIS_3 = "90322", _("Larus fuscus x Larus michahellis")
    LARUS_MARINUS_X_LARUS_ARGENTATUS = "90800", _("Larus marinus x Larus argentatus")
    LARUS_MICHAHELLIS_X_LARUS_CACHINNANS = "90500", _("Larus michahellis x Larus cachinnans")
    LARUS_MICHAHELLIS_X_LARUS_CACHINNANS_2 = "90501", _("Larus michahellis x Larus cachinnans")
    LARUS_MICHAHELLIS_X_LARUS_CACHINNANS_3 = "90502", _("Larus michahellis x Larus cachinnans")
    LARUS_VEGAE_SENSU_LATO = "36150", _("Larus vegae sensu lato")
    LATHAM_S_FRANCOLIN = "33970", _("Latham's Francolin")
    LATHAM_S_SNIPE = "05230", _("Latham's Snipe")
    LAUGHING_DOVE = "06900", _("Laughing Dove")
    LAUGHING_GULL = "05760", _("Laughing Gull")
    LAUREL_PIGEON = "06730", _("Laurel Pigeon")
    LAVENDER_WAXBILL = "31960", _("Lavender Waxbill")
    LAWRENCE_S_GOLDFINCH = "16590", _("Lawrence's Goldfinch")
    LAYSAN_ALBATROSS = "00180", _("Laysan Albatross")
    LAZULI_BUNTING = "18930", _("Lazuli Bunting")
    LECONTE_S_SPARROW = "18290", _("LeConte's Sparrow")
    LECONTE_S_THRASHER = "10750", _("LeConte's Thrasher")
    LEACH_S_STORM_PETREL = "00550", _("Leach's Storm Petrel")
    LEAF_LOVE = "34670", _("Leaf-love")
    LEAST_AUKLET = "06510", _("Least Auklet")
    LEAST_BITTERN = "00970", _("Least Bittern")
    LEAST_FLYCATCHER = "09150", _("Least Flycatcher")
    LEAST_GREBE = "00080", _("Least Grebe")
    LEAST_HONEYGUIDE = "32530", _("Least Honeyguide")
    LEAST_SANDPIPER = "05040", _("Least Sandpiper")
    LEAST_STORM_PETREL = "00530", _("Least Storm Petrel")
    LEMON_DOVE = "30490", _("Lemon Dove")
    LEMON_BELLIED_CROMBEC = "35030", _("Lemon-bellied Crombec")
    LESSER_BLACK_BACKED_GULL = "05910", _("Lesser Black-backed Gull")
    LESSER_BLUE_EARED_STARLING = "32741", _("Lesser Blue-eared Starling")
    LESSER_CRESTED_TERN = "06090", _("Lesser Crested Tern")
    LESSER_CUCKOO = "07260", _("Lesser Cuckoo")
    LESSER_FLAMINGO = "01480", _("Lesser Flamingo")
    LESSER_FRIGATEBIRD = "00940", _("Lesser Frigatebird")
    LESSER_GOLDFINCH = "16580", _("Lesser Goldfinch")
    LESSER_GREY_SHRIKE = "15190", _("Lesser Grey Shrike")
    LESSER_HONEYGUIDE = "32560", _("Lesser Honeyguide")
    LESSER_JACANA = "33270", _("Lesser Jacana")
    LESSER_KESTREL = "03030", _("Lesser Kestrel")
    LESSER_MASKED_WEAVER = "26420", _("Lesser Masked Weaver")
    LESSER_MOORHEN = "32160", _("Lesser Moorhen")
    LESSER_NIGHTHAWK = "07870", _("Lesser Nighthawk")
    LESSER_NODDY = "06290", _("Lesser Noddy")
    LESSER_SCAUP = "02050", _("Lesser Scaup")
    LESSER_SPOTTED_EAGLE = "02920", _("Lesser Spotted Eagle")
    LESSER_SPOTTED_WOODPECKER = "08870", _("Lesser Spotted Woodpecker")
    LESSER_STRIPED_SWALLOW = "32380", _("Lesser Striped Swallow")
    LESSER_SWAMP_WARBLER = "30050", _("Lesser Swamp Warbler")
    LESSER_WHITE_FRONTED_GOOSE = "01600", _("Lesser White-fronted Goose")
    LESSER_WHITETHROAT = "12740", _("Lesser Whitethroat")
    LESSER_YELLOWLEGS = "05510", _("Lesser Yellowlegs")
    LESSER_YELLOWNAPE = "08530", _("Lesser Yellownape")
    LEVAILLANT_S_CUCKOO = "26500", _("Levaillant's Cuckoo")
    LEVAILLANT_S_WOODPECKER = "08570", _("Levaillant's Woodpecker")
    LEVANT_SPARROWHAWK = "02730", _("Levant Sparrowhawk")
    LEWIS_S_WOODPECKER = "08710", _("Lewis's Woodpecker")
    LICHTENSTEIN_S_SANDGROUSE = "06570", _("Lichtenstein's Sandgrouse")
    LIDTH_S_JAY = "15410", _("Lidth's Jay")
    LIGHT_MANTLED_ALBATROSS = "20100", _("Light-mantled Albatross")
    LIGHT_VENTED_BULBUL = "10340", _("Light-vented Bulbul")
    LIMPKIN = "04320", _("Limpkin")
    LINCOLN_S_SPARROW = "18360", _("Lincoln's Sparrow")
    LITTLE_AUK = "06470", _("Little Auk")
    LITTLE_BEE_EATER = "33250", _("Little Bee-eater")
    LITTLE_BITTERN = "00980", _("Little Bittern")
    LITTLE_BLUE_HERON = "01120", _("Little Blue Heron")
    LITTLE_BUNTING = "18740", _("Little Bunting")
    LITTLE_BUSTARD = "04420", _("Little Bustard")
    LITTLE_CORMORANT = "00840", _("Little Cormorant")
    LITTLE_CRAKE = "04100", _("Little Crake")
    LITTLE_CURLEW = "05360", _("Little Curlew")
    LITTLE_EGRET = "01190", _("Little Egret")
    LITTLE_FORKTAIL = "12080", _("Little Forktail")
    LITTLE_GREBE = "00070", _("Little Grebe")
    LITTLE_GREEN_SUNBIRD = "33620", _("Little Green Sunbird")
    LITTLE_GREEN_WOODPECKER = "36470", _("Little Green Woodpecker")
    LITTLE_GREENBUL = "23400", _("Little Greenbul")
    LITTLE_GREY_FLYCATCHER = "33360", _("Little Grey Flycatcher")
    LITTLE_GREY_GREENBUL = "30250", _("Little Grey Greenbul")
    LITTLE_GREY_WOODPECKER = "31650", _("Little Grey Woodpecker")
    LITTLE_GULL = "05780", _("Little Gull")
    LITTLE_HERON = "01072", _("Little Heron")
    LITTLE_NIGHTJAR = "26810", _("Little Nightjar")
    LITTLE_OWL = "07570", _("Little Owl")
    LITTLE_RINGED_PLOVER = "04690", _("Little Ringed Plover")
    LITTLE_ROCK_THRUSH = "11610", _("Little Rock Thrush")
    LITTLE_RUSH_WARBLER = "30710", _("Little Rush Warbler")
    LITTLE_SHEARWATER = "00481", _("Little Shearwater")
    LITTLE_SPOTTED_WOODPECKER = "30900", _("Little Spotted Woodpecker")
    LITTLE_STINT = "05010", _("Little Stint")
    LITTLE_SWIFT = "08000", _("Little Swift")
    LITTLE_TERN = "06240", _("Little Tern")
    LITTLE_WEAVER = "34250", _("Little Weaver")
    LITTLE_WOODPECKER = "27670", _("Little Woodpecker")
    LIZARD_BUZZARD = "32640", _("Lizard Buzzard")
    LOCUSTELLA_HELOPSALTES_SP = "12399", _("Locustella/Helopsaltes sp.")
    LOGGERHEAD_KINGBIRD = "09470", _("Loggerhead Kingbird")
    LOGGERHEAD_SHRIKE = "15220", _("Loggerhead Shrike")
    LONCHURA_MALACCA_SENSU_LATO = "20290", _("Lonchura malacca sensu lato")
    LONCHURA_SP = "20459", _("Lonchura sp.")
    LONG_BILLED_BUSH_WARBLER = "12220", _("Long-billed Bush Warbler")
    LONG_BILLED_CURLEW = "05420", _("Long-billed Curlew")
    LONG_BILLED_DOWITCHER = "05270", _("Long-billed Dowitcher")
    LONG_BILLED_MURRELET = "06412", _("Long-billed Murrelet")
    LONG_BILLED_PIPIT = "10070", _("Long-billed Pipit")
    LONG_BILLED_PLOVER = "04720", _("Long-billed Plover")
    LONG_BILLED_THRASHER = "10700", _("Long-billed Thrasher")
    LONG_CRESTED_EAGLE = "32940", _("Long-crested Eagle")
    LONG_EARED_OWL = "07670", _("Long-eared Owl")
    LONG_LEGGED_BUZZARD = "02880", _("Long-legged Buzzard")
    LONG_LEGGED_PIPIT = "36390", _("Long-legged Pipit")
    LONG_TAILED_DUCK = "02120", _("Long-tailed Duck")
    LONG_TAILED_GLOSSY_STARLING = "32710", _("Long-tailed Glossy Starling")
    LONG_TAILED_HAWK = "35400", _("Long-tailed Hawk")
    LONG_TAILED_JAEGER = "05680", _("Long-tailed Jaeger")
    LONG_TAILED_MINIVET = "10260", _("Long-tailed Minivet")
    LONG_TAILED_NIGHTJAR = "30950", _("Long-tailed Nightjar")
    LONG_TAILED_PARADISE_WHYDAH = "35520", _("Long-tailed Paradise Whydah")
    LONG_TAILED_REED_FINCH = "26940", _("Long-tailed Reed Finch")
    LONG_TAILED_SHRIKE = "15170", _("Long-tailed Shrike")
    LONG_TAILED_THRUSH = "11690", _("Long-tailed Thrush")
    LONG_TAILED_TIT = "14370", _("Long-tailed Tit")
    LONG_TOED_LAPWING = "35410", _("Long-toed Lapwing")
    LONG_TOED_STINT = "05030", _("Long-toed Stint")
    LOPHOCEROS_FASCIATUS_SENSU_LATO = "35220", _("Lophoceros fasciatus sensu lato")
    LORD_DERBY_S_PARAKEET = "07130", _("Lord Derby's Parakeet")
    LOUISIANA_WATERTHRUSH = "17580", _("Louisiana Waterthrush")
    LOWLAND_AKALAT = "34890", _("Lowland Akalat")
    LOWLAND_SOOTY_BOUBOU = "32840", _("Lowland Sooty Boubou")
    LOXIA_SP = "16689", _("Loxia sp.")
    LUCIFER_SHEARTAIL = "08140", _("Lucifer Sheartail")
    LUCY_S_WARBLER = "17290", _("Lucy's Warbler")
    LUSCINIA_MEGARHYNCHOS_X_LUSCINIA_LUSCINIA = (
        "90290",
        _("Luscinia megarhynchos x Luscinia luscinia"),
    )
    LUSCINIA_MEGARHYNCHOS_X_LUSCINIA_LUSCINIA_2 = (
        "90291",
        _("Luscinia megarhynchos x Luscinia luscinia"),
    )
    LUSCINIA_MEGARHYNCHOS_X_LUSCINIA_LUSCINIA_3 = (
        "90292",
        _("Luscinia megarhynchos x Luscinia luscinia"),
    )
    LUSCINIA_SP = "11129", _("Luscinia sp.")
    LYRE_TAILED_HONEYGUIDE = "33150", _("Lyre-tailed Honeyguide")
    LYRURUS_TETRIX_X_TETRAO_UROGALLUS = "90070", _("Lyrurus tetrix x Tetrao urogallus")
    LYRURUS_TETRIX_X_TETRAO_UROGALLUS_2 = "90071", _("Lyrurus tetrix x Tetrao urogallus")
    LYRURUS_TETRIX_X_TETRAO_UROGALLUS_3 = "90072", _("Lyrurus tetrix x Tetrao urogallus")
    L_HDER_S_BUSHSHRIKE = "32850", _("Lühder's Bushshrike")
    MACGILLIVRAY_S_PRION = "35942", _("MacGillivray's Prion")
    MACGILLIVRAY_S_WARBLER = "17700", _("MacGillivray's Warbler")
    MACARONI_PENGUIN = "20300", _("Macaroni Penguin")
    MACKINNON_S_SHRIKE = "32900", _("Mackinnon's Shrike")
    MACRONECTES_GIGANTEUS_X_MACRONECTES_HALLI = (
        "90830",
        _("Macronectes giganteus x Macronectes halli"),
    )
    MACRONECTES_SP = "00210", _("Macronectes sp.")
    MADAGASCAR_HOOPOE = "08468", _("Madagascar Hoopoe")
    MADAGASCAR_MAGPIE_ROBIN = "27910", _("Madagascar Magpie-Robin")
    MADEIRA_FIRECREST = "13154", _("Madeira Firecrest")
    MAGHREB_MAGPIE = "15493", _("Maghreb Magpie")
    MAGHREB_OWL = "36350", _("Maghreb Owl")
    MAGNIFICENT_FRIGATEBIRD = "00930", _("Magnificent Frigatebird")
    MAGNOLIA_WARBLER = "17500", _("Magnolia Warbler")
    MAGPIE_MANNIKIN = "34950", _("Magpie Mannikin")
    MALACHITE_KINGFISHER = "30120", _("Malachite Kingfisher")
    MALAGASY_BULBUL = "10400", _("Malagasy Bulbul")
    MALAYSIAN_HAWK_CUCKOO = "07170", _("Malaysian Hawk-Cuckoo")
    MALLARD = "01860", _("Mallard")
    MANDARIN_DUCK = "01780", _("Mandarin Duck")
    MANED_DUCK = "35610", _("Maned Duck")
    MANGROVE_CUCKOO = "07290", _("Mangrove Cuckoo")
    MANGROVE_KINGFISHER = "21800", _("Mangrove Kingfisher")
    MANGROVE_RAIL = "04040", _("Mangrove Rail")
    MANGROVE_SUNBIRD = "30350", _("Mangrove Sunbird")
    MANGROVE_SWALLOW = "09840", _("Mangrove Swallow")
    MANGROVE_VIREO = "16220", _("Mangrove Vireo")
    MANGROVE_WARBLER = "17332", _("Mangrove Warbler")
    MANX_SHEARWATER = "00461", _("Manx Shearwater")
    MANY_COLORED_BUSHSHRIKE = "35120", _("Many-colored Bushshrike")
    MARABOU_STORK = "01350", _("Marabou Stork")
    MARBLED_DUCK = "01950", _("Marbled Duck")
    MARBLED_GODWIT = "05350", _("Marbled Godwit")
    MARBLED_MURRELET = "06411", _("Marbled Murrelet")
    MARKHAM_S_STORM_PETREL = "20400", _("Markham's Storm Petrel")
    MARMORA_S_WARBLER = "12611", _("Marmora's Warbler")
    MAROON_ORIOLE = "15060", _("Maroon Oriole")
    MAROON_BACKED_ACCENTOR = "10820", _("Maroon-backed Accentor")
    MAROON_FRONTED_PARROT = "07100", _("Maroon-fronted Parrot")
    MARSH_GRASSBIRD = "12400", _("Marsh Grassbird")
    MARSH_OWL = "07690", _("Marsh Owl")
    MARSH_SANDPIPER = "05470", _("Marsh Sandpiper")
    MARSH_TCHAGRA = "35090", _("Marsh Tchagra")
    MARSH_TIT = "14400", _("Marsh Tit")
    MARSH_WARBLER = "12500", _("Marsh Warbler")
    MARSH_WIDOWBIRD = "32030", _("Marsh Widowbird")
    MARSH_WREN = "10590", _("Marsh Wren")
    MARTIAL_EAGLE = "34430", _("Martial Eagle")
    MASKED_BOOBY = "00680", _("Masked Booby")
    MASKED_DUCK = "02240", _("Masked Duck")
    MASKED_GNATCATCHER = "27360", _("Masked Gnatcatcher")
    MASKED_LAUGHINGTHRUSH = "13840", _("Masked Laughingthrush")
    MASKED_SHRIKE = "15240", _("Masked Shrike")
    MASKED_TITYRA = "09050", _("Masked Tityra")
    MASKED_YELLOWTHROAT = "27061", _("Masked Yellowthroat")
    MATSUDAIRA_S_STORM_PETREL = "00610", _("Matsudaira's Storm Petrel")
    MAXWELL_S_BLACK_WEAVER = "34180", _("Maxwell's Black Weaver")
    MEADOW_BUNTING = "18610", _("Meadow Bunting")
    MEADOW_PIPIT = "10110", _("Meadow Pipit")
    MEDITERRANEAN_FLYCATCHER = "13355", _("Mediterranean Flycatcher")
    MEDITERRANEAN_GULL = "05750", _("Mediterranean Gull")
    MEDITERRANEAN_SHORT_TOED_LARK = "09703", _("Mediterranean Short-toed Lark")
    MEDIUM_EGRET = "01200", _("Medium Egret")
    MELODIOUS_WARBLER = "12600", _("Melodious Warbler")
    MENETRIES_S_WARBLER = "12660", _("Menetries's Warbler")
    MERGUS_SP = "02239", _("Mergus sp.")
    MERLIN = "03090", _("Merlin")
    MEROPS_ORIENTALIS_SENSU_LATO = "08380", _("Merops orientalis sensu lato")
    MEROPS_SUPERCILIOSUS_SENSU_LATO = "08390", _("Merops superciliosus sensu lato")
    MEXICAN_CACIQUE = "19220", _("Mexican Cacique")
    MEXICAN_CHICKADEE = "14450", _("Mexican Chickadee")
    MIDDENDORFF_S_GRASSHOPPER_WARBLER = "12340", _("Middendorff's Grasshopper Warbler")
    MIDDLE_SPOTTED_WOODPECKER = "08830", _("Middle Spotted Woodpecker")
    MILVUS_MILVUS_X_MILVUS_MIGRANS = "90550", _("Milvus milvus x Milvus migrans")
    MILVUS_SP = "02399", _("Milvus sp.")
    MIRAFRA_JAVANICA_CANTILLANS = "09520", _("Mirafra javanica cantillans")
    MISSISSIPPI_KITE = "02360", _("Mississippi Kite")
    MISTLE_THRUSH = "12020", _("Mistle Thrush")
    MITRED_PARAKEET = "35690", _("Mitred Parakeet")
    MOCKING_CLIFF_CHAT = "35161", _("Mocking Cliff Chat")
    MOLTONI_S_WARBLER = "12652", _("Moltoni's Warbler")
    MOMOTUS_MOMOTA_SENSU_LATO = "27210", _("Momotus momota sensu lato")
    MONGOLIAN_FINCH = "16750", _("Mongolian Finch")
    MONGOLIAN_GROUND_JAY = "15510", _("Mongolian Ground Jay")
    MONGOLIAN_GULL = "26560", _("Mongolian Gull")
    MONGOLIAN_LARK = "09640", _("Mongolian Lark")
    MONK_PARAKEET = "20390", _("Monk Parakeet")
    MONTAGU_S_HARRIER = "02630", _("Montagu's Harrier")
    MONTEIRO_S_STORM_PETREL = "00581", _("Monteiro's Storm Petrel")
    MONTEZUMA_QUAIL = "03460", _("Montezuma Quail")
    MOSQUE_SWALLOW = "32460", _("Mosque Swallow")
    MOTACILLA_FLAVA_X_MOTACILLA_CITREOLA = "90190", _("Motacilla flava x Motacilla citreola")
    MOTACILLA_FLAVA_X_MOTACILLA_CITREOLA_2 = "90191", _("Motacilla flava x Motacilla citreola")
    MOTACILLA_FLAVA_X_MOTACILLA_CITREOLA_3 = "90192", _("Motacilla flava x Motacilla citreola")
    MOTACILLA_SP = "10239", _("Motacilla sp.")
    MOTTLED_PETREL = "00270", _("Mottled Petrel")
    MOTTLED_SPINETAIL = "35110", _("Mottled Spinetail")
    MOTTLED_SWIFT = "35040", _("Mottled Swift")
    MOUNTAIN_BLUEBIRD = "11320", _("Mountain Bluebird")
    MOUNTAIN_BULBUL = "10380", _("Mountain Bulbul")
    MOUNTAIN_CHICKADEE = "14460", _("Mountain Chickadee")
    MOUNTAIN_CHIFFCHAFF = "13100", _("Mountain Chiffchaff")
    MOUNTAIN_HAWK_EAGLE = "03000", _("Mountain Hawk-Eagle")
    MOUNTAIN_PLOVER = "04830", _("Mountain Plover")
    MOUNTAIN_PYGMY_OWL = "07520", _("Mountain Pygmy Owl")
    MOUNTAIN_QUAIL = "03390", _("Mountain Quail")
    MOUNTAIN_ROBIN_CHAT = "31530", _("Mountain Robin-Chat")
    MOUNTAIN_SAW_WING = "34510", _("Mountain Saw-wing")
    MOUNTAIN_SOOTY_BOUBOU = "36540", _("Mountain Sooty Boubou")
    MOUNTAIN_TROGON = "08240", _("Mountain Trogon")
    MOUNTAIN_WAGTAIL = "33310", _("Mountain Wagtail")
    MOURNING_COLLARED_DOVE = "35000", _("Mourning Collared Dove")
    MOURNING_DOVE = "06950", _("Mourning Dove")
    MOURNING_WARBLER = "17690", _("Mourning Warbler")
    MOURNING_WHEATEAR = "11540", _("Mourning Wheatear")
    MOUSSIER_S_REDSTART = "11270", _("Moussier's Redstart")
    MOUSTACHED_GRASS_WARBLER = "33170", _("Moustached Grass Warbler")
    MOUSTACHED_LAUGHINGTHRUSH = "13920", _("Moustached Laughingthrush")
    MOUSTACHED_WARBLER = "12410", _("Moustached Warbler")
    MOUSTACHED_WREN = "27600", _("Moustached Wren")
    MRS_GOULD_S_SUNBIRD = "14960", _("Mrs. Gould's Sunbird")
    MUGIMAKI_FLYCATCHER = "13440", _("Mugimaki Flycatcher")
    MUSCICAPA_STRIATA_SENSU_LATO = "13350", _("Muscicapa striata sensu lato")
    MUSCICAPIDAE = "13369", _("Muscicapidae")
    MUSCOVY_DUCK = "01750", _("Muscovy Duck")
    MUTE_SWAN = "01520", _("Mute Swan")
    MYRTLE_WARBLER = "17510", _("Myrtle Warbler")
    NAKED_FACED_BARBET = "32240", _("Naked-faced Barbet")
    NAMAQUA_DOVE = "06920", _("Namaqua Dove")
    NANDAY_PARAKEET = "36040", _("Nanday Parakeet")
    NANKEEN_NIGHT_HERON = "01050", _("Nankeen Night Heron")
    NARCISSUS_FLYCATCHER = "13460", _("Narcissus Flycatcher")
    NARINA_TROGON = "30470", _("Narina Trogon")
    NARROW_BILLED_WOODCREEPER = "27160", _("Narrow-billed Woodcreeper")
    NARROW_TAILED_STARLING = "34320", _("Narrow-tailed Starling")
    NASHVILLE_WARBLER = "17260", _("Nashville Warbler")
    NAUMANN_S_THRUSH = "11961", _("Naumann's Thrush")
    NEOTROPIC_CORMORANT = "00790", _("Neotropic Cormorant")
    NEPAL_HOUSE_MARTIN = "09990", _("Nepal House Martin")
    NILE_VALLEY_SUNBIRD = "14920", _("Nile Valley Sunbird")
    NKULENGU_RAIL = "32370", _("Nkulengu Rail")
    NORDMANN_S_GREENSHANK = "05490", _("Nordmann's Greenshank")
    NORTHERN_BALD_IBIS = "01400", _("Northern Bald Ibis")
    NORTHERN_BEARDLESS_TYRANNULET = "09080", _("Northern Beardless Tyrannulet")
    NORTHERN_BLACK_FLYCATCHER = "21900", _("Northern Black Flycatcher")
    NORTHERN_BOBWHITE = "03450", _("Northern Bobwhite")
    NORTHERN_CARDINAL = "18880", _("Northern Cardinal")
    NORTHERN_CARMINE_BEE_EATER = "33240", _("Northern Carmine Bee-eater")
    NORTHERN_CROMBEC = "22900", _("Northern Crombec")
    NORTHERN_DOUBLE_COLLARED_SUNBIRD = "33590", _("Northern Double-collared Sunbird")
    NORTHERN_FLICKER = "08500", _("Northern Flicker")
    NORTHERN_FULMAR = "00220", _("Northern Fulmar")
    NORTHERN_GANNET = "00710", _("Northern Gannet")
    NORTHERN_GIANT_PETREL = "00212", _("Northern Giant Petrel")
    NORTHERN_GREY_HEADED_SPARROW = "20050", _("Northern Grey-headed Sparrow")
    NORTHERN_HAWK_OWL = "07500", _("Northern Hawk-Owl")
    NORTHERN_HOUSE_WREN = "10651", _("Northern House Wren")
    NORTHERN_JACANA = "04480", _("Northern Jacana")
    NORTHERN_LAPWING = "04930", _("Northern Lapwing")
    NORTHERN_LONG_TAILED_WOODCREEPER = "26910", _("Northern Long-tailed Woodcreeper")
    NORTHERN_MOCKINGBIRD = "10670", _("Northern Mockingbird")
    NORTHERN_NUTCRACKER = "15570", _("Northern Nutcracker")
    NORTHERN_PARULA = "17320", _("Northern Parula")
    NORTHERN_PINTAIL = "01890", _("Northern Pintail")
    NORTHERN_PUFFBACK = "31790", _("Northern Puffback")
    NORTHERN_RAVEN = "15720", _("Northern Raven")
    NORTHERN_RED_BISHOP = "20480", _("Northern Red Bishop")
    NORTHERN_ROCKHOPPER_PENGUIN = "35880", _("Northern Rockhopper Penguin")
    NORTHERN_SAW_WHET_OWL = "07710", _("Northern Saw-whet Owl")
    NORTHERN_SHOVELER = "01940", _("Northern Shoveler")
    NORTHERN_SLATY_ANTSHRIKE = "27550", _("Northern Slaty Antshrike")
    NORTHERN_TUFTED_FLYCATCHER = "09260", _("Northern Tufted Flycatcher")
    NORTHERN_WATERTHRUSH = "17570", _("Northern Waterthrush")
    NORTHERN_WHEATEAR = "11460", _("Northern Wheatear")
    NORTHERN_WHITE_FACED_OWL = "33880", _("Northern White-faced Owl")
    NORTHERN_YELLOW_WHITE_EYE = "35570", _("Northern Yellow White-eye")
    NUBIAN_BUSTARD = "33710", _("Nubian Bustard")
    NUBIAN_NIGHTJAR = "07730", _("Nubian Nightjar")
    NUMENIUS_SP = "05439", _("Numenius sp.")
    NUTTALL_S_WOODPECKER = "08920", _("Nuttall's Woodpecker")
    NUTTING_S_FLYCATCHER = "09330", _("Nutting's Flycatcher")
    OAK_TITMOUSE = "14520", _("Oak Titmouse")
    OCELLATED_THRASHER = "10730", _("Ocellated Thrasher")
    OCHRE_BELLIED_FLYCATCHER = "36220", _("Ochre-bellied Flycatcher")
    OCHRE_RUMPED_BUNTING = "18790", _("Ochre-rumped Bunting")
    OENANTHE_HISPANICA_SENSU_LATO = "11480", _("Oenanthe hispanica sensu lato")
    OENANTHE_PLESCHANKA_X_OENANTHE_HISPANICA = (
        "90820",
        _("Oenanthe pleschanka x Oenanthe hispanica"),
    )
    OENANTHE_SP = "11589", _("Oenanthe sp.")
    OKINAWA_WOODPECKER = "08600", _("Okinawa Woodpecker")
    OLIVACEOUS_FLYCATCHER = "33380", _("Olivaceous Flycatcher")
    OLIVACEOUS_WOODCREEPER = "27440", _("Olivaceous Woodcreeper")
    OLIVE_BEE_EATER = "08391", _("Olive Bee-eater")
    OLIVE_IBIS = "30680", _("Olive Ibis")
    OLIVE_LONG_TAILED_CUCKOO = "31090", _("Olive Long-tailed Cuckoo")
    OLIVE_SPARROW = "17960", _("Olive Sparrow")
    OLIVE_SUNBIRD = "25200", _("Olive Sunbird")
    OLIVE_WARBLER = "17810", _("Olive Warbler")
    OLIVE_BACKED_PIPIT = "10080", _("Olive-backed Pipit")
    OLIVE_BELLIED_SUNBIRD = "33500", _("Olive-bellied Sunbird")
    OLIVE_CAPPED_WARBLER = "17390", _("Olive-capped Warbler")
    OLIVE_GREEN_CAMAROPTERA = "30830", _("Olive-green Camaroptera")
    OLIVE_NAPED_WEAVER = "34260", _("Olive-naped Weaver")
    OLIVE_SIDED_FLYCATCHER = "09310", _("Olive-sided Flycatcher")
    OLIVE_TREE_WARBLER = "12580", _("Olive-tree Warbler")
    OMANI_OWL = "07620", _("Omani Owl")
    OMAO = "10430", _("Omao")
    ORANGE_BULLFINCH = "17070", _("Orange Bullfinch")
    ORANGE_WEAVER = "34190", _("Orange Weaver")
    ORANGE_BELLIED_LEAFBIRD = "10410", _("Orange-bellied Leafbird")
    ORANGE_BILLED_NIGHTINGALE_THRUSH = "11800", _("Orange-billed Nightingale-Thrush")
    ORANGE_BREASTED_BUNTING = "18960", _("Orange-breasted Bunting")
    ORANGE_BREASTED_BUSHSHRIKE = "33060", _("Orange-breasted Bushshrike")
    ORANGE_BREASTED_FOREST_ROBIN = "24200", _("Orange-breasted Forest Robin")
    ORANGE_BREASTED_WAXBILL = "16170", _("Orange-breasted Waxbill")
    ORANGE_CHEEKED_WAXBILL = "20430", _("Orange-cheeked Waxbill")
    ORANGE_CROWNED_WARBLER = "17250", _("Orange-crowned Warbler")
    ORANGE_HEADED_TANAGER = "27570", _("Orange-headed Tanager")
    ORANGE_TUFTED_SUNBIRD = "33490", _("Orange-tufted Sunbird")
    ORCHARD_ORIOLE = "19170", _("Orchard Oriole")
    ORIENTAL_DARTER = "00860", _("Oriental Darter")
    ORIENTAL_DOLLARBIRD = "08450", _("Oriental Dollarbird")
    ORIENTAL_GREENFINCH = "16500", _("Oriental Greenfinch")
    ORIENTAL_MAGPIE_ROBIN = "27920", _("Oriental Magpie-Robin")
    ORIENTAL_PLOVER = "04810", _("Oriental Plover")
    ORIENTAL_PRATINCOLE = "04660", _("Oriental Pratincole")
    ORIENTAL_SCOPS_OWL = "07370", _("Oriental Scops Owl")
    ORIENTAL_SKYLARK = "09750", _("Oriental Skylark")
    ORIENTAL_TURTLE_DOVE = "06890", _("Oriental Turtle Dove")
    ORINOCO_GOOSE = "27900", _("Orinoco Goose")
    ORIOLE_FINCH = "32920", _("Oriole Finch")
    ORIOLE_WARBLER = "32490", _("Oriole Warbler")
    ORTOLAN_BUNTING = "18660", _("Ortolan Bunting")
    OSPREY = "03010", _("Osprey")
    OTHER_HYBRIDS_OR_INTERMEDIATE = "24998", _("Other hybrids or intermediate")
    OVAMBO_SPARROWHAWK = "30040", _("Ovambo Sparrowhawk")
    OVENBIRD = "17560", _("Ovenbird")
    PACHYPTILA_SALVINI_SENSU_LATO = "35940", _("Pachyptila salvini sensu lato")
    PACIFIC_GOLDEN_PLOVER = "04842", _("Pacific Golden Plover")
    PACIFIC_LOON = "00033", _("Pacific Loon")
    PACIFIC_REEF_HERON = "01170", _("Pacific Reef Heron")
    PACIFIC_SWIFT = "07970", _("Pacific Swift")
    PADDYFIELD_WARBLER = "12470", _("Paddyfield Warbler")
    PAINTED_BUNTING = "18950", _("Painted Bunting")
    PAINTED_STORK = "01280", _("Painted Stork")
    PAINTED_WHITESTART = "17760", _("Painted Whitestart")
    PALE_CRAG_MARTIN = "09901", _("Pale Crag Martin")
    PALE_FLYCATCHER = "30700", _("Pale Flycatcher")
    PALE_MARTIN = "09813", _("Pale Martin")
    PALE_ROCKFINCH = "16010", _("Pale Rockfinch")
    PALE_THRUSH = "11940", _("Pale Thrush")
    PALE_BREASTED_ILLADOPSIS = "32520", _("Pale-breasted Illadopsis")
    PALE_BREASTED_SPINETAIL = "27490", _("Pale-breasted Spinetail")
    PALE_FRONTED_NIGRITA = "33770", _("Pale-fronted Nigrita")
    PALE_HEADED_BRUSHFINCH = "26100", _("Pale-headed Brushfinch")
    PALE_LEGGED_HORNERO = "27030", _("Pale-legged Hornero")
    PALE_LEGGED_LEAF_WARBLER = "12880", _("Pale-legged Leaf Warbler")
    PALESTINE_SUNBIRD = "14950", _("Palestine Sunbird")
    PALLAS_S_FISH_EAGLE = "02420", _("Pallas's Fish Eagle")
    PALLAS_S_GRASSHOPPER_WARBLER = "12330", _("Pallas's Grasshopper Warbler")
    PALLAS_S_GULL = "05730", _("Pallas's Gull")
    PALLAS_S_LEAF_WARBLER = "12980", _("Pallas's Leaf Warbler")
    PALLAS_S_REED_BUNTING = "18780", _("Pallas's Reed Bunting")
    PALLAS_S_ROSEFINCH = "16890", _("Pallas's Rosefinch")
    PALLAS_S_SANDGROUSE = "06630", _("Pallas's Sandgrouse")
    PALLID_HARRIER = "02620", _("Pallid Harrier")
    PALLID_SCOPS_OWL = "07380", _("Pallid Scops Owl")
    PALLID_SWIFT = "07960", _("Pallid Swift")
    PALM_TANAGER = "27580", _("Palm Tanager")
    PALM_WARBLER = "17520", _("Palm Warbler")
    PALM_NUT_VULTURE = "32260", _("Palm-nut Vulture")
    PARADISE_SHELDUCK = "26680", _("Paradise Shelduck")
    PARAKEET_AUKLET = "06520", _("Parakeet Auklet")
    PARASITIC_JAEGER = "05670", _("Parasitic Jaeger")
    PARIDAE_SP = "14669", _("Paridae sp.")
    PARROT_CROSSBILL = "16680", _("Parrot Crossbill")
    PASSENGER_PIGEON = "06940", _("Passenger Pigeon")
    PASSER_DOMESTICUS_X_PASSER_HISPANIOLENSIS = (
        "90210",
        _("Passer domesticus x Passer hispaniolensis"),
    )
    PASSER_DOMESTICUS_X_PASSER_HISPANIOLENSIS_2 = (
        "90211",
        _("Passer domesticus x Passer hispaniolensis"),
    )
    PASSER_DOMESTICUS_X_PASSER_HISPANIOLENSIS_3 = (
        "90212",
        _("Passer domesticus x Passer hispaniolensis"),
    )
    PASSER_DOMESTICUS_X_PASSER_MONTANUS = "90310", _("Passer domesticus x Passer montanus")
    PASSER_DOMESTICUS_X_PASSER_MONTANUS_2 = "90311", _("Passer domesticus x Passer montanus")
    PASSER_DOMESTICUS_X_PASSER_MONTANUS_3 = "90312", _("Passer domesticus x Passer montanus")
    PASSER_DOMESTICUS_HISPANIOLENSIS = "15919", _("Passer domesticus/hispaniolensis")
    PASSER_HISPANIOLENSIS_X_PASSER_MONTANUS = "90540", _("Passer hispaniolensis x Passer montanus")
    PASSER_HISPANIOLENSIS_X_PASSER_MONTANUS_2 = (
        "90541",
        _("Passer hispaniolensis x Passer montanus"),
    )
    PASSER_HISPANIOLENSIS_X_PASSER_MONTANUS_3 = (
        "90542",
        _("Passer hispaniolensis x Passer montanus"),
    )
    PASSER_SP = "16009", _("Passer sp.")
    PASSERELLA_ILIACA_SENSU_LATO = "18340", _("Passerella iliaca sensu lato")
    PAURAQUE = "07850", _("Pauraque")
    PEACEFUL_DOVE = "35800", _("Peaceful Dove")
    PEARL_SPOTTED_OWLET = "32190", _("Pearl-spotted Owlet")
    PEARLY_EYED_THRASHER = "10790", _("Pearly-eyed Thrasher")
    PECHORA_PIPIT = "10100", _("Pechora Pipit")
    PECTORAL_SANDPIPER = "05070", _("Pectoral Sandpiper")
    PECTORAL_SPARROW = "26760", _("Pectoral Sparrow")
    PEL_S_FISHING_OWL = "34840", _("Pel's Fishing Owl")
    PELAGIC_CORMORANT = "00750", _("Pelagic Cormorant")
    PELECANIDAE_SP = "00919", _("Pelecanidae sp.")
    PENNANT_WINGED_NIGHTJAR = "33000", _("Pennant-winged Nightjar")
    PERDIX_SP = "03699", _("Perdix sp.")
    PERE_DAVID_S_SNOWFINCH = "16080", _("Pere David's Snowfinch")
    PERE_DAVID_S_TIT = "14550", _("Pere David's Tit")
    PEREGRINE_FALCON = "03200", _("Peregrine Falcon")
    PERSIAN_SHEARWATER = "00484", _("Persian Shearwater")
    PETIT_S_CUCKOOSHRIKE = "30860", _("Petit's Cuckooshrike")
    PHAINOPEPLA = "10440", _("Phainopepla")
    PHALACROCORACIDAE_SP = "00849", _("Phalacrocoracidae sp.")
    PHARAOH_EAGLE_OWL = "07441", _("Pharaoh Eagle-Owl")
    PHEASANT_TAILED_JACANA = "04470", _("Pheasant-tailed Jacana")
    PHILADELPHIA_VIREO = "16310", _("Philadelphia Vireo")
    PHILBY_S_PARTRIDGE = "03600", _("Philby's Partridge")
    PHOENICOPTERUS_RUBER_SENSU_LATO = "01470", _("Phoenicopterus ruber sensu lato")
    PHOENICURUS_OCHRUROS_X_PHOENICURUS_PHOENICURUS = (
        "90110",
        _("Phoenicurus ochruros x Phoenicurus phoenicurus"),
    )
    PHOENICURUS_OCHRUROS_X_PHOENICURUS_PHOENICURUS_2 = (
        "90111",
        _("Phoenicurus ochruros x Phoenicurus phoenicurus"),
    )
    PHOENICURUS_OCHRUROS_X_PHOENICURUS_PHOENICURUS_3 = (
        "90112",
        _("Phoenicurus ochruros x Phoenicurus phoenicurus"),
    )
    PHOENICURUS_SP = "11289", _("Phoenicurus sp.")
    PHYLLOSCOPUS_BONELLI_SENSU_LATO = "13070", _("Phylloscopus bonelli sensu lato")
    PHYLLOSCOPUS_COLLYBITA_SENSU_LATO = "13110", _("Phylloscopus collybita sensu lato")
    PHYLLOSCOPUS_COLLYBITA_X_PHYLLOSCOPUS_TROCHILUS = (
        "90790",
        _("Phylloscopus collybita x Phylloscopus trochilus"),
    )
    PHYLLOSCOPUS_INORNATUS_SENSU_LATO = "13000", _("Phylloscopus inornatus sensu lato")
    PHYLLOSCOPUS_SP = "13129", _("Phylloscopus sp.")
    PIAPIAC = "34650", _("Piapiac")
    PICUI_GROUND_DOVE = "26860", _("Picui Ground Dove")
    PICUS_VIRIDIS_SENSU_LATO = "08560", _("Picus viridis sensu lato")
    PIED_AVOCET = "04560", _("Pied Avocet")
    PIED_BUSH_CHAT = "11410", _("Pied Bush Chat")
    PIED_CROW = "15700", _("Pied Crow")
    PIED_HARRIER = "02640", _("Pied Harrier")
    PIED_KINGFISHER = "08330", _("Pied Kingfisher")
    PIED_SHRIKE_BABBLER = "14100", _("Pied Shrike-babbler")
    PIED_WHEATEAR = "11470", _("Pied Wheatear")
    PIED_BILLED_GREBE = "00060", _("Pied-billed Grebe")
    PIED_WINGED_SWALLOW = "32420", _("Pied-winged Swallow")
    PIGEON_GUILLEMOT = "06390", _("Pigeon Guillemot")
    PILEATED_FLYCATCHER = "09250", _("Pileated Flycatcher")
    PILEATED_WOODPECKER = "08620", _("Pileated Woodpecker")
    PIN_TAILED_SANDGROUSE = "06620", _("Pin-tailed Sandgrouse")
    PIN_TAILED_SNIPE = "05210", _("Pin-tailed Snipe")
    PIN_TAILED_WHYDAH = "26430", _("Pin-tailed Whydah")
    PINE_BUNTING = "18560", _("Pine Bunting")
    PINE_FLYCATCHER = "09190", _("Pine Flycatcher")
    PINE_GROSBEAK = "16990", _("Pine Grosbeak")
    PINE_SISKIN = "16550", _("Pine Siskin")
    PINE_WARBLER = "17370", _("Pine Warbler")
    PINK_BACKED_PELICAN = "00900", _("Pink-backed Pelican")
    PINK_BROWED_ROSEFINCH = "16850", _("Pink-browed Rosefinch")
    PINK_FOOTED_GOOSE = "01580", _("Pink-footed Goose")
    PINK_FOOTED_PUFFBACK = "31780", _("Pink-footed Puffback")
    PINK_FOOTED_SHEARWATER = "00390", _("Pink-footed Shearwater")
    PINK_RUMPED_ROSEFINCH = "16841", _("Pink-rumped Rosefinch")
    PINTADO_PETREL = "00230", _("Pintado Petrel")
    PINYON_JAY = "15380", _("Pinyon Jay")
    PIPING_HORNBILL = "31060", _("Piping Hornbill")
    PIPING_PLOVER = "04750", _("Piping Plover")
    PLAIN_ANTVIREO = "26950", _("Plain Antvireo")
    PLAIN_CHACHALACA = "03220", _("Plain Chachalaca")
    PLAIN_GREENBUL = "23500", _("Plain Greenbul")
    PLAIN_INEZIA = "27110", _("Plain Inezia")
    PLAIN_LAUGHINGTHRUSH = "13900", _("Plain Laughingthrush")
    PLAIN_LEAF_WARBLER = "13090", _("Plain Leaf Warbler")
    PLAIN_MOUNTAIN_FINCH = "16690", _("Plain Mountain Finch")
    PLAIN_NIGHTJAR = "07720", _("Plain Nightjar")
    PLAIN_PRINIA = "12280", _("Plain Prinia")
    PLAIN_SWIFT = "07940", _("Plain Swift")
    PLAIN_BACKED_PIPIT = "30390", _("Plain-backed Pipit")
    PLAIN_BROWN_WOODCREEPER = "35630", _("Plain-brown Woodcreeper")
    PLAIN_CROWNED_SPINETAIL = "27500", _("Plain-crowned Spinetail")
    PLAIN_WINGED_ANTSHRIKE = "27560", _("Plain-winged Antshrike")
    PLAINTIVE_CUCKOO = "07220", _("Plaintive Cuckoo")
    PLUMBEOUS_ANTBIRD = "27280", _("Plumbeous Antbird")
    PLUMBEOUS_WATER_REDSTART = "11290", _("Plumbeous Water Redstart")
    PLUVIALIS_DOMINICA_FULVA = "04840", _("Pluvialis dominica/fulva")
    PODICIPEDIDAE_SP = "00129", _("Podicipedidae sp.")
    POECILE_MONTANUS_X_PERIPARUS_ATER = "90410", _("Poecile montanus x Periparus ater")
    POECILE_MONTANUS_X_POECILE_CINCTUS = "90430", _("Poecile montanus x Poecile cinctus")
    POECILE_MONTANUS_X_POECILE_CRISTATUS = "90360", _("Poecile montanus x Poecile cristatus")
    POECILE_SP = "14409", _("Poecile sp.")
    POMARINE_JAEGER = "05660", _("Pomarine Jaeger")
    PORZANA_ZAPORNIS_SP = "04169", _("Porzana / Zapornis sp.")
    PRAIRIE_FALCON = "03190", _("Prairie Falcon")
    PRAIRIE_WARBLER = "17480", _("Prairie Warbler")
    PREUSS_S_CLIFF_SWALLOW = "32440", _("Preuss's Cliff Swallow")
    PROTHONOTARY_WARBLER = "17610", _("Prothonotary Warbler")
    PROVIDENCE_PETREL = "00280", _("Providence Petrel")
    PRUNELLA_SP = "10949", _("Prunella sp.")
    PRZEVALSKI_S_FINCH = "17050", _("Przevalski's Finch")
    PRZEVALSKI_S_PARROTBILL = "13720", _("Przevalski's Parrotbill")
    PRZEVALSKI_S_PARTRIDGE = "03560", _("Przevalski's Partridge")
    PRZEVALSKI_S_REDSTART = "11190", _("Przevalski's Redstart")
    PTERODROMA_FEAE_SENSU_LATO = "00262", _("Pterodroma feae sensu lato")
    PTERODROMA_MOLLIS_SENSU_LATO = "00260", _("Pterodroma mollis sensu lato")
    PTYONOPOGNE_FULIGULA_SENSU_LATO = "09900", _("Ptyonopogne fuligula sensu lato")
    PUFFINUS_ASSIMILIS_SENSU_LATO = "00480", _("Puffinus assimilis sensu lato")
    PUFFINUS_PUFFINUS_SENSU_LATO = "00460", _("Puffinus puffinus sensu lato")
    PURPLE_FINCH = "16800", _("Purple Finch")
    PURPLE_GALLINULE = "04260", _("Purple Gallinule")
    PURPLE_HERON = "01240", _("Purple Heron")
    PURPLE_MARTIN = "09890", _("Purple Martin")
    PURPLE_ROLLER = "31450", _("Purple Roller")
    PURPLE_SANDPIPER = "05100", _("Purple Sandpiper")
    PURPLE_STARLING = "32770", _("Purple Starling")
    PURPLE_SUNBIRD = "14930", _("Purple Sunbird")
    PURPLE_BANDED_SUNBIRD = "22300", _("Purple-banded Sunbird")
    PURPLE_HEADED_STARLING = "32760", _("Purple-headed Starling")
    PURPLE_THROATED_CUCKOOSHRIKE = "30880", _("Purple-throated Cuckooshrike")
    PURPLE_THROATED_EUPHONIA = "27000", _("Purple-throated Euphonia")
    PURPLISH_BACKED_JAY = "15330", _("Purplish-backed Jay")
    PUVEL_S_ILLADOPSIS = "26480", _("Puvel's Illadopsis")
    PYGMY_CORMORANT = "00820", _("Pygmy Cormorant")
    PYGMY_CUPWING = "13590", _("Pygmy Cupwing")
    PYGMY_NUTHATCH = "14730", _("Pygmy Nuthatch")
    PYGMY_SUNBIRD = "14910", _("Pygmy Sunbird")
    PYRRHULOXIA = "18890", _("Pyrrhuloxia")
    QUAIL_PLOVER = "33870", _("Quail-plover")
    QUAILFINCH = "33860", _("Quailfinch")
    QUAILFINCH_INDIGOBIRD = "35510", _("Quailfinch Indigobird")
    RACHEL_S_MALIMBE = "33100", _("Rachel's Malimbe")
    RADDE_S_ACCENTOR = "10881", _("Radde's Accentor")
    RADDE_S_WARBLER = "13010", _("Radde's Warbler")
    RADJAH_SHELDUCK = "26650", _("Radjah Shelduck")
    RASO_LARK = "09770", _("Raso Lark")
    RAZORBILL = "06360", _("Razorbill")
    RED_AVADAVAT = "20250", _("Red Avadavat")
    RED_COLLARED_DOVE = "06860", _("Red Collared Dove")
    RED_CROSSBILL = "16660", _("Red Crossbill")
    RED_FODY = "35740", _("Red Fody")
    RED_FOX_SPARROW = "18341", _("Red Fox Sparrow")
    RED_GROUSE = "03292", _("Red Grouse")
    RED_JUNGLEFOWL = "03860", _("Red Junglefowl")
    RED_KITE = "02390", _("Red Kite")
    RED_KNOT = "04960", _("Red Knot")
    RED_PHALAROPE = "05650", _("Red Phalarope")
    RED_TANAGER = "17850", _("Red Tanager")
    RED_WARBLER = "17750", _("Red Warbler")
    RED_BACKED_SHRIKE = "15150", _("Red-backed Shrike")
    RED_BELLIED_MALIMBE = "33070", _("Red-bellied Malimbe")
    RED_BELLIED_PARADISE_FLYCATCHER = "23000", _("Red-bellied Paradise Flycatcher")
    RED_BELLIED_WOODPECKER = "08650", _("Red-bellied Woodpecker")
    RED_BILLED_BLUE_MAGPIE = "15460", _("Red-billed Blue Magpie")
    RED_BILLED_CHOUGH = "15590", _("Red-billed Chough")
    RED_BILLED_DWARF_HORNBILL = "35200", _("Red-billed Dwarf Hornbill")
    RED_BILLED_FIREFINCH = "16130", _("Red-billed Firefinch")
    RED_BILLED_HELMETSHRIKE = "34480", _("Red-billed Helmetshrike")
    RED_BILLED_LEIOTHRIX = "14070", _("Red-billed Leiothrix")
    RED_BILLED_PIGEON = "06820", _("Red-billed Pigeon")
    RED_BILLED_QUELEA = "20240", _("Red-billed Quelea")
    RED_BILLED_STARLING = "15780", _("Red-billed Starling")
    RED_BILLED_TEAL = "28000", _("Red-billed Teal")
    RED_BILLED_TROPICBIRD = "00640", _("Red-billed Tropicbird")
    RED_BREASTED_FLYCATCHER = "13431", _("Red-breasted Flycatcher")
    RED_BREASTED_GOOSE = "01690", _("Red-breasted Goose")
    RED_BREASTED_MERGANSER = "02210", _("Red-breasted Merganser")
    RED_BREASTED_NUTHATCH = "14720", _("Red-breasted Nuthatch")
    RED_BREASTED_SAPSUCKER = "08740", _("Red-breasted Sapsucker")
    RED_BREASTED_SWALLOW = "32450", _("Red-breasted Swallow")
    RED_CAPPED_CARDINAL = "27320", _("Red-capped Cardinal")
    RED_CAPPED_LARK = "09670", _("Red-capped Lark")
    RED_CAPPED_ROBIN_CHAT = "20340", _("Red-capped Robin-Chat")
    RED_CHEEKED_CORDON_BLEU = "16140", _("Red-cheeked Cordon-bleu")
    RED_CHEEKED_WATTLE_EYE = "34140", _("Red-cheeked Wattle-eye")
    RED_CHESTED_CUCKOO = "31630", _("Red-chested Cuckoo")
    RED_CHESTED_FLUFFTAIL = "34810", _("Red-chested Flufftail")
    RED_CHESTED_SWALLOW = "20080", _("Red-chested Swallow")
    RED_COCKADED_WOODPECKER = "08940", _("Red-cockaded Woodpecker")
    RED_COLLARED_WIDOWBIRD = "32000", _("Red-collared Widowbird")
    RED_CRESTED_KORHAAN = "32070", _("Red-crested Korhaan")
    RED_CRESTED_POCHARD = "01960", _("Red-crested Pochard")
    RED_CROWNED_ANT_TANAGER = "35860", _("Red-crowned Ant Tanager")
    RED_CROWNED_CRANE = "04380", _("Red-crowned Crane")
    RED_EYED_DOVE = "06850", _("Red-eyed Dove")
    RED_EYED_PUFFBACK = "21600", _("Red-eyed Puffback")
    RED_EYED_VIREO = "16330", _("Red-eyed Vireo")
    RED_FACED_CISTICOLA = "31290", _("Red-faced Cisticola")
    RED_FACED_CORMORANT = "00760", _("Red-faced Cormorant")
    RED_FACED_CRIMSONWING = "36510", _("Red-faced Crimsonwing")
    RED_FACED_WARBLER = "17740", _("Red-faced Warbler")
    RED_FLANKED_BLUETAIL = "11130", _("Red-flanked Bluetail")
    RED_FOOTED_BOOBY = "00670", _("Red-footed Booby")
    RED_FOOTED_FALCON = "03070", _("Red-footed Falcon")
    RED_FRONTED_PARROT = "34400", _("Red-fronted Parrot")
    RED_FRONTED_ROSEFINCH = "16970", _("Red-fronted Rosefinch")
    RED_FRONTED_SERIN = "16390", _("Red-fronted Serin")
    RED_HEADED_BULLFINCH = "17080", _("Red-headed Bullfinch")
    RED_HEADED_BUNTING = "18800", _("Red-headed Bunting")
    RED_HEADED_LOVEBIRD = "30090", _("Red-headed Lovebird")
    RED_HEADED_MALIMBE = "33110", _("Red-headed Malimbe")
    RED_HEADED_QUELEA = "36480", _("Red-headed Quelea")
    RED_HEADED_TANAGER = "17890", _("Red-headed Tanager")
    RED_HEADED_WEAVER = "30180", _("Red-headed Weaver")
    RED_HEADED_WOODPECKER = "08690", _("Red-headed Woodpecker")
    RED_KNOBBED_COOT = "04310", _("Red-knobbed Coot")
    RED_LEGGED_KITTIWAKE = "06030", _("Red-legged Kittiwake")
    RED_LEGGED_PARTRIDGE = "03580", _("Red-legged Partridge")
    RED_LEGGED_THRUSH = "12070", _("Red-legged Thrush")
    RED_MANTLED_ROSEFINCH = "16930", _("Red-mantled Rosefinch")
    RED_MASKED_PARAKEET = "35700", _("Red-masked Parakeet")
    RED_NAPED_SAPSUCKER = "08730", _("Red-naped Sapsucker")
    RED_NECKED_BUZZARD = "30810", _("Red-necked Buzzard")
    RED_NECKED_FALCON = "03060", _("Red-necked Falcon")
    RED_NECKED_GREBE = "00100", _("Red-necked Grebe")
    RED_NECKED_NIGHTJAR = "07790", _("Red-necked Nightjar")
    RED_NECKED_PHALAROPE = "05640", _("Red-necked Phalarope")
    RED_NECKED_STINT = "05000", _("Red-necked Stint")
    RED_PATE_CISTICOLA = "31350", _("Red-pate Cisticola")
    RED_RUMPED_TINKERBIRD = "34330", _("Red-rumped Tinkerbird")
    RED_RUMPED_WHEATEAR = "11510", _("Red-rumped Wheatear")
    RED_SHOULDERED_CUCKOOSHRIKE = "30870", _("Red-shouldered Cuckooshrike")
    RED_SHOULDERED_HAWK = "02810", _("Red-shouldered Hawk")
    RED_TAILED_ANT_THRUSH = "33700", _("Red-tailed Ant Thrush")
    RED_TAILED_BRISTLEBILL = "30660", _("Red-tailed Bristlebill")
    RED_TAILED_GREENBUL = "24000", _("Red-tailed Greenbul")
    RED_TAILED_HAWK = "02860", _("Red-tailed Hawk")
    RED_TAILED_MINLA = "14150", _("Red-tailed Minla")
    RED_TAILED_SHRIKE = "15152", _("Red-tailed Shrike")
    RED_TAILED_TROPICBIRD = "00650", _("Red-tailed Tropicbird")
    RED_TAILED_WHEATEAR = "11521", _("Red-tailed Wheatear")
    RED_THIGHED_SPARROWHAWK = "30020", _("Red-thighed Sparrowhawk")
    RED_THROATED_BEE_EATER = "33190", _("Red-throated Bee-eater")
    RED_THROATED_LOON = "00020", _("Red-throated Loon")
    RED_THROATED_PIPIT = "10120", _("Red-throated Pipit")
    RED_THROATED_THRUSH = "11971", _("Red-throated Thrush")
    RED_THROATED_WRYNECK = "32620", _("Red-throated Wryneck")
    RED_VENTED_BULBUL = "36060", _("Red-vented Bulbul")
    RED_VENTED_MALIMBE = "33120", _("Red-vented Malimbe")
    RED_WATTLED_LAPWING = "04900", _("Red-wattled Lapwing")
    RED_WINGED_BLACKBIRD = "19090", _("Red-winged Blackbird")
    RED_WINGED_GREY_WARBLER = "31770", _("Red-winged Grey Warbler")
    RED_WINGED_LAUGHINGTHRUSH = "14050", _("Red-winged Laughingthrush")
    RED_WINGED_PRINIA = "32340", _("Red-winged Prinia")
    RED_WINGED_PYTILIA = "34700", _("Red-winged Pytilia")
    RED_WINGED_STARLING = "33810", _("Red-winged Starling")
    REDDISH_EGRET = "01140", _("Reddish Egret")
    REDHEAD = "01990", _("Redhead")
    REDPOLL = "16635", _("Redpoll")
    REDWING = "12010", _("Redwing")
    REED_CORMORANT = "00830", _("Reed Cormorant")
    REED_PARROTBILL = "13760", _("Reed Parrotbill")
    REEVES_S_PHEASANT = "03930", _("Reeves's Pheasant")
    REGULUS_REGULUS_X_REGULUS_IGNICAPILLA = "90860", _("Regulus regulus x Regulus ignicapilla")
    REGULUS_SP = "13169", _("Regulus sp.")
    REICHENBACH_S_SUNBIRD = "33600", _("Reichenbach's Sunbird")
    RELICT_GULL = "05740", _("Relict Gull")
    RHINOCEROS_AUKLET = "06530", _("Rhinoceros Auklet")
    RICHARD_S_PIPIT = "10020", _("Richard's Pipit")
    RING_OUZEL = "11860", _("Ring Ouzel")
    RING_DESTROYED_OR_LOST = "99999", _("Ring destroyed or lost")
    RING_BILLED_GULL = "05890", _("Ring-billed Gull")
    RING_NECKED_DUCK = "02000", _("Ring-necked Duck")
    RINGED_KINGFISHER = "08350", _("Ringed Kingfisher")
    RINGED_TEAL = "25700", _("Ringed Teal")
    RIVER_PRINIA = "34460", _("River Prinia")
    RIVER_WARBLER = "12370", _("River Warbler")
    RIVOLI_S_HUMMINGBIRD = "08120", _("Rivoli's Hummingbird")
    ROADSIDE_HAWK = "26780", _("Roadside Hawk")
    ROBIN_ACCENTOR = "10920", _("Robin Accentor")
    ROCK_BUNTING = "18600", _("Rock Bunting")
    ROCK_DOVE = "06650", _("Rock Dove")
    ROCK_FIREFINCH = "32700", _("Rock Firefinch")
    ROCK_PARTRIDGE = "03570", _("Rock Partridge")
    ROCK_PRATINCOLE = "32180", _("Rock Pratincole")
    ROCK_PTARMIGAN = "03300", _("Rock Ptarmigan")
    ROCK_SANDPIPER = "05110", _("Rock Sandpiper")
    ROCK_SPARROW = "16040", _("Rock Sparrow")
    ROCK_WREN = "10560", _("Rock Wren")
    ROCK_LOVING_CISTICOLA = "31281", _("Rock-loving Cisticola")
    ROOK = "15630", _("Rook")
    ROSE_BREASTED_GROSBEAK = "18870", _("Rose-breasted Grosbeak")
    ROSE_RINGED_PARAKEET = "07120", _("Rose-ringed Parakeet")
    ROSE_THROATED_BECARD = "09040", _("Rose-throated Becard")
    ROSEATE_SPOONBILL = "01460", _("Roseate Spoonbill")
    ROSEATE_TERN = "06140", _("Roseate Tern")
    ROSS_S_GOOSE = "01640", _("Ross's Goose")
    ROSS_S_GULL = "06010", _("Ross's Gull")
    ROSY_BEE_EATER = "33220", _("Rosy Bee-eater")
    ROSY_MINIVET = "10280", _("Rosy Minivet")
    ROSY_PIPIT = "10130", _("Rosy Pipit")
    ROSY_STARLING = "15840", _("Rosy Starling")
    ROSY_PATCHED_BUSHSHRIKE = "15100", _("Rosy-patched Bushshrike")
    ROUGH_LEGGED_BUZZARD = "02900", _("Rough-legged Buzzard")
    ROYAL_TERN = "06070", _("Royal Tern")
    RUBY_CROWNED_KINGLET = "13130", _("Ruby-crowned Kinglet")
    RUBY_THROATED_HUMMINGBIRD = "08150", _("Ruby-throated Hummingbird")
    RUDDY_DUCK = "02250", _("Ruddy Duck")
    RUDDY_KINGFISHER = "08260", _("Ruddy Kingfisher")
    RUDDY_QUAIL_DOVE = "07020", _("Ruddy Quail-Dove")
    RUDDY_SHELDUCK = "01710", _("Ruddy Shelduck")
    RUDDY_TURNSTONE = "05610", _("Ruddy Turnstone")
    RUDDY_BREASTED_CRAKE = "04140", _("Ruddy-breasted Crake")
    RUDDY_HEADED_GOOSE = "35850", _("Ruddy-headed Goose")
    RUFF = "05170", _("Ruff")
    RUFFED_GROUSE = "03280", _("Ruffed Grouse")
    RUFOUS_CISTICOLA = "31360", _("Rufous Cisticola")
    RUFOUS_HORNERO = "27040", _("Rufous Hornero")
    RUFOUS_HUMMINGBIRD = "08220", _("Rufous Hummingbird")
    RUFOUS_SIBIA = "14250", _("Rufous Sibia")
    RUFOUS_BACKED_THRUSH = "12040", _("Rufous-backed Thrush")
    RUFOUS_BELLIED_HERON = "30560", _("Rufous-bellied Heron")
    RUFOUS_BELLIED_NILTAVA = "13230", _("Rufous-bellied Niltava")
    RUFOUS_BELLIED_WOODPECKER = "08850", _("Rufous-bellied Woodpecker")
    RUFOUS_BREASTED_ACCENTOR = "10850", _("Rufous-breasted Accentor")
    RUFOUS_BREASTED_BUSH_ROBIN = "11160", _("Rufous-breasted Bush Robin")
    RUFOUS_BREASTED_WREN = "36240", _("Rufous-breasted Wren")
    RUFOUS_CAPPED_BABBLER = "13610", _("Rufous-capped Babbler")
    RUFOUS_CAPPED_BRUSHFINCH = "17940", _("Rufous-capped Brushfinch")
    RUFOUS_CAPPED_LARK = "09691", _("Rufous-capped Lark")
    RUFOUS_CAPPED_WARBLER = "17800", _("Rufous-capped Warbler")
    RUFOUS_CROWNED_EREMOMELA = "31900", _("Rufous-crowned Eremomela")
    RUFOUS_CROWNED_SPARROW = "18140", _("Rufous-crowned Sparrow")
    RUFOUS_FACED_WARBLER = "12790", _("Rufous-faced Warbler")
    RUFOUS_FRONTED_BUSHTIT = "14330", _("Rufous-fronted Bushtit")
    RUFOUS_GORGETED_FLYCATCHER = "13420", _("Rufous-gorgeted Flycatcher")
    RUFOUS_HEADED_ROBIN = "11080", _("Rufous-headed Robin")
    RUFOUS_NAPED_LARK = "33280", _("Rufous-naped Lark")
    RUFOUS_NAPED_TIT = "14580", _("Rufous-naped Tit")
    RUFOUS_NECKED_SNOWFINCH = "16070", _("Rufous-necked Snowfinch")
    RUFOUS_RUMPED_LARK = "34110", _("Rufous-rumped Lark")
    RUFOUS_SIDED_BROADBILL = "34910", _("Rufous-sided Broadbill")
    RUFOUS_SIDED_CRAKE = "27140", _("Rufous-sided Crake")
    RUFOUS_TAILED_BABBLER = "13620", _("Rufous-tailed Babbler")
    RUFOUS_TAILED_HUMMINGBIRD = "08090", _("Rufous-tailed Hummingbird")
    RUFOUS_TAILED_JACAMAR = "27050", _("Rufous-tailed Jacamar")
    RUFOUS_TAILED_LARK = "09560", _("Rufous-tailed Lark")
    RUFOUS_TAILED_PALM_THRUSH = "36420", _("Rufous-tailed Palm Thrush")
    RUFOUS_TAILED_ROBIN = "11020", _("Rufous-tailed Robin")
    RUFOUS_TAILED_SCRUB_ROBIN = "10950", _("Rufous-tailed Scrub Robin")
    RUFOUS_THROATED_PARTRIDGE = "03740", _("Rufous-throated Partridge")
    RUFOUS_VENTED_PARADISE_FLYCATCHER = "35140", _("Rufous-vented Paradise Flycatcher")
    RUFOUS_VENTED_TIT = "14590", _("Rufous-vented Tit")
    RUFOUS_VENTED_YUHINA = "14290", _("Rufous-vented Yuhina")
    RUFOUS_WINGED_CISTICOLA = "31310", _("Rufous-winged Cisticola")
    RUFOUS_WINGED_FULVETTA = "14180", _("Rufous-winged Fulvetta")
    RUFOUS_WINGED_ILLADOPSIS = "24900", _("Rufous-winged Illadopsis")
    RUFOUS_WINGED_SPARROW = "18130", _("Rufous-winged Sparrow")
    RUSSET_NIGHTINGALE_THRUSH = "11810", _("Russet Nightingale-Thrush")
    RUSSET_SPARROW = "15940", _("Russet Sparrow")
    RUSTIC_BUNTING = "18730", _("Rustic Bunting")
    RUSTY_BLACKBIRD = "19010", _("Rusty Blackbird")
    RUSTY_SPARROW = "18150", _("Rusty Sparrow")
    RUSTY_BACKED_ANTWREN = "27020", _("Rusty-backed Antwren")
    RUSTY_CHEEKED_SCIMITAR_BABBLER = "13560", _("Rusty-cheeked Scimitar Babbler")
    RUSTY_COLLARED_SEEDEATER = "27460", _("Rusty-collared Seedeater")
    RUSTY_CROWNED_GROUND_SPARROW = "18010", _("Rusty-crowned Ground Sparrow")
    RUSTY_FLANKED_TREECREEPER = "14850", _("Rusty-flanked Treecreeper")
    RUSTY_FRONTED_TODY_FLYCATCHER = "27620", _("Rusty-fronted Tody-Flycatcher")
    RUSTY_MARGINED_FLYCATCHER = "27260", _("Rusty-margined Flycatcher")
    RUSTY_TAILED_FLYCATCHER = "13320", _("Rusty-tailed Flycatcher")
    RYUKYU_MINIVET = "10300", _("Ryukyu Minivet")
    RYUKYU_ROBIN = "11010", _("Ryukyu Robin")
    RYUKYU_WOOD_PIGEON = "06780", _("Ryukyu Wood Pigeon")
    R_PPELL_S_VULTURE = "02530", _("Rüppell's Vulture")
    R_PPELL_S_WARBLER = "12690", _("Rüppell's Warbler")
    R_PPELL_S_WEAVER = "16120", _("Rüppell's Weaver")
    SABINE_S_GULL = "05790", _("Sabine's Gull")
    SABINE_S_PUFFBACK = "31800", _("Sabine's Puffback")
    SABINE_S_SPINETAIL = "34710", _("Sabine's Spinetail")
    SADDLE_BILLED_STORK = "31890", _("Saddle-billed Stork")
    SAFFRON_FINCH = "36250", _("Saffron Finch")
    SAGE_GROUSE = "03380", _("Sage Grouse")
    SAGE_THRASHER = "10780", _("Sage Thrasher")
    SAHEL_BUSH_SPARROW = "16030", _("Sahel Bush Sparrow")
    SAKER_FALCON = "03160", _("Saker Falcon")
    SALPORNIS_SPILONOTA_SENSU_LATO = "34760", _("Salpornis spilonota sensu lato")
    SALTMARSH_SPARROW = "18300", _("Saltmarsh Sparrow")
    SALVIN_S_PRION = "35941", _("Salvin's Prion")
    SAN_BLAS_JAY = "15320", _("San Blas Jay")
    SAND_LARK = "09710", _("Sand Lark")
    SAND_MARTIN = "09810", _("Sand Martin")
    SAND_PARTRIDGE = "03630", _("Sand Partridge")
    SANDERLING = "04970", _("Sanderling")
    SANDHILL_CRANE = "04360", _("Sandhill Crane")
    SANDWICH_TERN = "06110", _("Sandwich Tern")
    SAPPHIRE_FLYCATCHER = "13370", _("Sapphire Flycatcher")
    SARDINIAN_WARBLER = "12670", _("Sardinian Warbler")
    SARGASSO_SHEARWATER = "00490", _("Sargasso Shearwater")
    SATYR_TRAGOPAN = "03790", _("Satyr Tragopan")
    SAUNDERS_S_GULL = "05800", _("Saunders's Gull")
    SAUNDERS_S_TERN = "06250", _("Saunders's Tern")
    SAVANNAH_SPARROW = "18260", _("Savannah Sparrow")
    SAVI_S_WARBLER = "12380", _("Savi's Warbler")
    SAXAUL_SPARROW = "15900", _("Saxaul Sparrow")
    SAXICOLA_MAURUS_X_SAXICOLA_RUBETRA = "90420", _("Saxicola maurus x Saxicola rubetra")
    SAXICOLA_SP = "11429", _("Saxicola sp.")
    SAXICOLA_TORQUATUS_SENSU_LATO = "11390", _("Saxicola torquatus sensu lato")
    SAY_S_PHOEBE = "09110", _("Say's Phoebe")
    SAYACA_TANAGER = "27590", _("Sayaca Tanager")
    SCALED_DOVE = "06990", _("Scaled Dove")
    SCALED_QUAIL = "03400", _("Scaled Quail")
    SCALY_LAUGHINGTHRUSH = "14000", _("Scaly Laughingthrush")
    SCALY_SPURFOWL = "34610", _("Scaly Spurfowl")
    SCALY_BELLIED_WOODPECKER = "08590", _("Scaly-bellied Woodpecker")
    SCALY_BREASTED_CUPWING = "13580", _("Scaly-breasted Cupwing")
    SCALY_BREASTED_MUNIA = "20260", _("Scaly-breasted Munia")
    SCALY_BREASTED_THRASHER = "35640", _("Scaly-breasted Thrasher")
    SCALY_NAPED_PIGEON = "06800", _("Scaly-naped Pigeon")
    SCALY_SIDED_MERGANSER = "02220", _("Scaly-sided Merganser")
    SCARLET_FINCH = "17020", _("Scarlet Finch")
    SCARLET_FLYCATCHER = "09120", _("Scarlet Flycatcher")
    SCARLET_IBIS = "01390", _("Scarlet Ibis")
    SCARLET_TANAGER = "17880", _("Scarlet Tanager")
    SCARLET_CHESTED_SUNBIRD = "33630", _("Scarlet-chested Sunbird")
    SCISSOR_TAILED_FLYCATCHER = "09500", _("Scissor-tailed Flycatcher")
    SCISSOR_TAILED_KITE = "31150", _("Scissor-tailed Kite")
    SCISSOR_TAILED_NIGHTJAR = "27090", _("Scissor-tailed Nightjar")
    SCLATER_S_MONAL = "03840", _("Sclater's Monal")
    SCOPOLI_S_SHEARWATER = "00363", _("Scopoli's Shearwater")
    SCOTT_S_ORIOLE = "19120", _("Scott's Oriole")
    SCOTTISH_CROSSBILL = "16670", _("Scottish Crossbill")
    SCRUB_EUPHONIA = "17910", _("Scrub Euphonia")
    SEASIDE_SPARROW = "18310", _("Seaside Sparrow")
    SECRETARYBIRD = "34750", _("Secretarybird")
    SEDGE_WARBLER = "12430", _("Sedge Warbler")
    SEDGE_WREN = "10582", _("Sedge Wren")
    SEE_SEE_PARTRIDGE = "03620", _("See-see Partridge")
    SEMICOLLARED_FLYCATCHER = "13470", _("Semicollared Flycatcher")
    SEMIPALMATED_PLOVER = "04710", _("Semipalmated Plover")
    SEMIPALMATED_SANDPIPER = "04980", _("Semipalmated Sandpiper")
    SENEGAL_BATIS = "21100", _("Senegal Batis")
    SENEGAL_COUCAL = "07340", _("Senegal Coucal")
    SENEGAL_EREMOMELA = "31930", _("Senegal Eremomela")
    SENEGAL_LAPWING = "35420", _("Senegal Lapwing")
    SENEGAL_PARROT = "34420", _("Senegal Parrot")
    SENEGAL_THICK_KNEE = "04600", _("Senegal Thick-knee")
    SENNAR_PENDULINE_TIT = "30330", _("Sennar Penduline Tit")
    SEPIA_CAPPED_FLYCATCHER = "27170", _("Sepia-capped Flycatcher")
    SETOPHAGA_PETECHIA_SENSU_LATO = "17330", _("Setophaga petechia sensu lato")
    SEYCHELLES_BLUE_PIGEON = "35720", _("Seychelles Blue Pigeon")
    SEYCHELLES_FODY = "35750", _("Seychelles Fody")
    SEYCHELLES_MAGPIE_ROBIN = "27930", _("Seychelles Magpie-Robin")
    SEYCHELLES_SCOPS_OWL = "27830", _("Seychelles Scops Owl")
    SEYCHELLES_SUNBIRD = "35730", _("Seychelles Sunbird")
    SEYCHELLES_WARBLER = "35930", _("Seychelles Warbler")
    SEYCHELLES_WHITE_EYE = "35760", _("Seychelles White-eye")
    SHARP_SHINNED_HAWK = "02700", _("Sharp-shinned Hawk")
    SHARP_TAILED_GRASS_TYRANT = "26900", _("Sharp-tailed Grass Tyrant")
    SHARP_TAILED_GROUSE = "03370", _("Sharp-tailed Grouse")
    SHARP_TAILED_SANDPIPER = "05080", _("Sharp-tailed Sandpiper")
    SHARPE_S_APALIS = "36140", _("Sharpe's Apalis")
    SHELLEY_S_OLIVEBACK = "33730", _("Shelley's Oliveback")
    SHIKRA = "02720", _("Shikra")
    SHINING_DRONGO = "31740", _("Shining Drongo")
    SHINING_BLUE_KINGFISHER = "30140", _("Shining-blue Kingfisher")
    SHORT_BILLED_DOWITCHER = "05260", _("Short-billed Dowitcher")
    SHORT_CRESTED_FLYCATCHER = "27230", _("Short-crested Flycatcher")
    SHORT_EARED_OWL = "07680", _("Short-eared Owl")
    SHORT_TAILED_ALBATROSS = "00190", _("Short-tailed Albatross")
    SHORT_TAILED_HAWK = "02830", _("Short-tailed Hawk")
    SHORT_TAILED_SHEARWATER = "00440", _("Short-tailed Shearwater")
    SHORT_TOED_SNAKE_EAGLE = "02560", _("Short-toed Snake Eagle")
    SHORT_TOED_TREECREEPER = "14870", _("Short-toed Treecreeper")
    SHORT_WINGED_CISTICOLA = "31240", _("Short-winged Cisticola")
    SHY_ALBATROSS = "00160", _("Shy Albatross")
    SIBERIAN_ACCENTOR = "10860", _("Siberian Accentor")
    SIBERIAN_BLUE_ROBIN = "11120", _("Siberian Blue Robin")
    SIBERIAN_CRANE = "04400", _("Siberian Crane")
    SIBERIAN_GROUSE = "03230", _("Siberian Grouse")
    SIBERIAN_JAY = "15430", _("Siberian Jay")
    SIBERIAN_LONG_TAILED_ROSEFINCH = "17040", _("Siberian Long-tailed Rosefinch")
    SIBERIAN_PIPIT = "10146", _("Siberian Pipit")
    SIBERIAN_RUBYTHROAT = "11050", _("Siberian Rubythroat")
    SIBERIAN_SAND_PLOVER = "04780", _("Siberian Sand Plover")
    SIBERIAN_STONECHAT = "11394", _("Siberian Stonechat")
    SIBERIAN_THRUSH = "11710", _("Siberian Thrush")
    SICHUAN_JAY = "15440", _("Sichuan Jay")
    SICHUAN_PARTRIDGE = "03750", _("Sichuan Partridge")
    SIERRA_LEONE_PRINIA = "36090", _("Sierra Leone Prinia")
    SIERRA_MADRE_SPARROW = "18320", _("Sierra Madre Sparrow")
    SIKKIM_TREECREEPER = "14830", _("Sikkim Treecreeper")
    SILVER_TEAL = "35830", _("Silver Teal")
    SILVER_BEAKED_TANAGER = "27380", _("Silver-beaked Tanager")
    SILVERED_ANTBIRD = "36260", _("Silvered Antbird")
    SIMPLE_GREENBUL = "31160", _("Simple Greenbul")
    SINAI_ROSEFINCH = "16880", _("Sinai Rosefinch")
    SINALOA_WREN = "10640", _("Sinaloa Wren")
    SIND_SPARROW = "15930", _("Sind Sparrow")
    SIND_WOODPECKER = "08790", _("Sind Woodpecker")
    SINGING_BUSH_LARK = "09521", _("Singing Bush Lark")
    SINGING_CISTICOLA = "31250", _("Singing Cisticola")
    SJ_STEDT_S_BARRED_OWLET = "32200", _("Sjöstedt's Barred Owlet")
    SJ_STEDT_S_GREENBUL = "30580", _("Sjöstedt's Greenbul")
    SLATE_COLORED_HAWK = "27190", _("Slate-colored Hawk")
    SLATE_THROATED_WHITESTART = "17770", _("Slate-throated Whitestart")
    SLATY_BUNTING = "18510", _("Slaty Bunting")
    SLATY_BACKED_FLYCATCHER = "13400", _("Slaty-backed Flycatcher")
    SLATY_BACKED_FORKTAIL = "12090", _("Slaty-backed Forktail")
    SLATY_BACKED_GULL = "05950", _("Slaty-backed Gull")
    SLATY_BLUE_FLYCATCHER = "13380", _("Slaty-blue Flycatcher")
    SLATY_HEADED_PARAKEET = "07140", _("Slaty-headed Parakeet")
    SLATY_LEGGED_CRAKE = "04030", _("Slaty-legged Crake")
    SLENDER_BILLED_CURLEW = "05400", _("Slender-billed Curlew")
    SLENDER_BILLED_GRACKLE = "19030", _("Slender-billed Grackle")
    SLENDER_BILLED_GREENBUL = "30240", _("Slender-billed Greenbul")
    SLENDER_BILLED_GULL = "05850", _("Slender-billed Gull")
    SLENDER_BILLED_PRION = "26700", _("Slender-billed Prion")
    SLENDER_BILLED_WEAVER = "34280", _("Slender-billed Weaver")
    SLENDER_BILLED_XENOPS = "27680", _("Slender-billed Xenops")
    SMALL_MINIVET = "10270", _("Small Minivet")
    SMALL_PRATINCOLE = "04680", _("Small Pratincole")
    SMALL_BILLED_ELAENIA = "26970", _("Small-billed Elaenia")
    SMALL_BILLED_TINAMOU = "26890", _("Small-billed Tinamou")
    SMEW = "02200", _("Smew")
    SMITH_S_LONGSPUR = "18490", _("Smith's Longspur")
    SMOKY_WARBLER = "13040", _("Smoky Warbler")
    SMOOTH_BILLED_ANI = "07310", _("Smooth-billed Ani")
    SNAIL_KITE = "02370", _("Snail Kite")
    SNOW_BUNTING = "18500", _("Snow Bunting")
    SNOW_GOOSE = "01630", _("Snow Goose")
    SNOW_PARTRIDGE = "03470", _("Snow Partridge")
    SNOW_PETREL = "20060", _("Snow Petrel")
    SNOW_PIGEON = "06670", _("Snow Pigeon")
    SNOWY_ALBATROSS = "00201", _("Snowy Albatross")
    SNOWY_EGRET = "01150", _("Snowy Egret")
    SNOWY_OWL = "07490", _("Snowy Owl")
    SNOWY_SHEATHBILL = "20070", _("Snowy Sheathbill")
    SNOWY_BROWED_FLYCATCHER = "13410", _("Snowy-browed Flycatcher")
    SNOWY_CHEEKED_LAUGHINGTHRUSH = "13910", _("Snowy-cheeked Laughingthrush")
    SNOWY_CROWNED_ROBIN_CHAT = "21400", _("Snowy-crowned Robin-Chat")
    SNOWY_CROWNED_TERN = "06190", _("Snowy-crowned Tern")
    SOCIABLE_LAPWING = "04910", _("Sociable Lapwing")
    SOCIAL_FLYCATCHER = "09390", _("Social Flycatcher")
    SOCOTRA_CORMORANT = "00810", _("Socotra Cormorant")
    SOCOTRA_GOLDEN_WINGED_GROSBEAK = "16470", _("Socotra Golden-winged Grosbeak")
    SOFT_PLUMAGED_PETREL = "00261", _("Soft-plumaged Petrel")
    SOLITARY_SANDPIPER = "05520", _("Solitary Sandpiper")
    SOLITARY_SNIPE = "05240", _("Solitary Snipe")
    SOMATERIA_SP = "02089", _("Somateria sp.")
    SOMBRE_GREENBUL = "21000", _("Sombre Greenbul")
    SOMBRE_TIT = "14410", _("Sombre Tit")
    SONG_SPARROW = "18350", _("Song Sparrow")
    SONG_THRUSH = "12000", _("Song Thrush")
    SOOTY_ALBATROSS = "35910", _("Sooty Albatross")
    SOOTY_BUSHTIT = "14320", _("Sooty Bushtit")
    SOOTY_CHAT = "33450", _("Sooty Chat")
    SOOTY_FALCON = "03120", _("Sooty Falcon")
    SOOTY_FLYCATCHER = "33370", _("Sooty Flycatcher")
    SOOTY_GULL = "05710", _("Sooty Gull")
    SOOTY_SHEARWATER = "00430", _("Sooty Shearwater")
    SOOTY_TERN = "06230", _("Sooty Tern")
    SORA = "04090", _("Sora")
    SOUTH_AFRICAN_SHELDUCK = "26660", _("South African Shelduck")
    SOUTH_AMERICAN_TERN = "20350", _("South American Tern")
    SOUTH_GEORGIA_DIVING_PETREL = "20180", _("South Georgia Diving Petrel")
    SOUTH_GEORGIA_PIPIT = "27780", _("South Georgia Pipit")
    SOUTH_GEORGIA_SHAG = "20193", _("South Georgia Shag")
    SOUTH_POLAR_SKUA = "05700", _("South Polar Skua")
    SOUTHERN_BEARDLESS_TYRANNULET = "26800", _("Southern Beardless Tyrannulet")
    SOUTHERN_CARMINE_BEE_EATER = "36340", _("Southern Carmine Bee-eater")
    SOUTHERN_CHESTNUT_TAILED_ANTBIRD = "27270", _("Southern Chestnut-tailed Antbird")
    SOUTHERN_FISCAL = "32870", _("Southern Fiscal")
    SOUTHERN_FULMAR = "20130", _("Southern Fulmar")
    SOUTHERN_GIANT_PETREL = "00211", _("Southern Giant Petrel")
    SOUTHERN_RED_BISHOP = "20470", _("Southern Red Bishop")
    SOUTHERN_RED_FRONTED_TINKERBIRD = "34370", _("Southern Red-fronted Tinkerbird")
    SOUTHERN_ROUGH_WINGED_SWALLOW = "09820", _("Southern Rough-winged Swallow")
    SPANISH_IMPERIAL_EAGLE = "02952", _("Spanish Imperial Eagle")
    SPANISH_SPARROW = "15920", _("Spanish Sparrow")
    SPECIES_NOT_ACCEPTED = "24995", _("Species not accepted")
    SPECKLE_BREASTED_WOODPECKER = "31710", _("Speckle-breasted Woodpecker")
    SPECKLE_FRONTED_WEAVER = "34980", _("Speckle-fronted Weaver")
    SPECKLED_MOUSEBIRD = "31390", _("Speckled Mousebird")
    SPECKLED_PICULET = "08490", _("Speckled Piculet")
    SPECKLED_PIGEON = "31420", _("Speckled Pigeon")
    SPECKLED_REED_WARBLER = "12440", _("Speckled Reed Warbler")
    SPECKLED_SPINETAIL = "26880", _("Speckled Spinetail")
    SPECKLED_TINKERBIRD = "34380", _("Speckled Tinkerbird")
    SPECKLED_WOOD_PIGEON = "06740", _("Speckled Wood Pigeon")
    SPECTACLED_CORMORANT = "00740", _("Spectacled Cormorant")
    SPECTACLED_EIDER = "02080", _("Spectacled Eider")
    SPECTACLED_FINCH = "16480", _("Spectacled Finch")
    SPECTACLED_FULVETTA = "14210", _("Spectacled Fulvetta")
    SPECTACLED_GUILLEMOT = "06400", _("Spectacled Guillemot")
    SPECTACLED_PARROTBILL = "13690", _("Spectacled Parrotbill")
    SPECTACLED_TERN = "06210", _("Spectacled Tern")
    SPECTACLED_WARBLER = "12640", _("Spectacled Warbler")
    SPECTACLED_WEAVER = "34270", _("Spectacled Weaver")
    SPINUS_SPINUS_HYBRID = "90160", _("Spinus spinus hybrid")
    SPLENDID_STARLING = "32780", _("Splendid Starling")
    SPLENDID_SUNBIRD = "33510", _("Splendid Sunbird")
    SPOON_BILLED_SANDPIPER = "05130", _("Spoon-billed Sandpiper")
    SPOROPHILA_TORQUEOLA_SENSU_LATO = "18040", _("Sporophila torqueola sensu lato")
    SPOT_BREASTED_IBIS = "30690", _("Spot-breasted Ibis")
    SPOT_BREASTED_ORIOLE = "19210", _("Spot-breasted Oriole")
    SPOT_BREASTED_WREN = "10620", _("Spot-breasted Wren")
    SPOT_WINGED_GROSBEAK = "17130", _("Spot-winged Grosbeak")
    SPOT_WINGED_ROSEFINCH = "16910", _("Spot-winged Rosefinch")
    SPOTLESS_STARLING = "15830", _("Spotless Starling")
    SPOTTED_BUSH_WARBLER = "12210", _("Spotted Bush Warbler")
    SPOTTED_CRAKE = "04080", _("Spotted Crake")
    SPOTTED_DOVE = "06910", _("Spotted Dove")
    SPOTTED_EAGLE_OWL = "07450", _("Spotted Eagle-Owl")
    SPOTTED_FLYCATCHER = "13354", _("Spotted Flycatcher")
    SPOTTED_FORKTAIL = "12110", _("Spotted Forktail")
    SPOTTED_GREENBUL = "32610", _("Spotted Greenbul")
    SPOTTED_HONEYGUIDE = "32550", _("Spotted Honeyguide")
    SPOTTED_LAUGHINGTHRUSH = "13950", _("Spotted Laughingthrush")
    SPOTTED_OWL = "07640", _("Spotted Owl")
    SPOTTED_OWLET = "07580", _("Spotted Owlet")
    SPOTTED_REDSHANK = "05450", _("Spotted Redshank")
    SPOTTED_SANDGROUSE = "06590", _("Spotted Sandgrouse")
    SPOTTED_SANDPIPER = "05570", _("Spotted Sandpiper")
    SPOTTED_THICK_KNEE = "04610", _("Spotted Thick-knee")
    SPOTTED_WREN = "10540", _("Spotted Wren")
    SPRAGUE_S_PIPIT = "10150", _("Sprague's Pipit")
    SPRUCE_GROUSE = "03240", _("Spruce Grouse")
    SPUR_WINGED_GOOSE = "01740", _("Spur-winged Goose")
    SPUR_WINGED_LAPWING = "04870", _("Spur-winged Lapwing")
    SQUACCO_HERON = "01080", _("Squacco Heron")
    SQUARE_TAILED_DRONGO = "31750", _("Square-tailed Drongo")
    SQUARE_TAILED_NIGHTJAR = "36400", _("Square-tailed Nightjar")
    SQUARE_TAILED_SAW_WING = "34530", _("Square-tailed Saw-wing")
    STANDARD_WINGED_NIGHTJAR = "32990", _("Standard-winged Nightjar")
    STEJNEGER_S_PETREL = "00320", _("Stejneger's Petrel")
    STEJNEGER_S_SCOTER = "02153", _("Stejneger's Scoter")
    STELLER_S_EIDER = "02090", _("Steller's Eider")
    STELLER_S_JAY = "15340", _("Steller's Jay")
    STELLER_S_SEA_EAGLE = "02450", _("Steller's Sea Eagle")
    STEPPE_EAGLE = "02942", _("Steppe Eagle")
    STERCORARIIDAE_SP = "05709", _("Stercorariidae sp.")
    STERCORARIUS_MACCORMICKI_X_S_ANTARCTICUS = (
        "90560",
        _("Stercorarius maccormicki x S. antarcticus"),
    )
    STERCORARIUS_MACCORMICKI_S_ANTARCTICUS = "05699", _("Stercorarius maccormicki/S. antarcticus")
    STERNA_HIRUNDO_X_STERNA_PARADISAEA = "90840", _("Sterna hirundo x Sterna paradisaea")
    STERNA_HIRUNDO_PARADISAEA = "06159", _("Sterna hirundo/paradisaea")
    STERNINAE_SP = "06259", _("Sterninae sp.")
    STILT_SANDPIPER = "05150", _("Stilt Sandpiper")
    STOCK_DOVE = "06680", _("Stock Dove")
    STOLID_FLYCATCHER = "09350", _("Stolid Flycatcher")
    STONE_PARTRIDGE = "34640", _("Stone Partridge")
    STOUT_CISTICOLA = "31340", _("Stout Cisticola")
    STRAIGHT_BILLED_WOODCREEPER = "27700", _("Straight-billed Woodcreeper")
    STREAK_BACKED_ORIOLE = "19190", _("Streak-backed Oriole")
    STREAK_BREASTED_SCIMITAR_BABBLER = "13570", _("Streak-breasted Scimitar Babbler")
    STREAK_THROATED_SWALLOW = "09960", _("Streak-throated Swallow")
    STREAKED_LAUGHINGTHRUSH = "13990", _("Streaked Laughingthrush")
    STREAKED_ROSEFINCH = "16950", _("Streaked Rosefinch")
    STREAKED_SCRUB_WARBLER = "12310", _("Streaked Scrub Warbler")
    STREAKED_SHEARWATER = "00370", _("Streaked Shearwater")
    STREAKED_WEAVER = "36570", _("Streaked Weaver")
    STREAKY_BREASTED_FLUFFTAIL = "34780", _("Streaky-breasted Flufftail")
    STREAKY_HEADED_SEEDEATER = "34860", _("Streaky-headed Seedeater")
    STREPTOPELIA_ROSEOGRISEA_VAR_RISORIA = "06831", _("Streptopelia roseogrisea var. risoria")
    STREPTOPELIA_SP = "06919", _("Streptopelia sp.")
    STREPTOPELIA_TURTUR_X_STREPTOPELIA_DECAOCTO = (
        "90270",
        _("Streptopelia turtur x Streptopelia decaocto"),
    )
    STREPTOPELIA_TURTUR_X_STREPTOPELIA_DECAOCTO_2 = (
        "90271",
        _("Streptopelia turtur x Streptopelia decaocto"),
    )
    STREPTOPELIA_TURTUR_X_STREPTOPELIA_DECAOCTO_3 = (
        "90272",
        _("Streptopelia turtur x Streptopelia decaocto"),
    )
    STRIATED_LAUGHINGTHRUSH = "13870", _("Striated Laughingthrush")
    STRIGIDAE = "07719", _("Strigidae")
    STRIOLATED_BUNTING = "18631", _("Striolated Bunting")
    STRIPE_THROATED_YUHINA = "14270", _("Stripe-throated Yuhina")
    STRIPED_CRAKE = "04120", _("Striped Crake")
    STRIPED_CUCKOO = "27520", _("Striped Cuckoo")
    STRIPED_KINGFISHER = "32300", _("Striped Kingfisher")
    STRIPED_SPARROW = "18160", _("Striped Sparrow")
    STRIX_SP = "07669", _("Strix sp.")
    STURNIDAE_SP = "15859", _("Sturnidae sp.")
    SUDAN_GOLDEN_SPARROW = "15990", _("Sudan Golden Sparrow")
    SULPHUR_BELLIED_FLYCATCHER = "09380", _("Sulphur-bellied Flycatcher")
    SULPHUR_BELLIED_TYRANT_MANAKIN = "27300", _("Sulphur-bellied Tyrant-Manakin")
    SULPHUR_BELLIED_WARBLER = "13050", _("Sulphur-bellied Warbler")
    SULPHUR_BREASTED_WARBLER = "12820", _("Sulphur-breasted Warbler")
    SUMMER_TANAGER = "17860", _("Summer Tanager")
    SUN_LARK = "32150", _("Sun Lark")
    SUNDA_ZEBRA_FINCH = "20441", _("Sunda Zebra Finch")
    SUPERB_STARLING = "35580", _("Superb Starling")
    SUPERB_SUNBIRD = "33640", _("Superb Sunbird")
    SURF_SCOTER = "02140", _("Surf Scoter")
    SURFBIRD = "04940", _("Surfbird")
    SWAINSON_S_FLYCATCHER = "27240", _("Swainson's Flycatcher")
    SWAINSON_S_HAWK = "02820", _("Swainson's Hawk")
    SWAINSON_S_THRUSH = "11770", _("Swainson's Thrush")
    SWAINSON_S_WARBLER = "17590", _("Swainson's Warbler")
    SWALLOW_TAILED_BEE_EATER = "33210", _("Swallow-tailed Bee-eater")
    SWALLOW_TAILED_KITE = "02330", _("Swallow-tailed Kite")
    SWAMP_FLYCATCHER = "33330", _("Swamp Flycatcher")
    SWAMP_NIGHTJAR = "30960", _("Swamp Nightjar")
    SWAMP_PALM_BULBUL = "35180", _("Swamp Palm Bulbul")
    SWAMP_SPARROW = "18370", _("Swamp Sparrow")
    SWAN_GOOSE = "01560", _("Swan Goose")
    SWINHOE_S_RAIL = "04170", _("Swinhoe's Rail")
    SWINHOE_S_SNIPE = "05220", _("Swinhoe's Snipe")
    SWINHOE_S_STORM_PETREL = "00560", _("Swinhoe's Storm Petrel")
    SYKES_S_NIGHTJAR = "07750", _("Sykes's Nightjar")
    SYKES_S_WARBLER = "12562", _("Sykes's Warbler")
    SYLVIA_ATRICAPILLA_X_SYLVIA_BORIN = "90380", _("Sylvia atricapilla x Sylvia borin")
    SYLVIA_CURRUCA_SP = "12779", _("Sylvia/Curruca sp.")
    SYRIAN_SERIN = "16410", _("Syrian Serin")
    SYRIAN_WOODPECKER = "08780", _("Syrian Woodpecker")
    TACHYSPIZA_VIRGATA_SENSU_LATO = "02680", _("Tachyspiza virgata sensu lato")
    TAENIOPYGIA_GUTTATA_SENSU_LATO = "20440", _("Taeniopygia guttata sensu lato")
    TAHITI_SWALLOW = "09930", _("Tahiti Swallow")
    TAIGA_BEAN_GOOSE = "01575", _("Taiga Bean Goose")
    TAIGA_FLYCATCHER = "13432", _("Taiga Flycatcher")
    TAIWAN_GREEN_PIGEON = "07060", _("Taiwan Green Pigeon")
    TAIWAN_LIOCICHLA = "14060", _("Taiwan Liocichla")
    TAIWAN_VIVID_NILTAVA = "13250", _("Taiwan Vivid Niltava")
    TAMAULIPAS_CROW = "15650", _("Tamaulipas Crow")
    TAMBOURINE_DOVE = "23300", _("Tambourine Dove")
    TAVETA_WEAVER = "26400", _("Taveta Weaver")
    TAWNY_EAGLE = "02941", _("Tawny Eagle")
    TAWNY_FISH_OWL = "07480", _("Tawny Fish Owl")
    TAWNY_OWL = "07610", _("Tawny Owl")
    TAWNY_PIPIT = "10050", _("Tawny Pipit")
    TAWNY_FLANKED_PRINIA = "34470", _("Tawny-flanked Prinia")
    TAWNY_SHOULDERED_BLACKBIRD = "19100", _("Tawny-shouldered Blackbird")
    TEMMINCK_S_COURSER = "31640", _("Temminck's Courser")
    TEMMINCK_S_LARK = "09790", _("Temminck's Lark")
    TEMMINCK_S_STINT = "05020", _("Temminck's Stint")
    TEMMINCK_S_TRAGOPAN = "03810", _("Temminck's Tragopan")
    TENERIFE_BLUE_CHAFFINCH = "16371", _("Tenerife Blue Chaffinch")
    TENNESSEE_WARBLER = "17240", _("Tennessee Warbler")
    TEREK_SANDPIPER = "05550", _("Terek Sandpiper")
    TESSMANN_S_FLYCATCHER = "33400", _("Tessmann's Flycatcher")
    THALASSARCHE_CHLORORHYNCHOS_CARTERI = "00150", _("Thalassarche chlororhynchos/carteri")
    THAMNOLAEA_CINNAMOMEIVENTRIS_CINNAMOMIVENTRIS_SENSU_LATO = (
        "35160",
        _("Thamnolaea cinnamomeiventris cinnamomiventris sensu lato"),
    )
    THEKLA_S_LARK = "09730", _("Thekla's Lark")
    THICK_BILLED_CUCKOO = "33900", _("Thick-billed Cuckoo")
    THICK_BILLED_EUPHONIA = "27010", _("Thick-billed Euphonia")
    THICK_BILLED_KINGBIRD = "09430", _("Thick-billed Kingbird")
    THICK_BILLED_LARK = "09600", _("Thick-billed Lark")
    THICK_BILLED_LONGSPUR = "18460", _("Thick-billed Longspur")
    THICK_BILLED_MURRE = "06350", _("Thick-billed Murre")
    THICK_BILLED_PARROT = "07090", _("Thick-billed Parrot")
    THICK_BILLED_SEEDEATER = "34850", _("Thick-billed Seedeater")
    THICK_BILLED_VIREO = "16240", _("Thick-billed Vireo")
    THICK_BILLED_WARBLER = "12540", _("Thick-billed Warbler")
    THICK_BILLED_WEAVER = "30170", _("Thick-billed Weaver")
    THREE_BANDED_PLOVER = "31140", _("Three-banded Plover")
    THREE_BANDED_ROSEFINCH = "16900", _("Three-banded Rosefinch")
    THREE_TOED_PARROTBILL = "13660", _("Three-toed Parrotbill")
    THRUSH_NIGHTINGALE = "11030", _("Thrush Nightingale")
    TIBETAN_BABAX = "13830", _("Tibetan Babax")
    TIBETAN_BUNTING = "18550", _("Tibetan Bunting")
    TIBETAN_LARK = "09630", _("Tibetan Lark")
    TIBETAN_PARTRIDGE = "03690", _("Tibetan Partridge")
    TIBETAN_ROSEFINCH = "16980", _("Tibetan Rosefinch")
    TIBETAN_SAND_PLOVER = "36370", _("Tibetan Sand Plover")
    TIBETAN_SANDGROUSE = "06640", _("Tibetan Sandgrouse")
    TIBETAN_SERIN = "16430", _("Tibetan Serin")
    TIBETAN_SNOWCOCK = "03530", _("Tibetan Snowcock")
    TICKELL_S_LEAF_WARBLER = "13060", _("Tickell's Leaf Warbler")
    TICKELL_S_THRUSH = "11830", _("Tickell's Thrush")
    TIGER_SHRIKE = "15110", _("Tiger Shrike")
    TINY_SUNBIRD = "33560", _("Tiny Sunbird")
    TIT_HYLIA = "34010", _("Tit Hylia")
    TOWNSEND_S_SHEARWATER = "00470", _("Townsend's Shearwater")
    TOWNSEND_S_SOLITAIRE = "10420", _("Townsend's Solitaire")
    TOWNSEND_S_WARBLER = "17440", _("Townsend's Warbler")
    TRANSVOLCANIC_JAY = "15360", _("Transvolcanic Jay")
    TREE_PIPIT = "10090", _("Tree Pipit")
    TREE_SWALLOW = "09830", _("Tree Swallow")
    TRICOLORED_BLACKBIRD = "19080", _("Tricolored Blackbird")
    TRICOLORED_HERON = "01130", _("Tricolored Heron")
    TRICOLORED_MUNIA = "20291", _("Tricolored Munia")
    TRINDADE_PETREL = "00240", _("Trindade Petrel")
    TRINIDAD_MOTMOT = "36310", _("Trinidad Motmot")
    TRISTAN_ALBATROSS = "36000", _("Tristan Albatross")
    TRISTRAM_S_BUNTING = "18720", _("Tristram's Bunting")
    TRISTRAM_S_STARLING = "15750", _("Tristram's Starling")
    TRISTRAM_S_STORM_PETREL = "00630", _("Tristram's Storm Petrel")
    TRISTRAM_S_WARBLER = "12630", _("Tristram's Warbler")
    TROCAZ_PIGEON = "06710", _("Trocaz Pigeon")
    TROGLODYTES_AEDON_SENSU_LATO = "10650", _("Troglodytes aedon sensu lato")
    TROPICAL_BOUBOU = "36120", _("Tropical Boubou")
    TROPICAL_PARULA = "17310", _("Tropical Parula")
    TROPICAL_SHEARWATER = "00491", _("Tropical Shearwater")
    TRUMPETER_FINCH = "16760", _("Trumpeter Finch")
    TRUMPETER_HORNBILL = "31040", _("Trumpeter Hornbill")
    TRUMPETER_SWAN = "01550", _("Trumpeter Swan")
    TUFTED_DUCK = "02030", _("Tufted Duck")
    TUFTED_JAY = "15280", _("Tufted Jay")
    TUFTED_PUFFIN = "06560", _("Tufted Puffin")
    TUFTED_TITMOUSE = "14510", _("Tufted Titmouse")
    TULLBERG_S_WOODPECKER = "30930", _("Tullberg's Woodpecker")
    TUNDRA_BEAN_GOOSE = "01574", _("Tundra Bean Goose")
    TUNDRA_SWAN = "01530", _("Tundra Swan")
    TURDUS_NAUMANNI_SENSU_LATO = "11960", _("Turdus naumanni sensu lato")
    TURDUS_RUFICOLLIS_SENSU_LATO = "11970", _("Turdus ruficollis sensu lato")
    TURDUS_SP = "12069", _("Turdus sp.")
    TURKESTAN_GROUND_JAY = "15530", _("Turkestan Ground Jay")
    TURKESTAN_SHORT_TOED_LARK = "36180", _("Turkestan Short-toed Lark")
    TURKEY_VULTURE = "02270", _("Turkey Vulture")
    TURQUOISE_FRONTED_AMAZON = "36030", _("Turquoise-fronted Amazon")
    TWITE = "16620", _("Twite")
    TWO_BARRED_CROSSBILL = "16650", _("Two-barred Crossbill")
    TWO_BARRED_WARBLER = "12920", _("Two-barred Warbler")
    TYTLER_S_LEAF_WARBLER = "12900", _("Tytler's Leaf Warbler")
    ULTRAMARINE_FLYCATCHER = "13390", _("Ultramarine Flycatcher")
    UNICOLORED_BLACKBIRD = "26720", _("Unicolored Blackbird")
    UNIDENTIFIED_DUCK = "99931", _("Unidentified duck")
    UNKNOWN_SPECIES = "00000", _("Unknown species")
    UPCHER_S_WARBLER = "12570", _("Upcher's Warbler")
    UPLAND_BUZZARD = "02890", _("Upland Buzzard")
    UPLAND_GOOSE = "20380", _("Upland Goose")
    UPLAND_PIPIT = "10030", _("Upland Pipit")
    UPLAND_SANDPIPER = "05440", _("Upland Sandpiper")
    URAL_OWL = "07650", _("Ural Owl")
    URIA_SP = "06359", _("Uria sp.")
    USSHER_S_FLYCATCHER = "33410", _("Ussher's Flycatcher")
    VARIABLE_SUNBIRD = "33650", _("Variable Sunbird")
    VARIABLE_WHEATEAR = "11530", _("Variable Wheatear")
    VARIED_BUNTING = "18940", _("Varied Bunting")
    VARIED_THRUSH = "11720", _("Varied Thrush")
    VARIED_TIT = "14570", _("Varied Tit")
    VARIEGATED_LAUGHINGTHRUSH = "13890", _("Variegated Laughingthrush")
    VAUX_S_SWIFT = "07910", _("Vaux's Swift")
    VEERY = "11790", _("Veery")
    VEGA_GULL = "05924", _("Vega Gull")
    VELVET_SCOTER = "02150", _("Velvet Scoter")
    VELVET_MANTLED_DRONGO = "31760", _("Velvet-mantled Drongo")
    VERDIN = "14890", _("Verdin")
    VERDITER_FLYCATCHER = "13280", _("Verditer Flycatcher")
    VERMICULATED_FISHING_OWL = "34830", _("Vermiculated Fishing Owl")
    VERREAUX_S_EAGLE = "02970", _("Verreaux's Eagle")
    VERREAUX_S_EAGLE_OWL = "30740", _("Verreaux's Eagle-Owl")
    VESPER_SPARROW = "18250", _("Vesper Sparrow")
    VIEILLOT_S_BARBET = "32970", _("Vieillot's Barbet")
    VIEILLOT_S_BLACK_WEAVER = "36100", _("Vieillot's Black Weaver")
    VILLAGE_INDIGOBIRD = "35460", _("Village Indigobird")
    VILLAGE_WEAVER = "20030", _("Village Weaver")
    VINACEOUS_DOVE = "26510", _("Vinaceous Dove")
    VINACEOUS_ROSEFINCH = "16860", _("Vinaceous Rosefinch")
    VINOUS_THROATED_PARROTBILL = "13700", _("Vinous-throated Parrotbill")
    VIOLET_TURACO = "33420", _("Violet Turaco")
    VIOLET_BACKED_HYLIOTA = "32480", _("Violet-backed Hyliota")
    VIOLET_BACKED_STARLING = "15760", _("Violet-backed Starling")
    VIOLET_CROWNED_HUMMINGBIRD = "08100", _("Violet-crowned Hummingbird")
    VIOLET_GREEN_SWALLOW = "09850", _("Violet-green Swallow")
    VIRGINIA_RAIL = "04060", _("Virginia Rail")
    VIRGINIA_S_WARBLER = "17270", _("Virginia's Warbler")
    VITELLINE_MASKED_WEAVER = "34300", _("Vitelline Masked Weaver")
    VON_SCHRENCK_S_BITTERN = "01000", _("Von Schrenck's Bittern")
    WAHLBERG_S_EAGLE = "30540", _("Wahlberg's Eagle")
    WALLCREEPER = "14820", _("Wallcreeper")
    WALLER_S_STARLING = "33820", _("Waller's Starling")
    WANDERING_TATTLER = "05590", _("Wandering Tattler")
    WARBLING_VIREO = "16350", _("Warbling Vireo")
    WARBLING_WHITE_EYE = "15030", _("Warbling White-eye")
    WATER_PIPIT = "10141", _("Water Pipit")
    WATER_RAIL = "04070", _("Water Rail")
    WATER_THICK_KNEE = "30790", _("Water Thick-knee")
    WATERCOCK = "04280", _("Watercock")
    WATTLED_JACANA = "27120", _("Wattled Jacana")
    WATTLED_STARLING = "15860", _("Wattled Starling")
    WAVED_ALBATROSS = "36500", _("Waved Albatross")
    WEDGE_RUMPED_STORM_PETREL = "00590", _("Wedge-rumped Storm Petrel")
    WEDGE_TAILED_GRASS_FINCH = "26980", _("Wedge-tailed Grass Finch")
    WEDGE_TAILED_GREEN_PIGEON = "07040", _("Wedge-tailed Green Pigeon")
    WEDGE_TAILED_SHEARWATER = "00410", _("Wedge-tailed Shearwater")
    WEST_AFRICAN_PIED_HORNBILL = "35222", _("West African Pied Hornbill")
    WEST_INDIAN_WHISTLING_DUCK = "01500", _("West Indian Whistling Duck")
    WEST_INDIAN_WOODPECKER = "08680", _("West Indian Woodpecker")
    WESTERN_BANDED_SNAKE_EAGLE = "31200", _("Western Banded Snake Eagle")
    WESTERN_BARN_OWL = "07350", _("Western Barn Owl")
    WESTERN_BEARDED_GREENBUL = "23900", _("Western Bearded Greenbul")
    WESTERN_BLACK_EARED_WHEATEAR = "11481", _("Western Black-eared Wheatear")
    WESTERN_BLUEBILL = "25500", _("Western Bluebill")
    WESTERN_BLUEBIRD = "11330", _("Western Bluebird")
    WESTERN_BONELLI_S_WARBLER = "13071", _("Western Bonelli's Warbler")
    WESTERN_BRONZE_NAPED_PIGEON = "36080", _("Western Bronze-naped Pigeon")
    WESTERN_CAPERCAILLIE = "03350", _("Western Capercaillie")
    WESTERN_CATTLE_EGRET = "01110", _("Western Cattle Egret")
    WESTERN_CITRIL = "34880", _("Western Citril")
    WESTERN_CROWNED_WARBLER = "12870", _("Western Crowned Warbler")
    WESTERN_DWARF_HORNBILL = "35230", _("Western Dwarf Hornbill")
    WESTERN_FLYCATCHER = "09200", _("Western Flycatcher")
    WESTERN_GREBE = "00130", _("Western Grebe")
    WESTERN_GULL = "05940", _("Western Gull")
    WESTERN_HOUSE_MARTIN = "10010", _("Western House Martin")
    WESTERN_JACKDAW = "15600", _("Western Jackdaw")
    WESTERN_KINGBIRD = "09420", _("Western Kingbird")
    WESTERN_LONG_TAILED_HORNBILL = "35300", _("Western Long-tailed Hornbill")
    WESTERN_MARSH_HARRIER = "02600", _("Western Marsh Harrier")
    WESTERN_MEADOWLARK = "19060", _("Western Meadowlark")
    WESTERN_MOUNTAIN_GREENBUL = "30270", _("Western Mountain Greenbul")
    WESTERN_NICATOR = "25300", _("Western Nicator")
    WESTERN_OLIVACEOUS_WARBLER = "12552", _("Western Olivaceous Warbler")
    WESTERN_ORIOLE = "33840", _("Western Oriole")
    WESTERN_ORPHEAN_WARBLER = "12721", _("Western Orphean Warbler")
    WESTERN_PLANTAIN_EATER = "31580", _("Western Plantain-eater")
    WESTERN_RED_BILLED_HORNBILL = "35210", _("Western Red-billed Hornbill")
    WESTERN_REEF_HERON = "01180", _("Western Reef Heron")
    WESTERN_ROCK_NUTHATCH = "14810", _("Western Rock Nuthatch")
    WESTERN_ROCKHOPPER_PENGUIN = "35890", _("Western Rockhopper Penguin")
    WESTERN_SANDPIPER = "04990", _("Western Sandpiper")
    WESTERN_SPINDALIS = "17900", _("Western Spindalis")
    WESTERN_SUBALPINE_WARBLER = "12654", _("Western Subalpine Warbler")
    WESTERN_SWAMPHEN = "04270", _("Western Swamphen")
    WESTERN_TANAGER = "17870", _("Western Tanager")
    WESTERN_TINKERBIRD = "34360", _("Western Tinkerbird")
    WESTERN_TRAGOPAN = "03780", _("Western Tragopan")
    WESTERN_VIOLET_BACKED_SUNBIRD = "30360", _("Western Violet-backed Sunbird")
    WESTERN_WOOD_PEWEE = "09290", _("Western Wood Pewee")
    WESTERN_YELLOW_WAGTAIL = "10170", _("Western Yellow Wagtail")
    WESTLAND_PETREL = "27820", _("Westland Petrel")
    WHINCHAT = "11370", _("Whinchat")
    WHISKERED_AUKLET = "06500", _("Whiskered Auklet")
    WHISKERED_SCREECH_OWL = "07420", _("Whiskered Screech Owl")
    WHISKERED_TERN = "06260", _("Whiskered Tern")
    WHISTLING_CISTICOLA = "31320", _("Whistling Cisticola")
    WHITE_EARED_PHEASANT = "03880", _("White Eared Pheasant")
    WHITE_STORK = "01340", _("White Stork")
    WHITE_TERN = "06310", _("White Tern")
    WHITE_WAGTAIL = "10200", _("White Wagtail")
    WHITE_S_THRUSH = "11700", _("White's Thrush")
    WHITE_BACKED_DUCK = "35150", _("White-backed Duck")
    WHITE_BACKED_NIGHT_HERON = "32210", _("White-backed Night Heron")
    WHITE_BACKED_THRUSH = "11890", _("White-backed Thrush")
    WHITE_BACKED_VULTURE = "32270", _("White-backed Vulture")
    WHITE_BACKED_WOODPECKER = "08840", _("White-backed Woodpecker")
    WHITE_BEARDED_MANAKIN = "36270", _("White-bearded Manakin")
    WHITE_BELLIED_BUSTARD = "32080", _("White-bellied Bustard")
    WHITE_BELLIED_CRESTED_FLYCATCHER = "31840", _("White-bellied Crested Flycatcher")
    WHITE_BELLIED_GREEN_PIGEON = "07050", _("White-bellied Green Pigeon")
    WHITE_BELLIED_HERON = "01248", _("White-bellied Heron")
    WHITE_BELLIED_KINGFISHER = "30130", _("White-bellied Kingfisher")
    WHITE_BELLIED_REDSTART = "11300", _("White-bellied Redstart")
    WHITE_BELLIED_ROBIN_CHAT = "31550", _("White-bellied Robin-Chat")
    WHITE_BELLIED_SEEDEATER = "27470", _("White-bellied Seedeater")
    WHITE_BELLIED_STORM_PETREL = "27720", _("White-bellied Storm Petrel")
    WHITE_BELLIED_TIT = "33930", _("White-bellied Tit")
    WHITE_BELLIED_WOODPECKER = "08640", _("White-bellied Woodpecker")
    WHITE_BIBBED_SWALLOW = "32430", _("White-bibbed Swallow")
    WHITE_BILLED_BUFFALO_WEAVER = "30730", _("White-billed Buffalo Weaver")
    WHITE_BREASTED_CUCKOOSHRIKE = "31480", _("White-breasted Cuckooshrike")
    WHITE_BREASTED_NIGRITA = "33760", _("White-breasted Nigrita")
    WHITE_BREASTED_NUTHATCH = "14760", _("White-breasted Nuthatch")
    WHITE_BREASTED_WATERHEN = "04230", _("White-breasted Waterhen")
    WHITE_BROWED_ANTBIRD = "27290", _("White-browed Antbird")
    WHITE_BROWED_BUSH_CHAT = "11360", _("White-browed Bush Chat")
    WHITE_BROWED_BUSH_ROBIN = "11150", _("White-browed Bush Robin")
    WHITE_BROWED_COUCAL = "26710", _("White-browed Coucal")
    WHITE_BROWED_CRAKE = "04130", _("White-browed Crake")
    WHITE_BROWED_FOREST_FLYCATCHER = "24600", _("White-browed Forest Flycatcher")
    WHITE_BROWED_FULVETTA = "14190", _("White-browed Fulvetta")
    WHITE_BROWED_LAUGHINGTHRUSH = "13980", _("White-browed Laughingthrush")
    WHITE_BROWED_SCRUB_ROBIN = "36410", _("White-browed Scrub Robin")
    WHITE_BROWED_SHAMA = "27960", _("White-browed Shama")
    WHITE_BROWED_SPARROW_WEAVER = "22800", _("White-browed Sparrow-Weaver")
    WHITE_BROWED_TIT = "14390", _("White-browed Tit")
    WHITE_BROWED_TIT_WARBLER = "13170", _("White-browed Tit-warbler")
    WHITE_BROWED_WAGTAIL = "10220", _("White-browed Wagtail")
    WHITE_CAPPED_BUNTING = "18590", _("White-capped Bunting")
    WHITE_CAPPED_REDSTART = "11590", _("White-capped Redstart")
    WHITE_CHEEKED_BUSHTIT = "14350", _("White-cheeked Bushtit")
    WHITE_CHEEKED_NUTHATCH = "14750", _("White-cheeked Nuthatch")
    WHITE_CHEEKED_PINTAIL = "01900", _("White-cheeked Pintail")
    WHITE_CHEEKED_STARLING = "15850", _("White-cheeked Starling")
    WHITE_CHEEKED_TERN = "06200", _("White-cheeked Tern")
    WHITE_CHINNED_PETREL = "27800", _("White-chinned Petrel")
    WHITE_CHINNED_PRINIA = "36560", _("White-chinned Prinia")
    WHITE_CHINNED_WOODCREEPER = "26920", _("White-chinned Woodcreeper")
    WHITE_COLLARED_BLACKBIRD = "11850", _("White-collared Blackbird")
    WHITE_COLLARED_YUHINA = "14280", _("White-collared Yuhina")
    WHITE_CRESTED_HELMETSHRIKE = "26490", _("White-crested Helmetshrike")
    WHITE_CRESTED_TIGER_HERON = "35190", _("White-crested Tiger Heron")
    WHITE_CRESTED_TURACO = "35050", _("White-crested Turaco")
    WHITE_CRESTED_TYRANNULET = "27431", _("White-crested Tyrannulet")
    WHITE_CROWNED_FORKTAIL = "12100", _("White-crowned Forktail")
    WHITE_CROWNED_LAPWING = "26470", _("White-crowned Lapwing")
    WHITE_CROWNED_PENDULINE_TIT = "14902", _("White-crowned Penduline Tit")
    WHITE_CROWNED_PIGEON = "06790", _("White-crowned Pigeon")
    WHITE_CROWNED_ROBIN_CHAT = "31510", _("White-crowned Robin-Chat")
    WHITE_CROWNED_SPARROW = "18390", _("White-crowned Sparrow")
    WHITE_CROWNED_WHEATEAR = "11570", _("White-crowned Wheatear")
    WHITE_EARED_BULBUL = "36050", _("White-eared Bulbul")
    WHITE_EARED_HUMMINGBIRD = "08060", _("White-eared Hummingbird")
    WHITE_EYED_ATTILA = "26770", _("White-eyed Attila")
    WHITE_EYED_BUZZARD = "02750", _("White-eyed Buzzard")
    WHITE_EYED_GULL = "05720", _("White-eyed Gull")
    WHITE_EYED_PARAKEET = "26750", _("White-eyed Parakeet")
    WHITE_EYED_TODY_TYRANT = "27080", _("White-eyed Tody-Tyrant")
    WHITE_EYED_VIREO = "16230", _("White-eyed Vireo")
    WHITE_FACED_IBIS = "01370", _("White-faced Ibis")
    WHITE_FACED_STORM_PETREL = "00510", _("White-faced Storm Petrel")
    WHITE_FACED_WHISTLING_DUCK = "35950", _("White-faced Whistling Duck")
    WHITE_FLANKED_ANTWREN = "36280", _("White-flanked Antwren")
    WHITE_FRONTED_BEE_EATER = "36450", _("White-fronted Bee-eater")
    WHITE_FRONTED_BLACK_CHAT = "33440", _("White-fronted Black Chat")
    WHITE_FRONTED_PLOVER = "20460", _("White-fronted Plover")
    WHITE_HEADED_BARBET = "32960", _("White-headed Barbet")
    WHITE_HEADED_DUCK = "02260", _("White-headed Duck")
    WHITE_HEADED_MUNIA = "20450", _("White-headed Munia")
    WHITE_HEADED_VULTURE = "35280", _("White-headed Vulture")
    WHITE_HEADED_WOOD_HOOPOE = "33980", _("White-headed Wood Hoopoe")
    WHITE_HEADED_WOODPECKER = "08970", _("White-headed Woodpecker")
    WHITE_LINED_TANAGER = "36290", _("White-lined Tanager")
    WHITE_NAPED_CRANE = "04370", _("White-naped Crane")
    WHITE_NECKED_THRUSH = "12060", _("White-necked Thrush")
    WHITE_RUMPED_MONJITA = "27710", _("White-rumped Monjita")
    WHITE_RUMPED_MUNIA = "16200", _("White-rumped Munia")
    WHITE_RUMPED_SANDPIPER = "05050", _("White-rumped Sandpiper")
    WHITE_RUMPED_SEEDEATER = "34870", _("White-rumped Seedeater")
    WHITE_RUMPED_SHAMA = "27940", _("White-rumped Shama")
    WHITE_RUMPED_SNOWFINCH = "16090", _("White-rumped Snowfinch")
    WHITE_RUMPED_SWIFT = "07990", _("White-rumped Swift")
    WHITE_RUMPED_VULTURE = "02490", _("White-rumped Vulture")
    WHITE_SHOULDERED_STARLING = "15810", _("White-shouldered Starling")
    WHITE_SHOULDERED_TANAGER = "36300", _("White-shouldered Tanager")
    WHITE_SPECTACLED_BULBUL = "10360", _("White-spectacled Bulbul")
    WHITE_SPOTTED_FLUFFTAIL = "34800", _("White-spotted Flufftail")
    WHITE_STRIPED_WOODCREEPER = "09030", _("White-striped Woodcreeper")
    WHITE_TAILED_ALETHE = "30150", _("White-tailed Alethe")
    WHITE_TAILED_ANT_THRUSH = "33690", _("White-tailed Ant Thrush")
    WHITE_TAILED_EAGLE = "02430", _("White-tailed Eagle")
    WHITE_TAILED_HAWK = "02840", _("White-tailed Hawk")
    WHITE_TAILED_KITE = "02340", _("White-tailed Kite")
    WHITE_TAILED_LAPWING = "04920", _("White-tailed Lapwing")
    WHITE_TAILED_NUTHATCH = "14770", _("White-tailed Nuthatch")
    WHITE_TAILED_PTARMIGAN = "03310", _("White-tailed Ptarmigan")
    WHITE_TAILED_TROPICBIRD = "00660", _("White-tailed Tropicbird")
    WHITE_TAILED_WARBLER = "34440", _("White-tailed Warbler")
    WHITE_THIGHED_HORNBILL = "31020", _("White-thighed Hornbill")
    WHITE_THROATED_BEE_EATER = "08370", _("White-throated Bee-eater")
    WHITE_THROATED_BUSH_CHAT = "11400", _("White-throated Bush Chat")
    WHITE_THROATED_BUSHTIT = "14340", _("White-throated Bushtit")
    WHITE_THROATED_DIPPER = "10500", _("White-throated Dipper")
    WHITE_THROATED_FANTAIL = "13520", _("White-throated Fantail")
    WHITE_THROATED_FLYCATCHER = "09210", _("White-throated Flycatcher")
    WHITE_THROATED_FRANCOLIN = "33950", _("White-throated Francolin")
    WHITE_THROATED_GREENBUL = "23700", _("White-throated Greenbul")
    WHITE_THROATED_KINGFISHER = "08270", _("White-throated Kingfisher")
    WHITE_THROATED_LAUGHINGTHRUSH = "13850", _("White-throated Laughingthrush")
    WHITE_THROATED_MAGPIE_JAY = "15300", _("White-throated Magpie-Jay")
    WHITE_THROATED_MOUNTAIN_BABBLER = "32650", _("White-throated Mountain Babbler")
    WHITE_THROATED_NEEDLETAIL = "07920", _("White-throated Needletail")
    WHITE_THROATED_REDSTART = "11250", _("White-throated Redstart")
    WHITE_THROATED_ROBIN = "11170", _("White-throated Robin")
    WHITE_THROATED_ROCK_THRUSH = "11640", _("White-throated Rock Thrush")
    WHITE_THROATED_SPARROW = "18400", _("White-throated Sparrow")
    WHITE_THROATED_SWIFT = "08010", _("White-throated Swift")
    WHITE_TIPPED_DOVE = "07000", _("White-tipped Dove")
    WHITE_VENTED_SHAMA = "27970", _("White-vented Shama")
    WHITE_WEDGED_PICULET = "27340", _("White-wedged Piculet")
    WHITE_WINGED_BLACK_TIT = "22000", _("White-winged Black Tit")
    WHITE_WINGED_BLACK_TIT_2 = "33940", _("White-winged Black Tit")
    WHITE_WINGED_DOVE = "06970", _("White-winged Dove")
    WHITE_WINGED_GROSBEAK = "17140", _("White-winged Grosbeak")
    WHITE_WINGED_LARK = "09650", _("White-winged Lark")
    WHITE_WINGED_SCOTER = "02152", _("White-winged Scoter")
    WHITE_WINGED_SNOWFINCH = "16110", _("White-winged Snowfinch")
    WHITE_WINGED_TERN = "06280", _("White-winged Tern")
    WHITE_WINGED_WIDOWBIRD = "26620", _("White-winged Widowbird")
    WHITE_WINGED_WOODPECKER = "08770", _("White-winged Woodpecker")
    WHOOPER_SWAN = "01540", _("Whooper Swan")
    WHOOPING_CRANE = "04390", _("Whooping Crane")
    WILD_TURKEY = "03990", _("Wild Turkey")
    WILLCOCKS_S_HONEYGUIDE = "32570", _("Willcocks's Honeyguide")
    WILLET = "05600", _("Willet")
    WILLIAMSON_S_SAPSUCKER = "08750", _("Williamson's Sapsucker")
    WILLOW_FLYCATCHER = "09220", _("Willow Flycatcher")
    WILLOW_PTARMIGAN = "03291", _("Willow Ptarmigan")
    WILLOW_TIT = "14420", _("Willow Tit")
    WILLOW_WARBLER = "13120", _("Willow Warbler")
    WILSON_S_INDIGOBIRD = "35540", _("Wilson's Indigobird")
    WILSON_S_PHALAROPE = "05630", _("Wilson's Phalarope")
    WILSON_S_PLOVER = "04730", _("Wilson's Plover")
    WILSON_S_SNIPE = "05192", _("Wilson's Snipe")
    WILSON_S_STORM_PETREL = "00500", _("Wilson's Storm Petrel")
    WILSON_S_WARBLER = "17720", _("Wilson's Warbler")
    WIRE_TAILED_SWALLOW = "09940", _("Wire-tailed Swallow")
    WOOD_DUCK = "01770", _("Wood Duck")
    WOOD_SANDPIPER = "05540", _("Wood Sandpiper")
    WOOD_SNIPE = "05250", _("Wood Snipe")
    WOOD_STORK = "01270", _("Wood Stork")
    WOOD_THRUSH = "11750", _("Wood Thrush")
    WOOD_WARBLER = "13080", _("Wood Warbler")
    WOODCHAT_SHRIKE = "15230", _("Woodchat Shrike")
    WOODHOUSE_S_ANTPECKER = "33920", _("Woodhouse's Antpecker")
    WOODLAND_KINGFISHER = "32320", _("Woodland Kingfisher")
    WOODLARK = "09740", _("Woodlark")
    WORM_EATING_WARBLER = "17600", _("Worm-eating Warbler")
    WORTHEN_S_SPARROW = "18220", _("Worthen's Sparrow")
    WRENTIT = "13630", _("Wrentit")
    XANTUS_S_HUMMINGBIRD = "08050", _("Xantus's Hummingbird")
    XAVIER_S_GREENBUL = "34070", _("Xavier's Greenbul")
    XINJIANG_GROUND_JAY = "15520", _("Xinjiang Ground Jay")
    YELKOUAN_SHEARWATER = "00462", _("Yelkouan Shearwater")
    YELLOW_BISHOP = "32020", _("Yellow Bishop")
    YELLOW_BITTERN = "00990", _("Yellow Bittern")
    YELLOW_BUNTING = "18540", _("Yellow Bunting")
    YELLOW_GROSBEAK = "18850", _("Yellow Grosbeak")
    YELLOW_LONGBILL = "33010", _("Yellow Longbill")
    YELLOW_PENDULINE_TIT = "30320", _("Yellow Penduline Tit")
    YELLOW_RAIL = "04180", _("Yellow Rail")
    YELLOW_BEARDED_GREENBUL = "31600", _("Yellow-bearded Greenbul")
    YELLOW_BELLIED_BUSH_WARBLER = "12180", _("Yellow-bellied Bush Warbler")
    YELLOW_BELLIED_ELAENIA = "26960", _("Yellow-bellied Elaenia")
    YELLOW_BELLIED_EREMOMELA = "31920", _("Yellow-bellied Eremomela")
    YELLOW_BELLIED_FANTAIL = "13510", _("Yellow-bellied Fantail")
    YELLOW_BELLIED_FLOWERPECKER = "14990", _("Yellow-bellied Flowerpecker")
    YELLOW_BELLIED_FLYCATCHER = "09130", _("Yellow-bellied Flycatcher")
    YELLOW_BELLIED_HYLIOTA = "32470", _("Yellow-bellied Hyliota")
    YELLOW_BELLIED_PRINIA = "36520", _("Yellow-bellied Prinia")
    YELLOW_BELLIED_SAPSUCKER = "08720", _("Yellow-bellied Sapsucker")
    YELLOW_BELLIED_TIT = "14560", _("Yellow-bellied Tit")
    YELLOW_BELLIED_WATTLE_EYE = "34160", _("Yellow-bellied Wattle-eye")
    YELLOW_BILLED_BLUE_MAGPIE = "15450", _("Yellow-billed Blue Magpie")
    YELLOW_BILLED_CUCKOO = "07280", _("Yellow-billed Cuckoo")
    YELLOW_BILLED_DUCK = "30210", _("Yellow-billed Duck")
    YELLOW_BILLED_KITE = "02382", _("Yellow-billed Kite")
    YELLOW_BILLED_LOON = "00050", _("Yellow-billed Loon")
    YELLOW_BILLED_MAGPIE = "15500", _("Yellow-billed Magpie")
    YELLOW_BILLED_OXPECKER = "30780", _("Yellow-billed Oxpecker")
    YELLOW_BILLED_PINTAIL = "27770", _("Yellow-billed Pintail")
    YELLOW_BILLED_SHRIKE = "31490", _("Yellow-billed Shrike")
    YELLOW_BILLED_STORK = "01290", _("Yellow-billed Stork")
    YELLOW_BILLED_TEAL = "35780", _("Yellow-billed Teal")
    YELLOW_BILLED_TURACO = "35060", _("Yellow-billed Turaco")
    YELLOW_BREASTED_APALIS = "30410", _("Yellow-breasted Apalis")
    YELLOW_BREASTED_BARBET = "35240", _("Yellow-breasted Barbet")
    YELLOW_BREASTED_BOUBOU = "32800", _("Yellow-breasted Boubou")
    YELLOW_BREASTED_BUNTING = "18760", _("Yellow-breasted Bunting")
    YELLOW_BREASTED_CHAT = "17820", _("Yellow-breasted Chat")
    YELLOW_BREASTED_GREENFINCH = "16520", _("Yellow-breasted Greenfinch")
    YELLOW_BROWED_BUNTING = "18710", _("Yellow-browed Bunting")
    YELLOW_BROWED_CAMAROPTERA = "30840", _("Yellow-browed Camaroptera")
    YELLOW_BROWED_TIT = "14380", _("Yellow-browed Tit")
    YELLOW_BROWED_TYRANT = "27400", _("Yellow-browed Tyrant")
    YELLOW_BROWED_WARBLER = "13001", _("Yellow-browed Warbler")
    YELLOW_CASQUED_HORNBILL = "31050", _("Yellow-casqued Hornbill")
    YELLOW_CHINNED_SPINETAIL = "26820", _("Yellow-chinned Spinetail")
    YELLOW_CHINNED_SUNBIRD = "30370", _("Yellow-chinned Sunbird")
    YELLOW_COLLARED_LOVEBIRD = "36020", _("Yellow-collared Lovebird")
    YELLOW_CRESTED_WOODPECKER = "31730", _("Yellow-crested Woodpecker")
    YELLOW_CROWNED_BISHOP = "20420", _("Yellow-crowned Bishop")
    YELLOW_CROWNED_GONOLEK = "32810", _("Yellow-crowned Gonolek")
    YELLOW_CROWNED_NIGHT_HERON = "01060", _("Yellow-crowned Night Heron")
    YELLOW_EYED_JUNCO = "18440", _("Yellow-eyed Junco")
    YELLOW_EYED_PIGEON = "06690", _("Yellow-eyed Pigeon")
    YELLOW_FOOTED_FLYCATCHER = "33390", _("Yellow-footed Flycatcher")
    YELLOW_FRONTED_CANARY = "36160", _("Yellow-fronted Canary")
    YELLOW_FRONTED_TINKERBIRD = "34350", _("Yellow-fronted Tinkerbird")
    YELLOW_GORGETED_GREENBUL = "26540", _("Yellow-gorgeted Greenbul")
    YELLOW_GREEN_VIREO = "16320", _("Yellow-green Vireo")
    YELLOW_HEADED_AMAZON = "26690", _("Yellow-headed Amazon")
    YELLOW_HEADED_BLACKBIRD = "19110", _("Yellow-headed Blackbird")
    YELLOW_LEGGED_BUTTONQUAIL = "04010", _("Yellow-legged Buttonquail")
    YELLOW_LEGGED_GULL = "05926", _("Yellow-legged Gull")
    YELLOW_MANTLED_WEAVER = "34290", _("Yellow-mantled Weaver")
    YELLOW_MANTLED_WIDOWBIRD = "32050", _("Yellow-mantled Widowbird")
    YELLOW_OLIVE_FLATBILL = "27630", _("Yellow-olive Flatbill")
    YELLOW_RUMPED_CACIQUE = "26790", _("Yellow-rumped Cacique")
    YELLOW_RUMPED_FLYCATCHER = "13450", _("Yellow-rumped Flycatcher")
    YELLOW_RUMPED_TINKERBIRD = "34340", _("Yellow-rumped Tinkerbird")
    YELLOW_SPOTTED_BARBET = "30760", _("Yellow-spotted Barbet")
    YELLOW_STREAKED_WARBLER = "13020", _("Yellow-streaked Warbler")
    YELLOW_THROATED_BUNTING = "18700", _("Yellow-throated Bunting")
    YELLOW_THROATED_CUCKOO = "31190", _("Yellow-throated Cuckoo")
    YELLOW_THROATED_FULVETTA = "14170", _("Yellow-throated Fulvetta")
    YELLOW_THROATED_SPARROW = "16020", _("Yellow-throated Sparrow")
    YELLOW_THROATED_TINKERBIRD = "34390", _("Yellow-throated Tinkerbird")
    YELLOW_THROATED_VIREO = "16280", _("Yellow-throated Vireo")
    YELLOW_THROATED_WARBLER = "17400", _("Yellow-throated Warbler")
    YELLOW_VENTED_WARBLER = "12830", _("Yellow-vented Warbler")
    YELLOW_WHISKERED_GREENBUL = "23600", _("Yellow-whiskered Greenbul")
    YELLOW_WINGED_PYTILIA = "34680", _("Yellow-winged Pytilia")
    YELLOWHAMMER = "18570", _("Yellowhammer")
    YEMEN_LINNET = "16610", _("Yemen Linnet")
    YEMEN_SERIN = "16460", _("Yemen Serin")
    YEMEN_THRUSH = "11820", _("Yemen Thrush")
    YEMEN_WARBLER = "12250", _("Yemen Warbler")
    YUNNAN_NUTHATCH = "14670", _("Yunnan Nuthatch")
    ZEBRA_DOVE = "35790", _("Zebra Dove")
    ZENAIDA_DOVE = "06960", _("Zenaida Dove")
    ZINO_S_PETREL = "00263", _("Zino's Petrel")
    ZITTING_CISTICOLA = "12260", _("Zitting Cisticola")
    ZONE_TAILED_HAWK = "02850", _("Zone-tailed Hawk")
    ZOSTEROPIDAE_SP = "15049", _("Zosteropidae sp.")


SPECIES_SCIENTIFIC_NAME: dict[str, str] = {
    "00000": "Unknown species",
    "00010": "Struthio camelus",
    "00020": "Gavia stellata",
    "00030": "Gavia arctica",
    "00033": "Gavia pacifica",
    "00040": "Gavia immer",
    "00050": "Gavia adamsii",
    "00059": "Gavia sp.",
    "00060": "Podilymbus podiceps",
    "00070": "Tachybaptus ruficollis",
    "00080": "Tachybaptus dominicus",
    "00090": "Podiceps cristatus",
    "00100": "Podiceps grisegena",
    "00110": "Podiceps auritus",
    "00120": "Podiceps nigricollis",
    "00129": "Podicipedidae sp.",
    "00130": "Aechmophorus occidentalis",
    "00140": "Thalassarche melanophris",
    "00150": "Thalassarche chlororhynchos/carteri",
    "00151": "Thalassarche chlororhynchos",
    "00152": "Thalassarche carteri",
    "00160": "Thalassarche cauta",
    "00170": "Phoebastria nigripes",
    "00180": "Phoebastria immutabilis",
    "00190": "Phoebastria albatrus",
    "00200": "Diomedea exulans sensu lato",
    "00201": "Diomedea exulans",
    "00210": "Macronectes sp.",
    "00211": "Macronectes giganteus",
    "00212": "Macronectes halli",
    "00220": "Fulmarus glacialis",
    "00230": "Daption capense",
    "00240": "Pterodroma arminjoniana",
    "00250": "Pterodroma neglecta",
    "00260": "Pterodroma mollis sensu lato",
    "00261": "Pterodroma mollis",
    "00262": "Pterodroma feae sensu lato",
    "00263": "Pterodroma madeira",
    "00264": "Pterodroma feae",
    "00270": "Pterodroma inexpectata",
    "00280": "Pterodroma solandri",
    "00290": "Pterodroma hasitata",
    "00300": "Pterodroma hypoleuca",
    "00310": "Pterodroma cookii",
    "00320": "Pterodroma longirostris",
    "00330": "Pterodroma leucoptera",
    "00340": "Bulweria bulwerii",
    "00350": "Bulweria fallax",
    "00360": "Calonectris diomedea sensu lato",
    "00361": "Calonectris borealis",
    "00362": "Calonectris edwardsii",
    "00363": "Calonectris diomedea",
    "00370": "Calonectris leucomelas",
    "00380": "Ardenna carneipes",
    "00390": "Ardenna creatopus",
    "00400": "Ardenna gravis",
    "00410": "Ardenna pacifica",
    "00420": "Ardenna bulleri",
    "00430": "Ardenna grisea",
    "00440": "Ardenna tenuirostris",
    "00450": "Puffinus nativitatis",
    "00460": "Puffinus puffinus sensu lato",
    "00461": "Puffinus puffinus",
    "00462": "Puffinus yelkouan",
    "00463": "Puffinus mauretanicus",
    "00470": "Puffinus auricularis",
    "00480": "Puffinus assimilis sensu lato",
    "00481": "Puffinus assimilis",
    "00482": "Puffinus baroli",
    "00483": "Puffinus boydi",
    "00484": "Puffinus persicus",
    "00485": "Puffinus bannermani",
    "00490": "Puffinus lherminieri",
    "00491": "Puffinus bailloni",
    "00500": "Oceanites oceanicus",
    "00510": "Pelagodroma marina",
    "00520": "Hydrobates pelagicus",
    "00530": "Hydrobates microsoma",
    "00540": "Hydrobates furcatus",
    "00550": "Hydrobates leucorhous",
    "00560": "Hydrobates monorhis",
    "00570": "Hydrobates homochroa",
    "00580": "Hydrobates castro sensu lato",
    "00581": "Hydrobates monteiroi",
    "00582": "Hydrobates castro",
    "00590": "Hydrobates tethys",
    "00600": "Hydrobates melania",
    "00610": "Hydrobates matsudairae",
    "00620": "Hydrobates macrodactylus",
    "00630": "Hydrobates tristrami",
    "00639": "Hydrobates sp.",
    "00640": "Phaethon aethereus",
    "00650": "Phaethon rubricauda",
    "00660": "Phaethon lepturus",
    "00670": "Sula sula",
    "00680": "Sula dactylatra",
    "00690": "Sula nebouxii",
    "00700": "Sula leucogaster",
    "00710": "Morus bassanus",
    "00712": "Morus capensis",
    "00720": "Phalacrocorax carbo",
    "00730": "Phalacrocorax capillatus",
    "00740": "Urile perspicillatus",
    "00750": "Urile pelagicus",
    "00760": "Urile urile",
    "00770": "Urile penicillatus",
    "00780": "Nannopterum auritum",
    "00790": "Nannopterum brasilianum",
    "00800": "Gulosus aristotelis",
    "00810": "Phalacrocorax nigrogularis",
    "00820": "Microcarbo pygmaeus",
    "00830": "Microcarbo africanus",
    "00840": "Microcarbo niger",
    "00849": "Phalacrocoracidae sp.",
    "00850": "Anhinga anhinga",
    "00860": "Anhinga melanogaster",
    "00870": "Pelecanus erythrorhynchos",
    "00880": "Pelecanus onocrotalus",
    "00890": "Pelecanus crispus",
    "00900": "Pelecanus rufescens",
    "00910": "Pelecanus occidentalis",
    "00919": "Pelecanidae sp.",
    "00920": "Fregata minor",
    "00930": "Fregata magnificens",
    "00940": "Fregata ariel",
    "00950": "Botaurus stellaris",
    "00960": "Botaurus lentiginosus",
    "00970": "Botaurus exilis",
    "00980": "Botaurus minutus",
    "00990": "Botaurus sinensis",
    "01000": "Botaurus eurhythmus",
    "01010": "Botaurus cinnamomeus",
    "01020": "Botaurus sturmii",
    "01030": "Gorsachius goisagi",
    "01040": "Nycticorax nycticorax",
    "01050": "Nycticorax caledonicus",
    "01060": "Nyctanassa violacea",
    "01070": "Butorides virescens sensu lato",
    "01071": "Butorides virescens",
    "01072": "Butorides atricapilla",
    "01080": "Ardeola ralloides",
    "01090": "Ardeola grayii",
    "01100": "Ardeola bacchus",
    "01110": "Ardea ibis",
    "01120": "Egretta caerulea",
    "01130": "Egretta tricolor",
    "01140": "Egretta rufescens",
    "01150": "Egretta thula",
    "01160": "Egretta eulophotes",
    "01170": "Egretta sacra",
    "01180": "Egretta gularis",
    "01190": "Egretta garzetta",
    "01200": "Ardea intermedia",
    "01210": "Ardea alba",
    "01219": "Egretta sp.",
    "01220": "Ardea cinerea",
    "01230": "Ardea herodias",
    "01240": "Ardea purpurea",
    "01248": "Ardea insignis",
    "01250": "Ardea goliath",
    "01259": "Ardea sp.",
    "01260": "Scopus umbretta",
    "01270": "Mycteria americana",
    "01280": "Mycteria leucocephala",
    "01290": "Mycteria ibis",
    "01300": "Anastomus oscitans",
    "01310": "Ciconia nigra",
    "01320": "Ciconia abdimii",
    "01330": "Ciconia episcopus",
    "01340": "Ciconia ciconia",
    "01349": "Ciconia sp.",
    "01350": "Leptoptilos crumenifer",
    "01360": "Plegadis falcinellus",
    "01370": "Plegadis chihi",
    "01380": "Eudocimus albus",
    "01390": "Eudocimus ruber",
    "01400": "Geronticus eremita",
    "01410": "Nipponia nippon",
    "01420": "Threskiornis aethiopicus",
    "01430": "Threskiornis melanocephalus",
    "01440": "Platalea leucorodia",
    "01450": "Platalea minor",
    "01460": "Platalea ajaja",
    "01470": "Phoenicopterus ruber sensu lato",
    "01471": "Phoenicopterus ruber",
    "01472": "Phoenicopterus roseus",
    "01480": "Phoeniconaias minor",
    "01490": "Dendrocygna bicolor",
    "01500": "Dendrocygna arborea",
    "01510": "Dendrocygna autumnalis",
    "01520": "Cygnus olor",
    "01530": "Cygnus columbianus",
    "01540": "Cygnus cygnus",
    "01550": "Cygnus buccinator",
    "01559": "Cygnus sp.",
    "01560": "Anser cygnoides",
    "01569": "Anserinae sp.",
    "01570": "Anser fabalis sensu lato",
    "01574": "Anser serrirostris",
    "01575": "Anser fabalis",
    "01580": "Anser brachyrhynchus",
    "01590": "Anser albifrons",
    "01600": "Anser erythropus",
    "01610": "Anser anser",
    "01613": "Anser anser var. domestica",
    "01620": "Anser indicus",
    "01630": "Anser caerulescens",
    "01640": "Anser rossii",
    "01650": "Anser canagicus",
    "01659": "Anser sp.",
    "01660": "Branta canadensis",
    "01666": "Branta hutchinsii",
    "01670": "Branta leucopsis",
    "01680": "Branta bernicla",
    "01690": "Branta ruficollis",
    "01699": "Branta sp.",
    "01700": "Alopochen aegyptiaca",
    "01710": "Tadorna ferruginea",
    "01720": "Tadorna cristata",
    "01730": "Tadorna tadorna",
    "01740": "Plectropterus gambensis",
    "01750": "Cairina moschata",
    "01760": "Nettapus coromandelianus",
    "01770": "Aix sponsa",
    "01780": "Aix galericulata",
    "01790": "Mareca penelope",
    "01800": "Mareca americana",
    "01810": "Mareca falcata",
    "01820": "Mareca strepera",
    "01830": "Sibirionetta formosa",
    "01840": "Anas crecca",
    "01842": "Anas carolinensis",
    "01850": "Anas capensis",
    "01860": "Anas platyrhynchos",
    "01863": "Anas platyrhynchos var. domestica",
    "01870": "Anas rubripes",
    "01880": "Anas poecilorhyncha",
    "01890": "Anas acuta",
    "01900": "Anas bahamensis",
    "01910": "Spatula querquedula",
    "01920": "Spatula discors",
    "01930": "Spatula cyanoptera",
    "01940": "Spatula clypeata",
    "01949": "Anas sp.",
    "01950": "Marmaronetta angustirostris",
    "01960": "Netta rufina",
    "01970": "Aythya valisineria",
    "01980": "Aythya ferina",
    "01990": "Aythya americana",
    "02000": "Aythya collaris",
    "02010": "Aythya baeri",
    "02020": "Aythya nyroca",
    "02030": "Aythya fuligula",
    "02040": "Aythya marila",
    "02050": "Aythya affinis",
    "02059": "Aythya sp.",
    "02060": "Somateria mollissima",
    "02070": "Somateria spectabilis",
    "02080": "Somateria fischeri",
    "02089": "Somateria sp.",
    "02090": "Polysticta stelleri",
    "02100": "Camptorhynchus labradorius",
    "02110": "Histrionicus histrionicus",
    "02120": "Clangula hyemalis",
    "02130": "Melanitta nigra",
    "02132": "Melanitta americana",
    "02140": "Melanitta perspicillata",
    "02150": "Melanitta fusca",
    "02152": "Melanitta deglandi",
    "02153": "Melanitta stejnegeri",
    "02160": "Bucephala albeola",
    "02170": "Bucephala islandica",
    "02180": "Bucephala clangula",
    "02190": "Lophodytes cucullatus",
    "02200": "Mergellus albellus",
    "02210": "Mergus serrator",
    "02220": "Mergus squamatus",
    "02230": "Mergus merganser",
    "02239": "Mergus sp.",
    "02240": "Nomonyx dominicus",
    "02250": "Oxyura jamaicensis",
    "02260": "Oxyura leucocephala",
    "02270": "Cathartes aura",
    "02280": "Coragyps atratus",
    "02290": "Gymnogyps californianus",
    "02300": "Chondrohierax uncinatus",
    "02310": "Pernis apivorus",
    "02320": "Pernis ptilorhynchus",
    "02330": "Elanoides forficatus",
    "02340": "Elanus leucurus",
    "02350": "Elanus caeruleus",
    "02360": "Ictinia mississippiensis",
    "02370": "Rostrhamus sociabilis",
    "02380": "Milvus migrans",
    "02382": "Milvus aegyptius",
    "02390": "Milvus milvus",
    "02399": "Milvus sp.",
    "02400": "Haliastur indus",
    "02410": "Icthyophaga vocifer",
    "02420": "Haliaeetus leucoryphus",
    "02430": "Haliaeetus albicilla",
    "02440": "Haliaeetus leucocephalus",
    "02450": "Haliaeetus pelagicus",
    "02460": "Gypaetus barbatus",
    "02470": "Neophron percnopterus",
    "02480": "Necrosyrtes monachus",
    "02490": "Gyps bengalensis",
    "02500": "Gyps indicus",
    "02510": "Gyps fulvus",
    "02520": "Gyps himalayensis",
    "02530": "Gyps rueppelli",
    "02540": "Torgos tracheliotos",
    "02550": "Aegypius monachus",
    "02560": "Circaetus gallicus",
    "02570": "Terathopius ecaudatus",
    "02580": "Spilornis cheela",
    "02590": "Geranospiza caerulescens",
    "02600": "Circus aeruginosus",
    "02610": "Circus cyaneus",
    "02620": "Circus macrourus",
    "02630": "Circus pygargus",
    "02640": "Circus melanoleucos",
    "02649": "Circus sp.",
    "02650": "Melierax metabates",
    "02660": "Micronisus gabar",
    "02670": "Astur gentilis",
    "02680": "Tachyspiza virgata sensu lato",
    "02681": "Tachyspiza virgata",
    "02682": "Tachyspiza gularis",
    "02690": "Accipiter nisus",
    "02700": "Accipiter striatus",
    "02710": "Tachyspiza soloensis",
    "02720": "Tachyspiza badia",
    "02730": "Tachyspiza brevipes",
    "02740": "Astur cooperii",
    "02749": "Accipiter; Astur; Tachyspiza; Aerospiza sp.",
    "02750": "Butastur teesa",
    "02760": "Butastur indicus",
    "02770": "Buteogallus anthracinus",
    "02780": "Parabuteo unicinctus",
    "02790": "Buteo nitidus",
    "02800": "Buteo platypterus",
    "02810": "Buteo lineatus",
    "02820": "Buteo swainsoni",
    "02830": "Buteo brachyurus",
    "02840": "Geranoaetus albicaudatus",
    "02850": "Buteo albonotatus",
    "02860": "Buteo jamaicensis",
    "02870": "Buteo buteo",
    "02880": "Buteo rufinus",
    "02890": "Buteo hemilasius",
    "02900": "Buteo lagopus",
    "02910": "Buteo regalis",
    "02919": "Buteo spp.",
    "02920": "Clanga pomarina",
    "02930": "Clanga clanga",
    "02940": "Aquila rapax sensu lato",
    "02941": "Aquila rapax",
    "02942": "Aquila nipalensis",
    "02950": "Aquila heliaca",
    "02952": "Aquila adalberti",
    "02960": "Aquila chrysaetos",
    "02970": "Aquila verreauxii",
    "02979": "Aquila sp.",
    "02980": "Hieraaetus pennatus",
    "02990": "Aquila fasciata",
    "03000": "Nisaetus nipalensis",
    "03010": "Pandion haliaetus",
    "03020": "Caracara plancus",
    "03030": "Falco naumanni",
    "03040": "Falco tinnunculus",
    "03050": "Falco sparverius",
    "03060": "Falco chicquera",
    "03070": "Falco vespertinus",
    "03080": "Falco amurensis",
    "03090": "Falco columbarius",
    "03100": "Falco subbuteo",
    "03110": "Falco eleonorae",
    "03120": "Falco concolor",
    "03130": "Falco femoralis",
    "03140": "Falco biarmicus",
    "03150": "Falco jugger",
    "03160": "Falco cherrug",
    "03180": "Falco rusticolus",
    "03190": "Falco mexicanus",
    "03200": "Falco peregrinus",
    "03219": "Falco sp.",
    "03220": "Ortalis vetula",
    "03230": "Falcipennis falcipennis",
    "03240": "Canachites canadensis",
    "03250": "Dendragapus obscurus",
    "03260": "Tetrastes bonasia",
    "03270": "Tetrastes sewerzowi",
    "03280": "Bonasa umbellus",
    "03290": "Lagopus lagopus sensu lato",
    "03291": "Lagopus lagopus",
    "03292": "Lagopus scotica",
    "03300": "Lagopus muta",
    "03310": "Lagopus leucura",
    "03320": "Lyrurus tetrix",
    "03330": "Lyrurus mlokosiewiczi",
    "03340": "Tetrao urogalloides",
    "03350": "Tetrao urogallus",
    "03360": "Tympanuchus cupido",
    "03370": "Tympanuchus phasianellus",
    "03380": "Centrocercus urophasianus",
    "03390": "Oreortyx pictus",
    "03400": "Callipepla squamata",
    "03410": "Callipepla californica",
    "03420": "Callipepla gambelii",
    "03430": "Callipepla douglasii",
    "03440": "Philortyx fasciatus",
    "03450": "Colinus virginianus",
    "03460": "Cyrtonyx montezumae",
    "03470": "Lerwa lerwa",
    "03480": "Tetraophasis obscurus",
    "03490": "Tetraophasis szechenyii",
    "03500": "Tetraogallus caucasicus",
    "03510": "Tetraogallus caspius",
    "03520": "Tetraogallus himalayensis",
    "03530": "Tetraogallus tibetanus",
    "03540": "Tetraogallus altaicus",
    "03550": "Alectoris chukar",
    "03560": "Alectoris magna",
    "03570": "Alectoris graeca",
    "03580": "Alectoris rufa",
    "03590": "Alectoris barbara",
    "03600": "Alectoris philbyi",
    "03610": "Alectoris melanocephala",
    "03620": "Ammoperdix griseogularis",
    "03630": "Ammoperdix heyi",
    "03640": "Francolinus francolinus",
    "03650": "Ortygornis pondicerianus",
    "03660": "Pternistis bicalcaratus",
    "03670": "Perdix perdix",
    "03680": "Perdix dauurica",
    "03690": "Perdix hodgsoniae",
    "03699": "Perdix sp.",
    "03700": "Coturnix coturnix",
    "03710": "Coturnix japonica",
    "03720": "Perdicula asiatica",
    "03730": "Arborophila torqueola",
    "03740": "Arborophila rufogularis",
    "03750": "Arborophila rufipectus",
    "03760": "Bambusicola thoracicus",
    "03770": "Ithaginis cruentus",
    "03780": "Tragopan melanocephalus",
    "03790": "Tragopan satyra",
    "03800": "Tragopan blythii",
    "03810": "Tragopan temminckii",
    "03820": "Pucrasia macrolopha",
    "03830": "Lophophorus impejanus",
    "03840": "Lophophorus sclateri",
    "03850": "Lophophorus lhuysii",
    "03860": "Gallus gallus",
    "03870": "Lophura leucomelanos",
    "03880": "Crossoptilon crossoptilon",
    "03890": "Crossoptilon mantchuricum",
    "03900": "Crossoptilon auritum",
    "03910": "Catreus wallichii",
    "03920": "Syrmaticus soemmerringii",
    "03930": "Syrmaticus reevesii",
    "03940": "Phasianus colchicus",
    "03950": "Phasianus versicolor",
    "03960": "Chrysolophus pictus",
    "03970": "Chrysolophus amherstiae",
    "03980": "Numida meleagris",
    "03990": "Meleagris gallopavo",
    "04000": "Turnix sylvaticus",
    "04010": "Turnix tanki",
    "04020": "Turnix suscitator",
    "04030": "Rallina eurizonoides",
    "04040": "Rallus longirostris",
    "04050": "Rallus elegans",
    "04060": "Rallus limicola",
    "04070": "Rallus aquaticus",
    "04080": "Porzana porzana",
    "04090": "Porzana carolina",
    "04100": "Zapornia parva",
    "04110": "Zapornia pusilla",
    "04120": "Aenigmatolimnas marginalis",
    "04130": "Poliolimnas cinereus",
    "04140": "Zapornia fusca",
    "04150": "Zapornia paykullii",
    "04160": "Zapornia bicolor",
    "04169": "Porzana / Zapornis sp.",
    "04170": "Coturnicops exquisitus",
    "04180": "Coturnicops noveboracensis",
    "04190": "Laterallus jamaicensis",
    "04200": "Zapornia flavirostra",
    "04210": "Crex crex",
    "04220": "Zapornia akool",
    "04230": "Amaurornis phoenicurus",
    "04240": "Gallinula chloropus",
    "04250": "Porphyrio alleni",
    "04260": "Porphyrio martinica",
    "04270": "Porphyrio porphyrio",
    "04272": "Porphyrio madagascariensis",
    "04273": "Porphyrio poliocephalus",
    "04280": "Gallicrex cinerea",
    "04290": "Fulica atra",
    "04300": "Fulica americana",
    "04310": "Fulica cristata",
    "04320": "Aramus guarauna",
    "04330": "Grus grus",
    "04340": "Grus nigricollis",
    "04350": "Grus monacha",
    "04360": "Antigone canadensis",
    "04370": "Antigone vipio",
    "04380": "Grus japonensis",
    "04390": "Grus americana",
    "04400": "Leucogeranus leucogeranus",
    "04409": "Grus sp.",
    "04410": "Grus virgo",
    "04420": "Tetrax tetrax",
    "04430": "Neotis denhami",
    "04440": "Chlamydotis undulata",
    "04442": "Chlamydotis macqueenii",
    "04450": "Ardeotis arabs",
    "04460": "Otis tarda",
    "04470": "Hydrophasianus chirurgus",
    "04480": "Jacana spinosa",
    "04490": "Rostratula benghalensis",
    "04500": "Haematopus ostralegus",
    "04510": "Haematopus palliatus",
    "04520": "Haematopus bachmani",
    "04530": "Haematopus moquini",
    "04540": "Ibidorhyncha struthersii",
    "04550": "Himantopus himantopus",
    "04560": "Recurvirostra avosetta",
    "04570": "Recurvirostra americana",
    "04580": "Dromas ardeola",
    "04590": "Burhinus oedicnemus",
    "04600": "Burhinus senegalensis",
    "04610": "Burhinus capensis",
    "04620": "Esacus recurvirostris",
    "04630": "Pluvianus aegyptius",
    "04640": "Cursorius cursor",
    "04650": "Glareola pratincola",
    "04660": "Glareola maldivarum",
    "04670": "Glareola nordmanni",
    "04680": "Glareola lactea",
    "04689": "Glareola sp.",
    "04690": "Charadrius dubius",
    "04700": "Charadrius hiaticula",
    "04710": "Charadrius semipalmatus",
    "04720": "Charadrius placidus",
    "04730": "Anarhynchus wilsonia",
    "04740": "Charadrius vociferus",
    "04750": "Charadrius melodus",
    "04760": "Anarhynchus pecuarius",
    "04770": "Anarhynchus alexandrinus",
    "04780": "Anarhynchus mongolus",
    "04790": "Anarhynchus leschenaultii",
    "04800": "Anarhynchus asiaticus",
    "04810": "Anarhynchus veredus",
    "04820": "Eudromias morinellus",
    "04830": "Anarhynchus montanus",
    "04839": "Charadrius sp.",
    "04840": "Pluvialis dominica/fulva",
    "04841": "Pluvialis dominica",
    "04842": "Pluvialis fulva",
    "04850": "Pluvialis apricaria",
    "04860": "Pluvialis squatarola",
    "04870": "Vanellus spinosus",
    "04880": "Vanellus tectus",
    "04890": "Vanellus cinereus",
    "04900": "Vanellus indicus",
    "04910": "Vanellus gregarius",
    "04920": "Vanellus leucurus",
    "04930": "Vanellus vanellus",
    "04940": "Calidris virgata",
    "04950": "Calidris tenuirostris",
    "04960": "Calidris canutus",
    "04970": "Calidris alba",
    "04980": "Calidris pusilla",
    "04990": "Calidris mauri",
    "05000": "Calidris ruficollis",
    "05010": "Calidris minuta",
    "05020": "Calidris temminckii",
    "05030": "Calidris subminuta",
    "05040": "Calidris minutilla",
    "05050": "Calidris fuscicollis",
    "05060": "Calidris bairdii",
    "05070": "Calidris melanotos",
    "05080": "Calidris acuminata",
    "05090": "Calidris ferruginea",
    "05100": "Calidris maritima",
    "05110": "Calidris ptilocnemis",
    "05120": "Calidris alpina",
    "05128": "Calidris alpina schinzii/arctica",
    "05129": "Calidris sp.",
    "05130": "Calidris pygmaea",
    "05140": "Calidris falcinellus",
    "05150": "Calidris himantopus",
    "05160": "Calidris subruficollis",
    "05170": "Calidris pugnax",
    "05180": "Lymnocryptes minimus",
    "05190": "Gallinago gallinago",
    "05192": "Gallinago delicata",
    "05200": "Gallinago media",
    "05210": "Gallinago stenura",
    "05220": "Gallinago megala",
    "05230": "Gallinago hardwickii",
    "05240": "Gallinago solitaria",
    "05250": "Gallinago nemoricola",
    "05260": "Limnodromus griseus",
    "05270": "Limnodromus scolopaceus",
    "05280": "Limnodromus semipalmatus",
    "05290": "Scolopax rusticola",
    "05300": "Scolopax mira",
    "05310": "Scolopax minor",
    "05320": "Limosa limosa",
    "05330": "Limosa haemastica",
    "05340": "Limosa lapponica",
    "05350": "Limosa fedoa",
    "05360": "Numenius minutus",
    "05370": "Numenius borealis",
    "05380": "Numenius phaeopus",
    "05381": "Numenius hudsonicus",
    "05390": "Numenius tahitiensis",
    "05400": "Numenius tenuirostris",
    "05410": "Numenius arquata",
    "05420": "Numenius americanus",
    "05430": "Numenius madagascariensis",
    "05439": "Numenius sp.",
    "05440": "Bartramia longicauda",
    "05450": "Tringa erythropus",
    "05460": "Tringa totanus",
    "05470": "Tringa stagnatilis",
    "05480": "Tringa nebularia",
    "05490": "Tringa guttifer",
    "05500": "Tringa melanoleuca",
    "05510": "Tringa flavipes",
    "05520": "Tringa solitaria",
    "05530": "Tringa ochropus",
    "05540": "Tringa glareola",
    "05550": "Xenus cinereus",
    "05560": "Actitis hypoleucos",
    "05570": "Actitis macularius",
    "05580": "Tringa brevipes",
    "05590": "Tringa incana",
    "05600": "Tringa semipalmata",
    "05610": "Arenaria interpres",
    "05620": "Arenaria melanocephala",
    "05630": "Phalaropus tricolor",
    "05640": "Phalaropus lobatus",
    "05650": "Phalaropus fulicarius",
    "05659": "Charadriiformes",
    "05660": "Stercorarius pomarinus",
    "05670": "Stercorarius parasiticus",
    "05680": "Stercorarius longicaudus",
    "05690": "Stercorarius skua",
    "05693": "Stercorarius antarcticus",
    "05699": "Stercorarius maccormicki/S. antarcticus",
    "05700": "Stercorarius maccormicki",
    "05709": "Stercorariidae sp.",
    "05710": "Ichthyaetus hemprichii",
    "05720": "Ichthyaetus leucophthalmus",
    "05730": "Ichthyaetus ichthyaetus",
    "05740": "Ichthyaetus relictus",
    "05750": "Ichthyaetus melanocephalus",
    "05760": "Leucophaeus atricilla",
    "05770": "Leucophaeus pipixcan",
    "05780": "Hydrocoloeus minutus",
    "05790": "Xema sabini",
    "05800": "Saundersilarus saundersi",
    "05810": "Chroicocephalus philadelphia",
    "05820": "Chroicocephalus ridibundus",
    "05830": "Chroicocephalus brunnicephalus",
    "05840": "Chroicocephalus cirrocephalus",
    "05850": "Chroicocephalus genei",
    "05860": "Larus heermanni",
    "05870": "Larus crassirostris",
    "05880": "Ichthyaetus audouinii",
    "05890": "Larus delawarensis",
    "05900": "Larus canus",
    "05910": "Larus fuscus",
    "05920": "Larus argentatus sensu lato",
    "05924": "Larus vegae",
    "05926": "Larus michahellis",
    "05927": "Larus cachinnans",
    "05929": "Larus argentatus/cachinnans/michahellis",
    "05930": "Larus californicus",
    "05940": "Larus occidentalis",
    "05950": "Larus schistisagus",
    "05960": "Larus glaucescens",
    "05980": "Larus glaucoides",
    "05990": "Larus hyperboreus",
    "06000": "Larus marinus",
    "06009": "Laridae sp.",
    "06010": "Rhodostethia rosea",
    "06020": "Rissa tridactyla",
    "06030": "Rissa brevirostris",
    "06040": "Pagophila eburnea",
    "06050": "Gelochelidon nilotica",
    "06060": "Hydroprogne caspia",
    "06070": "Thalasseus maximus",
    "06080": "Thalasseus bergii",
    "06090": "Thalasseus bengalensis",
    "06100": "Thalasseus bernsteini",
    "06110": "Thalasseus sandvicensis",
    "06111": "Thalasseus acuflavidus",
    "06120": "Thalasseus elegans",
    "06130": "Sterna sumatrana",
    "06140": "Sterna dougallii",
    "06150": "Sterna hirundo",
    "06159": "Sterna hirundo/paradisaea",
    "06160": "Sterna paradisaea",
    "06170": "Onychoprion aleuticus",
    "06180": "Sterna forsteri",
    "06190": "Sterna trudeaui",
    "06200": "Sterna repressa",
    "06210": "Onychoprion lunatus",
    "06220": "Onychoprion anaethetus",
    "06230": "Onychoprion fuscatus",
    "06240": "Sternula albifrons",
    "06250": "Sternula saundersi",
    "06259": "Sterninae sp.",
    "06260": "Chlidonias hybrida",
    "06270": "Chlidonias niger",
    "06280": "Chlidonias leucopterus",
    "06289": "Chlidonias sp.",
    "06290": "Anous tenuirostris",
    "06300": "Anous stolidus",
    "06310": "Gygis alba",
    "06320": "Rynchops niger",
    "06330": "Rynchops flavirostris",
    "06340": "Uria aalge",
    "06350": "Uria lomvia",
    "06359": "Uria sp.",
    "06360": "Alca torda",
    "06370": "Pinguinus impennis",
    "06380": "Cepphus grylle",
    "06390": "Cepphus columba",
    "06400": "Cepphus carbo",
    "06409": "Cepphus sp.",
    "06410": "Brachyramphus marmoratus sensu lato",
    "06411": "Brachyramphus marmoratus",
    "06412": "Brachyramphus perdix",
    "06420": "Brachyramphus brevirostris",
    "06429": "Brachyramphus sp.",
    "06430": "Synthliboramphus hypoleucus",
    "06440": "Synthliboramphus craveri",
    "06450": "Synthliboramphus antiquus",
    "06460": "Synthliboramphus wumizusume",
    "06470": "Alle alle",
    "06480": "Ptychoramphus aleuticus",
    "06490": "Aethia cristatella",
    "06500": "Aethia pygmaea",
    "06510": "Aethia pusilla",
    "06520": "Aethia psittacula",
    "06530": "Cerorhinca monocerata",
    "06540": "Fratercula arctica",
    "06550": "Fratercula corniculata",
    "06560": "Fratercula cirrhata",
    "06570": "Pterocles lichtensteinii",
    "06580": "Pterocles coronatus",
    "06590": "Pterocles senegallus",
    "06600": "Pterocles exustus",
    "06610": "Pterocles orientalis",
    "06620": "Pterocles alchata",
    "06630": "Syrrhaptes paradoxus",
    "06640": "Syrrhaptes tibetanus",
    "06650": "Columba livia",
    "06657": "Columba livia var. domestica",
    "06660": "Columba rupestris",
    "06670": "Columba leuconota",
    "06680": "Columba oenas",
    "06690": "Columba eversmanni",
    "06700": "Columba palumbus",
    "06710": "Columba trocaz",
    "06720": "Columba bollii",
    "06730": "Columba junoniae",
    "06740": "Columba hodgsonii",
    "06750": "Columba pulchricollis",
    "06760": "Columba janthina",
    "06770": "Columba versicolor",
    "06780": "Columba jouyi",
    "06790": "Patagioenas leucocephala",
    "06800": "Patagioenas squamosa",
    "06810": "Patagioenas fasciata",
    "06820": "Patagioenas flavirostris",
    "06829": "Columbiformes sp.",
    "06830": "Streptopelia roseogrisea",
    "06831": "Streptopelia roseogrisea var. risoria",
    "06840": "Streptopelia decaocto",
    "06850": "Streptopelia semitorquata",
    "06860": "Streptopelia tranquebarica",
    "06870": "Streptopelia turtur",
    "06880": "Streptopelia lugens",
    "06890": "Streptopelia orientalis",
    "06900": "Spilopelia senegalensis",
    "06910": "Spilopelia chinensis",
    "06919": "Streptopelia sp.",
    "06920": "Oena capensis",
    "06930": "Chalcophaps indica",
    "06940": "Ectopistes migratorius",
    "06950": "Zenaida macroura",
    "06960": "Zenaida aurita",
    "06970": "Zenaida asiatica",
    "06980": "Columbina passerina",
    "06990": "Columbina squammata",
    "07000": "Leptotila verreauxi",
    "07010": "Geotrygon chrysia",
    "07020": "Geotrygon montana",
    "07030": "Treron waalia",
    "07040": "Treron sphenurus",
    "07050": "Treron sieboldii",
    "07060": "Treron formosae",
    "07070": "Psittacara holochlorus",
    "07080": "Conuropsis carolinensis",
    "07090": "Rhynchopsitta pachyrhyncha",
    "07100": "Rhynchopsitta terrisi",
    "07110": "Amazona leucocephala",
    "07120": "Psittacula krameri",
    "07130": "Psittacula derbiana",
    "07140": "Psittacula himalayana",
    "07150": "Clamator jacobinus",
    "07160": "Clamator glandarius",
    "07170": "Hierococcyx fugax",
    "07180": "Hierococcyx sparverioides",
    "07190": "Chrysococcyx maculatus",
    "07200": "Chrysococcyx caprius",
    "07210": "Chrysococcyx klaas",
    "07220": "Cacomantis merulinus",
    "07230": "Cuculus micropterus",
    "07240": "Cuculus canorus",
    "07250": "Cuculus saturatus",
    "07260": "Cuculus poliocephalus",
    "07270": "Coccyzus erythropthalmus",
    "07280": "Coccyzus americanus",
    "07290": "Coccyzus minor",
    "07300": "Coccyzus merlini",
    "07310": "Crotophaga ani",
    "07320": "Crotophaga sulcirostris",
    "07330": "Geococcyx californianus",
    "07340": "Centropus senegalensis",
    "07350": "Tyto alba",
    "07360": "Otus bakkamoena",
    "07370": "Otus sunia",
    "07380": "Otus brucei",
    "07390": "Otus scops",
    "07400": "Psiloscops flammeolus",
    "07410": "Megascops asio",
    "07420": "Megascops trichopsis",
    "07430": "Bubo virginianus",
    "07440": "Bubo bubo",
    "07441": "Bubo ascalaphus",
    "07450": "Bubo africanus",
    "07460": "Ketupa blakistoni",
    "07470": "Ketupa zeylonensis",
    "07480": "Ketupa flavipes",
    "07490": "Bubo scandiacus",
    "07500": "Surnia ulula",
    "07510": "Glaucidium passerinum",
    "07520": "Glaucidium gnoma",
    "07530": "Glaucidium brasilianum",
    "07540": "Taenioptynx brodiei",
    "07550": "Micrathene whitneyi",
    "07560": "Ninox scutulata",
    "07570": "Athene noctua",
    "07580": "Athene brama",
    "07590": "Athene cunicularia",
    "07600": "Strix leptogrammica",
    "07610": "Strix aluco",
    "07620": "Strix butleri",
    "07621": "Strix hadorami",
    "07630": "Strix varia",
    "07640": "Strix occidentalis",
    "07650": "Strix uralensis",
    "07660": "Strix nebulosa",
    "07669": "Strix sp.",
    "07670": "Asio otus",
    "07680": "Asio flammeus",
    "07690": "Asio capensis",
    "07700": "Aegolius funereus",
    "07710": "Aegolius acadicus",
    "07719": "Strigidae",
    "07720": "Caprimulgus inornatus",
    "07730": "Caprimulgus nubicus",
    "07750": "Caprimulgus mahrattensis",
    "07760": "Caprimulgus asiaticus",
    "07770": "Caprimulgus indicus",
    "07780": "Caprimulgus europaeus",
    "07790": "Caprimulgus ruficollis",
    "07800": "Caprimulgus eximius",
    "07810": "Caprimulgus aegyptius",
    "07820": "Antrostomus carolinensis",
    "07830": "Antrostomus vociferus",
    "07839": "Caprimulgidae sp.",
    "07840": "Phalaenoptilus nuttallii",
    "07850": "Nyctidromus albicollis",
    "07860": "Chordeiles minor",
    "07870": "Chordeiles acutipennis",
    "07880": "Cypseloides niger",
    "07890": "Aerodramus brevirostris",
    "07900": "Chaetura pelagica",
    "07910": "Chaetura vauxi",
    "07920": "Hirundapus caudacutus",
    "07930": "Apus alexandri",
    "07940": "Apus unicolor",
    "07950": "Apus apus",
    "07960": "Apus pallidus",
    "07970": "Apus pacificus",
    "07980": "Tachymarptis melba",
    "07990": "Apus caffer",
    "08000": "Apus affinis",
    "08009": "Apus sp.",
    "08010": "Aeronautes saxatalis",
    "08020": "Cypsiurus parvus",
    "08030": "Riccordia ricordii",
    "08040": "Cynanthus latirostris",
    "08050": "Basilinna xantusii",
    "08060": "Basilinna leucotis",
    "08070": "Saucerottia beryllina",
    "08080": "Amazilia yucatanensis",
    "08090": "Amazilia tzacatl",
    "08100": "Ramosomyia violiceps",
    "08110": "Lampornis clemenciae",
    "08120": "Eugenes fulgens",
    "08130": "Nesophlox evelynae",
    "08140": "Calothorax lucifer",
    "08150": "Archilochus colubris",
    "08160": "Archilochus alexandri",
    "08170": "Calypte costae",
    "08180": "Calypte anna",
    "08190": "Selasphorus calliope",
    "08200": "Selasphorus heloisa",
    "08210": "Selasphorus platycercus",
    "08220": "Selasphorus rufus",
    "08230": "Selasphorus sasin",
    "08240": "Trogon mexicanus",
    "08250": "Trogon elegans",
    "08260": "Halcyon coromanda",
    "08270": "Halcyon smyrnensis",
    "08280": "Halcyon pileata",
    "08290": "Halcyon leucocephala",
    "08300": "Todiramphus cinnamominus",
    "08310": "Alcedo atthis",
    "08320": "Chloroceryle americana",
    "08330": "Ceryle rudis",
    "08340": "Megaceryle alcyon",
    "08350": "Megaceryle torquata",
    "08360": "Megaceryle lugubris",
    "08370": "Merops albicollis",
    "08380": "Merops orientalis sensu lato",
    "08381": "Merops cyanophrys",
    "08390": "Merops superciliosus sensu lato",
    "08391": "Merops superciliosus",
    "08400": "Merops apiaster",
    "08410": "Coracias garrulus",
    "08420": "Coracias abyssinicus",
    "08430": "Coracias benghalensis",
    "08440": "Eurystomus glaucurus",
    "08450": "Eurystomus orientalis",
    "08460": "Upupa epops",
    "08468": "Upupa marginata",
    "08470": "Lophoceros nasutus",
    "08480": "Jynx torquilla",
    "08490": "Picumnus innominatus",
    "08500": "Colaptes auratus",
    "08520": "Colaptes chrysoides",
    "08530": "Picus chlorolophus",
    "08540": "Chrysophlegma flavinucha",
    "08550": "Picus canus",
    "08560": "Picus viridis sensu lato",
    "08561": "Picus viridis",
    "08562": "Picus sharpei",
    "08570": "Picus vaillantii",
    "08580": "Picus awokera",
    "08590": "Picus squamatus",
    "08600": "Dendrocopos noguchii",
    "08610": "Dinopium benghalense",
    "08620": "Dryocopus pileatus",
    "08630": "Dryocopus martius",
    "08640": "Dryocopus javensis",
    "08650": "Melanerpes carolinus",
    "08660": "Melanerpes aurifrons",
    "08670": "Melanerpes uropygialis",
    "08680": "Melanerpes superciliaris",
    "08690": "Melanerpes erythrocephalus",
    "08700": "Melanerpes formicivorus",
    "08710": "Melanerpes lewis",
    "08720": "Sphyrapicus varius",
    "08730": "Sphyrapicus nuchalis",
    "08740": "Sphyrapicus ruber",
    "08750": "Sphyrapicus thyroideus",
    "08760": "Dendrocopos major",
    "08770": "Dendrocopos leucopterus",
    "08780": "Dendrocopos syriacus",
    "08790": "Dendrocopos assimilis",
    "08800": "Dendrocopos himalayensis",
    "08810": "Dendrocopos darjellensis",
    "08820": "Dryobates cathpharius",
    "08830": "Dendrocoptes medius",
    "08840": "Dendrocopos leucotos",
    "08850": "Dendrocopos hyperythrus",
    "08860": "Dendrocoptes auriceps",
    "08870": "Dryobates minor",
    "08880": "Yungipicus canicapillus",
    "08890": "Yungipicus kizuki",
    "08900": "Dendrocoptes dorae",
    "08910": "Dryobates scalaris",
    "08920": "Dryobates nuttallii",
    "08930": "Dryobates pubescens",
    "08940": "Leuconotopicus borealis",
    "08950": "Leuconotopicus arizonae",
    "08960": "Leuconotopicus villosus",
    "08970": "Leuconotopicus albolarvatus",
    "08979": "Dendrocopos sp.",
    "08980": "Picoides tridactylus",
    "08990": "Picoides arcticus",
    "09000": "Campephilus principalis",
    "09010": "Campephilus imperialis",
    "09020": "Xiphorhynchus flavigaster",
    "09030": "Lepidocolaptes leucogaster",
    "09040": "Pachyramphus aglaiae",
    "09050": "Tityra semifasciata",
    "09060": "Myiopagis viridicata",
    "09070": "Elaenia martinica",
    "09080": "Camptostoma imberbe",
    "09090": "Sayornis phoebe",
    "09100": "Sayornis nigricans",
    "09110": "Sayornis saya",
    "09120": "Pyrocephalus rubinus",
    "09130": "Empidonax flaviventris",
    "09140": "Empidonax virescens",
    "09150": "Empidonax minimus",
    "09160": "Empidonax hammondii",
    "09170": "Empidonax oberholseri",
    "09180": "Empidonax wrightii",
    "09190": "Empidonax affinis",
    "09200": "Empidonax difficilis",
    "09210": "Empidonax albigularis",
    "09220": "Empidonax traillii",
    "09230": "Empidonax alnorum",
    "09240": "Empidonax fulvifrons",
    "09250": "Xenotriccus mexicanus",
    "09260": "Mitrephanes phaeocercus",
    "09270": "Contopus caribaeus",
    "09280": "Contopus pertinax",
    "09290": "Contopus sordidulus",
    "09300": "Contopus virens",
    "09310": "Contopus cooperi",
    "09320": "Myiarchus tuberculifer",
    "09330": "Myiarchus nuttingi",
    "09340": "Myiarchus cinerascens",
    "09350": "Myiarchus stolidus",
    "09360": "Myiarchus tyrannulus",
    "09370": "Myiarchus crinitus",
    "09380": "Myiodynastes luteiventris",
    "09390": "Myiozetetes similis",
    "09400": "Pitangus sulphuratus",
    "09410": "Tyrannus vociferans",
    "09420": "Tyrannus verticalis",
    "09430": "Tyrannus crassirostris",
    "09440": "Tyrannus couchii",
    "09450": "Tyrannus dominicensis",
    "09460": "Tyrannus cubensis",
    "09470": "Tyrannus caudifasciatus",
    "09480": "Tyrannus tyrannus",
    "09500": "Tyrannus forficatus",
    "09510": "Pitta brachyura",
    "09520": "Mirafra javanica cantillans",
    "09521": "Mirafra javanica",
    "09530": "Eremopterix nigriceps",
    "09540": "Eremalauda dunni",
    "09550": "Ammomanes cinctura",
    "09560": "Ammomanes phoenicura",
    "09570": "Ammomanes deserti",
    "09580": "Alaemon alaudipes",
    "09590": "Chersophilus duponti",
    "09600": "Ramphocoris clotbey",
    "09610": "Melanocorypha calandra",
    "09620": "Melanocorypha bimaculata",
    "09630": "Melanocorypha maxima",
    "09640": "Melanocorypha mongolica",
    "09650": "Alauda leucoptera",
    "09660": "Melanocorypha yeltoniensis",
    "09670": "Calandrella cinerea",
    "09680": "Calandrella brachydactyla",
    "09690": "Calandrella acutirostris",
    "09691": "Calandrella eremica",
    "09700": "Alaudala rufescens s. lato",
    "09702": "Alaudala cheleensis",
    "09703": "Alaudala rufescens",
    "09710": "Alaudala raytal",
    "09720": "Galerida cristata",
    "09730": "Galerida theklae",
    "09739": "Galerida sp.",
    "09740": "Lullula arborea",
    "09750": "Alauda gulgula",
    "09760": "Alauda arvensis",
    "09770": "Alauda razae",
    "09780": "Eremophila alpestris",
    "09790": "Eremophila bilopha",
    "09799": "Alaudidae sp.",
    "09800": "Riparia paludicola",
    "09810": "Riparia riparia",
    "09813": "Riparia diluta",
    "09820": "Stelgidopteryx ruficollis",
    "09830": "Tachycineta bicolor",
    "09840": "Tachycineta albilinea",
    "09850": "Tachycineta thalassina",
    "09860": "Tachycineta cyaneoviridis",
    "09870": "Progne chalybea",
    "09880": "Progne dominicensis",
    "09890": "Progne subis",
    "09900": "Ptyonopogne fuligula sensu lato",
    "09901": "Ptyonoprogne obsoleta",
    "09910": "Ptyonoprogne rupestris",
    "09920": "Hirundo rustica",
    "09930": "Hirundo tahitica",
    "09940": "Hirundo smithii",
    "09950": "Cecropis rufula",
    "09951": "Cecropis daurica",
    "09953": "Cecropis melanocrissus",
    "09960": "Petrochelidon fluvicola",
    "09970": "Petrochelidon fulva",
    "09980": "Petrochelidon pyrrhonota",
    "09990": "Delichon nipalense",
    "10000": "Delichon dasypus",
    "10010": "Delichon urbicum",
    "10019": "Hirundinidae sp.",
    "10020": "Anthus richardi",
    "10030": "Anthus sylvanus",
    "10040": "Anthus godlewskii",
    "10050": "Anthus campestris",
    "10060": "Anthus berthelotii",
    "10070": "Anthus similis",
    "10080": "Anthus hodgsoni",
    "10090": "Anthus trivialis",
    "10100": "Anthus gustavi",
    "10110": "Anthus pratensis",
    "10120": "Anthus cervinus",
    "10130": "Anthus roseatus",
    "10140": "Anthus petrosus/spinoletta",
    "10141": "Anthus spinoletta",
    "10144": "Anthus rubescens",
    "10145": "Anthus petrosus",
    "10146": "Anthus japonicus",
    "10150": "Anthus spragueii",
    "10159": "Anthus sp.",
    "10160": "Dendronanthus indicus",
    "10170": "Motacilla flava",
    "10180": "Motacilla citreola",
    "10190": "Motacilla cinerea",
    "10200": "Motacilla alba",
    "10210": "Motacilla grandis",
    "10220": "Motacilla maderaspatensis",
    "10230": "Motacilla aguimp",
    "10239": "Motacilla sp.",
    "10240": "Tephrodornis pondicerianus",
    "10250": "Lalage melaschistos",
    "10260": "Pericrocotus ethologus",
    "10270": "Pericrocotus cinnamomeus",
    "10280": "Pericrocotus roseus",
    "10290": "Pericrocotus divaricatus",
    "10300": "Pericrocotus tegimae",
    "10310": "Spizixos canifrons",
    "10320": "Spizixos semitorques",
    "10330": "Pycnonotus xanthorrhous",
    "10340": "Pycnonotus sinensis",
    "10350": "Pycnonotus leucogenys",
    "10360": "Pycnonotus xanthopygos",
    "10370": "Pycnonotus barbatus",
    "10380": "Ixos mcclellandii",
    "10390": "Hypsipetes amaurotis",
    "10400": "Hypsipetes madagascariensis",
    "10410": "Chloropsis hardwickii",
    "10420": "Myadestes townsendi",
    "10430": "Myadestes obscurus",
    "10440": "Phainopepla nitens",
    "10450": "Ptiliogonys cinereus",
    "10460": "Bombycilla cedrorum",
    "10470": "Bombycilla japonica",
    "10480": "Bombycilla garrulus",
    "10490": "Hypocolius ampelinus",
    "10500": "Cinclus cinclus",
    "10510": "Cinclus pallasii",
    "10520": "Cinclus mexicanus",
    "10530": "Campylorhynchus jocosus",
    "10540": "Campylorhynchus gularis",
    "10550": "Campylorhynchus brunneicapillus",
    "10560": "Salpinctes obsoletus",
    "10570": "Catherpes mexicanus",
    "10580": "Cistothorus platensis sensu lato",
    "10581": "Cistothorus platensis",
    "10582": "Cistothorus stellaris",
    "10590": "Cistothorus palustris",
    "10600": "Thryomanes bewickii",
    "10610": "Pheugopedius felix",
    "10620": "Pheugopedius maculipectus",
    "10630": "Thryothorus ludovicianus",
    "10640": "Thryophilus sinaloa",
    "10650": "Troglodytes aedon sensu lato",
    "10651": "Troglodytes aedon",
    "10660": "Troglodytes troglodytes",
    "10670": "Mimus polyglottos",
    "10680": "Mimus gundlachii",
    "10690": "Toxostoma rufum",
    "10700": "Toxostoma longirostre",
    "10710": "Toxostoma bendirei",
    "10720": "Toxostoma cinereum",
    "10730": "Toxostoma ocellatum",
    "10740": "Toxostoma curvirostre",
    "10750": "Toxostoma lecontei",
    "10760": "Toxostoma crissale",
    "10770": "Toxostoma redivivum",
    "10780": "Oreoscoptes montanus",
    "10790": "Margarops fuscatus",
    "10800": "Dumetella carolinensis",
    "10810": "Melanotis caerulescens",
    "10820": "Prunella immaculata",
    "10830": "Prunella rubida",
    "10840": "Prunella modularis",
    "10850": "Prunella strophiata",
    "10860": "Prunella montanella",
    "10870": "Prunella fulvescens",
    "10881": "Prunella ocularis",
    "10900": "Prunella atrogularis",
    "10910": "Prunella koslowi",
    "10920": "Prunella rubeculoides",
    "10930": "Prunella himalayana",
    "10940": "Prunella collaris",
    "10949": "Prunella sp.",
    "10950": "Cercotrichas galactotes",
    "10960": "Cercotrichas podobe",
    "10970": "Heteroxenicus stellatus",
    "10980": "Brachypteryx montana",
    "10990": "Erithacus rubecula",
    "11000": "Larvivora akahige",
    "11010": "Larvivora komadori",
    "11020": "Larvivora sibilans",
    "11030": "Luscinia luscinia",
    "11040": "Luscinia megarhynchos",
    "11050": "Calliope calliope",
    "11060": "Luscinia svecica",
    "11070": "Calliope pectoralis",
    "11080": "Larvivora ruficeps",
    "11090": "Calliope obscura",
    "11100": "Calliope pectardens",
    "11110": "Larvivora brunnea",
    "11120": "Larvivora cyane",
    "11129": "Luscinia sp.",
    "11130": "Tarsiger cyanurus",
    "11140": "Tarsiger chrysaeus",
    "11150": "Tarsiger indicus",
    "11160": "Tarsiger hyperythrus",
    "11170": "Irania gutturalis",
    "11180": "Phoenicurus erythronotus",
    "11190": "Phoenicurus alaschanicus",
    "11200": "Phoenicurus coeruleocephala",
    "11210": "Phoenicurus ochruros",
    "11220": "Phoenicurus phoenicurus",
    "11230": "Phoenicurus hodgsoni",
    "11240": "Phoenicurus frontalis",
    "11250": "Phoenicurus schisticeps",
    "11260": "Phoenicurus auroreus",
    "11270": "Phoenicurus moussieri",
    "11280": "Phoenicurus erythrogastrus",
    "11289": "Phoenicurus sp.",
    "11290": "Phoenicurus fuliginosus",
    "11300": "Luscinia phaenicuroides",
    "11310": "Grandala coelicolor",
    "11320": "Sialia currucoides",
    "11330": "Sialia mexicana",
    "11340": "Sialia sialis",
    "11350": "Oenanthe melanura",
    "11360": "Saxicola macrorhynchus",
    "11370": "Saxicola rubetra",
    "11380": "Saxicola dacotiae",
    "11390": "Saxicola torquatus sensu lato",
    "11391": "Saxicola torquatus",
    "11392": "Saxicola stejnegeri",
    "11394": "Saxicola maurus",
    "11397": "Saxicola rubicola",
    "11400": "Saxicola insignis",
    "11410": "Saxicola caprata",
    "11420": "Saxicola ferreus",
    "11429": "Saxicola sp.",
    "11430": "Myrmecocichla aethiops",
    "11440": "Oenanthe isabellina",
    "11450": "Oenanthe bottae",
    "11460": "Oenanthe oenanthe",
    "11463": "Oenanthe seebohmi",
    "11470": "Oenanthe pleschanka",
    "11471": "Oenanthe cypriaca",
    "11480": "Oenanthe hispanica sensu lato",
    "11481": "Oenanthe hispanica",
    "11482": "Oenanthe melanoleuca",
    "11490": "Oenanthe deserti",
    "11500": "Oenanthe finschii",
    "11510": "Oenanthe moesta",
    "11520": "Oenanthe xanthoprymna",
    "11521": "Oenanthe chrysopygia",
    "11530": "Oenanthe picata",
    "11540": "Oenanthe lugens",
    "11541": "Oenanthe lugentoides",
    "11542": "Oenanthe lugubris",
    "11550": "Oenanthe monacha",
    "11560": "Oenanthe albonigra",
    "11570": "Oenanthe leucopyga",
    "11580": "Oenanthe leucura",
    "11589": "Oenanthe sp.",
    "11590": "Phoenicurus leucocephalus",
    "11600": "Copsychus fulicatus",
    "11610": "Monticola rufocinereus",
    "11620": "Monticola saxatilis",
    "11630": "Monticola cinclorhyncha",
    "11640": "Monticola gularis",
    "11650": "Monticola rufiventris",
    "11660": "Monticola solitarius",
    "11670": "Myophonus caeruleus",
    "11680": "Zoothera mollissima",
    "11690": "Zoothera dixoni",
    "11700": "Zoothera aurea",
    "11710": "Geokichla sibirica",
    "11720": "Ixoreus naevius",
    "11730": "Ridgwayia pinicola",
    "11740": "Zoothera terrestris",
    "11750": "Hylocichla mustelina",
    "11760": "Catharus guttatus",
    "11770": "Catharus ustulatus",
    "11780": "Catharus minimus sensu lato",
    "11781": "Catharus minimus",
    "11782": "Catharus bicknelli",
    "11790": "Catharus fuscescens",
    "11800": "Catharus aurantiirostris",
    "11810": "Catharus occidentalis",
    "11820": "Turdus menachensis",
    "11830": "Turdus unicolor",
    "11840": "Turdus cardis",
    "11850": "Turdus albocinctus",
    "11860": "Turdus torquatus",
    "11870": "Turdus merula",
    "11880": "Turdus rubrocanus",
    "11890": "Turdus kessleri",
    "11900": "Turdus chrysolaus",
    "11910": "Turdus celaenops",
    "11920": "Turdus feae",
    "11930": "Turdus hortulorum",
    "11940": "Turdus pallidus",
    "11950": "Turdus obscurus",
    "11960": "Turdus naumanni sensu lato",
    "11961": "Turdus naumanni",
    "11962": "Turdus eunomus",
    "11970": "Turdus ruficollis sensu lato",
    "11971": "Turdus ruficollis",
    "11972": "Turdus atrogularis",
    "11980": "Turdus pilaris",
    "11990": "Turdus mupinensis",
    "12000": "Turdus philomelos",
    "12010": "Turdus iliacus",
    "12020": "Turdus viscivorus",
    "12030": "Turdus migratorius",
    "12040": "Turdus rufopalliatus",
    "12050": "Turdus grayi",
    "12060": "Turdus albicollis",
    "12069": "Turdus sp.",
    "12070": "Turdus plumbeus",
    "12080": "Enicurus scouleri",
    "12090": "Enicurus schistaceus",
    "12100": "Enicurus leschenaulti",
    "12110": "Enicurus maculatus",
    "12120": "Cettia castaneocoronata",
    "12130": "Urosphena squameiceps",
    "12140": "Horornis diphone",
    "12150": "Horornis fortipes",
    "12160": "Cettia major",
    "12170": "Horornis flavolivaceus",
    "12180": "Horornis acanthizoides",
    "12190": "Cettia brunnifrons",
    "12200": "Cettia cetti",
    "12210": "Locustella thoracica",
    "12220": "Locustella major",
    "12230": "Locustella tacsanowskia",
    "12240": "Locustella luteoventris",
    "12250": "Curruca buryi",
    "12260": "Cisticola juncidis",
    "12270": "Prinia gracilis",
    "12280": "Prinia inornata",
    "12290": "Prinia crinigera",
    "12300": "Prinia atrogularis",
    "12310": "Scotocerca inquieta",
    "12320": "Rhopophilus pekinensis",
    "12330": "Helopsaltes certhiola",
    "12340": "Helopsaltes ochotensis",
    "12350": "Locustella lanceolata",
    "12360": "Locustella naevia",
    "12370": "Locustella fluviatilis",
    "12380": "Locustella luscinioides",
    "12390": "Helopsaltes fasciolatus",
    "12399": "Locustella/Helopsaltes sp.",
    "12400": "Helopsaltes pryeri",
    "12410": "Acrocephalus melanopogon",
    "12420": "Acrocephalus paludicola",
    "12430": "Acrocephalus schoenobaenus",
    "12440": "Acrocephalus sorghophilus",
    "12450": "Acrocephalus bistrigiceps",
    "12460": "Acrocephalus concinens",
    "12470": "Acrocephalus agricola",
    "12480": "Acrocephalus dumetorum",
    "12490": "Acrocephalus brevipennis",
    "12500": "Acrocephalus palustris",
    "12510": "Acrocephalus scirpaceus",
    "12520": "Acrocephalus stentoreus",
    "12530": "Acrocephalus arundinaceus",
    "12532": "Acrocephalus griseldis",
    "12540": "Arundinax aedon",
    "12549": "Acrocephalus sp.",
    "12550": "Iduna pallida",
    "12552": "Iduna opaca",
    "12560": "Iduna caligata sensu lato",
    "12561": "Iduna caligata",
    "12562": "Iduna rama",
    "12570": "Hippolais languida",
    "12580": "Hippolais olivetorum",
    "12590": "Hippolais icterina",
    "12600": "Hippolais polyglotta",
    "12609": "Hippolais/Iduna sp.",
    "12610": "Curruca sarda sensu lato",
    "12611": "Curruca sarda",
    "12612": "Curruca balearica",
    "12620": "Curruca undata",
    "12630": "Curruca deserticola",
    "12640": "Curruca conspicillata",
    "12650": "Curruca cantillans sensu lato",
    "12652": "Curruca subalpina",
    "12654": "Curruca iberiae",
    "12656": "Curruca cantillans",
    "12660": "Curruca mystacea",
    "12670": "Curruca melanocephala",
    "12680": "Curruca melanothorax",
    "12690": "Curruca ruppeli",
    "12700": "Curruca nana sensu lato",
    "12701": "Curruca deserti",
    "12702": "Curruca nana",
    "12710": "Curruca leucomelaena",
    "12720": "Curruca hortensis sensu lato",
    "12721": "Curruca hortensis",
    "12725": "Curruca crassirostris",
    "12730": "Curruca nisoria",
    "12740": "Curruca curruca",
    "12750": "Curruca communis",
    "12760": "Sylvia borin",
    "12770": "Sylvia atricapilla",
    "12779": "Sylvia/Curruca sp.",
    "12780": "Phylloscopus burkii",
    "12790": "Abroscopus albogularis",
    "12800": "Abroscopus schisticeps",
    "12810": "Phylloscopus umbrovirens",
    "12820": "Phylloscopus ricketti",
    "12830": "Phylloscopus cantator",
    "12840": "Phylloscopus intensior",
    "12850": "Phylloscopus reguloides",
    "12860": "Phylloscopus coronatus",
    "12870": "Phylloscopus occipitalis",
    "12880": "Phylloscopus tenellipes",
    "12890": "Phylloscopus ijimae",
    "12900": "Phylloscopus tytleri",
    "12910": "Phylloscopus nitidus",
    "12920": "Phylloscopus plumbeitarsus",
    "12930": "Phylloscopus trochiloides",
    "12940": "Phylloscopus magnirostris",
    "12950": "Phylloscopus borealis",
    "12960": "Phylloscopus pulcher",
    "12970": "Phylloscopus maculipennis",
    "12980": "Phylloscopus proregulus",
    "12990": "Phylloscopus subviridis",
    "13000": "Phylloscopus inornatus sensu lato",
    "13001": "Phylloscopus inornatus",
    "13002": "Phylloscopus humei",
    "13010": "Phylloscopus schwarzi",
    "13020": "Phylloscopus armandii",
    "13030": "Phylloscopus fuscatus",
    "13040": "Phylloscopus fuligiventer",
    "13050": "Phylloscopus griseolus",
    "13060": "Phylloscopus affinis",
    "13070": "Phylloscopus bonelli sensu lato",
    "13071": "Phylloscopus bonelli",
    "13072": "Phylloscopus orientalis",
    "13080": "Phylloscopus sibilatrix",
    "13090": "Phylloscopus neglectus",
    "13100": "Phylloscopus sindianus",
    "13110": "Phylloscopus collybita sensu lato",
    "13115": "Phylloscopus ibericus",
    "13117": "Phylloscopus canariensis",
    "13118": "Phylloscopus collybita",
    "13120": "Phylloscopus trochilus",
    "13129": "Phylloscopus sp.",
    "13130": "Corthylio calendula",
    "13140": "Regulus regulus",
    "13150": "Regulus ignicapilla",
    "13154": "Regulus madeirensis",
    "13160": "Regulus satrapa",
    "13169": "Regulus sp.",
    "13170": "Leptopoecile sophiae",
    "13180": "Leptopoecile elegans",
    "13190": "Polioptila melanura",
    "13200": "Polioptila nigriceps",
    "13210": "Polioptila caerulea",
    "13220": "Niltava grandis",
    "13230": "Niltava sundara",
    "13240": "Niltava davidi",
    "13250": "Niltava vivida",
    "13260": "Cyornis rubeculoides",
    "13270": "Cyanoptila cyanomelana",
    "13280": "Eumyias thalassinus",
    "13290": "Muscicapa ferruginea",
    "13300": "Muscicapa sibirica",
    "13310": "Muscicapa griseisticta",
    "13320": "Ficedula ruficauda",
    "13330": "Muscicapa muttui",
    "13340": "Muscicapa randi",
    "13350": "Muscicapa striata sensu lato",
    "13354": "Muscicapa striata",
    "13355": "Muscicapa tyrrhenica",
    "13360": "Muscicapa gambagae",
    "13369": "Muscicapidae",
    "13370": "Ficedula sapphira",
    "13380": "Ficedula tricolor",
    "13390": "Ficedula superciliaris",
    "13400": "Ficedula erithacus",
    "13410": "Ficedula hyperythra",
    "13420": "Ficedula strophiata",
    "13430": "Ficedula parva sensu lato",
    "13431": "Ficedula parva",
    "13432": "Ficedula albicilla",
    "13440": "Ficedula mugimaki",
    "13450": "Ficedula zanthopygia",
    "13460": "Ficedula narcissina",
    "13470": "Ficedula semitorquata",
    "13480": "Ficedula albicollis",
    "13490": "Ficedula hypoleuca",
    "13493": "Ficedula speculigera",
    "13499": "Ficedula sp.",
    "13500": "Culicicapa ceylonensis",
    "13510": "Chelidorhynx hypoxanthus",
    "13520": "Rhipidura albicollis",
    "13530": "Terpsiphone viridis",
    "13540": "Terpsiphone paradisi",
    "13550": "Terpsiphone atrocaudata",
    "13560": "Erythrogenys erythrogenys",
    "13570": "Pomatorhinus ruficollis",
    "13580": "Pnoepyga albiventer",
    "13590": "Pnoepyga pusilla",
    "13600": "Spelaeornis troglodytoides",
    "13610": "Cyanoderma ruficeps",
    "13620": "Moupinia poecilotis",
    "13630": "Chamaea fasciata",
    "13640": "Panurus biarmicus",
    "13650": "Paradoxornis aemodius",
    "13660": "Paradoxornis paradoxus",
    "13670": "Paradoxornis unicolor",
    "13680": "Paradoxornis flavirostris",
    "13690": "Suthora conspicillata",
    "13700": "Suthora webbiana",
    "13705": "Suthora alphonsiana",
    "13710": "Suthora zappeyi",
    "13720": "Suthora przewalskii",
    "13730": "Suthora fulvifrons",
    "13740": "Suthora nipalensis",
    "13750": "Suthora verreauxi",
    "13760": "Paradoxornis heudei",
    "13770": "Argya altirostris",
    "13780": "Argya caudata",
    "13790": "Argya squamiceps",
    "13800": "Argya fulva",
    "13810": "Pterorhinus lanceolatus",
    "13820": "Pterorhinus waddelli",
    "13830": "Pterorhinus koslowi",
    "13840": "Pterorhinus perspicillatus",
    "13850": "Pterorhinus albogularis",
    "13860": "Pterorhinus pectoralis",
    "13870": "Grammatoptila striata",
    "13880": "Garrulax maesi",
    "13890": "Trochalopteron variegatum",
    "13900": "Pterorhinus davidi",
    "13910": "Ianthocincla sukatschewi",
    "13920": "Ianthocincla cineracea",
    "13930": "Ianthocincla lunulata",
    "13940": "Ianthocincla maxima",
    "13950": "Ianthocincla ocellata",
    "13960": "Pterorhinus caerulatus",
    "13970": "Garrulax canorus",
    "13980": "Pterorhinus sannio",
    "13990": "Trochalopteron lineatum",
    "14000": "Trochalopteron subunicolor",
    "14010": "Trochalopteron elliotii",
    "14020": "Trochalopteron henrici",
    "14030": "Trochalopteron affine",
    "14040": "Trochalopteron erythrocephalum",
    "14050": "Trochalopteron formosum",
    "14060": "Liocichla steerii",
    "14070": "Leiothrix lutea",
    "14080": "Myzornis pyrrhoura",
    "14090": "Cutia nipalensis",
    "14100": "Pteruthius flaviscapis",
    "14110": "Pteruthius xanthochlorus",
    "14120": "Actinodura nipalensis",
    "14130": "Actinodura cyanouroptera",
    "14140": "Actinodura strigula",
    "14150": "Minla ignotincta",
    "14160": "Lioparus chrysotis",
    "14170": "Schoeniparus cinereus",
    "14180": "Schoeniparus castaneceps",
    "14190": "Fulvetta vinipectus",
    "14200": "Fulvetta striaticollis",
    "14210": "Fulvetta ruficapilla",
    "14220": "Fulvetta cinereiceps",
    "14230": "Schoeniparus brunneus",
    "14240": "Alcippe morrisonia",
    "14250": "Heterophasia capistrata",
    "14260": "Heterophasia pulchella",
    "14270": "Yuhina gularis",
    "14280": "Parayuhina diademata",
    "14290": "Yuhina occipitalis",
    "14300": "Yuhina nigrimenta",
    "14310": "Psaltriparus minimus",
    "14320": "Aegithalos fuliginosus",
    "14330": "Aegithalos iouschistos",
    "14340": "Aegithalos niveogularis",
    "14350": "Aegithalos leucogenys",
    "14360": "Aegithalos concinnus",
    "14370": "Aegithalos caudatus",
    "14380": "Sylviparus modestus",
    "14390": "Poecile superciliosus",
    "14400": "Poecile palustris",
    "14409": "Poecile sp.",
    "14410": "Poecile lugubris",
    "14420": "Poecile montanus",
    "14430": "Poecile atricapillus",
    "14440": "Poecile carolinensis",
    "14450": "Poecile sclateri",
    "14460": "Poecile gambeli",
    "14470": "Baeolophus wollweberi",
    "14480": "Poecile cinctus",
    "14490": "Poecile hudsonicus",
    "14500": "Poecile rufescens",
    "14510": "Baeolophus bicolor",
    "14520": "Baeolophus inornatus",
    "14530": "Lophophanes dichrous",
    "14540": "Lophophanes cristatus",
    "14550": "Poecile davidi",
    "14560": "Pardaliparus venustulus",
    "14570": "Sittiparus varius",
    "14580": "Periparus rufonuchalis",
    "14590": "Periparus rubidiventris",
    "14610": "Periparus ater",
    "14620": "Cyanistes caeruleus",
    "14625": "Cyanistes teneriffae",
    "14630": "Cyanistes cyanus",
    "14640": "Parus major",
    "14660": "Parus monticolus",
    "14669": "Paridae sp.",
    "14670": "Sitta yunnanensis",
    "14680": "Sitta villosa",
    "14690": "Sitta krueperi",
    "14700": "Sitta whiteheadi",
    "14710": "Sitta ledanti",
    "14720": "Sitta canadensis",
    "14730": "Sitta pygmaea",
    "14740": "Sitta pusilla",
    "14750": "Sitta leucopsis",
    "14760": "Sitta carolinensis",
    "14770": "Sitta himalayensis",
    "14780": "Sitta castanea",
    "14790": "Sitta europaea",
    "14800": "Sitta tephronota",
    "14810": "Sitta neumayer",
    "14820": "Tichodroma muraria",
    "14830": "Certhia discolor",
    "14840": "Certhia himalayana",
    "14850": "Certhia nipalensis",
    "14860": "Certhia familiaris",
    "14870": "Certhia brachydactyla",
    "14879": "Certhia sp.",
    "14880": "Cephalopyrus flammiceps",
    "14890": "Auriparus flaviceps",
    "14900": "Remiz pendulinus",
    "14902": "Remiz coronatus",
    "14903": "Remiz macronyx",
    "14910": "Hedydipna platura",
    "14920": "Hedydipna metallica",
    "14930": "Cinnyris asiaticus",
    "14940": "Cinnyris habessinicus",
    "14950": "Cinnyris osea",
    "14960": "Aethopyga gouldiae",
    "14970": "Aethopyga nipalensis",
    "14980": "Aethopyga ignicauda",
    "14990": "Pachyglossa melanozantha",
    "15000": "Dicaeum ignipectus",
    "15010": "Zosterops palpebrosus",
    "15020": "Zosterops erythropleurus",
    "15030": "Zosterops japonicus",
    "15040": "Zosterops abyssinicus",
    "15049": "Zosteropidae sp.",
    "15050": "Apalopteron familiare",
    "15060": "Oriolus traillii",
    "15070": "Oriolus chinensis",
    "15080": "Oriolus oriolus",
    "15090": "Tchagra senegalus",
    "15100": "Telophorus cruentus",
    "15110": "Lanius tigrinus",
    "15120": "Lanius bucephalus",
    "15130": "Lanius cristatus",
    "15140": "Lanius isabellinus sensu lato",
    "15141": "Lanius isabellinus",
    "15150": "Lanius collurio",
    "15152": "Lanius phoenicuroides",
    "15160": "Lanius vittatus",
    "15170": "Lanius schach",
    "15180": "Lanius tephronotus",
    "15190": "Lanius minor",
    "15200": "Lanius excubitor",
    "15203": "Lanius meridionalis",
    "15210": "Lanius sphenocercus",
    "15220": "Lanius ludovicianus",
    "15230": "Lanius senator",
    "15240": "Lanius nubicus",
    "15249": "Lanius sp.",
    "15250": "Dicrurus macrocercus",
    "15260": "Dicrurus leucophaeus",
    "15270": "Dicrurus hottentottus",
    "15280": "Cyanocorax dickeyi",
    "15290": "Cyanocorax yncas",
    "15300": "Cyanocorax formosus",
    "15310": "Cyanocorax morio",
    "15320": "Cyanocorax sanblasianus",
    "15330": "Cyanocorax beecheii",
    "15340": "Cyanocitta stelleri",
    "15350": "Cyanocitta cristata",
    "15360": "Aphelocoma ultramarina",
    "15370": "Aphelocoma coerulescens",
    "15380": "Gymnorhinus cyanocephalus",
    "15390": "Garrulus glandarius",
    "15400": "Garrulus lanceolatus",
    "15410": "Garrulus lidthi",
    "15420": "Perisoreus canadensis",
    "15430": "Perisoreus infaustus",
    "15440": "Perisoreus internigrans",
    "15450": "Urocissa flavirostris",
    "15460": "Urocissa erythroryncha",
    "15470": "Cyanopica cooki",
    "15480": "Dendrocitta formosae",
    "15490": "Pica pica",
    "15493": "Pica mauritanica",
    "15500": "Pica nuttalli",
    "15510": "Podoces hendersoni",
    "15520": "Podoces biddulphi",
    "15530": "Podoces panderi",
    "15540": "Podoces pleskei",
    "15550": "Pseudopodoces humilis",
    "15560": "Nucifraga columbiana",
    "15570": "Nucifraga caryocatactes",
    "15580": "Pyrrhocorax graculus",
    "15590": "Pyrrhocorax pyrrhocorax",
    "15600": "Coloeus monedula",
    "15610": "Coloeus dauuricus",
    "15620": "Corvus splendens",
    "15630": "Corvus frugilegus",
    "15640": "Corvus brachyrhynchos",
    "15650": "Corvus imparatus",
    "15660": "Corvus ossifragus",
    "15670": "Corvus corone sensu lato",
    "15671": "Corvus corone",
    "15673": "Corvus cornix",
    "15680": "Corvus macrorhynchos",
    "15690": "Corvus torquatus",
    "15700": "Corvus albus",
    "15710": "Corvus ruficollis",
    "15720": "Corvus corax",
    "15730": "Corvus cryptoleucus",
    "15740": "Corvus rhipidurus",
    "15749": "Corvus sp.",
    "15750": "Onychognathus tristramii",
    "15760": "Cinnyricinclus leucogaster",
    "15770": "Sturnia pagodarum",
    "15780": "Spodiopsar sericeus",
    "15790": "Agropsar sturninus",
    "15800": "Agropsar philippensis",
    "15810": "Sturnia sinensis",
    "15820": "Sturnus vulgaris",
    "15830": "Sturnus unicolor",
    "15840": "Pastor roseus",
    "15850": "Spodiopsar cineraceus",
    "15859": "Sturnidae sp.",
    "15860": "Creatophora cinerea",
    "15870": "Acridotheres tristis",
    "15880": "Acridotheres ginginianus",
    "15890": "Acridotheres cristatellus",
    "15900": "Passer ammodendri",
    "15910": "Passer domesticus",
    "15912": "Passer italiae",
    "15919": "Passer domesticus/hispaniolensis",
    "15920": "Passer hispaniolensis",
    "15930": "Passer pyrrhonotus",
    "15940": "Passer cinnamomeus",
    "15950": "Passer moabiticus",
    "15960": "Passer iagoensis",
    "15970": "Passer simplex",
    "15980": "Passer montanus",
    "15990": "Passer luteus",
    "16000": "Passer euchlorus",
    "16009": "Passer sp.",
    "16010": "Carpospiza brachydactyla",
    "16020": "Gymnoris xanthocollis",
    "16030": "Gymnoris dentata",
    "16040": "Petronia petronia",
    "16050": "Pyrgilauda theresae",
    "16060": "Pyrgilauda blanfordi",
    "16070": "Pyrgilauda ruficollis",
    "16080": "Pyrgilauda davidiana",
    "16090": "Onychostruthus taczanowskii",
    "16100": "Montifringilla adamsi",
    "16110": "Montifringilla nivalis",
    "16120": "Ploceus galbula",
    "16130": "Lagonosticta senegala",
    "16140": "Uraeginthus bengalus",
    "16150": "Estrilda astrild",
    "16160": "Estrilda rufibarba",
    "16170": "Amandava subflava",
    "16180": "Euodice malabarica",
    "16190": "Euodice cantans",
    "16200": "Lonchura striata",
    "16210": "Vireo atricapilla",
    "16220": "Vireo pallens",
    "16230": "Vireo griseus",
    "16240": "Vireo crassirostris",
    "16250": "Vireo bellii",
    "16260": "Vireo vicinior",
    "16270": "Vireo solitarius",
    "16280": "Vireo flavifrons",
    "16290": "Vireo huttoni",
    "16300": "Vireo hypochryseus",
    "16310": "Vireo philadelphicus",
    "16320": "Vireo flavoviridis",
    "16330": "Vireo olivaceus",
    "16340": "Vireo altiloquus",
    "16350": "Vireo gilvus",
    "16360": "Fringilla coelebs",
    "16366": "Fringilla moreletti",
    "16367": "Fringilla spodiogenys",
    "16370": "Fringilla teydea sensu lato",
    "16371": "Fringilla teydea",
    "16372": "Fringilla polatzeki",
    "16380": "Fringilla montifringilla",
    "16389": "Fringilla sp.",
    "16390": "Serinus pusillus",
    "16400": "Serinus serinus",
    "16410": "Serinus syriacus",
    "16420": "Serinus canaria",
    "16430": "Spinus thibetanus",
    "16440": "Carduelis citrinella sensu lato",
    "16441": "Carduelis citrinella",
    "16442": "Carduelis corsicana",
    "16450": "Crithagra rothschildi",
    "16460": "Crithagra menachensis",
    "16470": "Rhynchostruthus socotranus",
    "16480": "Callacanthis burtoni",
    "16490": "Chloris chloris",
    "16500": "Chloris sinica",
    "16510": "Chloris ambigua",
    "16520": "Chloris spinoides",
    "16530": "Carduelis carduelis",
    "16532": "Carduelis caniceps",
    "16540": "Spinus spinus",
    "16550": "Spinus pinus",
    "16560": "Spinus notatus",
    "16570": "Spinus tristis",
    "16580": "Spinus psaltria",
    "16590": "Spinus lawrencei",
    "16600": "Linaria cannabina",
    "16610": "Linaria yemenensis",
    "16620": "Linaria flavirostris",
    "16630": "Acanthis flammea flammea sensu lato",
    "16633": "Acanthis flammea flammea sensu lato",
    "16635": "Acanthis flammea",
    "16640": "Acanthis flammea hornemanni sensu lato",
    "16649": "Carduelis/Chloris/Acanthis/Linaria/Spinus sp.",
    "16650": "Loxia leucoptera",
    "16660": "Loxia curvirostra",
    "16670": "Loxia scotica",
    "16680": "Loxia pytyopsittacus",
    "16689": "Loxia sp.",
    "16690": "Leucosticte nemoricola",
    "16700": "Leucosticte brandti",
    "16710": "Leucosticte arctoa",
    "16720": "Leucosticte tephrocotis",
    "16730": "Rhodopechys sanguineus",
    "16740": "Rhodospiza obsoleta",
    "16750": "Bucanetes mongolicus",
    "16760": "Bucanetes githagineus",
    "16770": "Agraphospiza rubescens",
    "16780": "Procarduelis nipalensis",
    "16790": "Carpodacus erythrinus",
    "16800": "Haemorhous purpureus",
    "16810": "Haemorhous cassinii",
    "16820": "Haemorhous mexicanus",
    "16830": "Carpodacus pulcherrimus",
    "16841": "Carpodacus waltoni",
    "16850": "Carpodacus rodochroa",
    "16860": "Carpodacus vinaceus",
    "16870": "Carpodacus edwardsii",
    "16880": "Carpodacus synoicus",
    "16890": "Carpodacus roseus",
    "16900": "Carpodacus trifasciatus",
    "16910": "Carpodacus rodopeplus",
    "16920": "Carpodacus thura",
    "16930": "Carpodacus rhodochlamys",
    "16940": "Carpodacus grandis",
    "16950": "Carpodacus rubicilloides",
    "16960": "Carpodacus rubicilla",
    "16970": "Carpodacus puniceus",
    "16980": "Carpodacus roborowskii",
    "16990": "Pinicola enucleator",
    "17000": "Carpodacus subhimachalus",
    "17010": "Carpodacus ferreorostris",
    "17020": "Carpodacus sipahi",
    "17030": "Pyrrhoplectes epauletta",
    "17040": "Carpodacus sibiricus",
    "17050": "Urocynchramus pylzowi",
    "17060": "Pyrrhula nipalensis",
    "17070": "Pyrrhula aurantiaca",
    "17080": "Pyrrhula erythrocephala",
    "17090": "Pyrrhula erythaca",
    "17100": "Pyrrhula pyrrhula",
    "17105": "Pyrrhula murina",
    "17110": "Mycerobas icterioides",
    "17120": "Mycerobas affinis",
    "17130": "Mycerobas melanozanthos",
    "17140": "Mycerobas carnipes",
    "17150": "Eophona migratoria",
    "17160": "Eophona personata",
    "17170": "Coccothraustes coccothraustes",
    "17180": "Hesperiphona vespertina",
    "17190": "Hesperiphona abeillei",
    "17200": "Mniotilta varia",
    "17210": "Vermivora bachmanii",
    "17220": "Vermivora chrysoptera",
    "17230": "Vermivora cyanoptera",
    "17240": "Leiothlypis peregrina",
    "17250": "Leiothlypis celata",
    "17260": "Leiothlypis ruficapilla",
    "17270": "Leiothlypis virginiae",
    "17280": "Leiothlypis crissalis",
    "17290": "Leiothlypis luciae",
    "17300": "Oreothlypis superciliosa",
    "17310": "Setophaga pitiayumi",
    "17320": "Setophaga americana",
    "17330": "Setophaga petechia sensu lato",
    "17331": "Setophaga aestiva",
    "17332": "Setophaga petechia",
    "17340": "Setophaga pensylvanica",
    "17350": "Setophaga cerulea",
    "17360": "Setophaga caerulescens",
    "17370": "Setophaga pinus",
    "17380": "Setophaga graciae",
    "17390": "Setophaga pityophila",
    "17400": "Setophaga dominica",
    "17410": "Setophaga kirtlandii",
    "17420": "Setophaga nigrescens",
    "17430": "Setophaga occidentalis",
    "17440": "Setophaga townsendi",
    "17450": "Setophaga virens",
    "17460": "Setophaga chrysoparia",
    "17470": "Setophaga fusca",
    "17480": "Setophaga discolor",
    "17490": "Setophaga tigrina",
    "17500": "Setophaga magnolia",
    "17510": "Setophaga coronata",
    "17520": "Setophaga palmarum",
    "17530": "Setophaga striata",
    "17540": "Setophaga castanea",
    "17550": "Setophaga ruticilla",
    "17560": "Seiurus aurocapilla",
    "17570": "Parkesia noveboracensis",
    "17580": "Parkesia motacilla",
    "17590": "Limnothlypis swainsonii",
    "17600": "Helmitheros vermivorum",
    "17610": "Protonotaria citrea",
    "17620": "Geothlypis trichas",
    "17630": "Geothlypis rostrata",
    "17640": "Geothlypis speciosa",
    "17650": "Geothlypis nelsoni",
    "17660": "Geothlypis poliocephala",
    "17670": "Geothlypis formosa",
    "17680": "Oporornis agilis",
    "17690": "Geothlypis philadelphia",
    "17700": "Geothlypis tolmiei",
    "17710": "Setophaga citrina",
    "17720": "Cardellina pusilla",
    "17730": "Cardellina canadensis",
    "17740": "Cardellina rubrifrons",
    "17750": "Cardellina rubra",
    "17760": "Myioborus pictus",
    "17770": "Myioborus miniatus",
    "17780": "Basileuterus lachrymosus",
    "17790": "Basileuterus culicivorus",
    "17800": "Basileuterus rufifrons",
    "17810": "Peucedramus taeniatus",
    "17820": "Icteria virens",
    "17830": "Coereba flaveola",
    "17840": "Piranga bidentata",
    "17850": "Piranga flava",
    "17860": "Piranga rubra",
    "17870": "Piranga ludoviciana",
    "17880": "Piranga olivacea",
    "17890": "Piranga erythrocephala",
    "17900": "Spindalis zena",
    "17910": "Euphonia affinis",
    "17920": "Chlorophonia elegantissima",
    "17930": "Diglossa baritula",
    "17940": "Atlapetes pileatus",
    "17950": "Arremon torquatus sensu lato",
    "17960": "Arremonops rufivirgatus",
    "17970": "Pipilo chlorurus",
    "17980": "Pipilo erythrophthalmus",
    "17990": "Melozone fusca",
    "18000": "Melozone aberti",
    "18010": "Melozone kieneri",
    "18020": "Phonipara canora",
    "18030": "Melanospiza bicolor",
    "18040": "Sporophila torqueola sensu lato",
    "18050": "Volatinia jacarina",
    "18060": "Amphispiza bilineata",
    "18070": "Artemisiospiza belli",
    "18080": "Peucaea mystacalis",
    "18090": "Peucaea botterii",
    "18100": "Peucaea cassinii",
    "18110": "Peucaea aestivalis",
    "18120": "Amphispizopsis quinquestriata",
    "18130": "Peucaea carpalis",
    "18140": "Aimophila ruficeps",
    "18150": "Aimophila rufescens",
    "18160": "Oriturus superciliosus",
    "18170": "Spizelloides arborea",
    "18180": "Spizella passerina",
    "18190": "Spizella pallida",
    "18200": "Spizella breweri",
    "18210": "Spizella pusilla",
    "18220": "Spizella wortheni",
    "18230": "Spizella atrogularis",
    "18240": "Chondestes grammacus",
    "18250": "Pooecetes gramineus",
    "18260": "Passerculus sandwichensis",
    "18270": "Centronyx bairdii",
    "18280": "Ammodramus savannarum",
    "18290": "Ammospiza leconteii",
    "18300": "Ammospiza caudacuta",
    "18310": "Ammospiza maritima",
    "18320": "Xenospiza baileyi",
    "18330": "Centronyx henslowii",
    "18340": "Passerella iliaca sensu lato",
    "18341": "Passerella iliaca",
    "18350": "Melospiza melodia",
    "18360": "Melospiza lincolnii",
    "18370": "Melospiza georgiana",
    "18380": "Zonotrichia querula",
    "18390": "Zonotrichia leucophrys",
    "18400": "Zonotrichia albicollis",
    "18410": "Zonotrichia atricapilla",
    "18420": "Junco hyemalis",
    "18440": "Junco phaeonotus",
    "18450": "Calamospiza melanocorys",
    "18460": "Rhynchophanes mccownii",
    "18470": "Calcarius lapponicus",
    "18480": "Calcarius ornatus",
    "18490": "Calcarius pictus",
    "18500": "Plectrophenax nivalis",
    "18510": "Emberiza siemsseni",
    "18520": "Emberiza variabilis",
    "18530": "Emberiza spodocephala",
    "18540": "Emberiza sulphurata",
    "18550": "Emberiza koslowi",
    "18560": "Emberiza leucocephalos",
    "18570": "Emberiza citrinella",
    "18580": "Emberiza cirlus",
    "18590": "Emberiza stewarti",
    "18600": "Emberiza cia",
    "18610": "Emberiza cioides",
    "18620": "Emberiza jankowskii",
    "18630": "Emberiza striolata sensu lato",
    "18631": "Emberiza striolata",
    "18640": "Emberiza tahapisi sensu lato",
    "18641": "Emberiza tahapisi",
    "18642": "Emberiza goslingi",
    "18650": "Emberiza cineracea",
    "18660": "Emberiza hortulana",
    "18670": "Emberiza buchanani",
    "18680": "Emberiza caesia",
    "18690": "Emberiza fucata",
    "18700": "Emberiza elegans",
    "18710": "Emberiza chrysophrys",
    "18720": "Emberiza tristrami",
    "18730": "Emberiza rustica",
    "18740": "Emberiza pusilla",
    "18750": "Emberiza rutila",
    "18760": "Emberiza aureola",
    "18770": "Emberiza schoeniclus",
    "18780": "Emberiza pallasi",
    "18790": "Emberiza yessoensis",
    "18800": "Emberiza bruniceps",
    "18810": "Emberiza melanocephala",
    "18819": "Emberiza sp.",
    "18820": "Emberiza calandra",
    "18830": "Emberiza lathami",
    "18840": "Spiza americana",
    "18850": "Pheucticus chrysopeplus",
    "18860": "Pheucticus melanocephalus",
    "18870": "Pheucticus ludovicianus",
    "18880": "Cardinalis cardinalis",
    "18890": "Cardinalis sinuatus",
    "18900": "Periporphyrus celaeno",
    "18910": "Passerina caerulea",
    "18920": "Passerina cyanea",
    "18930": "Passerina amoena",
    "18940": "Passerina versicolor",
    "18950": "Passerina ciris",
    "18960": "Passerina leclancherii",
    "18970": "Dolichonyx oryzivorus",
    "18980": "Molothrus aeneus",
    "18990": "Molothrus ater",
    "19000": "Euphagus cyanocephalus",
    "19010": "Euphagus carolinus",
    "19020": "Quiscalus mexicanus",
    "19030": "Quiscalus palustris",
    "19040": "Quiscalus major",
    "19050": "Quiscalus quiscula",
    "19060": "Sturnella neglecta",
    "19070": "Sturnella magna",
    "19080": "Agelaius tricolor",
    "19090": "Agelaius phoeniceus",
    "19100": "Agelaius humeralis",
    "19110": "Xanthocephalus xanthocephalus",
    "19120": "Icterus parisorum",
    "19130": "Icterus graduacauda",
    "19140": "Icterus wagleri",
    "19150": "Icterus dominicensis sensu lato",
    "19160": "Icterus cucullatus",
    "19170": "Icterus spurius",
    "19180": "Icterus galbula",
    "19190": "Icterus pustulatus",
    "19200": "Icterus gularis",
    "19210": "Icterus pectoralis",
    "19220": "Cassiculus melanicterus",
    "20010": "Turtur afer",
    "20020": "Thalassoica antarctica",
    "20030": "Ploceus cucullatus",
    "20040": "Phalacrocorax capensis",
    "20050": "Passer griseus",
    "20060": "Pagodroma nivea",
    "20070": "Chionis albus",
    "20080": "Hirundo lucida",
    "20090": "Thalassarche chrysostoma",
    "20100": "Phoebetria palpebrata",
    "20120": "Aphrodroma brevirostris",
    "20130": "Fulmarus glacialoides",
    "20140": "Garrodia nereis",
    "20150": "Porphyrio flavirostris",
    "20160": "Halobaena caerulea",
    "20170": "Pelecanoides urinatrix",
    "20180": "Pelecanoides georgicus",
    "20190": "Leucocarbo atriceps",
    "20192": "Leucocarbo nivalis",
    "20193": "Leucocarbo georgianus",
    "20200": "Pygoscelis adeliae",
    "20210": "Pygoscelis antarcticus",
    "20220": "Pygoscelis papua",
    "20230": "Phoenicopterus chilensis",
    "20240": "Quelea quelea",
    "20250": "Amandava amandava",
    "20260": "Lonchura punctulata",
    "20270": "Estrilda troglodytes",
    "20290": "Lonchura malacca sensu lato",
    "20291": "Lonchura malacca",
    "20293": "Lonchura atricapilla",
    "20300": "Eudyptes chrysolophus",
    "20310": "Ardea melanocephala",
    "20320": "Pachyptila desolata",
    "20330": "Pterodroma incerta",
    "20340": "Cossypha natalensis",
    "20350": "Sterna hirundinacea",
    "20360": "Chroicocephalus maculipennis",
    "20380": "Chloephaga picta",
    "20390": "Myiopsitta monachus",
    "20400": "Hydrobates markhami",
    "20410": "Ploceus melanocephalus",
    "20420": "Euplectes afer",
    "20430": "Estrilda melpoda",
    "20439": "Estrilda sp.",
    "20440": "Taeniopygia guttata sensu lato",
    "20441": "Taeniopygia guttata",
    "20442": "Taeniopygia castanotis",
    "20450": "Lonchura maja",
    "20459": "Lonchura sp.",
    "20460": "Anarhynchus marginatus",
    "20470": "Euplectes orix",
    "20480": "Euplectes franciscanus",
    "20490": "Pterodroma cahow",
    "20600": "Larus dominicanus",
    "20700": "Sterna vittata",
    "20800": "Cygnus atratus",
    "20900": "Acrocephalus scirpaceus baeticatus sensu lato",
    "21000": "Andropadus importunus",
    "21100": "Batis senegalensis",
    "21200": "Camaroptera brachyura",
    "21300": "Chalcites basalis",
    "21400": "Cossypha niveicapilla",
    "21500": "Dicrurus adsimilis",
    "21600": "Dryoscopus senegalensis",
    "21700": "Elminia longicauda",
    "21800": "Halcyon senegaloides",
    "21900": "Melaenornis edolioides",
    "22000": "Melaniparus leucomelas",
    "22100": "Fraseria caerulescens",
    "22200": "Fraseria plumbea",
    "22300": "Cinnyris bifasciatus",
    "22310": "Cyanomitra veroxii",
    "22400": "Cinnyris pulchellus",
    "22500": "Passer motitensis",
    "22700": "Platysteira cyanea",
    "22800": "Plocepasser mahali",
    "22900": "Sylvietta brachyura",
    "23000": "Terpsiphone rufiventer",
    "23100": "Trochocercus cyanomelas",
    "23200": "Aerospiza tachiro",
    "23300": "Turtur tympanistria",
    "23400": "Eurillas virens",
    "23500": "Eurillas curvirostris",
    "23600": "Eurillas latirostris",
    "23700": "Phyllastrephus albigularis",
    "23800": "Bleda canicapillus",
    "23900": "Criniger barbatus",
    "24000": "Criniger calurus",
    "24200": "Stiphrornis erythrothorax",
    "24300": "Camaroptera brevicaudata",
    "24400": "Sylvietta virens",
    "24500": "Hylia prasina",
    "24600": "Fraseria cinerascens",
    "24700": "Platysteira castanea",
    "24900": "Illadopsis rufescens",
    "24995": "Species not accepted",
    "24997": "Cage & exotic birds",
    "24998": "Other hybrids or intermediate",
    "25100": "Hedydipna collaris",
    "25200": "Cyanomitra olivacea",
    "25300": "Nicator chloris",
    "25400": "Malimbus nitens",
    "25500": "Spermophaga haematina",
    "25600": "Laniarius aethiopicus",
    "25700": "Callonetta leucophrys",
    "25800": "Mareca sibilatrix",
    "26000": "Pyrrhura orcesi",
    "26100": "Atlapetes pallidiceps",
    "26200": "Cyanoliseus patagonus",
    "26300": "Larus belcheri",
    "26400": "Ploceus castaneiceps",
    "26420": "Ploceus intermedius",
    "26430": "Vidua macroura",
    "26440": "Glaucestrilda perreini",
    "26450": "Estrilda rhodopyga",
    "26470": "Vanellus albiceps",
    "26480": "Illadopsis puveli",
    "26490": "Prionops plumatus",
    "26500": "Clamator levaillantii",
    "26510": "Streptopelia vinacea",
    "26520": "Campethera punctuligera",
    "26530": "Turdus pelios",
    "26540": "Atimastillas flavicollis",
    "26550": "Pogonornis dubius",
    "26560": "Larus mongolicus",
    "26580": "Curruca curruca minula sensu lato",
    "26590": "Nettapus auritus",
    "26600": "Coturnix delegorguei",
    "26610": "Psittacula eupatria",
    "26620": "Euplectes albonotatus",
    "26632": "Larus smithsonianus",
    "26643": "Motacilla tschutschensis",
    "26650": "Radjah radjah",
    "26660": "Tadorna cana",
    "26670": "Tadorna tadornoides",
    "26680": "Tadorna variegata",
    "26690": "Amazona oratrix",
    "26700": "Pachyptila belcheri",
    "26710": "Centropus superciliosus",
    "26714": "Centropus burchellii",
    "26720": "Agelasticus cyanopus",
    "26730": "Ammodramus humeralis",
    "26740": "Anthus hellmayri",
    "26750": "Psittacara leucophthalmus",
    "26760": "Arremon taciturnus",
    "26770": "Attila bolivianus",
    "26780": "Rupornis magnirostris",
    "26790": "Cacicus cela",
    "26800": "Camptostoma obsoletum",
    "26810": "Setopagis parvula",
    "26820": "Certhiaxis cinnamomeus",
    "26830": "Chloroceryle amazona",
    "26840": "Cnemotriccus fuscatus",
    "26850": "Colaptes campestris",
    "26860": "Columbina picui",
    "26870": "Coryphaspiza melanotis",
    "26880": "Thripophaga gutturata",
    "26890": "Crypturellus parvirostris",
    "26900": "Culicivora caudacuta",
    "26910": "Deconychura longicauda",
    "26920": "Dendrocincla merula",
    "26930": "Donacobius atricapilla",
    "26940": "Donacospiza albifrons",
    "26950": "Dysithamnus mentalis",
    "26960": "Elaenia flavogaster",
    "26970": "Elaenia parvirostris",
    "26980": "Emberizoides herbicola",
    "26990": "Eucometis penicillata",
    "27000": "Euphonia chlorotica",
    "27010": "Euphonia laniirostris",
    "27020": "Formicivora rufa",
    "27030": "Furnarius leucopus",
    "27040": "Furnarius rufus",
    "27050": "Galbula ruficauda",
    "27060": "Geothlypis aequinoctialis sensu lato",
    "27061": "Geothlypis aequinoctialis",
    "27070": "Hemitriccus flammulatus",
    "27080": "Hemitriccus zosterops",
    "27090": "Hydropsalis torquata",
    "27100": "Icterus cayanensis",
    "27110": "Inezia inornata",
    "27120": "Jacana jacana",
    "27130": "Knipolegus hudsoni",
    "27140": "Laterallus melanophaius",
    "27150": "Lathrotriccus euleri",
    "27160": "Lepidocolaptes angustirostris",
    "27170": "Leptopogon amaurocephalus",
    "27180": "Leptotila rufaxilla",
    "27190": "Buteogallus schistaceus",
    "27200": "Mimus saturninus",
    "27210": "Momotus momota sensu lato",
    "27211": "Momotus momota",
    "27212": "Momotus coeruliceps",
    "27220": "Monasa nigrifrons",
    "27230": "Myiarchus ferox",
    "27240": "Myiarchus swainsoni",
    "27250": "Myiophobus fasciatus",
    "27260": "Myiozetetes cayanensis",
    "27270": "Sciaphylax hemimelaena",
    "27280": "Myrmelastes hyperythrus",
    "27290": "Myrmoborus leucophrys",
    "27300": "Neopelma sulphureiventer",
    "27310": "Sporophila angolensis",
    "27320": "Paroaria gularis",
    "27330": "Phacellodomus ruber",
    "27340": "Picumnus albosquamatus",
    "27350": "Pipra fasciicauda",
    "27360": "Polioptila dumicola",
    "27370": "Pseudocolopteryx sclateri",
    "27380": "Ramphocelus carbo",
    "27390": "Saltator maximus",
    "27400": "Satrapa icterophrys",
    "27410": "Schiffornis turdina",
    "27420": "Schistochlamys melanopis",
    "27431": "Serpophaga subcristata",
    "27440": "Sittasomus griseicapillus",
    "27450": "Sporophila caerulescens",
    "27460": "Sporophila collaris",
    "27470": "Sporophila leucoptera",
    "27480": "Sporophila ruficollis",
    "27490": "Synallaxis albescens",
    "27500": "Synallaxis gujanensis",
    "27510": "Synallaxis hypospodia",
    "27520": "Tapera naevia",
    "27530": "Taraba major",
    "27540": "Thamnophilus doliatus",
    "27550": "Thamnophilus punctatus",
    "27560": "Thamnophilus schistaceus",
    "27570": "Thlypopsis sordida",
    "27580": "Thraupis palmarum",
    "27590": "Thraupis sayaca",
    "27600": "Pheugopedius genibarbis",
    "27610": "Cantorchilus guarayanus",
    "27620": "Poecilotriccus latirostris",
    "27630": "Tolmomyias sulphurescens",
    "27640": "Trogon melanurus",
    "27650": "Turdus amaurochalinus",
    "27660": "Turdus hauxwelli",
    "27670": "Veniliornis passerinus",
    "27680": "Xenops tenuirostris",
    "27690": "Xiphorhynchus guttatus",
    "27700": "Dendroplex picus",
    "27710": "Xolmis velatus",
    "27720": "Fregetta grallaria",
    "27730": "Fregetta tropica",
    "27740": "Pachyptila turtur",
    "27750": "Aptenodytes patagonicus",
    "27760": "Aptenodytes forsteri",
    "27770": "Anas georgica",
    "27780": "Anthus antarcticus",
    "27790": "Procellaria cinerea",
    "27800": "Procellaria aequinoctialis",
    "27810": "Procellaria parkinsoni",
    "27820": "Procellaria westlandica",
    "27830": "Otus insularis",
    "27900": "Neochen jubata",
    "27910": "Copsychus albospecularis",
    "27920": "Copsychus saularis",
    "27930": "Copsychus sechellarum",
    "27940": "Copsychus malabaricus",
    "27960": "Copsychus luzoniensis",
    "27970": "Copsychus niger",
    "27980": "Copsychus cebuensis",
    "27990": "Balearica regulorum",
    "28000": "Anas erythrorhyncha",
    "28010": "Pternistis erckelii",
    "28020": "Anumbius annumbi",
    "28030": "Anas bernieri",
    "30010": "Aerospiza castanilius",
    "30020": "Tachyspiza erythropus",
    "30030": "Astur melanoleucus",
    "30040": "Accipiter ovampensis",
    "30050": "Acrocephalus gracilirostris",
    "30060": "Acrocephalus rufescens",
    "30070": "Actophilornis africanus",
    "30090": "Agapornis pullarius",
    "30100": "Agelastes niger",
    "30110": "Alcedo coerulescens",
    "30120": "Corythornis cristatus",
    "30130": "Corythornis leucogaster",
    "30140": "Alcedo quadribrachys",
    "30150": "Alethe diademata",
    "30160": "Amadina fasciata",
    "30170": "Amblyospiza albifrons",
    "30180": "Anaplectes rubriceps",
    "30190": "Spatula hottentota",
    "30200": "Anas sparsa",
    "30210": "Anas undulata",
    "30220": "Anastomus lamelligerus",
    "30230": "Eurillas ansorgei",
    "30240": "Stelgidillas gracilirostris",
    "30250": "Eurillas gracilis",
    "30260": "Arizelocichla montana",
    "30270": "Arizelocichla tephrolaema",
    "30280": "Anhinga rufa",
    "30290": "Anomalospiza imberbis",
    "30300": "Anous minutus",
    "30310": "Anthoscopus flavifrons",
    "30320": "Anthoscopus parvulus",
    "30330": "Anthoscopus punctifrons",
    "30340": "Deleornis fraseri",
    "30350": "Anthreptes gabonicus",
    "30360": "Anthreptes longuemarei",
    "30370": "Anthreptes rectirostris",
    "30380": "Anthus cinnamomeus",
    "30390": "Anthus leucophrys",
    "30400": "Apalis cinerea",
    "30410": "Apalis flavida",
    "30420": "Apalis jacksoni",
    "30430": "Apalis nigriceps",
    "30440": "Oreolais pulcher",
    "30450": "Apalis rufogularis",
    "30460": "Apaloderma aequatoriale",
    "30470": "Apaloderma narina",
    "30480": "Apaloderma vittatum",
    "30490": "Columba larvata",
    "30500": "Apus barbatus",
    "30510": "Apus horus",
    "30520": "Apus sladeniae",
    "30540": "Hieraaetus wahlbergi",
    "30560": "Ardeola rufiventris",
    "30570": "Aviceda cuculoides",
    "30580": "Baeopogon clamans",
    "30590": "Baeopogon indicator",
    "30600": "Balearica pavonina",
    "30610": "Batis orientalis",
    "30620": "Batis poensis",
    "30630": "Megabyas flammulatus",
    "30640": "Bias musicus",
    "30650": "Bleda eximius",
    "30660": "Bleda syndactylus",
    "30670": "Bostrychia hagedash",
    "30680": "Bostrychia olivacea",
    "30690": "Bostrychia rara",
    "30700": "Agricola pallidus",
    "30710": "Bradypterus baboecala",
    "30720": "Bradypterus bangwaensis",
    "30730": "Bubalornis albirostris",
    "30740": "Ketupa lactea",
    "30750": "Ketupa poensis",
    "30760": "Buccanodon duchaillui",
    "30770": "Bucorvus abyssinicus",
    "30780": "Buphagus africanus",
    "30790": "Burhinus vermiculatus",
    "30800": "Butastur rufipennis",
    "30810": "Buteo auguralis",
    "30820": "Calyptocichla serinus",
    "30830": "Camaroptera chloronota",
    "30840": "Camaroptera superciliaris",
    "30850": "Lobotos oriolinus",
    "30860": "Campephaga petiti",
    "30870": "Campephaga phoenicea",
    "30880": "Campephaga quiscalina",
    "30890": "Campethera abingoni",
    "30900": "Campethera cailliautii",
    "30910": "Pardipicus caroli",
    "30920": "Pardipicus nivosus",
    "30930": "Campethera tullbergi",
    "30940": "Canirallus oculeus",
    "30950": "Caprimulgus climacurus",
    "30960": "Caprimulgus natalensis",
    "30970": "Caprimulgus pectoralis",
    "30980": "Caprimulgus tristigma",
    "30990": "Centropus grillii",
    "31000": "Centropus leucogaster",
    "31010": "Centropus monachus",
    "31020": "Bycanistes albotibialis",
    "31030": "Ceratogymna atrata",
    "31040": "Bycanistes bucinator",
    "31050": "Ceratogymna elata",
    "31060": "Bycanistes fistulator",
    "31070": "Bycanistes subcylindricus",
    "31080": "Cercococcyx mechowi",
    "31090": "Cercococcyx olivinus",
    "31100": "Oenanthe familiaris",
    "31110": "Cercotrichas hartlaubi",
    "31120": "Ceuthmochares aereus",
    "31130": "Charadrius forbesi",
    "31140": "Charadrius tricollaris",
    "31150": "Chelictinia riocourii",
    "31160": "Chlorocichla simplex",
    "31170": "Iduna natalensis",
    "31180": "Chrysococcyx cupreus",
    "31190": "Chrysococcyx flavigularis",
    "31200": "Circaetus cinerascens",
    "31210": "Circaetus cinereus",
    "31220": "Cisticola anonymus",
    "31230": "Cisticola aridulus",
    "31240": "Cisticola brachypterus",
    "31250": "Cisticola cantans",
    "31260": "Cisticola chubbi",
    "31270": "Cisticola guinea",
    "31280": "Cisticola aberrans emini sensu lato",
    "31281": "Cisticola aberrans",
    "31290": "Cisticola erythrops",
    "31300": "Cisticola eximius",
    "31310": "Cisticola galactotes",
    "31320": "Cisticola lateralis",
    "31330": "Cisticola natalensis",
    "31340": "Cisticola robustus",
    "31350": "Cisticola ruficeps",
    "31360": "Cisticola rufus",
    "31380": "Clytospiza monteiri",
    "31390": "Colius striatus",
    "31400": "Columba arquatrix",
    "31410": "Columba delegorguei",
    "31420": "Columba guinea",
    "31430": "Columba unicincta",
    "31440": "Coracias cyanogaster",
    "31450": "Coracias naevius",
    "31460": "Cyanograucalus azureus",
    "31470": "Ceblepyris caesius",
    "31480": "Ceblepyris pectoralis",
    "31490": "Lanius corvinus",
    "31500": "Corythaeola cristata",
    "31510": "Cossypha albicapillus",
    "31520": "Cossypha cyanocampter",
    "31530": "Cossyphicula isabellae",
    "31540": "Sheppardia polioptera",
    "31550": "Cossyphicula roberti",
    "31560": "Synoicus adansonii",
    "31570": "Crecopsis egregia",
    "31580": "Crinifer piscator",
    "31590": "Criniger chloronotus",
    "31600": "Criniger olivaceus",
    "31610": "Cuculus clamosus",
    "31620": "Cuculus gularis",
    "31630": "Cuculus solitarius",
    "31640": "Cursorius temminckii",
    "31650": "Dendropicos elachus",
    "31660": "Dendropicos elliotii",
    "31670": "Dendropicos fuscescens",
    "31680": "Dendropicos gabonensis",
    "31690": "Dendropicos goertae",
    "31700": "Dendropicos obsoletus",
    "31710": "Dendropicos poecilolaemus",
    "31720": "Chloropicus pyrrhogaster",
    "31730": "Chloropicus xantholophus",
    "31740": "Dicrurus atripennis",
    "31750": "Dicrurus ludwigii",
    "31760": "Dicrurus modestus",
    "31770": "Drymocichla incana",
    "31780": "Dryoscopus angolensis",
    "31790": "Dryoscopus gambensis",
    "31800": "Dryoscopus sabini",
    "31810": "Circaetus spectabilis",
    "31820": "Egretta ardesiaca",
    "31830": "Elanus axillaris",
    "31840": "Elminia albiventris",
    "31850": "Elminia nigromitrata",
    "31860": "Emberiza affinis",
    "31870": "Emberiza cabanisi",
    "31880": "Emberiza flaviventris",
    "31890": "Ephippiorhynchus senegalensis",
    "31900": "Eremomela badiceps",
    "31910": "Eremomela canescens",
    "31920": "Eremomela icteropygialis",
    "31930": "Eremomela pusilla",
    "31940": "Eremopterix leucotis",
    "31950": "Erythrocercus mccallii",
    "31960": "Glaucestrilda caerulescens",
    "31970": "Estrilda nonnula",
    "31980": "Estrilda paludicola",
    "31990": "Estrilda poliopareia",
    "32000": "Euplectes ardens",
    "32010": "Euplectes axillaris",
    "32020": "Euplectes capensis",
    "32030": "Euplectes hartlaubi",
    "32040": "Euplectes hordeaceus",
    "32050": "Euplectes macroura",
    "32060": "Lissotis melanogaster",
    "32070": "Lophotis ruficrista",
    "32080": "Eupodotis senegalensis",
    "32090": "Eurystomus gularis",
    "32100": "Euschistospiza dybowskii",
    "32110": "Falco alopex",
    "32120": "Falco ardosiaceus",
    "32130": "Falco cuvierii",
    "32140": "Fraseria ocreata",
    "32150": "Galerida modesta",
    "32160": "Paragallinula angulata",
    "32170": "Glareola cinerea",
    "32180": "Glareola nuchalis",
    "32190": "Glaucidium perlatum",
    "32200": "Glaucidium sjostedti",
    "32210": "Calherodius leuconotus",
    "32230": "Guttera pucherani",
    "32240": "Gymnobucco calvus",
    "32250": "Gymnobucco peli",
    "32260": "Gypohierax angolensis",
    "32270": "Gyps africanus",
    "32280": "Halcyon badia",
    "32300": "Halcyon chelicuti",
    "32310": "Halcyon malimbica",
    "32320": "Halcyon senegalensis",
    "32330": "Buteogallus coronatus",
    "32340": "Prinia erythroptera",
    "32350": "Hieraaetus ayresii",
    "32360": "Aquila spilogaster",
    "32370": "Himantornis haematopus",
    "32380": "Cecropis abyssinica",
    "32390": "Hirundo aethiopica",
    "32420": "Hirundo leucosoma",
    "32430": "Hirundo nigrita",
    "32440": "Petrochelidon preussi",
    "32450": "Cecropis semirufa",
    "32460": "Cecropis senegalensis",
    "32470": "Hyliota flavigaster",
    "32480": "Hyliota violacea",
    "32490": "Hypergerus atriceps",
    "32500": "Illadopsis cleaveri",
    "32510": "Illadopsis fulvescens",
    "32520": "Illadopsis rufipennis",
    "32530": "Indicator exilis",
    "32540": "Indicator indicator",
    "32550": "Indicator maculatus",
    "32560": "Indicator minor",
    "32570": "Indicator willcocksi",
    "32580": "Ispidina lecontei",
    "32590": "Ispidina picta",
    "32610": "Ixonotus guttatus",
    "32620": "Jynx ruficollis",
    "32630": "Kakamega poliothorax",
    "32640": "Kaupifalco monogrammicus",
    "32650": "Turdoides gilberti",
    "32660": "Lagonosticta larvata",
    "32670": "Lagonosticta rara",
    "32680": "Lagonosticta rubricata",
    "32690": "Lagonosticta rufopicta",
    "32700": "Lagonosticta sanguinodorsalis",
    "32710": "Lamprotornis caudatus",
    "32720": "Lamprotornis chalcurus",
    "32730": "Lamprotornis chalybaeus",
    "32741": "Lamprotornis chloropterus",
    "32750": "Lamprotornis pulcher",
    "32760": "Hylopsar purpureiceps",
    "32770": "Lamprotornis purpureus",
    "32780": "Lamprotornis splendidus",
    "32790": "Laniarius atrococcineus",
    "32800": "Laniarius atroflavus",
    "32810": "Laniarius barbarus",
    "32820": "Laniarius erythrogaster",
    "32830": "Laniarius fuelleborni",
    "32840": "Laniarius leucorhynchus",
    "32850": "Laniarius luehderi",
    "32870": "Lanius collaris",
    "32880": "Lanius excubitoroides",
    "32890": "Lanius gubernator",
    "32900": "Lanius mackinnoni",
    "32920": "Linurgus olivaceus",
    "32940": "Lophaetus occipitalis",
    "32950": "Pogonornis bidentatus",
    "32960": "Lybius leucocephalus",
    "32970": "Lybius vieilloti",
    "32980": "Macheiramphus alcinus",
    "32990": "Caprimulgus longipennis",
    "33000": "Caprimulgus vexillarius",
    "33010": "Macrosphenus flavicans",
    "33020": "Macrosphenus kempi",
    "33030": "Malaconotus blanchoti",
    "33040": "Malaconotus cruentus",
    "33050": "Malaconotus gladiator",
    "33060": "Chlorophoneus sulfureopectus",
    "33070": "Malimbus erythrogaster",
    "33080": "Malimbus ibadanensis",
    "33090": "Malimbus malimbicus",
    "33100": "Malimbus racheliae",
    "33110": "Malimbus rubricollis",
    "33120": "Malimbus scutatus",
    "33130": "Mandingoa nitidula",
    "33140": "Megaceryle maxima",
    "33150": "Melichneutes robustus",
    "33170": "Melocichla mentalis",
    "33180": "Merops breweri",
    "33190": "Merops bulocki",
    "33200": "Merops gularis",
    "33210": "Merops hirundineus",
    "33220": "Merops malimbicus",
    "33230": "Merops muelleri",
    "33240": "Merops nubicus",
    "33250": "Merops pusillus",
    "33260": "Merops variegatus",
    "33270": "Microparra capensis",
    "33280": "Corypha africana",
    "33290": "Amirafra rufocinnamomea",
    "33310": "Motacilla clara",
    "33320": "Muscicapa adusta",
    "33330": "Muscicapa aquatica",
    "33340": "Muscicapa cassini",
    "33350": "Bradornis comitatus",
    "33360": "Muscicapa epulata",
    "33370": "Artomyias fuliginosa",
    "33380": "Fraseria olivascens",
    "33390": "Muscicapa sethsmithi",
    "33400": "Fraseria tessmanni",
    "33410": "Artomyias ussheri",
    "33420": "Tauraco violaceus",
    "33430": "Fraseria griseigularis",
    "33440": "Oenanthe albifrons",
    "33450": "Myrmecocichla nigra",
    "33460": "Neafrapus cassini",
    "33470": "Chalcomitra adelberti",
    "33480": "Cinnyris batesi",
    "33490": "Cinnyris bouvieri",
    "33500": "Cinnyris chloropygius",
    "33510": "Cinnyris coccinigastrus",
    "33520": "Cinnyris cupreus",
    "33530": "Cyanomitra cyanolaema",
    "33540": "Chalcomitra fuliginosa",
    "33550": "Cinnyris johannae",
    "33560": "Cinnyris minullus",
    "33580": "Cyanomitra oritis",
    "33590": "Cinnyris reichenowi",
    "33600": "Anabathmis reichenbachii",
    "33610": "Chalcomitra rubescens",
    "33620": "Anthreptes seimundi",
    "33630": "Chalcomitra senegalensis",
    "33640": "Cinnyris superbus",
    "33650": "Cinnyris venustus",
    "33660": "Cyanomitra verticalis",
    "33670": "Stizorhina finschi",
    "33680": "Stizorhina fraseri",
    "33690": "Neocossyphus poensis",
    "33700": "Neocossyphus rufus",
    "33710": "Neotis nuba",
    "33720": "Delacourella capistrata",
    "33730": "Nesocharis shelleyi",
    "33740": "Nigrita bicolor",
    "33750": "Nigrita canicapillus",
    "33760": "Nigrita fusconotus",
    "33770": "Nigrita luteifrons",
    "33780": "Nilaus afer",
    "33790": "Oenanthe heuglinii",
    "33800": "Onychognathus fulgidus",
    "33810": "Onychognathus morio",
    "33820": "Onychognathus walleri",
    "33830": "Oriolus auratus",
    "33840": "Oriolus brachyrynchus",
    "33850": "Oriolus nigripennis",
    "33860": "Ortygospiza atricollis",
    "33870": "Ortyxelos meiffrenii",
    "33880": "Ptilopsis leucotis",
    "33890": "Otus senegalensis",
    "33891": "Otus pamelae",
    "33900": "Pachycoccyx audeberti",
    "33910": "Ploceus superciliosus",
    "33920": "Parmoptila woodhousei",
    "33930": "Melaniparus albiventris",
    "33940": "Melaniparus leucomelas",
    "33950": "Campocolinus albogularis",
    "33960": "Campocolinus coqui",
    "33970": "Peliperdix lathami",
    "33980": "Phoeniculus bollei",
    "33990": "Phoeniculus castaneiceps",
    "34000": "Phoeniculus purpureus",
    "34010": "Pholidornis rushiae",
    "34020": "Turdoides atripennis",
    "34030": "Phyllastrephus baumanni",
    "34040": "Phyllastrephus icterinus",
    "34050": "Phyllastrephus poensis",
    "34060": "Phyllastrephus poliocephalus",
    "34070": "Phyllastrephus xavieri",
    "34080": "Phyllolais pulchella",
    "34090": "Phylloscopus herberti",
    "34100": "Picathartes oreas",
    "34110": "Pinarocorys erythropygia",
    "34120": "Pitta angolensis",
    "34130": "Platalea alba",
    "34140": "Platysteira blissetti",
    "34160": "Platysteira concreta",
    "34170": "Plocepasser superciliosus",
    "34180": "Ploceus albinucha",
    "34190": "Ploceus aurantius",
    "34200": "Ploceus baglafecht",
    "34210": "Ploceus bannermani",
    "34220": "Ploceus bicolor",
    "34230": "Ploceus heuglini",
    "34240": "Ploceus insignis",
    "34250": "Ploceus luteolus",
    "34260": "Ploceus brachypterus",
    "34270": "Ploceus ocularis",
    "34280": "Ploceus pelzelni",
    "34290": "Ploceus tricolor",
    "34300": "Ploceus vitellinus",
    "34310": "Podica senegalensis",
    "34320": "Poeoptera lugubris",
    "34330": "Pogoniulus atroflavus",
    "34340": "Pogoniulus bilineatus",
    "34350": "Pogoniulus chrysoconus",
    "34360": "Pogoniulus coryphaea",
    "34370": "Pogoniulus pusillus",
    "34380": "Pogoniulus scolopaceus",
    "34390": "Pogoniulus subsulphureus",
    "34400": "Poicephalus gulielmi",
    "34410": "Poicephalus robustus",
    "34420": "Poicephalus senegalus",
    "34430": "Polemaetus bellicosus",
    "34440": "Poliolais lopezi",
    "34450": "Polyboroides typus",
    "34460": "Prinia fluviatilis",
    "34470": "Prinia subflava",
    "34480": "Prionops caniceps",
    "34490": "Prodotiscus insignis",
    "34500": "Prodotiscus regulus",
    "34510": "Psalidoprocne fuliginosa",
    "34530": "Psalidoprocne nitens",
    "34540": "Psalidoprocne obscura",
    "34550": "Pseudhirundo griseopyga",
    "34560": "Sylvia abyssinica",
    "34570": "Psittacus erithacus",
    "34580": "Pternistis ahantensis",
    "34600": "Pternistis clappertoni",
    "34610": "Pternistis squamatus",
    "34620": "Pterocles quadricinctus",
    "34630": "Pteronetta hartlaubii",
    "34640": "Ptilopachus petrosus",
    "34650": "Ptilostomus afer",
    "34660": "Pyrenestes ostrinus",
    "34670": "Phyllastrephus scandens",
    "34680": "Pytilia hypogrammica",
    "34690": "Pytilia melba",
    "34700": "Pytilia phoenicoptera",
    "34710": "Rhaphidura sabini",
    "34720": "Rhinopomastus aterrimus",
    "34730": "Rhinoptilus chalcopterus",
    "34740": "Neophedina cincta",
    "34750": "Sagittarius serpentarius",
    "34760": "Salpornis spilonota sensu lato",
    "34761": "Salpornis spilonota",
    "34762": "Salpornis salvadori",
    "34770": "Sarkidiornis melanotos",
    "34780": "Sarothrura boehmi",
    "34790": "Sarothrura elegans",
    "34800": "Sarothrura pulchra",
    "34810": "Sarothrura rufa",
    "34820": "Catriscus brevirostris",
    "34830": "Scotopelia bouvieri",
    "34840": "Scotopelia peli",
    "34850": "Crithagra burtoni",
    "34860": "Crithagra gularis",
    "34870": "Crithagra leucopygia",
    "34880": "Crithagra frontalis",
    "34890": "Sheppardia cyornithopsis",
    "34900": "Smithornis capensis",
    "34910": "Smithornis rufolateralis",
    "34920": "Smithornis sharpei",
    "34930": "Spermestes bicolor",
    "34940": "Spermestes cucullata",
    "34950": "Spermestes fringilloides",
    "34960": "Spiloptila clamans",
    "34970": "Aquila africana",
    "34980": "Sporopipes frontalis",
    "34990": "Sternula balaenarum",
    "35000": "Streptopelia decipiens",
    "35010": "Streptopelia hypopyrrha",
    "35020": "Strix woodfordii",
    "35030": "Sylvietta denti",
    "35040": "Tachymarptis aequatorialis",
    "35050": "Tauraco leucolophus",
    "35060": "Tauraco macrorhynchus",
    "35070": "Tauraco persa",
    "35080": "Tchagra australis",
    "35090": "Bocagia minuta",
    "35100": "Telacanthura melanopygia",
    "35110": "Telacanthura ussheri",
    "35120": "Chlorophoneus multicolor",
    "35140": "Terpsiphone rufocinerea",
    "35150": "Thalassornis leuconotus",
    "35160": "Thamnolaea cinnamomeiventris cinnamomiventris sensu lato",
    "35161": "Thamnolaea cinnamomeiventris",
    "35180": "Thescelocichla leucopleura",
    "35190": "Tigriornis leucolopha",
    "35200": "Lophoceros camurus",
    "35210": "Tockus kempi",
    "35220": "Lophoceros fasciatus sensu lato",
    "35221": "Lophoceros fasciatus",
    "35222": "Lophoceros semifasciatus",
    "35230": "Horizocerus hartlaubi",
    "35240": "Trachyphonus margaritatus",
    "35250": "Trachylaemus purpuratus",
    "35260": "Treron calvus",
    "35270": "Tricholaema hirsuta",
    "35280": "Trigonoceps occipitalis",
    "35290": "Trochocercus nitens",
    "35300": "Horizocerus albocristatus",
    "35310": "Turdoides plebejus",
    "35320": "Turdoides reinwardtii",
    "35330": "Turnix nanus",
    "35340": "Turtur abyssinicus",
    "35350": "Turtur brehmeri",
    "35380": "Urocolius macrourus",
    "35390": "Urolais epichlorus",
    "35400": "Urotriorchis macrourus",
    "35410": "Vanellus crassirostris",
    "35420": "Vanellus lugubris",
    "35430": "Vanellus senegallus",
    "35440": "Vanellus superciliosus",
    "35460": "Vidua chalybeata",
    "35470": "Vidua funerea",
    "35480": "Vidua interjecta",
    "35490": "Vidua larvaticola",
    "35500": "Vidua maryae",
    "35510": "Vidua nigeriae",
    "35520": "Vidua paradisaea",
    "35530": "Vidua raricola",
    "35540": "Vidua wilsoni",
    "35550": "Geokichla crossleyi",
    "35560": "Geokichla princei",
    "35570": "Zosterops senegalensis",
    "35580": "Lamprotornis superbus",
    "35590": "Eudynamys scolopaceus",
    "35610": "Chenonetta jubata",
    "35620": "Cereopsis novaehollandiae",
    "35630": "Dendrocincla fuliginosa",
    "35640": "Allenia fusca",
    "35660": "Rhea americana",
    "35670": "Pavo cristatus",
    "35680": "Thectocercus acuticaudatus",
    "35690": "Psittacara mitratus",
    "35700": "Psittacara erythrogenys",
    "35710": "Agapornis fischeri",
    "35720": "Alectroenas pulcherrimus",
    "35730": "Cinnyris dussumieri",
    "35740": "Foudia madagascariensis",
    "35750": "Foudia sechellarum",
    "35760": "Zosterops modestus",
    "35770": "Emberiza godlewskii",
    "35780": "Anas flavirostris",
    "35790": "Geopelia striata",
    "35800": "Geopelia placida",
    "35810": "Glaucidium cuculoides",
    "35830": "Spatula versicolor",
    "35840": "Emberiza sahari",
    "35850": "Chloephaga rubidiceps",
    "35860": "Habia rubica",
    "35880": "Eudyptes moseleyi",
    "35890": "Eudyptes chrysocome",
    "35900": "Pachyptila vittata",
    "35910": "Phoebetria fusca",
    "35920": "Dromaius novaehollandiae",
    "35930": "Acrocephalus sechellensis",
    "35940": "Pachyptila salvini sensu lato",
    "35941": "Pachyptila salvini",
    "35942": "Pachyptila macgillivrayi",
    "35950": "Dendrocygna viduata",
    "35980": "Larus armenicus",
    "35990": "Pterodroma deserta",
    "36000": "Diomedea dabbenena",
    "36010": "Rowettia goughensis",
    "36020": "Agapornis personatus",
    "36030": "Amazona aestiva",
    "36040": "Aratinga nenday",
    "36050": "Pycnonotus leucotis",
    "36060": "Pycnonotus cafer",
    "36070": "Poecile hyrcanus",
    "36080": "Columba iriditorques",
    "36090": "Schistolais leontica",
    "36100": "Ploceus nigerrimus",
    "36110": "Pyrenestes sanguineus",
    "36120": "Laniarius major",
    "36130": "Macrosphenus concolor",
    "36140": "Apalis sharpii",
    "36150": "Larus vegae sensu lato",
    "36160": "Crithagra mozambica",
    "36170": "Lophonetta specularioides",
    "36180": "Alaudala heinei",
    "36190": "Nannopterum harrisi",
    "36200": "Ceratopipra erythrocephala",
    "36210": "Sclerurus albigularis",
    "36220": "Mionectes oleagineus",
    "36240": "Pheugopedius rutilus",
    "36250": "Sicalis flaveola",
    "36260": "Sclateria naevia",
    "36270": "Manacus manacus",
    "36280": "Myrmotherula axillaris",
    "36290": "Tachyphonus rufus",
    "36300": "Loriotus luctuosus",
    "36310": "Momotus bahamensis",
    "36320": "Phylloscopus examinandus",
    "36330": "Eremalauda eremodites",
    "36340": "Merops nubicoides",
    "36350": "Strix mauritanica",
    "36360": "Otus cyprius",
    "36370": "Anarhynchus atrifrons",
    "36380": "Larus argentatus",
    "36390": "Anthus pallidiventris",
    "36400": "Caprimulgus fossii",
    "36410": "Cercotrichas leucophrys",
    "36420": "Cichladusa ruficauda",
    "36430": "Merops persicus",
    "36440": "Halcyon albiventris",
    "36450": "Merops bullockoides",
    "36460": "Turtur chalcospilos",
    "36470": "Campethera maculosa",
    "36480": "Quelea erythrops",
    "36490": "Ploceus melanogaster",
    "36500": "Phoebastria irrorata",
    "36510": "Cryptospiza reichenovii",
    "36520": "Prinia flaviventris",
    "36530": "Chamaetylas poliocephala",
    "36540": "Laniarius poensis",
    "36550": "Pogonornis minor",
    "36560": "Schistolais leucopogon",
    "36570": "Ploceus manyar",
    "36580": "Ploceus philippinus",
    "90010": "Anser erythropus x Branta leucopsis",
    "90011": "Anser erythropus x Branta leucopsis",
    "90012": "Anser erythropus x Branta leucopsis",
    "90020": "Anser anser x Branta canadensis",
    "90021": "Anser anser x Branta canadensis",
    "90022": "Anser anser x Branta canadensis",
    "90030": "Anser indicus x Branta leucopsis",
    "90031": "Anser indicus x Branta leucopsis",
    "90032": "Anser indicus x Branta leucopsis",
    "90040": "Branta canadensis x Branta leucopsis",
    "90041": "Branta canadensis x Branta leucopsis",
    "90042": "Branta canadensis x Branta leucopsis",
    "90050": "Anas platyrhynchos x Anas platyrhynchos var. domestica",
    "90051": "Anas platyrhynchos x Anas platyrhynchos var. domestica",
    "90052": "Anas platyrhynchos x Anas platyrhynchos var. domestica",
    "90060": "Falco peregrinus hybrid",
    "90070": "Lyrurus tetrix x Tetrao urogallus",
    "90071": "Lyrurus tetrix x Tetrao urogallus",
    "90072": "Lyrurus tetrix x Tetrao urogallus",
    "90080": "Larus argentatus x Larus hyperboreus",
    "90081": "Larus argentatus x Larus hyperboreus",
    "90082": "Larus argentatus x Larus hyperboreus",
    "90090": "Larus argentatus x Larus cachinnans",
    "90091": "Larus argentatus x Larus cachinnans",
    "90092": "Larus argentatus x Larus cachinnans",
    "90100": "Hirundo rustica x Delichon urbicum",
    "90101": "Hirundo rustica x Delichon urbicum",
    "90102": "Hirundo rustica x Delichon urbicum",
    "90110": "Phoenicurus ochruros x Phoenicurus phoenicurus",
    "90111": "Phoenicurus ochruros x Phoenicurus phoenicurus",
    "90112": "Phoenicurus ochruros x Phoenicurus phoenicurus",
    "90120": "Acrocephalus scirpaceus x Acrocephalus arundinaceus",
    "90121": "Acrocephalus scirpaceus x Acrocephalus arundinaceus",
    "90122": "Acrocephalus scirpaceus x Acrocephalus arundinaceus",
    "90130": "Ficedula sp. Hybrid",
    "90140": "Ficedula albicollis x Ficedula hypoleuca",
    "90141": "Ficedula albicollis x Ficedula hypoleuca",
    "90142": "Ficedula albicollis x Ficedula hypoleuca",
    "90150": "Cyanistes caeruleus x Cyanistes cyanus",
    "90151": "Cyanistes caeruleus x Cyanistes cyanus",
    "90152": "Cyanistes caeruleus x Cyanistes cyanus",
    "90160": "Spinus spinus hybrid",
    "90161": "Chloris chloris x Spinus spinus",
    "90170": "Hippolais icterina x Hippolais polyglotta",
    "90171": "Hippolais icterina x Hippolais polyglotta",
    "90172": "Hippolais icterina x Hippolais polyglotta",
    "90180": "Clanga pomarina x Clanga clanga",
    "90181": "Clanga pomarina x Clanga clanga",
    "90182": "Clanga pomarina x Clanga clanga",
    "90190": "Motacilla flava x Motacilla citreola",
    "90191": "Motacilla flava x Motacilla citreola",
    "90192": "Motacilla flava x Motacilla citreola",
    "90200": "Corvus cornix x Corvus corone",
    "90201": "Corvus cornix x Corvus corone",
    "90202": "Corvus cornix x Corvus corone",
    "90210": "Passer domesticus x Passer hispaniolensis",
    "90211": "Passer domesticus x Passer hispaniolensis",
    "90212": "Passer domesticus x Passer hispaniolensis",
    "90220": "Fringilla coelebs x Fringilla montifringilla",
    "90221": "Fringilla coelebs x Fringilla montifringilla",
    "90222": "Fringilla coelebs x Fringilla montifringilla",
    "90240": "Ardea cinerea x Ardea purpurea",
    "90241": "Ardea cinerea x Ardea purpurea",
    "90242": "Ardea cinerea x Ardea purpurea",
    "90250": "Aythya nyroca x Anas platyrhynchos",
    "90251": "Aythya nyroca x Anas platyrhynchos",
    "90252": "Aythya nyroca x Anas platyrhynchos",
    "90260": "Buteo buteo x Buteo rufinus",
    "90261": "Buteo buteo x Buteo rufinus",
    "90262": "Buteo buteo x Buteo rufinus",
    "90270": "Streptopelia turtur x Streptopelia decaocto",
    "90271": "Streptopelia turtur x Streptopelia decaocto",
    "90272": "Streptopelia turtur x Streptopelia decaocto",
    "90280": "Delichon urbicum x Riparia riparia",
    "90281": "Delichon urbicum x Riparia riparia",
    "90282": "Delichon urbicum x Riparia riparia",
    "90290": "Luscinia megarhynchos x Luscinia luscinia",
    "90291": "Luscinia megarhynchos x Luscinia luscinia",
    "90292": "Luscinia megarhynchos x Luscinia luscinia",
    "90300": "Acrocephalus palustris x Acrocephalus scirpaceus",
    "90301": "Acrocephalus palustris x Acrocephalus scirpaceus",
    "90302": "Acrocephalus palustris x Acrocephalus scirpaceus",
    "90310": "Passer domesticus x Passer montanus",
    "90311": "Passer domesticus x Passer montanus",
    "90312": "Passer domesticus x Passer montanus",
    "90320": "Larus fuscus x Larus michahellis",
    "90321": "Larus fuscus x Larus michahellis",
    "90322": "Larus fuscus x Larus michahellis",
    "90330": "Larus argentatus x Larus michahellis",
    "90331": "Larus argentatus x Larus michahellis",
    "90332": "Larus argentatus x Larus michahellis",
    "90340": "Acrocephalus palustris x Acrocephalus dumetorum",
    "90350": "Circus cyaneus x Circus macrourus",
    "90360": "Poecile montanus x Poecile cristatus",
    "90380": "Sylvia atricapilla x Sylvia borin",
    "90390": "Circus macrourus x Circus pygargus",
    "90400": "Dendrocopos major x Dendrocopos leucotos",
    "90410": "Poecile montanus x Periparus ater",
    "90420": "Saxicola maurus x Saxicola rubetra",
    "90430": "Poecile montanus x Poecile cinctus",
    "90440": "Hirundo rustica x Riparia riparia",
    "90450": "Gallinago media x Gallinago gallinago",
    "90460": "Ardea alba x Ardea cinerea",
    "90470": "Aythya ferina x Aythya nyroca",
    "90471": "Aythya ferina x Aythya nyroca",
    "90472": "Aythya ferina x Aythya nyroca",
    "90480": "Anas platyrhynchos x Anas acuta",
    "90481": "Anas platyrhynchos x Anas acuta",
    "90482": "Anas platyrhynchos x Anas acuta",
    "90490": "Branta leucopsis x Branta ruficollis",
    "90491": "Branta leucopsis x Branta ruficollis",
    "90492": "Branta leucopsis x Branta ruficollis",
    "90500": "Larus michahellis x Larus cachinnans",
    "90501": "Larus michahellis x Larus cachinnans",
    "90502": "Larus michahellis x Larus cachinnans",
    "90510": "Hirundo rustica x Cecropsis daurica",
    "90511": "Hirundo rustica x Cecropsis daurica",
    "90512": "Hirundo rustica x Cecropsis daurica",
    "90520": "Emberiza leucocephalos x Emberiza citrinella",
    "90521": "Emberiza leucocephalos x Emberiza citrinella",
    "90522": "Emberiza leucocephalos x Emberiza citrinella",
    "90530": "Chroicocephalus ridibundus x Ichthyaetus melanocephalus",
    "90531": "Chroicocephalus ridibundus x Ichthyaetus melanocephalus",
    "90532": "Chroicocephalus ridibundus x Ichthyaetus melanocephalus",
    "90540": "Passer hispaniolensis x Passer montanus",
    "90541": "Passer hispaniolensis x Passer montanus",
    "90542": "Passer hispaniolensis x Passer montanus",
    "90550": "Milvus milvus x Milvus migrans",
    "90560": "Stercorarius maccormicki x S. antarcticus",
    "90570": "Anser anser x Anser albifrons",
    "90580": "Anser anser x Anser cygnoides",
    "90590": "Anser anser x Anser indicus",
    "90600": "Anser indicus x Anser caerulescens",
    "90610": "Anser indicus x Anser cygnoides",
    "90620": "Anser cygnoides x Branta canadensis",
    "90630": "Anser caerulescens x Branta canadensis",
    "90640": "Anser albifrons x Branta leucopsis",
    "90650": "Anser caerulescens x Branta leucopsis",
    "90660": "Anser albifrons x Anser erythropus",
    "90670": "Anser sp. x Branta sp.",
    "90680": "Anser anser x Branta leucopsis",
    "90690": "Anser indicus x Branta canadensis",
    "90700": "Acrocephalus hybrid",
    "90710": "Anas platyrhynchos hybrid",
    "90720": "Larus fuscus x Larus cachinnans",
    "90730": "Larus fuscus x Larus argentatus",
    "90740": "Lanius collurio x Lanius senator",
    "90750": "Anser albifrons x Anser indicus",
    "90760": "Dendrocopos major x Dendrocopos syriacus",
    "90770": "Anas platyrhynchos x Aythya ferina",
    "90780": "Aytha hybrid",
    "90790": "Phylloscopus collybita x Phylloscopus trochilus",
    "90800": "Larus marinus x Larus argentatus",
    "90810": "Emberiza rustica x Emberiza pusilla",
    "90820": "Oenanthe pleschanka x Oenanthe hispanica",
    "90830": "Macronectes giganteus x Macronectes halli",
    "90840": "Sterna hirundo x Sterna paradisaea",
    "90850": "Buteo buteo x Buteo lagopus",
    "90860": "Regulus regulus x Regulus ignicapilla",
    "99931": "Unidentified duck",
    "99999": "Ring destroyed or lost",
}
