#FIBONACCI SERIES

n_terms=int(input("How Many Terms? "))
n1,n2=0,1    
cp=1
# for i in range(0,len())
if n_terms<=0:
    print("enter positive integer!!")
elif n_terms==1:
    print("Fibonacci sequence upto",n_terms,":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while cp<n_terms:
        print(n1)
        np=n1+n2
        n1=n2
        n2=np
        cp+=1