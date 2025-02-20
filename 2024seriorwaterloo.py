#Problem 1 
N=int(input("Number of people:"))
A=int(N/2)
seating=[]
count=0
for i in range(N):
    hat_number=int(input("Hat number:"))
    seating.append(hat_number)
for i in range(A):
    if seating[i]==seating[A+i]:
        count+=1
print(count*2)

#Problem 2 
T,N=input("Values: ").split()
T=int(T)
N=int(N)
string_list=[]
nested_list=[]
for i in range(T): 
    string=input()
    string_list=list(string)
    nested_list.append(string_list)

for i in nested_list:
    count=0
    for a in range(N-1):
        if i[a]==i[a+1]:
            print("F")
            break
        if len(i)>len(set(i)):
            print("F")
            break 
        else: 
            print("T")
            break

#Problem 3         
N=int(input())
first=input()
second=input()

if first==second: 
    print("YES")
    print("0")

