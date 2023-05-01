
with open("words.txt") as f:
    words = f.read().split()


with open("text.txt") as f:
    text = f.read()

print(text)
print(words)


for word in words:
    if word in text:
        text = text.replace(word, "")
    if word.title() in text:
        text = text.replace(word.title(), "")

print(text)

with open("result.txt", "w") as f:
    f.write(text)
