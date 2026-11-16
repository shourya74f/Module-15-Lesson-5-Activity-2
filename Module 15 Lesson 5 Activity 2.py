l=int(input("Enter the Largest number: "))
s=int(input("Enter the Smallest number: "))
while(s):
    t=s
    s=l%s
    l=t
print("The HCF is: ", l)