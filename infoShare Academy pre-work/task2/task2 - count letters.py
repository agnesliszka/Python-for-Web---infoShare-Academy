import string
alphabet = dict.fromkeys(string.ascii_lowercase, 0)

i = 0

while i != 5:
    with open(f'word_{i}.txt','r') as file:
        for word in file:
            for char in word:
                    char = char.lower()
                    if char in alphabet:
                        alphabet[char] += 1
            i += 1

print(alphabet)        
                    
        
