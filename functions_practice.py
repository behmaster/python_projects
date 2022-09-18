def hello():
    print("hello user")

def pack(x, y, z):
    return [x, y, z]

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("The lunchbox is empty")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")

hello()
print(pack("wait","a","minute"))
eat_lunch([])
eat_lunch(["sandwich","drink","chips","apple"])