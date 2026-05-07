my_dict ={
    'name':'honda',
    'age': 22,
    'grade' : 'A'
    }
print(my_dict.get('grade'))

my_dict.update({'year': 2000})
print(my_dict)
my_dict['year']=2000
print(my_dict)


my_dict.pop('age')
print(my_dict)

my_dict.popitem()
print(my_dict)


del my_dict['grade']
print(my_dict)


my_dict.clear()
print(my_dict)

my_dict ={
    'name':'honda',
    'age': 22,
    'grade' : 'A'
    }
a= my_dict.items()
print(a)
