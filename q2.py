from collections import Counter
#counter is used so it is imported from collection

#Function count
def count(fname):
        with open(fname) as f:
            
            return Counter(f.read().split())
            #using counter to count number of words

#Main
print("Number of words are:-",count("TextFileA14.txt"))
#calling function count 
