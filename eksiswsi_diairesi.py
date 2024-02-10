def die(ek: str) -> float:
    meloi = ek.split("=")
    melos2 = meloi[1].strip()
    melos1 = meloi[0].strip()
    b = int(melos2)
    aa = melos1.split("/")
    a = int(aa[1])
    lisi = b*a

    return lisi
