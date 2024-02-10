from eksiswsi_prosthesi import pro
from eksiswsi_afairesi import afr
from eksiswsi_diairesi import die
from eksiswsi_pollaplasiasmos import pol


def geniki_lisi(ek: str) -> int | float:
    if "+" in ek:
        lisi = pro(ek)
    elif "-" in ek:
        lisi = afr(ek)
    elif "*" in ek:
        lisi = pol(ek)
    elif "/" in ek:
        lisi = die(ek)
    else:
        lisi = "n/a"

    return lisi