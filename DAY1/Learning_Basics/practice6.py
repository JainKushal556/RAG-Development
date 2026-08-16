# Write a Function (WAF) to check if a number is odd or even.
def checkOddEven(num):
    if num % 2 ==0:
        return "Even"
    else:
        return "Odd"

print(checkOddEven(5))


# WAF to count the number of vowels in a string.

def countVowels(word=""):
    # word.lower()
    count = 0
    for i in word.lower():
        if i == 'a' or i == 'e' or  i == 'i' or i == 'o' or i == 'u':
            count+=1
    return count

print(countVowels("My Name Is Kushal Jain"))


# WAF to print if a number is prime or not.

def primeOrNotCheck(num):
    count =0
    for i in range(1,num+1):
        if(num%i==0):
            count +=1
    if count == 2:
        print(str(num)+" Is A Prime NUmber..")
    else:
        print(str(num)+" Is Not A Prime NUmber..")

primeOrNotCheck(5)


# WAF to return the average marks if a list of marks is passed as parameter

def averageMarksCalculator(marks=[]):
    sub_count = len(marks)
    sum = 0
    for i in marks:
        sum += i
    return sum/sub_count

print(averageMarksCalculator([30,30,30])) 