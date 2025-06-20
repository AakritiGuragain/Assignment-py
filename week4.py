#qn.1
def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

write_to_file("example.txt", "Hello, this is a test.")

content = read_file_content("example.txt")
print("File Content:", content)

#qn.2
file_path = input("Enter the file name (e.g., sample.txt): ")
def find_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            longest = max(words, key=len)
            return longest
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "The file is empty."
longest_word = find_longest_word(file_path)
print("Longest word in the file:", longest_word)

#qn.3
def check_file_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return len(content) == 0
    except FileNotFoundError:
        print("File not found.")
        return False
file_path = input("Enter the file name: ")
if check_file_empty(file_path):
    print("The file is empty.")
else:
    print("The file is not empty.")

#qn.4
def reverse_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        reversed_content = content[::-1]  

        with open('reversed.txt', 'w') as reversed_file:
            reversed_file.write(reversed_content)

        print("Reversed content written to 'reversed.txt'.")

    except FileNotFoundError:
        print("File not found.")


#qn.5
def convert_to_uppercase(string_list):
    return list(map(lambda s: s.upper(), string_list))
words = ["aakriti", "hate", "me"]
uppercase_words = convert_to_uppercase(words)
print(uppercase_words)

#qn.6
def filter_even_length_words(words):
    return list(filter(lambda word: len(word) % 2 == 0, words))

new = ["aakriti", "hate", "me"]
even_words = filter_even_length_words(new)
print(even_words)

#qn.7
def process_file_with_lambda(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    lines = [' '.join(map(lambda w: w.upper(), line.strip().split())) + '\n' for line in lines]
    with open(file_name, 'w') as f:
        f.writelines(lines)
file = input("Enter file name: ")
process_file_with_lambda(file)
