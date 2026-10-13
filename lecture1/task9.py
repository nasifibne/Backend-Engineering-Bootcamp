num = int(input())

if(num>=0 and num<=100):
    if num>80:
        print("A")
    elif num>75:
        print("A-")
    elif num>70:
        print("B")
    elif num<50:
        print("F")
else:
    print("enter valid mark")

