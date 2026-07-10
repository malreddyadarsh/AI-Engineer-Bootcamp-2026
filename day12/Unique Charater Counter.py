
paragraph=input("Enter a paragragh :")
words=set()
for word in paragraph:
    if word.isalpha():
        words.add(word)
        
print("====Displaying All Unique Words====")
for ch in words:
    print(ch)

print("No.of Unique Words Are :",len(words))

print("Sorted Unique words are :")
for word in sorted(words):
    print(word)