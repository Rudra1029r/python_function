#Write a  Python function to find the maximum of three numbers.



def max_num(a,b,c):
    if a>b>c:
        print(a)
    elif b>a>c:
        print(b)
    else:
        print(c)
        
max_num(1,2,3)