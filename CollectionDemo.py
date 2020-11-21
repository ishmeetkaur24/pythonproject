#WAP to implement collection

BookList = ["wings of fire","The monk who sold his ferari","Harrypotter"]

print(BookList)
def Display():
    for book in BookList:
        print(book)
for book in BookList:
    print(book)

#adding more books
BookList.append("you can win")
BookList.append("white tiger")
for book in BookList:
    print(book)





print("enter 10 books you want in your list")
for i in range(10):
    name = input("Enter Book name")
    BookList.append(name)

Display()