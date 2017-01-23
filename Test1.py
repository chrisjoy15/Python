s = input("Type Bub or Bubs and some vowels: ").lower()
count = 0
num_Bubs = 0
num_Vows = 0
while (count < len(s)):
    count += 1
for chars in s:
    if chars == 'a':
            num_Vows += 1
    elif chars == 'e':
            num_Vows += 1
    elif chars == 'i':
            num_Vows += 1
    elif chars == 'o':
            num_Vows += 1
    elif chars == 'u':
            num_Vows += 1
one_Bub = s.replace('bub', '1')
for chars in one_Bub:
    if chars == '1':
         num_Bubs += 1
two_Bub = one_Bub.replace('1ub', '2')
for chars in two_Bub:
    if chars == '2':
        num_Bubs += 1
print('Number of Bubs: ' + str(num_Bubs))
print('Number of vowels: ' + str(num_Vows))
print('Number of character typed: ' + str(count))