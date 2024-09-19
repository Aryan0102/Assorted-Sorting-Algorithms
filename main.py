import matplotlib.pyplot as plt
import time
import sys
import random

sys.setrecursionlimit(100000)

def worstlst(x):
    lst = []
    for i in range(x):
        lst.append(x-i)
    return lst

def getGraph(name, functionName, worstcase, repeattime):
    x = 1
    prbsize = []
    timelst = []
    for i in range(repeattime):
        lst = worstcase(x * 100)
        prbsize.append(x * 100)
        x = x + 1
        time1 = time.time()
        functionName(lst)
        time2 = time.time()
        finaltime = time2 - time1
        timelst.append(finaltime)
    plt.plot(prbsize,timelst)
    plt.ylabel(name + " - Time")
    plt.xlabel(name + " - Problem Size")
    plt.show()

#print(listgenwcsen(10000))

def insertionsort(lst):
    for i in range(len(lst)):
        while lst[i] < lst[i - 1]:
            z = lst[i]
            lst[i] = lst[i-1]
            lst[i-1] = z
            if i != 1:
                i = i - 1
    return(lst)

timelst = []
x = 10

for i in range(4):
    time1 = time.time()
    holder = insertionsort(listgenwcsen(x))
    time2 = time.time()
    finaltime = time2 - time1
    print(finaltime)
    timelst.append(finaltime)
    x = x * 10

plt.plot(timelst)
plt.ylabel("Insertion Sort - Time")
plt.xlabel("Insertion Sort - Elements")
plt.show()

def bubblesort(lst):
    for j in range(len(lst) - 1):
        flag = False
        for i in range(len(lst) - 1 - j):
            if lst[i] > lst[i + 1]:
                holder = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = holder
                flag = True
        if not flag:
            break

    return lst

print(bubblesort([1,2,3,4,5]))

timelst = []
x = 10

for i in range(4):
    time1 = time.time()
    holder = bubblesort(listgenwcsen(x))
    time2 = time.time()
    finaltime = time2 - time1
    print(finaltime)
    timelst.append(finaltime)
    x = x * 10

plt.plot(timelst)
plt.ylabel("Bubble Sort - Time")
plt.xlabel("Bubble Sort - Elements")
plt.show()

def inversecascade(string):
    #print(string)
    if(len(string) > 1):
        inversecascade(string[:-1])

def cascade(string):
    if(len(string) > 1):
        cascade(string[:-1])
    #print(string)

cascade("dog")
inversecascade("dog")

def palindrome(word):
    print("Checking")
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        #return False
        return(palindrome(word[1:-1]))
    return False

#print(palindrome("racecar"))

def stringgen(x):
    str = ""
    half = x // 2
    for i in range(half):
        str += "("
    for i in range(half):
        str += ")"
    return str

openings = ["[","{","("]
closings = ["]","}",")"]

def parenthesisvalidator(parenthesis):
    returnstack = []
    for i in parenthesis:
        if i in openings:
            returnstack.append(i)
        elif i in closings:
            closingindex = closings.index(i)
            if returnstack[-1] == openings[closingindex]:
                returnstack.pop()
            else:
                return False
    if len(returnstack) > 0:
        return False
    return True

#print(parenthesisvalidator(""))

pairings = {"(":")","{":"}","[":"]"}
def parenthesisvalidator2(str):
    if len(str) % 2 == 1:
        return False
    if len(str) == 0:
        return True
    for i in range(len(str) // 2):
        for i in range(len(str) - 1):
            if str[i + 1] in closings and str[i] in openings:
                if pairings[str[i]] != str[i + 1]:
                    return False
                if i != 0 and i + 2 < len(str):
                    str = str[:i] + str[i + 2:]
                elif i == 0 and i + 2 < len(str):
                    str = str[i + 2:]
                elif i != 0 and i + 2 > len(str):
                    str = str[:i]
                else:
                    return True
                break
    return False

#print(parenthesisvalidator2(""))


def parenthesisvalidator3(str):
    if len(str) % 2 == 1:
        return False
    if len(str) == 0:
        return True
    for i in range(len(str) - 1):
        if str[i + 1] in closings and str[i] in openings:
            if pairings[str[i]] != str[i + 1]:
                return False
            return parenthesisvalidator3(str[:i] + str[i + 2:])
    return False

print(parenthesisvalidator3("{(((())))[}]"))

problemsizelst = []
timelst = []
x = 10

for i in range(3):
    problemsizelst.append(x)
    problem = stringgen(x)
    time1 = time.time()
    holder = parenthesisvalidator3(problem)
    time2 = time.time()
    finaltime = time2 - time1
    print(finaltime)
    timelst.append(finaltime)
    x = x * 10

plt.plot(problemsizelst,timelst)
plt.ylabel("Parenthesis Validator3 - Time")
plt.xlabel("Parenthesis Validator3 - Elements")
plt.show()

#recursion depth reached after 3

"""
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel("some numbers")
plt.show()
"""

"""
to plot x versus y:
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
"""

def merge(lst1,lst2):
    returnlst = []
    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] < lst2[0]:
            returnlst.append(lst1[0])
            lst1.pop(0)
        elif lst1[0] > lst2[0]:
            returnlst.append(lst2[0])
            lst2.pop(0)

    return returnlst + lst1 + lst2

# print((merge([1,2,3],[4,5,6])))

# def split(lst):
#     middle = len(lst) // 2
#     if len(lst) <= 1:
#         print(lst) # return lst
#     else:
#         split(lst[:middle]) # sort (recursion) then merge
#         split(lst[middle:]) # big O
#
# split([3,8,1,4,6,5,2])

def mergesort(lst):
    middle = len(lst) // 2
    if len(lst) <= 1:
        return(lst)

    list1 = mergesort(lst[:middle])
    list2 = mergesort(lst[middle:])
    return merge(list1,list2)

#print(mergesort([8,7,6,5,8,7,6,5]))

#mat plot lib graph

# x = 1
# prbsize = []
# timelst = []
# for i in range(100):
#     lst = worstlst(x * 100)
#     prbsize.append(x * 100)
#     x = x + 1
#     time1 = time.time()
#     mergesort(lst)
#     time2 = time.time()
#     finaltime = time2 - time1
#     timelst.append(finaltime)
# plt.plot(prbsize,timelst)
# plt.ylabel("Mergesort - Time")
# plt.xlabel("Mergesort - Problem Size")
# plt.show()

def swap(lst,x,y):
    x2 = lst[x]
    lst[x] = lst[y]
    lst[y] = x2

def shuffle(lst):
    for i in range(10000):
        elem1 = random.randint(0, len(lst) - 1)
        elem2 = random.randint(0, len(lst) - 1)
        swap(lst, elem1, elem2)

def quicksort2(lst, start, end):
    if(start >= end):
        return

    pivot = random.randint(start, end - 1)
    swap(lst, pivot, end)
    pivot = end
    lower = start
    upper = end - 1
    while lower <= upper:
        while lst[lower] < lst[pivot] and lower <= upper:
            lower = lower + 1
        while lst[upper] >= lst[pivot] and upper >= lower:
            upper = upper - 1
        if(lower <= upper):
            swap(lst, lower, upper)

    swap(lst, lower, pivot)

    quicksort2(lst, start, lower - 1)
    quicksort2(lst, lower + 1, end)

def quicksort(lst):
    shuffle(lst)
    quicksort2(lst, 0, len(lst) - 1)

lst = worstlst(10000) # reverse order
print(lst)
quicksort(lst)
print(lst)

getGraph("QuickSort", quicksort, worstlst, 10000)
