from multiprocessing import Pool


def f(a):
    print a * a
    return a * a


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
p = Pool(5)
b = p.map(f, a)
print b
