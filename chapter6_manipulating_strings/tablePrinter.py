tableData = [
    ['apples', 'cherries', 'oranges', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
]


c1 = tableData[0]
c2 = tableData[1]
c3 = tableData[2]
for c1, c2, c3 in zip(c1, c2, c3):
    print(c1,c2,c3)
