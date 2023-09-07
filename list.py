numbers = [1, 2, 3, 4, 5]
names = ['Marry','Peter']

print (numbers[0])

print (names[1])

# kiểm tra sự tồn tại của 1 phần tử

# kiểm tra theo giá trị
mylist = ['a','b','c']
print ('a' in mylist)
print ('b' not in mylist)

# trích xuất mảng con
numbers = ['a','b','c','d']
print (numbers[:2])

# xóa phần tử của mảng
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print (numbers)

# nối 2 mảng
a = [1, 2]
b = [1, 3]
print (a + b)

# thêm phần tử vào mảng
numberss = [1, 2, 3]
numbers.append(4)
print (numbers)

# lấy phần tử cuối mảng
numbers = [1, 2, 3]
mynumber = numbers.pop()
print (mynumber)


# tìm 1 phần tử trong mảng

aList = [123,'xyz','zara','abc'];
print ("Index for xyz : ", aList.index('xyz'))
print ("Index for zara : ", aList.index('zara'))

# đảo ngược giá trị trong mảng
number3 = [1, 2, 3, 4]
numbers.reverse()
print (number3)

# sắp xếp các giá trị phần tử
aList = ['123','xyz','zara','abc','xyz']
aList.sort()
print ("List : ", aList)

#tuple
mytuple = ('x'
,
'y'
,
'z')
print (mytuple)

# dictionary
point = {'x': 3,'y': 6,'z' : 9}
print (point['x'])

# thêm 1 phần tử
user = {'name': 'Jone','age': 30}
user['country'] = 'Vietnam'
print (user)

