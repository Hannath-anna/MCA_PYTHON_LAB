string=input("enter the string:")
if len (string)<1:
    print("invalid")
elif len(string)==1:
    print("latest string:",string)
else:
    first_char = string[0]
    last_char=string[-1]
    middle_part=string[1:-1]
    modified_string=last_char+middle_part+first_char
    print("modified string:",modified_string)
