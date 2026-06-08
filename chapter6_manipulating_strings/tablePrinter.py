tableData = [
    ['apples', 'cherries', 'oranges', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
]

c1 = tableData[0]
c2 = tableData[1]
c3 = tableData[2]

longest = max(len(name) for name in c1 + c2 + c3)
for i in range(len(c1)):
    print(f"{c1[i].rjust(longest)}{c2[i].rjust(longest)}{c3[i].rjust(longest)}")
