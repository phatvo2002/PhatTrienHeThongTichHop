str = "vo"
str2="dang"
str3="phat"

print (str + " "+ str2 +" "+str3)

# trích xuất chuỗi con
str = 'Hello world'
print (str[0:4])


# lấy độ dài chuỗi
count = len("vodangphat")
print(count)

# tìm và thay thế nội dung
str = 'Hello world'
newstr = str.replace('Hello','Bye')
print (newstr)

# tìm và thay thế chuỗi con
str = 'Hello world'
print (str.find('world'))
# tách chuỗi
str = 'Hello world'
print (str.split(' '))

#loại bỏ kí tự khoảng trắng
str = 'Hello world'
print (str.strip(' '))