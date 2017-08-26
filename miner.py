import numpy as np
import timeit


def vectorAdd(a, b, c):
    for i in range(a.size):
        c[i] = a[i] + b[i]


def main():
    N = 32000000

    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    start = timeit.default_timer()
    vectorAdd(A, B, C)
    vectoradd_time = timeit.default_timer() - start

    print("C[:5] = " + str(C[:5]))
    print("C[-5:] = " + str(C[-5:]))

    print("VectorAdd took %f seconds" % vectoradd_time)


if __name__ == '__main__':
    main()
