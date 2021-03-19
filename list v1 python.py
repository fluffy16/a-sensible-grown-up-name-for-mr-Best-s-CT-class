"""
program goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input th INTs from STRs
3.We need to provide choices to the user
    a. Add more values to the list
    b. Return a value at a specific index
"""
myList = []
def mainProgram():
    while True:
        try:
            print("Hello, there! let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to a list or
2. add a bunch of numbers
3. Return the value at an index 
4. random search
5. linear search
6. print contents of list
7. quit program""")
            #add a way to catch bad user responses
            if choice == "1":
                addToList ()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                print(myList)
            else:
                break
        except:
            print("you made an oopsie!")
    #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of repitition.
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

def randonSearch():
    print("RanDom seArcH?!?!")
    print(mylist[random.randint(0, len(myList)-1)])
                            

def linearSearch():
    print("we're gonna check out each item one at a time in your list! This sucks...")
    searchItem = input("whatcha lookin fer, pardner?   ")
    for x in range(len(myList[x] == int(searchItem):
        print("Your item is at index position {}".format(x)) #remind mr Best about the parerthesis
    
if __name__ == "__main__":
    mainProgram()
