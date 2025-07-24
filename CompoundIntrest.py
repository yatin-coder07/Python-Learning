import math
principle=int(input("Enter principle amount here"))
rate=int(input("Enter rate percentage % "))
time=int(input("Enter time duration"))


while principle<0:
    print("principle cannot be less than 0")
    principle=int(input("Enter principle amount here"))
while rate<0:
          print("Rate cannot be less than 0")
          rate=int(input("Enter rate percentage % "))
while time<0:
       print("time cannot be les than 0")
       time=int(input("Enter time duration"))

total=principle * pow((1 + rate/100),time)

print(f"your total amount after intrest is {total}")