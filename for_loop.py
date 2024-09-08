#FOR LOOP: This is used to iterate over objects or sequence. It can be used in a list, tuple, string e.t.c

languages = ['yoruba', 'igbo', 'hausa', 'english']
#for dialect in languages:
    #print(dialect)

#Using break statement 
for dialect in languages:
    print(dialect)
    if dialect == 'hausa':
        break
    print(dialect)

#Using continue statement 
for intonations in languages:
    print(intonations)
    if intonations == 'igbo':
        continue

for numbers in range(90):
    if numbers == 91:
        break 
    print(numbers)
else:
    print('DONE')

#for numbers_2 in range(90,1000):
    #print(numbers_2)
    
