#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def summ(num):
    total = 0
    for i in num:
        total += i
        print(total)
        
lst = [8,2,3,7,0]
summ(lst)            
        