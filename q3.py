with open('file1.txt','r') as f1:
    x=f1.read()
#opening file1 in read mode
with open('file2.txt','w') as f2:
    a=f2.write(x)
#writing the contents of f1 in f2
