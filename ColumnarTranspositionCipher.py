import CryptographyTools as ct

# text = input("Ciphertext: ")
ciphertext = ("ROREP MRTFO AMISS SEISI SETYL ILTHE YRBRA GAOUR HSENT OCAVE TEMPL EHEDT QNIRE EIUIR ADSAN WOREN OPINA OISIT "
        "ERNTO TTPOR FRHEI NIIND EHGST SEYAR RAUMM BDISE WWELO LUEWO AHDBE OTPPY FETAK EHURT TSRIN ITRUC FIONS RPYOU "
        "TREFE MROTE ETINA NITHE ITVES OIGAT TWNNO EWHEN DLWOU ARBEG LUTEF CETOR NEEIV IFOTI OICAT HTNSO CEATW TEANS "
        "OYTLE CCURA ATOUN OBTHE SADYW OTTHA UOFAY NANGM ORAPP TAXIM WTELY TYENT YEHRE OSEAR TILDW NOHBL RIDHA DAAND "
        "NIIST EVCTI ORSCA LSNHI HCEFT ONEEK EBMEM TFRSO UOHEH LOSEH OPDRE KDRTE NINOW AHGOR AGVIN CENYR CEOLL ONTIO "
        "TEFME IWING MITHH ACBHE DERRI PANOP OSERS SAITW OPNOT LBSSI SEETO ILTAB SISHH TNIDE TAITY STTHA OETAG EEFTH "
        "RINQU HTYWI ECANY NIRTA TLTYA HGHOU TSTHE FOYLE HSHIS NAOES MEDTH EUARQ SIOFH EKPOC CTTWA ERHWE POEUR USEAN "
        "TSGGE HTING WEATH LEASW VALTR DEELL UQCEN SEIRI EHATT LALOC IRCAR OCAGE YNMPA DLYIE EHEDT ROINF OIMAT TANTH "
        "DAHEH VIARR ANEDO HCCOA NMFRO ROEWY DEKTH FEAYB IHORE YDSBO IDWAS EVSCO HDRED AMISI SAGEW NINOT OROUR GSGUE "
        "REALL WTYBU EDEAD DEDTH IRESC NOPTI ICAND ALRCU TITED RUTOO OYNEW FFRKO AEICE BDIDE DEYTH NIIST EVCTI RUNAT "
        "HTEOF NUEYO SNGMA AEAPP ECRAN GAOUR WSENT BAERE FOLET WOOLL RTHIS ABAIL EOCKT ISLLI DNSLA ERWHE DAHEH VIARR "
        "TNEDO PSHES ASARI CPSHI IYARR AENGN WTRLY DNOHU APRED GNSSE RFERS UOOMS PMTHA NETON DNGLA CEFTH SNABI RFTAF "
        "LLECA APOUR GNSSE RSERA REATH ULREC SESIV REUFF RFING CIOMS SSKNE UMFOR TFCHO YOHEV RGAGE DRECO MOSFR HSTHE "
        "NIIPP PMGCO HSANY AHOWT RTTHE LLAVE DNEDU EHERT SENAM ELTAN ELYIS TDSAN IHHAT SSSPA AHAGE NEDBE FDPAI AYORB "
        "SKBOO NIHOP MSTHE AHALL IHMPS LIREV OELAG ERFAL DRSFO ELHIS NSSWA ONOTK TOWNT COHEL NOALC UBSTA BYLAR EHUTT "
        "SKBOO AWHOP IMSOF NINOR SETER EBTAS SESID LAASM PTLBU TIROF TEABL IERAD UCNIN LUNAB AWAIT OSSAL EPSUS ODCTE "
        "DAFTR NIING SMITE AHWIT DEMOR UOUBI VOSPR CNENA WEEIW NUERE TEABL EVOIN AGSTI RUTEO EJSUB RUCTF WRTHE UOITH "
        "RETAL TGTIN OOHEB LLKSE OOERT TNURI TSERE ROSOF EWNOW PEHAV DEAUS NETHE YRQUI OYJIF EVUHA ERANY TNASO ILOBE "
        "HTEVE EHATT FKBOO NDOUN OTEXT OBTHE DADYH ITPAR RACUL EUVAL AHORT RUTYO ELCOL NOCTI ULINC TIDES HWEMS IMICH "
        "AHGHT TTVEA ETRAC AEDTH TNTTE FOION REINT OINAT OBNAL UMOKS REGGL NESTH GIITM WEHTB EHORT DNXTE HTING EVEIN "
        "AGSTI TNTIO EVOCO BERTH ESOOK SRLLE HTBUT DIEEV WEENC EVEHA EHGAT OSRED SIFAR CYONL MUIRC TNSTA NAIAL CEDTH "
        "OSOST TRFFU NEHER IRQUI UOESC SELDB ATUBS LANTI")
ciphertext = ct.format_ciphertext(ciphertext)

# the idea here, is to guess a keyword length - then, split it into columns and perform digram analysis
# try different ones until it seems similar to english
# https://homepages.math.uic.edu/~leon/mcs425-s08/handouts/breaking_tranposition_cipher.pdf


def score_column_pair(column1: str, column2: str) -> float | str:
    """Returns a value based on how likely 2 columns are to be next to each other."""
    if column1 == column2:
        return "N/A"

    column1, column2, size = ct.trim_to_shared_size(column1, column2)
    total = 0
    for l, m in zip(column1, column2):
        total += ct.digram_scores_dict[f"{l}{m}"]
    return total / size


def evaluate_ciphertext(text: str, try_length: int) -> list[list[float | str]]:
    """Evaluate all pairs of columns in ciphertext. Takes the key length and text to evaluate."""
    columns = ct.split_cosets(text, try_length)

    results = [[] for i in range(try_length)]
    for i, column1 in enumerate(columns):
        for column2 in columns:
            score = score_column_pair(column1, column2)
            results[i].append(score)
    return results


print(evaluate_ciphertext(ciphertext, 4))

def format_results(results: list):
    """Prints the results of the ciphertext evaluation in a readable way."""





















