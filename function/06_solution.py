#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20


def sum_num(numbers):
    total = 0
    for i in numbers:
        total += i
        print(i)
        
sum_num()
