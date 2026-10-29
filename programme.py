num = int(input("Enter a number : "))

if num==0 or num==1:
    print(num, "is not a prime numbber")
elif num>1:
    for i in range(2, num):
        if(num % i )==0:
           break
      print(num, "is not a prime")
        else:
            print(num, "is Prime Number")
