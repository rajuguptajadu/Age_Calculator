num = int(input("Provide number to check if prime: "))
if num <=1:
    print("Invalid choice, try again")
    num = int(input("Provide number to check if prime: "))

for i in range(2,num):
    if num% i ==0:
        print("Number is not prime")
        break
    if num %i !=0:
        print("Number is prime")
