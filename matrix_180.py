#  Գրել ծրագիր, որը քառակուսային մատրիցը շրջում է 180 աստիճան։
# 1   2   3   4
# 5   6   7   8 
# 9   10  11  12 
# 13  14  15  16

# Output: 
# 16  15  14  13 
# 12  11  10  9 
# 8   7   6   5 
# 4   3   2   1


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix.reverse()

for row in matrix:
    row.reverse()

for row in matrix:
    print(row)




