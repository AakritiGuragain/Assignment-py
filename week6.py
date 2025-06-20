#qno.1
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Aakriti", 20, [85, 90, 78])
student2 = Student("Aayush", 19, [70, 80, 75])
student3 = Student("Aiska", 21, [95, 92, 88])

print(f"{student1.name}'s average grade: {student1.average_grade()}")
print(f"{student2.name}'s average grade: {student2.average_grade()}")
print(f"{student3.name}'s average grade: {student3.average_grade()}")

#qno.2
class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author
    
    def short_title(self):
        return self.title[:10]
    
book1 = Book("The Great", "Aakru Hing")
book2 = Book("Hunger Games", "Jay Park")
book3 = Book("1975", "Mat Hilly")       
print(f"Short title of book1: {book1.short_title()}")
print(f"Short title of book2: {book2.short_title()}")
print(f"Short title of book3: {book3.short_title()}")

#qno.3
class StudentResult:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def average_grade(self):
        average = sum(self.marks) / len(self.marks)
        if average >= 50:
            return "Pass"
        else:
            return "Fail"
student1 = StudentResult("Aakriti", 20,56)
student2 = StudentResult("Aayush", 19, 45)
student3 = StudentResult("Aiska", 21, 1)
print("Students who have passed:")
for student in [student1, student2, student3]:
    if student.has_passed():
        print(student.name)

#qno.4
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def total_price(self):
        return sum(item['price'] for item in self.items)

cart = ShoppingCart()

cart.add_item("Book", 12.99)
cart.add_item("Pen", 1.50)
cart.add_item("Copy", 5.25)
cart.add_item("Backpack", 35.00)
cart.add_item("Water Bottle", 8.75)

print(f"Total price: NRS{cart.total_price():.2f}")

#qno.5
class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

text = "Hello world! This is a sample text."
analyzer = TextAnalyzer(text)
print("Word count:", analyzer.word_count())

#qno.6
import random

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist):
        self.songs.append({'title': title, 'artist': artist})

    def shuffle(self):
        random.shuffle(self.songs)

playlist = Playlist()
playlist.add_song("About you", "1975")
playlist.add_song("Robbers", "1975")
playlist.add_song("Somebody Else", "1975")
playlist.add_song("Sunflower", "Post Malone")
playlist.add_song("Better", "Lauv")

playlist.shuffle()

print("Shuffled Playlist:")
for song in playlist.songs:
    print(f"{song['title']} by {song['artist']}")
