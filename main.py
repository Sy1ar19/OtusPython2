import random


def main():
    print(sum1(1, 6))
    print(list_comp(5, 10))
    print(seq_list_comp(5))
    print(rand_list_comp(5))
    print(positive_list_comp(rand_list_comp(5)))
    #ser_input_list_comprehension()
    matrix(3, 5)


def sum1(a, b):
    return a + b


def list_comp(number, count):
    return [number for i in range(count)]


def seq_list_comp(count):
    return [i for i in range(1, count + 1)]


def positive_list_comp(s):
    a = [random.randint(-10, 10) for i in range(1, 5 + 1)]
    print(a)
    b = [abs(elem) for elem in a]
    print(b)
    return [abs(elem) for elem in a]


def rand_list_comp(count):
    return [random.randint(-10, 10) for i in range(1, count + 1)]


def user_input_list_comprehension():
    a = input().split()
    a = [int(i) for i in a]
    print(a)


def matrix(n, m):
    a = [[0] * m for i in range(n)]

    for i in a:
        print(i)


main()
