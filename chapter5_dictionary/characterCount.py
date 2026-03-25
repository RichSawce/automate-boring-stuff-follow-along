message = "Hello, how are you doing today?"

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)