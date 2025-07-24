Temp=float(input("Enter the temperature"))
unit=input("enter the unit either C for celsius or F for farenhite")

if unit=="C":
 Answer=5/9*(Temp-32)
 print(Answer)

elif unit=="F":
  Answer= 9/5*Temp + 32
  print(Answer)