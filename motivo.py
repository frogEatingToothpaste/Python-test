

sum1 = 0
sum2 = 0


def klasma(ar: float, pa: float) -> float:
    return ar / pa


def ar_pa_motivo1(n: int):
    arithmitis = 1
    paronomastis = 2 * (n + 1)

    return arithmitis, paronomastis


def ar_pa_motivo2(n: int):
    arithmitis = 2 * (n + 1) - 1
    paronomastis = 4 * (n + 1)

    return arithmitis, paronomastis



for i in range(20):
    arithmitis, paronomastis = ar_pa_motivo1(i)
    
    sum1 = sum1 + klasma(arithmitis, paronomastis)

sum1 = sum1 / 4

for i in range(20):
    arithmitis, paronomastis = ar_pa_motivo2(i)

    sum2 = sum2 + klasma(arithmitis, paronomastis)


sum2 = sum2 / 2

print (sum1 + sum2)