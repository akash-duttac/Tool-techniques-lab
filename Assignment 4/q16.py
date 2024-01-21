# palindrome
def reversal(n):
    reverse = 0
    while n>0:
        temp = n%10
        reverse =  temp + reverse*10
        n //= 10
    return reverse


n = int(input("Enter a no.: "))
if n == reversal(n):
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")