import io


def sum(l: list[float]) -> float:
    s : int = 0

    for i in range(len(l)):
        s = s + l[i]

    return s


def average(l: list[float]) -> float :
    return sum(l) / len(l)   



path : str = "C:\\Users\\User\\OneDrive\\Υπολογιστής\\test.txt"


def list_from_file(path : str) -> list[float]:
    with open(path, "r") as file:
        return [float(line) for line in file.readlines()]



r1 : list[float] = list_from_file(path)

print(r1)

avg1 : float = average(r1)


print(avg1)

