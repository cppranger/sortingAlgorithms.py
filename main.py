from random import randint, shuffle
from time import time
from prettytable import PrettyTable
from colorama import Fore, Back, Style


def printPrettyTable(results: tuple, n: tuple):
    myTable = PrettyTable()
    myTable.field_names = ("#", "Built-in Sort", "Bubble Sort", "Selection Sort", "Insertion Sort",
                           "Merge Sort", "Quick Sort", "Bogo Sort")

    for i, cur_n in enumerate(n):
        if type(results[0][i]) != str:
            results[0][i] = round(results[0][i], 3)
        if type(results[1][i]) != str:
            results[1][i] = round(results[1][i], 3)
        if type(results[2][i]) != str:
            results[2][i] = round(results[2][i], 3)
        if type(results[3][i]) != str:
            results[3][i] = round(results[3][i], 3)
        if type(results[4][i]) != str:
            results[4][i] = round(results[4][i], 3)
        if type(results[5][i]) != str:
            results[5][i] = round(results[5][i], 3)
        if type(results[6][i]) != str:
            results[6][i] = round(results[6][i], 3)
        myTable.add_row([cur_n, results[0][i],
                         results[1][i], results[2][i], results[3][i], results[4][i], results[5][i], results[6][i]])

    print(Style.RESET_ALL, end="")
    print(myTable)


def sortingBenchmark(n=(10, 100, 1000, 10000)):
    builtinBenchmark = []
    bubbleBenchmark = []
    selectionBenchmark = []
    insertionBenchmark = []
    mergeBenchmark = []
    quickBenchmark = []
    bogoBenchmark = []

    for length in n:
        numbs = generateRandomList(length, length)
        print(Fore.BLUE + "Generated list is:", numbs)

        print(Fore.YELLOW + "Starting built-in sorting...")
        t0 = time()
        builtinSorted = sorted(numbs)
        t1 = time()
        builtinBenchmark.append(t1 - t0)
        print(Fore.GREEN + "Built-in sorting complete!")

        print(Fore.YELLOW + "Starting bubble sorting...")
        t0 = time()
        bubbleSorted = bubbleSort(numbs)
        t1 = time()
        if isSorted(bubbleSorted):
            print(Fore.GREEN + "Bubble sorting complete!")
            bubbleBenchmark.append(t1 - t0)
        else:
            print(Fore.RED + "Sorting wasn't successful")
            bubbleBenchmark.append("Error!")

        print(Fore.YELLOW + "Starting selection sorting...")
        t0 = time()
        selectionSorted = selectionSort(numbs)
        t1 = time()
        selectionBenchmark.append(t1 - t0)
        if isSorted(selectionSorted):
            print(Fore.GREEN + "Selection sorting complete!")
        else:
            print(Fore.RED + "Sorting wasn't successful")
            selectionBenchmark.append("Error!")
        print()

        print(Fore.YELLOW + "Starting insertion sorting...")
        t0 = time()
        insertionSorted = insertionSort(numbs)
        t1 = time()
        insertionBenchmark.append(t1 - t0)
        if isSorted(insertionSorted):
            print(Fore.GREEN + "Insertion sorting complete!")
        else:
            print(Fore.RED + "Sorting wasn't successful")
            insertionBenchmark.append("Error!")
        print()

        print(Fore.YELLOW + "Starting merge sorting...")
        t0 = time()
        mergeSorted = mergeSort(numbs)
        t1 = time()
        mergeBenchmark.append(t1 - t0)
        if isSorted(mergeSorted):
            print(Fore.GREEN + "Merge sorting complete!")
        else:
            print(Fore.RED + "Sorting wasn't successful")
            mergeBenchmark.append("Error!")
        print()

        print(Fore.YELLOW + "Starting quick sorting...")
        t0 = time()
        quickSorted = quickSort(numbs)
        t1 = time()
        quickBenchmark.append(t1 - t0)
        if isSorted(quickSorted):
            print(Fore.GREEN + "Quick sorting complete!")
        else:
            print(Fore.RED + "Sorting wasn't successful")
            quickBenchmark.append("Error!")
        print()

        print(Fore.YELLOW + "Starting bogo sorting...")
        t0 = time()
        bogoSorted = bogoSort(numbs)
        t1 = time()
        bogoBenchmark.append(t1 - t0)
        if isSorted(bogoSorted):
            print(Fore.GREEN + "Bogo sorting complete!")
        else:
            print(Fore.RED + "Sorting wasn't successful")
            bogoBenchmark.append("Error!")
        print()

    printPrettyTable((builtinBenchmark, bubbleBenchmark, selectionBenchmark, insertionBenchmark,
                      mergeBenchmark, quickBenchmark, bogoBenchmark), n)


def isSorted(numbs: list):
    return numbs == sorted(numbs)


def generateRandomList(n=10, max_number=10):
    numbs = []
    for i in range(n):
        numbs.append(randint(0, max_number))
    return numbs


def bubbleSort(numbs: list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(numbs)):
            if numbs[i - 1] > numbs[i]:
                numbs[i], numbs[i - 1] = numbs[i - 1], numbs[i]
                swapped = True
    return numbs


def selectionSort(numbs: list):
    sort_len = 0
    while sort_len < len(numbs):
        min_index = None
        for i, elem in enumerate(numbs[sort_len:]):
            if min_index is None or elem < numbs[min_index]:
                min_index = i + sort_len
        numbs[sort_len], numbs[min_index] = numbs[min_index], numbs[sort_len]
        sort_len += 1
    return numbs


def insertionSort(numbs: list):
    for sort_len in range(1, len(numbs)):
        cur_item = numbs[sort_len]
        insert_index = sort_len
        while insert_index > 0 and cur_item < numbs[insert_index-1]:
            numbs[insert_index] = numbs[insert_index-1]
            insert_index += -1
        numbs[insert_index] = cur_item
    return numbs


def merge(numbs_1: list, numbs_2: list):
    numbs_sorted = []
    one_index, two_index = 0, 0
    while one_index < len(numbs_1) and two_index < len(numbs_2):
        if numbs_1[one_index] < numbs_2[two_index]:
            numbs_sorted.append(numbs_1[one_index])
            one_index += 1
        else:
            numbs_sorted.append(numbs_2[two_index])
            two_index += 1
    if one_index == len(numbs_1):
        numbs_sorted.extend(numbs_2[two_index:])
    else:
        numbs_sorted.extend(numbs_1[one_index:])
    return numbs_sorted


def mergeSort(numbs: list):
    if len(numbs) <= 1:
        return numbs
    left, right = mergeSort(numbs[:len(numbs) // 2]), mergeSort(numbs[len(numbs) // 2:])
    return merge(left, right)


def quickSort(numbs: list):
    if len(numbs) <= 1:
        return numbs
    smaller, equal, larger = [], [], []
    pivot = numbs[randint(0, len(numbs)-1)]
    for x in numbs:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quickSort(smaller) + equal + quickSort(larger)


def bogoSort(numbs: list):
    ct = 0
    while not isSorted(numbs):
        shuffle(numbs)
        ct += 1
    tries = str(ct)
    print("It took " + tries + " tries to sort!")
    return numbs


if __name__ == '__main__':
    running = True
    while running:
        print(Fore.BLUE + "Hello, dear User!")
        print("What can i do for you?")
        print(Fore.GREEN +
              "1. Start sorting benchmark (all available algorithms);\n"
              "2. Start bubble sort;\n"
              "3. Start selection sort;\n"
              "4. Start insertion sort;\n"
              "5. Start merge sort;\n"
              "6. Start quick sort;\n"
              "7. Start bogo sort;\n"
              "0. Exit.")
        answer = int(input())
        if answer == 1:
            sortingBenchmark()
            input("Press any key to continue...")
        elif answer == 2:
            numbers = generateRandomList()
            print("Generated list:", numbers)
            numbers = bubbleSort(numbers)
            print("Sorted list:", numbers)
            print("The list is successfully sorted!") if isSorted(numbers) else print("The list isn't sorted!")
            input("Press any key to continue...")
        elif answer == 3:
            numbers = generateRandomList()
            print("Generated list:", numbers)
            numbers = selectionSort(numbers)
            print("Sorted list:", numbers)
            print("The list is successfully sorted!") if isSorted(numbers) else print("The list isn't sorted!")
            input("Press any key to continue...")
        elif answer == 4:
            numbers = generateRandomList()
            print("Generated list:", numbers)
            numbers = insertionSort(numbers)
            print("Sorted list:", numbers)
            print("The list is successfully sorted!") if isSorted(numbers) else print("The list isn't sorted!")
            input("Press any key to continue...")
        elif answer == 5:
            numbers = generateRandomList()
            print("Generated list:", numbers)
            numbers = mergeSort(numbers)
            print("Sorted list:", numbers)
            print("The list is successfully sorted!") if isSorted(numbers) else print("The list isn't sorted!")
            input("Press any key to continue...")
        elif answer == 6:
            numbers = generateRandomList()
            print("Generated list:", numbers)
            numbers = quickSort(numbers)
            print("Sorted list:", numbers)
            print("The list is successfully sorted!") if isSorted(numbers) else print("The list isn't sorted!")
            input("Press any key to continue...")
        elif answer == 7:
            numbers = generateRandomList()
            print("Generated list:", numbers)
            numbers = bogoSort(numbers)
            print("Sorted list:", numbers)
            print("The list is successfully sorted!") if isSorted(numbers) else print("The list isn't sorted!")
            input("Press any key to continue...")
        elif answer == 0:
            print("Good bye!")
            running = False
        else:
            print("Please, enter a valid number!")
            print()

# numbers = generateRandomList()
# print("Generated list:", numbers)
# numbers = bogoSort(numbers)
# print("Sorted list:", numbers)
# print("The list is successfully sorted!") if isSorted(numbers) else print("The list isn't sorted!")

# sortingBenchmark()
