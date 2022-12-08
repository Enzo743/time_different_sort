# Algorithme pour calculer le temps mis par différents algorithmes de tri à trier une liste de tailles variables
from time import *
import random
import matplotlib.pyplot as plt
import numpy as np
import sys
import math

sys.setrecursionlimit(9999)

result_sort = []
result_sorted = []
result_quick = []
result_insert = []
result_bubble = []
result_fusion = []
result_select = []
result_count = []
result_comb = []
n_list = []
n2_list = []

def list_create(x):
    blank_list = []

    if x == 1000:
        n_list.append(i * x)
    else:
        n2_list.append(i * x)

    for k in range(i * x):
        blank_list.append(random.randint(0, 100))
    return blank_list


def quicksort(array):
    left = []
    equal = []
    right = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(left) + equal + quicksort(greater)
    else:
        return array


def insert_sort(insert):
    for j in range(1, len(insert)):
        key = insert[j]
        i = j - 1

        while i > 0 and insert[i] > key:
            insert[i+1] = insert[i]
            i = i - 1
        insert[i+1] = key


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

# Tri par fusion
def fusion_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    a = fusion_sort(arr[:middle])
    b = fusion_sort(arr[middle:])

    return merge(a, b)

def merge(a, b):
    c = []

    while len(a) and len(b):
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    c.extend(a) if len(a) else c.extend(b)
    return c


def select_sort(select):
    min = i

    for j in range(i+1, len(select)):
        if select[min] > select[j]:
            min = j

    tmp = select[i]
    select[i] = select[min]
    select[min] = tmp


def count_sort(A, k):
    output = [0] * len(A)

    freq = [0] * (k + 1)

    for i in A:
        freq[i] = freq[i] + 1

    total = 0
    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount

    for i in A:
        output[freq[i]] = i
        freq[i] = freq[i] + 1

    for i in range(len(A)):
        A[i] = output[i]


def comb_sort(array):
    permutation = True
    gap = len(array)

    while (permutation == True) or (gap > 1):
        permutation = False
        gap = math.floor(gap / 1.3)
        if gap<1: gap = 1

        for en_cours in range(0, len(array) - gap):
            if array[en_cours] > array[en_cours + gap]:
                permutation = True
                array[en_cours], array[en_cours + gap] = \
                array[en_cours + gap],array[en_cours]
    return array


def sort_time(sort_list):
    t1 = time()
    sort_list.sort()
    t2 = time()
    delta = t2 - t1
    result_sort.append(delta)
    random.shuffle(sort_list)


def sorted_time(sorted_list):
    t1 = time()
    filter_sorted = sorted(sorted_list)
    t2 = time()
    delta = t2 - t1
    result_sorted.append(delta)


def quick_time(quick_list):
    t1 = time()
    quicksort(quick_list)
    t2 = time()
    delta = t2 - t1
    result_quick.append(delta)
    random.shuffle(quick_list)


def insert_time(insert_list):
    t1 = time()
    insert_sort(insert_list)
    t2 = time()
    delta = t2 - t1
    result_insert.append(delta)
    random.shuffle(insert_list)


def bubble_time(bubble_list):
    t1 = time()
    bubble_sort(bubble_list)
    t2 = time()
    delta = t2 - t1
    result_bubble.append(delta)
    random.shuffle(bubble_list)


def fusion_time(fusion_list):
    t1 = time()
    fusion_sort(fusion_list)
    t2 = time()
    delta = t2 - t1
    result_fusion.append(delta)
    random.shuffle(fusion_list)


def select_time(select_list):
    t1 = time()
    select_sort(select_list)
    t2 = time()
    delta = t2 - t1
    result_select.append(delta)
    random.shuffle(select_list)


def count_time(count_list):
    t1 = time()
    count_sort(count_list, 100)
    t2 = time()
    delta = t2 - t1
    result_count.append(delta)
    random.shuffle(count_list)


def comb_time(comb_list):
    t1 = time()
    comb_sort(comb_list)
    t2 = time()
    delta = t2 - t1
    result_comb.append(delta)
    random.shuffle(comb_list)


def model(num1, num2, inter, n, list, color):
    x = np.array([i for i in range(num1, num2, inter)])
    y = np.array(list)
    model = np.polyfit(x, y, 2)
    poly = np.poly1d(model)
    return plt.plot(n, poly(x), color=color, label="modèle y="+str(round(model[0], 10))+"x**2 + "+str(round(model[1], 10))+"x + "+str(round(model[2], 5)))


def graphical(y1, y2, y3, y4, y5, y6, y7, y8, y9, x, x2):
    plt.figure(figsize = (16, 10))
    plt.plot(x, y4, marker="p", color="magenta", linestyle="None", label="insertion")
    plt.plot(x, y5, marker="h", color="darkorange", linestyle="None", label="bubble")
    plt.plot(x, y6, marker="D", color="indigo", linestyle="None", label="fusion")
    plt.plot(x, y9, marker="s", color="gold", linestyle="None", label="peigne")
    model(1000, 11000, 1000, x, y4, "magenta")
    model(1000, 11000, 1000, x, y5, "darkorange")
    model(1000, 11000, 1000, x, y6, "indigo")
    model(1000, 11000, 1000, x, y9, "gold")
    plt.xlabel('n')
    plt.ylabel('Durée (en seconde)')
    plt.title("Résultats des différents tris (les + lents) effectués")
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize = (16, 10))
    plt.plot(x2, y1, marker="+", color="blue", linestyle="None", label="sort")
    plt.plot(x2, y2, marker="x", color="red", linestyle="None", label="sorted")
    plt.plot(x2, y3, marker="o", color="green", linestyle="None", label="rapide récurrsif")
    plt.plot(x2, y7, marker="P", color="lime", linestyle="None", label="selection")
    plt.plot(x2, y8, marker="^", color="navy", linestyle="None", label="comptage")
    model(50000, 550000, 50000, x2, y1, "blue")
    model(50000, 550000, 50000, x2, y2, "red")
    model(50000, 550000, 50000, x2, y3, "green")
    model(50000, 550000, 50000, x2, y7, "lime")
    model(50000, 550000, 50000, x2, y8, "navy")
    plt.xlabel('n')
    plt.ylabel('Durée (en seconde)')
    plt.title("Résultats des différents tris (les + rapides) effectués")
    plt.grid(True)
    plt.legend()
    plt.show()


for i in range(1, 11):
    print(i)
    L = list_create(1000)
    L2 = list_create(50000)
    sort_time(L2)
    sorted_time(L2)
    quick_time(L2)
    insert_time(L)
    bubble_time(L)
    fusion_time(L)
    select_time(L2)
    count_time(L2)
    comb_time(L)

graphical(result_sort, result_sorted, result_quick, result_insert, result_bubble, result_fusion, result_select, result_count, result_comb, n_list, n2_list)
