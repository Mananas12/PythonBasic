text = 'The political slogan "Workers of the world unite!"is from the Comunist Manifesto.'

with open('update.txt', 'w') as file:
    file.write(text)
    print('File Now Closed?: ', file.closed)

print('File Now Closed?: ', file.closed)

with open("update.txt", 'r+') as file:
    text = file.read()
    print('String:', text)

print("\nPosition in file now: ", file.tell())
position = file.seek(33)
print("Position in file now: ", file.tell())

file.write("All Lands")
file.seek(59)
file.write('the tombstone of Karl Marx.')

file.seek(0)
text = file.read()
print("String: ", text)