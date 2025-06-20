#qno.1
numbers= list(map(int, input("Enter number: ").split()))

for num in numbers:
    if num > 50:
        print("stopped")
        break
    if num % 5==0:
        continue
    print(num)

#qno.2

password= input("Enter:")
letter= any(char.isalpha() for char in password)
digit= any(char.isdigit() for char in password)
special= any(char in '@#%&$'for char in password)

if len(password)>6 and (letter and digit and not special):
    print('moderate')

elif len(password)>6 and (letter and digit and special):
    print('strong')

else:
    print('weak')

#qno.3

sentence= input("Enter sentence:")
final= sentence.split()

for i in range(len(final)):
    if i % 2 !=0:
        final[i]=final[i][::-1]

result=' '.join(final)
print(result)

#qno.4
def duplicates(words):
    word_count={ }
    for word in words:
        word_count[word]+=1
    else:
        word_count[word] = 1
    return word_count
words = input("Enter words separated by space: ").split()
result = duplicates(words)
print("Word counts:", result)

#qno.5
books = {
    'The Summer I turned pretty': 4,
    'Mockingjay': 7,
    'About you': 5,
    'Pride and Prejudice': 3,
    'Kite Runner': 2
}
book_name = input("Enter the name of the book: ")

while True:
    copies_input = input("Enter the number of copies: ")
    try:
        copies = int(copies_input)
        break
    except ValueError:
        print("Please enter a valid integer.")

if book_name in books:
    if books[book_name] >= copies:
        print("Available")
    elif books[book_name] > 0:
        print("Partially Available")
    else:
        print("Unavailable")
else:
    print("Unavailable")

#qno.6
List= input("Enter the words separated by space: ").split()
freq= {}
for word in List:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Word count:", freq)

