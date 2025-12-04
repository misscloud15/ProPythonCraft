
n = int(input("Enter the number of tomes the loop should run: "))


for i in range(n):
    def avg():                                      #Function definition
        b = int(input("Enter the number: "))
        a = int(input("Enter the number: "))
        c = int(input("Enter the number: "))

        average = (a+b+c)/3
        print(average)

    avg()                                            # function call
    print("Average is printed for the given numbers !")
    

