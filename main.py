import math
arr = ['a','b','c','d','e','f']
def swapInArr():
    print(arr)
    halfArr = len(arr)/2
    halfArr = math.trunc(halfArr)
    counter = 0
    while (halfArr>0):
        first = arr.pop(counter)
        last = arr.pop((len(arr)-1)-counter)  
        arr.insert(counter,last ) 
        arr.insert((len(arr))-counter, first) 
        halfArr-=1
        counter+=1
    print((arr))
swapInArr()