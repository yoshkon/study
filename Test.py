from collections import defaultdict
from collections import Counter

dd_list = defaultdict(int)
print(dd_list)
# dd_list[2].append(10)
print(dd_list)

dd_list = defaultdict(dict)
print(dd_list)
dd_list["a"]["b"] = "S"
print(dd_list)

print(Counter([1, 3, 4, 5, 4, 5, 3]))
yy = Counter([1, 3, 4, 5, 4, 5, 3])
if 1:
    print(1)
elif 0:
    print(0)
test = []
if test:
    print("a")
else :
    print("oo")

#yy = (0,1,2,1)
print(sorted(yy.items(), key=lambda key_value: key_value[1], reverse=False))

print([x for x in range(10) if x % 2 == 0])
print([(x , y)
    for x in range(5)
    for y in range(x+1,5)])
