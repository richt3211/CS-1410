def least_key(dictionary):
    list = []
    for x in dictionary:
        list.append(x)
    string = list[0]
    for x in list:
    	if len(string) > len(x):
    		string = x
    	print( "key: " + str(x))
    	print('string: ' + str(string))
    print (string)
    return string
least_key({'a': 999, 'b': 999, 'aa': 999, 'aaa': 999})
x = range(4,0,-1)
print (x)