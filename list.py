list_name = [1, 2, 3, "a", "b", "c", "ccc"]
print(list_name)
print(list_name[0:3])
list_new = list_name + [1, 2, 3]
print(list_new)
list_num = [1, 2, 3, 4, 5]
print(list_num*4)
list_num[3] = 4**3 # update,edit
print(list_num)
list_num.append(6) #add the list of 6
print(list_num)

list_num[0:2] = [6, "a"]
print(list_num)
print(len(list_num))
list_num[:] = [] #clear the list by replacing(替换) all
print(list_num)

#嵌套list
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
c = ['a', 'b', 'c']
x = [a,b,c]
print(x)

