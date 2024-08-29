#Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

string = ''
reverse_string = '1234abcd'

def reverse(strr):
    for i in strr:
        new_string = string + reverse_string + i
        print(new_string)
        
reverse(reverse_string)        