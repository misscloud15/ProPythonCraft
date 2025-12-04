
first = int(input("Enter the number : "))
second = int(input("Enter the number : "))
third = int(input("Enter the number : "))

def biggest(a,b,c):
    if(a>b and a>c ):
        print(f"a is biggest number among three : {a}")

    elif(b>a and b>c ):
        print(f"b is biggest number among three : {b}")

    else:
        print(f"c is biggest number among three : {c}")


biggest(first,second,third)