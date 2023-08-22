# to check dublicates in list
some_list = ['a', 'b','c', 'b', 'd', 'm', 'n', 'n']
dublicates = []
for x in some_list:
  if some_list.count(x)>1:
    if x not in dublicates:
      dublicates.append(x)
print(dublicates)