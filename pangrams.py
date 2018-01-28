s = 'We promptly judged antique ivory buckles for the next prize'
s = s.lower()
exist = True
for i in range(97,123):
    if chr(i) not in s:
        exist = False
        break
print(exist)

exist = False
for i in range(97, 123):
    if chr(i) in s:
        exist = True
    else:
        exist = False
        break
    
    
            
