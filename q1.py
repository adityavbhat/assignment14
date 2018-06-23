#Function
def last_n_lines(filename, lines):
    with open(filename, "r") as text_file:
        #Opening text file 
        content = text_file.readlines()[-lines:]
        #read lines from file
        for line in contents:
            print(line, end="")
            #print lines
            

#Main
n = int(input("Enter n: "))
# input number of lines to be read
last_n_lines("TextFileA14.txt", n)
#passing file name and n as arguments
