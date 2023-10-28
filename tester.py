from  main import Map

a = Map([1,2,3,4,5,6,7])
b = Map([4,5,6,7,1,2,3])

maps = a.maps
print(maps)
answer = []
lvl_1 = a.level
lvl_2 = b.level
funcs = [min, min, max, max, max, max]




# print(max(xc, key=lambda x: x != None))

print(answer)