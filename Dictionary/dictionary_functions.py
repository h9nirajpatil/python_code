d1={11:'aa',22:'bb',33:'cc'}
d2={'abc':22,'pqr':900}
d1.update(d2)
print(d1)

print("Number  of items",len(d1))
print("To check key is present",11in d1)
print("Print all values",d1.values())
print("Print all key",d1.keys())
print("Print all items",d1.items())
print("to get the values",d1.get(11))

for k,v in d1.items():
    print(k,'--->',v)

    data={1001:'aaa',1002:'bbbbb',1003:'cccc'}
    copyD=data.copy()
    print(copyD)