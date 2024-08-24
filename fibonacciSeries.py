number_of_terms = int(input("Enter the Number of Terms : "))
print("====================================================================")
print("====================================================================")
f1=0
f2=1
num=0
print(f" Fibonacci Series is : {f1}\t{f2}",end="\t")


while num<number_of_terms-2:
     f3=f2+f1
     print(f"{f3}",end="\t")
     f1=f2
     f2=f3
     num+=1
       
