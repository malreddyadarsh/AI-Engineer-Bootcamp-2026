paragraph=input("Enter a paragraph :")

words=paragraph.split()

unique_words=set()

for word in words:
    word=word.strip(".,!?;:'\"()[]{}").lower()
    if word:
        unique_words.add(word)

print("=====Displaying All Unique Words=====")
for word in unique_words:
    print(word)

print("No.of Unique words are :",len(unique_words))

print("Printing Sorted Unique Words :")
for word in sorted(unique_words):
    print(word)