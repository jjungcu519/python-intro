
chars = ['a', 'b', 'c', 'd']

for char in chars:
    print(char)
#실수해서 무한 루프 돌았어... 무서워.....
chars.append('e')

print(chars)