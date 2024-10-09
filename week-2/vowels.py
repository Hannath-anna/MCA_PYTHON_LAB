n=input("enter your string ")
vowels_count=0
vowels = ['a','e','i','o','u','A','E','I','O','U']
for char in n:
   if char in vowels:
       print(char)
       vowels_count+=1
print("vowels=",vowels_count)
