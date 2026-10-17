Bot_Name = "SearchBot"
version = 1
print(Bot_Name)
print(version)
name = input("Whats Your Name: ")
print("Launching Chat Bot..........")
print(f"Hello {name}", "Bot is Ready..")


with open("data/sample.txt","r",encoding="utf-8") as file:
    text = file.read()


lines = text.splitlines()

word = input("Enter the search word here: ")
found = False
for line in lines:
    if word.lower() in line.lower():
        print(line)
        found = True

if not found:
    print("This word is not in text")

