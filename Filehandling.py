def Read():
    myFile = open("MyDetails.txt", 'r')
    print(myFile.readlines())
    myFile.close()
Read()


myFile = open("MyDetails.txt", 'a')
details = input("Enter more details about you")
myFile.writelines("\n" + details)
myFile.write("\n")
myFile.close()

Read()