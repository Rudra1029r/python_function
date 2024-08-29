# Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336

lst = [8,2,3,7,-1]

def summ(numbers):
    total = 1
    for i in numbers:
        total *= i
        print(total)
        
summ(lst)        