#qno.1
def count_vowels(text):
    vowels = 'aeiou'
    count = 0  # Initialize count
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

user = input("Enter a string: ")
vcount = count_vowels(user)
print(f"Number of vowels: {vcount}")


#qno.2

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

def find_maximum(num_list):
    if not num_list:
        return None 

    max_val = num_list[0]
    for num in num_list[1:]:
        if num > max_val:
            max_val = num
    return max_val

max_value = find_maximum(numbers)
print(f"Maximum value: {max_value}")

#qno.3
multiplication_table = int(input("Enter a number for multiplication table: "))
def table(num):
    for i in range(1,11):
        print("Multiplications:",num * i)
table(multiplication_table)

#qno.4
sentence = input("Enter a string: ").split()
def counting(words):
    longest= words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
longest_word = counting(sentence)
print(f"The longest word is: {longest_word}")

#qno.5
number = input("Enter a number: ")

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

digits = [int(x) for x in number if x.isdigit()]
print(f"Sum of digits: {sum_of_list(digits)}")

#qno.6
user_input = input("Enter a sentence: ")

def to_title_case(sentence):
    words = sentence.split()
    title_cased = [word.capitalize() for word in words]
    return ' '.join(title_cased)
result = to_title_case(user_input)
print("Title case:", result)

#qno.7
def is_palindrome(word):
    word = word.lower()  # Make it case-insensitive
    return word == word[::-1]

user_input = input("Enter a word: ")
if is_palindrome(user_input):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

#qno.8
user_input = input("Enter a string: ")
def char_count(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict




