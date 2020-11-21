import sys


no1 = int(input("Enter first no"))
no2 = int(input("Enter secon no"))
try:
    output = no1/no2
    print(type(no1))
    print(type(no2))
    print(output)
    print(type(output))
    print("Final Output is " + str(output))
    print(Name)

except ZeroDivisionError:
       print("do not try to Divide by zero")
       error = sys.exc_info()[0]
       print(error)
except NameError:
      print("Define  All Vaariables befor using it")
      error = sys.exc_info()[0]
      print(error)

finally:
        print("Thank you for using our application")