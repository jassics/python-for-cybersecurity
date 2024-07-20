#!/usr/bin/python

# comparison operators on numbers
x = 19
y = 91

print('{} > {} is'.format(x,y),x>y)
print('{} < {} is'.format(x, y),x<y)
print('{} == {} is'.format(x,y),x==y)
print('{} != {} is'.format(x,y),x!=y)
print('{} >= {} is'.format(x,y),x>=y)
print('{} <= {} is'.format(x,y),x<=y)

# Let's see how it works with string
name_title = 'Jassi'
name_lowercase = 'jassi'

print('{} > {} is'.format(name_title, name_lowercase),name_title>name_lowercase)
print('{} < {} is'.format(name_title, name_lowercase),name_title<name_lowercase)
print('{} == {} is'.format(name_title, name_lowercase),name_title==name_lowercase)
print('{} != {} is'.format(name_title, name_lowercase),name_title!=name_lowercase)
print('{} >= {} is'.format(name_title, name_lowercase),name_title>=name_lowercase)
print('{} <= {} is'.format(name_title, name_lowercase),name_title<=name_lowercase)
