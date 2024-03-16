vowels = 'aeiouy'

for i in 'powerful':
    if i in vowels:
        print(i)

message = "Hello how are you?"
message.split() # returns a list

for word in message.split():
    print(word)

words = ('cool', 'powerful', 'readable')
for i in range(0, len(words)):
    print((i, words[i]))

for index, item in enumerate(words):
    print((index, item))

d = {'a': 1, 'b':1.2, 'c':1j}

for key, val in sorted(d.items()):
    print('Key: %s has value: %s' % (key, val))
