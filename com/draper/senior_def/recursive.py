def mysum1(L):
    if not L:
        return 0
    else:
        return L[0] + mysum1(L[1:])


print(mysum1(list(range(1, 101))))


def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])


print(mysum2(list(range(1, 101))))


def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])


print(mysum3(list(range(1, 101))))


def mysum4(L):
    first, *anoter = L
    return first if not anoter else first + mysum4(anoter)


print(mysum4(list(range(1, 101))))
