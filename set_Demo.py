MyMobiles = {"nokia","samsung","Apple","one plus"}

def Display():
    for mobile in MyMobiles:
        print(mobile)
        print("-------------------------")

Display()
MyMobiles.add("Mi")
Display()

MyMobiles.remove("samsung")
Display()

print(MyMobiles.pop())