#字典比较

def dict_cmpare( dict1, dict2 ):
    dict1_s = len(dict1)
    dict2_s = len(dict2)
    if dict1_s != dict2_s:
        return False
    for key1 in dict1:
        if(dict2.get(key1,None) == None):
            return False

        if dict1.get(key1) != dict2.get(key1):
            return False
    return True
print(dict_cmpare(dict1, dict2))