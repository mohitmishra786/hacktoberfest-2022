# name : blurryface

def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)


if __name__ == "__main__":
    print(fibbonaci(10))