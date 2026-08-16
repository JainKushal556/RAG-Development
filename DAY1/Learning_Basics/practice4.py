print("Print All Odd Numbers From 1 to 20 ")

for i in range(1,21):
    if i%2!=0:
        print(str(i) , end=" ")

print("\n\nPrint The Table Of 57\n")
num = 57
for i in range(1,11):
    print(str(num) + " * " + str(i) + " = " + str(num*i))


print("\n\nPrint all multiples of 3 from 1 to 50 but skip 15.\n")
for i in range(1,51):
    if i == 15:
        continue
    if i % 3 == 0:
        print(i,end=" ")

print("\n\nTake two integers a and b as input.\nFind and print the first number between 1 and 1000 that is divisible by both numbers.\n")

a = int(input("Enter Number :"))
b = int(input("Enter Number :"))

for i in range(1,10001):
    if i%a==0 and i%b==0:
        print(i)
        break
    