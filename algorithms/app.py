def minimum(arr):
    if len(arr) == 0:
        return None
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num


def maximum(arr):
    if len(arr) == 0:
        return None
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num


def min_max(arr):
    if len(arr) == 0:
        return None
    min_num = arr[0]
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return min_num, max_num


def binary(x):
    result = ''
    if x == 0:
        return '0'
    while x > 0:
        if x % 2 == 0:
            result += '0'
        elif x % 2 != 0:
            result += '1'
        x = x // 2
    return result[::-1]


def nwd(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a


def nww(a, b):
    return a * b / nwd(a, b)


def czynniki(a):
    a = int(a)
    k = 2
    odp = []
    while a > 1:
        while a % k == 0:
            odp.append(k)
            a /= k
        k += 1
    return odp


def bubble_sort(arr):
    for i in range(len(arr)):
        changed = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changed = True
        if not changed:
            break
    return arr


def selection_sort(arr):
    for i in range(len(arr) - 1):
        i_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i_min]:
                i_min = j
        if i_min != i:
            arr[i], arr[i_min] = arr[i_min], arr[i]
    return arr


def insertion_sort(arr):
    for j in range(1, len(arr)):
        while arr[j] < arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


tab = [10, 16, 25, 5, 20, 10, 10, 2, 3, 2, 5]

#print(minimum(tab))
#print(maximum(tab))
#print(min_max(tab))
#print(binary(7))
#print(nwd(5, 15))
#print(nww(10, 15))
#print(czynniki(768))
#print(bubble_sort(tab))
print(selection_sort(tab))
print(insertion_sort(tab))
