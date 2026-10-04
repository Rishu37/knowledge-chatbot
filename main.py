with open("data/sample.txt","r",encoding="utf-8") as file:
    text = file.read()

lines = text.splitlines()
print(lines)
print(len(lines))