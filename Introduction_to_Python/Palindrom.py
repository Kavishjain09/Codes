#M-1-----for String
def isPalindrome(s):
    return s == s[::-1]

ans = isPalindrome("malayalam")

if ans:
    print("Yes")
else:
    print("No")



# Driver code
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10#or num=int(num/10)
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
