# Text Analyzer Character Count , Word Count, Sentence Count ,Vowel Count,
# Digit Count, Space Count, Special Character Count, Consonant Count

text=input("Enter a paragraph :")
charc=0
wordc=0
sentc=0
vowelc=0
digitc=0
spacec=0
specc=0
consc=0

for each in text:
    charc +=1
    if each.endswith(' ') or each.endswith('.'):
        wordc+=1
    if each.endswith('.') or each.endswith('!'):
        sentc+=1
    if each.isalpha():
        if each=='a' or each=='e' or each=='i' or each=='o' or each=='u' or each=='A' or each=='E' or each=='I' or each=='O' or each=='U':
            vowelc+=1
        else:
            consc+=1
    if not each.isalnum() and each != ' ':
        specc+=1
    if each.isdigit():
        digitc+=1
    if each==' ':
        spacec+=1

print("Character Count :",charc)
print(" Word Count :",wordc)
print("Sentence Count :",sentc)
print("Vowel Count :",vowelc)
print("Digit Count :",digitc)
print("Space Count :",spacec)
print("Special Character Count :",specc)
print("Consonant Count :",consc)
