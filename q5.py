file1 = open("file1.txt", "w" )
#open file in write mode
for i in range(1,10):
    line = str(random.randint(1, 10))
    file1.write(line)
    #input 10 random numbers and write them in a file
    
file1.close()

with open("file1.txt","r") as f1:
    for line in myfile:
        print sorted(map(int, line.split(',')))
        #sort 10 random numbers which are inout in a file in separate lines
        #and splitted from each other by commas
list1[]
for line in file1:
    list1.append(int(line))
    #convert numbers from string to int and appending them in a list
list1.sort()
#sort the list

with open("file2.txt","w") as f2:
    for i in range(0,10):
        f2.write(str(list1[i] + "\n")
        #write back the numbers by converting them back to string from int
f1.close()
#close file 1
f2.close()
#close file 2
    
    

        
