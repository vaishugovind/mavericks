# Multiplication pattern analyzer
# Reading inpyt from the user
even_count=0
odd_count=0
n = int(input())
for i in range(1,11):
    if n %2 ==0:
        print(f"{n} * {i} = {n*i} -even")
        even_count+=1 
    else:
        print(f"{n} * {i} = {n*i} -odd")
        odd_count+=1
print(f"Even Result:{even_count}")
print(f"Odd Result:{odd_count}")
    

    