#Qno.1
number= float(input("Enter decimal:"))
integer= int(number)
string = str(number)
print(f"Integer={integer}\nString={string}\nOriginal text= {number}")

#Qno.2
username= input("Full Name:")
name= username.split()
Initial= ' '.join([word[0].upper() for word in name])
print(f"Initial is {Initial}")

#Qno.3
word= input("Enter a word:")
print(f"Reverse={word[::-1]}")

#Qno.4
enter= input("Enter a word:")
print(f"Results:{enter[3::]}")

#Qno.5
mail= input("Enter your mail:")
print(f"Domain is {mail[mail.index('@')+1:]}")

#Qno.6
new= input("Enter here:")
print(f"New word is {new[-1]+new[1:-1]+new[0]}")
