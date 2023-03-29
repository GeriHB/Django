age = 12

name = 'Geri'

todayIsCold = True

def hello(name='Sean', age='0'):
    return 'Hello {} you are {} years old'.format(name, age)


hello('Geri', 29)
hello('Mark', 20)
hello("Hey", 2)
sentence = hello()
sentence2 = hello('Geri', 29)

print(sentence)
print(sentence2)