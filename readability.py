from cs50 import get_string

text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

for i in range(len(text)):  # cycles through characters in text
    if ("A" <= text[i] and text[i] <= "Z") or ("a" <= text[i] and text[i] <= "z"):  # checks if current character is a letter
        letters += 1
    elif text[i] == " ":  # checks for spaces to count words
        words += 1
    elif text[i] == "." or text[i] == "!" or text[i] == "?":  # checks for punctuation to count sentences
        sentences += 1

index = 0.0588 * (letters * 100) / (words) - 0.296 * (sentences * 100) / (words) - 15.8  # Coleman-Liau index
index = round(index)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade " + str(index))