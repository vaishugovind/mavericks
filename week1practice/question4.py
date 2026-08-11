# charachter catagory counter
# Read user input
String=input()
uppercase=0
lowercase=0
digits=0
spaces=0
other_characters=0
for i in String:
    if i>="a" <= i <="z":
        lowercase+=1
    elif i>="A" and i <="Z":
        uppercase+=1
    elif i>="0" and i<="9":
        digits+=1
    elif i==" ":
        spaces+=1
    else:
        other_characters+=1

# Display the values
print(f"Upper case :{uppercase}")
print(f"Lower case :{lowercase}")
print(f"Digits :{digits}")
print(f"Spaces :{spaces}")
print(f"Other characters :{other_characters}")