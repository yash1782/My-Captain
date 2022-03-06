
from collections import Counter  
# initializing string 
test_str = "Mississippi"
 
def most_frequent(string):
    res = {}
    
    for keys in string:
        res[keys] = res.get(keys, 0) + 1
    
    
    res = Counter(test_str)
    
    # printing result 
    print ("Count of all characters in Mississippi is : \n"+  str(res))
most_frequent(test_str)