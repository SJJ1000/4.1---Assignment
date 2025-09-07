import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))




print()
print('*****  end section 1 ********')
print()

mydictionary = dict(m=8,n=9)
print(mydictionary)

print(phonebook['Chris'])

chrisphone = phonebook['Chris']
print(chrisphone)

print(phonebook['Kati'])




print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'katie'

if name in phonebook:      #this searches all the KEYS in the dictionary
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Joe'] = '555-0123'

phonebook['Chris'] = '555-4444'

print(phonebook)




print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

o=print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f"{key} - {phonebook[key]}")



for value in phonebook.values():
    print(value)



for k,v in phonebook.items():
    print(k,v)


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get('Chri', '999')
print(phone)

phonebook.clear()
print(phonebook)

print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

remove = phonebook.pop('Chris', 'not found')
print(remove)
print(phonebook)





print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()


a = phonebook.popitem()

print(a)

print(phonebook)




print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()

mylist = list(phonebook)
print(mylist)
random_key = random.choice(mylist)
print(random_key)
print(phonebook[random_key])



print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()








