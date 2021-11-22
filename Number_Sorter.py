# Program 1: Number Sorter
# The Program will ask for 4 numbers.
# The numbers entered will be printed from highest to lowest


def intro():
    print("Welcome!")
    print("You will be asked to input four (4) numbers.")
    print("At the end of the program, the numbers entered will be arranged from highest to lowest.")

intro()

numb_1 = int(input("Enter 1st number: "))
numb_2 = int(input("Enter 2nd number: "))
numb_3 = int(input("Enter 3rd number: "))
numb_4 = int(input("Enter 4th number: "))


def SortFormat_1():
    if numb_1>=numb_2 and numb_1>=numb_3 and numb_1>=numb_4:
        print(f"The highest number is {numb_1}.")
        if numb_2>=numb_3 and numb_2>=numb_4:
            print(f"The 2nd highest number is {numb_2}.")
            if numb_3>=numb_4:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_4}.")
            else:
                print(f"The 3rd highest number is {numb_4}.")
                print(f"The lowest number is {numb_3}.")
        elif numb_3>=numb_2 and numb_3>=numb_4:
            print(f"The 2nd highest number is {numb_3}.")
            if numb_2>=numb_4:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_4}.")
            else:
                print(f"The 3rd highest number is {numb_4}.")
                print(f"The lowest number is {numb_3}.")
        elif numb_4>=numb_2 and numb_4>=numb_3:
            print(f"The 2nd highest number is {numb_4}")
            if numb_2>=numb_3:
                print(f"The 3rd highest number is {numb_2}.")
                print(f"The lowest number is {numb_3}.")
            else:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_2}.")
                

def SortFormat_2():
    if numb_2>=numb_1 and numb_2>=numb_3 and numb_2>=numb_4:
        print(f"The highest number is {numb_2}.")
        if numb_1>=numb_3 and numb_1>=numb_4:
            print(f"The 2nd highest number is {numb_1}.")
            if numb_3>=numb_4:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_4}.")
            else:
                print(f"The 3rd highest number is {numb_4}.")
                print(f"The lowest number is {numb_3}.")
        elif numb_3>=numb_1 and numb_3>=numb_4:
            print(f"The 2nd highest number is {numb_3}.")
            if numb_1>=numb_4:
                print(f"The 3rd highest number is {numb_1}.")
                print(f"The lowest number is {numb_4}.")
            else:
                print(f"The 3rd highest number is {numb_4}.")
                print(f"The lowest number is {numb_1}.")
        elif numb_4>=numb_1 and numb_4>=numb_3:
            print(f"The lowest number is {numb_4}.")
            if numb_1>=numb_3:
                print(f"The 3rd highest number is {numb_1}.")
                print(f"The lowest number is {numb_3}.")
            else:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_1}.")
                

def SortFormat_3():
    if numb_3>=numb_1 and numb_3>=numb_2 and numb_3>=numb_4:
        print(f"The highest number is {numb_3}.")
        if numb_1>=numb_2 and numb_1>=numb_4:
            print(f"The 2nd highest number is {numb_1}.")
            if numb_2>=numb_4:
                print(f"The 3rd highest number is {numb_2}.")
                print(f"The lowest number is {numb_4}.")
            else:
                print(f"The 3rd highest number is {numb_4}.")
                print(f"The lowest number is {numb_2}.")
        elif numb_2>=numb_3 and numb_2>=numb_4:
            print(f"The 2nd highest number is {numb_2}.")
            if numb_3>=numb_4:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_4}.")
            else:
                print(f"The 3rd highest number is {numb_4}.")
                print(f"The lowest number is {numb_3}.")
        elif numb_4>=numb_1 and numb_4>=numb_2:
            print(f"The lowest number is {numb_4}.")
            if numb_1>=numb_2:
                print(f"The 3rd highest number is {numb_1}.")
                print(f"The lowest number is {numb_2}.")
            else:
                print(f"The 3rd highest number is {numb_2}.")
                print(f"The lowest number is {numb_3}.")
                
                
def SortFormat_4():
    if numb_4>=numb_1 and numb_4>=numb_2 and numb_4>=numb_3:
        print(f"The highest number is {numb_4}.")
        if numb_1>=numb_2 and numb_1>=numb_3:
            print(f"The 2nd highest number is {numb_1}.")
            if numb_2>=numb_3:
                print(f"The 3rd highest number is {numb_2}.")
                print(f"The lowest number is {numb_3}.")
            else:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_2}.")
        if numb_2>=numb_1 and numb_2>=numb_3:
            print(f"The 2nd highest number is {numb_2}.")
            if numb_1>=numb_3:
                print(f"The 3rd highest number is {numb_1}.")
                print(f"The lowest number is {numb_3}.")
            else:
                print(f"The 3rd highest number is {numb_3}.")
                print(f"The lowest number is {numb_1}.")
        if numb_3>=numb_1 and numb_3>=numb_2:
            print(f"The 2nd highest number is {numb_3}.")
            if numb_1>=numb_2:
                print(f"The 3rd highest number is {numb_1}.")
                print(f"The lowest number is {numb_2}.")
            else:
                print(f"The 3rd highest number is {numb_2}.")
                print(f"The lowest number is {numb_1}.")
                

def outro():
    print("Hope it helped! Thank you!")

def order():
    SortFormat_1()
    SortFormat_2()
    SortFormat_3()
    SortFormat_4()
    outro()
    
order()

