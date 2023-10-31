#Program to handle files in python

f1=open('file1.txt', 'r')
f2=open('file2.txt', 'w')
f3=open("file3.txt", "a+")

content=f1.read()
f2.write(content)

f3.write("\nNew line written\n")
f3.seek(0)
print(f3.read())
