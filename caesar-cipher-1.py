s = 'middle-Outz'
k = 2
encryptedString = ''

for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122:
        replaced = (97+(ord(s[i])+k-97)%26)
    elif 65 <= ord(s[i]) <= 90:
        replaced = (65+(ord(s[i])+k-65)%26)
    else:
        replaced = ord(s[i])
    encryptedString = encryptedString + chr(replaced)
    
print(encryptedString)
