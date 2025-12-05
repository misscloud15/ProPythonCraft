with open("poem.txt") as p:
    content = p.read()

if("Twinkle" in content ):
    print("Twinkle present in poem")

else:
    print("Twinkle is not present in poem")