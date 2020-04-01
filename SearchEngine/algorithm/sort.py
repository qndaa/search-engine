

# ------------------------- Merge sort -------------------------------------
def merge_sort(result, low, high):
    if low < high:
        mid = int(low + (high-low) / 2)

        merge_sort(result, low, mid)
        merge_sort(result, mid+1, high)

        merge(result, low, mid, high)


def merge(result, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    left = list()
    right = list()

    for i in range(0, n1):
        left.append(result[low + i])

    for i in range(0, n2):
        right.append(result[mid + 1 + i])

    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1


# -------------------------- Heap sort --------------------------------
def heap_sort(result):
    n = len(result)

    for i in range(n, -1, -1):
        heapify(result, n, i)

    for i in range(n-1, 0, -1):
        result[i], result[0] = result[0], result[i]
        heapify(result, i, 0)


def heapify(result, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and result[i][1] > result[l][1]:
        smallest = l

    if r < n and result[smallest][1] > result[r][1]:
        smallest = r

    if smallest != i:
        result[i], result[smallest] = result[smallest], result[i]

        heapify(result, n, smallest)


# -------------------------- Bubble sort --------------------------------
def bubble_sort(result):
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j][1] < result[j+1][1]:
                result[j], result[j+1] = result[j+1], result[j]


# -------------------------- Insertion sort --------------------------------
def insertion_sort(result):
    for i in range(1, len(result)):
        key = result[i]
        j = i-1
        while j >= 0 and result[j][1] < key[1]:
            result[j+1] = result[j]
            j -= 1
        result[j+1] = key
