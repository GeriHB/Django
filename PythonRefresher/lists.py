dognames = ['Fido', 'Sean', 'Sally', 'Mark']

dognames.insert(0, 'Jane')

print(dognames)
print(dognames[2])

del(dognames[2])
print(dognames[2])

print('length of the list: {}'.format(len(dognames)))

dognames[2] = 'NewDog'
print(dognames)