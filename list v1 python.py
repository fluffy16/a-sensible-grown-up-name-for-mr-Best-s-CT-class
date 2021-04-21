"""
program goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input th INTs from STRs
3.We need to provide choices to the user
    a. Add more values to the list
    b. Return a value at a specific index
"""
myList = []
uniqueList = []
def mainProgram():
    while True:
        try:
            print("Hello, there! let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to a list or
2. add a bunch of numbers
3. Return the value at an index 
4. sort list
5. random search
6. linear search
7. recursive binary search
8. iterative binary search
9. print list
10. quit    """)
        if choice == "1":
            addToList ()
        elif choice == "2":
            addABunch()
        elif choice == "3":
            indexValues()
        elif choice == "4":
            sortList(myList)
        elif choice == "5":
            randomsearch()
        elif choice == "6":
            linearSearch
        elif choice == "7":
            binSearch = input("what number are you looking for? ")
            recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(binSearch))
        elif choice == "8":
            binSearch = input("what number are you looking for? ")
            result = iterativeBinarySearch(uniqueList, int(binSearch))
            if result !=-1:
                print"your number is at index position {}".format(result))
            else:
                print("your number is not in that list, bud!")
            
        elif choice == "9":
            printLists()
        else:
            break
            
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("type an integer here!     ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("how many new integers would you like to add?   ")
    numRange = ("and how high would you like these numbers to go?    ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")
    
def indexValues():
    print("Ohhhh! I heard you need a particular piece of data!")
    indexPos =  input ("What index position are you curious about?    ")
    print(myList[int(indexpos)])

def sortList(myList):
    print("a little birdie told me you needed a sorted list!")
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showMe = input("wanna see your new list?   Y/N")
    if showMe.lower() == "y":
        print(uniqueList)


def randonSearch():
    print("RanDom seArcH?!?!")
    print(mylist[random.randint(0, len(myList)-1)])
                            

def linearSearch():
    print("we're gonna check out each item one at a time in your list! This sucks...")
    searchItem = input("whatcha lookin fer, pardner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqueList[mid] == x:
            print("your number is at index position {}".format(mid))
            return mid

        elif uniqueList[mid] > x:
            return recursiveBinarySearch(uniqueList, low, mid, -1, x)

        else:
            return recursiveBinrySearch(uniqueList, mid + 1, high, x)
    else:
        print("your number isn't here!")

def iterativeBinarySearch(uniqueList, x):
    low = 0
    high = len(uniqueList)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if uniqueList[mid] < x:
            low = mid + 1

        elif uniqueList[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        whichOne = input("which list? sorted or unsorted? ")
        if whichOne.lower() == "sorted":
            print(uniqueList)
        else:
            print(myList)
    
if __name__ == "__main__":
    mainProgram()
