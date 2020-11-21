MyDreamCar = {"name":"Tesla",
              "color":"Black",
              "Model":"cyber Truck",
              "Engine Type" : "6 cylinder fully automatic"
              }
def display():
    for mycar in MyDreamCar:
        print(mycar)


display()

print(MyDreamCar["Model"])
MyDreamCar["Model"] = "Roadstar"
print("-----------------------------")
print(MyDreamCar["Model"])

#Displaying values of Dictionary
for value in MyDreamCar:
    print(MyDreamCar[value])