# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.


# WAF that replace all occurrences of "java" with "python" in above file.

# Search if the word "learning" exists in the file or not.

import os

file_name= "p2.txt"

if os.path.exists(file_name):
    os.remove(file_name)

def write_data(data):
    with open(file_name,"w") as f:
        f.write(data)
        # f.close() No need with auto matic close the file as its block over

def read_data():
    with open("p2.txt",'r+') as f:
        data = f.read()
        return data

write_data("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
data = read_data()
data = data.replace("Java","Python")

write_data(data)

if data.__contains__("learning"):
    print("File Contains Learning....")

print(read_data())




