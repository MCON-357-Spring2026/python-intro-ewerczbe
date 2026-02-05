"""
TODO:
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table of 5

"""
for i in range(1, 11):
    print(i)
num = 1
while num <= 20:
    if num % 2 == 0:
        print("Even number: ", num)
    num += 1
sum = 0
for i in range(1, 101):
    sum += i
print("the sum of 1 to 100: ", sum)
for i in range(0, 13):
    print("5 x ", i, ": ", 5*i)


