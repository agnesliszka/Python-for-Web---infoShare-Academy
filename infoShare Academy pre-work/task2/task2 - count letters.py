
import string

''' Create dictionary:
key = alphabet letter;
value = number of time the letter appears in text files '''
alphabet = dict.fromkeys(string.ascii_lowercase, 0) 

# Count how many times each alphabet letter appears in word_{i}.txt files
i = 0

while i != 30:
    with open(f'word_{i}.txt','r') as file:
        for word in file:
            for char in word:
                    char = char.lower()
                    if char in alphabet:
                        alphabet[char] += 1
            i += 1

# Print dictionary with alphabet letters and information how many times the letter appears in text files
print(alphabet)        
                    
        
