#simple calculator

# a = int(input ("ENTER NUMBER : "))
# b = int(input ("ENTER NUMBER : "))

# print("THE ADDITION OF THE ABOVE TWO NUMBERS IS : ",a+b)

# c = "Mohammad,Hanzala,Shahbaz,Aslam,Sidhu,Jatt"
# print(c[0:8])
# print(len(c))

#calculator performing all arithmetic operations



# def add(a,b): return a+b

# def subtract(a,b): return a-b

# def multiply(a,b): return a*b

# def division(a,b): 
#     if b != 0:
#         return a/b
#     else: return a

# def calculator():
#        print("Welcome to the Simple Calculator")
#        print("Select an Operation")
#        print("1. ADDITION")
#        print("2. SUBTRACTION")
#        print("3. MULTIPLICATION")
#        print("4. DIVISION")

# try: choice = int(input("Enter a number of your choice from 1 to 4 : ")) # type: ignore
# finally:
#      choice in [1,2,3,4]
# num1 = float(input("Enter the first number : "))
# num2 = float(input("Enter the first number : "))

# if choice == 1:
#     print(f"The result is : { add (num1,num2)}")
# elif choice == 2:
#     print(f"The result is : { subtract (num1,num2)}")
# elif choice == 3:
#     print(f"The result is : { multiply (num1,num2)}")
# elif choice == 4:
#     print(f"The result is : { division (num1,num2)}")

# else :
#      print("Invalid input ! Please select a valid operation.")

# #string slicing
# fruit = "MANGO"
# print(fruit[0:5])
# print(fruit[-4:-1])

# # using loop
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabets:
#     print(i)

# nm = "Harry"
# print(nm[-4:-2])

# bk = "hanzala!!! Muhammad!!!."
# print(len(bk))
     
# print(bk.upper())
# print(nm.lower())
# print(bk.rstrip('!'))

# print(bk.replace("hanzala","Muhammad"))
# print(bk.split())
# print(bk.capitalize())
# print(bk.count("!"))
# print(bk.endswith("."))
# print(bk.find("!"))
# print(nm.isalnum())
# print(nm.isalpha())
# print(nm.isnumeric())
# print(nm.islower())
# print(bk.isprintable())
# print(bk.isspace())
# print(bk.istitle())
# print(bk.startswith("h"))
# print(bk.swapcase())
# print(bk.title())

#conditional operators

a = int (input("Enter the price: "))
print("The price is",a)
if(a<180):
    print("You can  buy it")
elif(a==180):
    print("You have no money left")
else:
    print("You do not have enough money")

num = int(input("Enter a number : "))
if(num>0):
    print("The number is Positive")
elif(num<0):
    if(num>0 & num<=10):
        print("The number is between 1-10")
    elif(num>10 & num<=20):
        print("The number is between 11-20")  
    else:
        print("The number is greater then 20")
else:
    print("The number is Negative")      

