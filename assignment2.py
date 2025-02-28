#qno.1
numbers = input("Enter the numbers seperating by space: ").split()
#taking input of list
numbers=[int(num)for num in numbers]
for num in numbers:
    if num>50:
        print("Number more than 50")
        break
    if num %5 == 0:
        continue
    print(num)

#qno.2

def check_strength(password):
    letter = any(char.isalpha()for char in password)
    digit = any (char.isdigit()for char in password)
    special = any (char in "@#$&*"for char in password)

    if len(password) < 6 or (letter and not digit and not special):
        return "weak"
    if len(password) >= 8 and (letter and digit and special):
         return"strong"
    if len(password) >=6 and (letter and digit):
        return"moderate"
    return"weak"

password=input("Enter your Password: ")
print(f"Password Strength:{check_strength(password)}")

#qno.3

def reversing(sentence):
    words = sentence.split()
    for i in range(1,len(words),2):
        words[i]= words[i][::-1]
    return" ".join(words)
sentence = input("Enter your thought to make it twisted: ") 
print("Twisted:", reversing(sentence))

#qno.4
def duplicates(words):
    word_count={ }
    for word in words:
        word_count[word]+=1
    else:
        word_count[word] = 1

