n = int(input("Enter the integer:"))
x = 0
diapozon = range(x,n+1)
new_list = list(diapozon)
print(new_list)
#new_list = list(range)
for i in new_list:
    if i % 2 == 1:
       print(i, end = " ")  
