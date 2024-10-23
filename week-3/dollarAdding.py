string=input("enter a string")
first_string=string[0]
New_string=first_string+string[1:].replace(first_string,'$')
print("New string:",New_string)
