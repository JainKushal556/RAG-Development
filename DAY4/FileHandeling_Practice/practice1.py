f = open("demo.txt")
data = f.read()

print(data)

f.close()
print("."*20)
f = open("demo.txt",'r')
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)