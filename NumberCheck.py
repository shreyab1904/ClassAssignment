def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def palindrome(num):
    temp = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        return True
    else:
        return False


if __name__=="__main__" :
    n1=int(input("enter the number"))
    result=prime(n1)
    print(result)
    result=palindrome(n1)
    print(result)