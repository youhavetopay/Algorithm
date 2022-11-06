def gridChallenge(grid):
    # Write your code here

    for idx, word in enumerate(grid):
        grid[idx] = sorted(list(map(str, word)))

    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if ord(grid[j][i]) > ord(grid[j+1][i]):
                return 'NO'

    return 'YES'

g1 = ['abc', 'ade', 'efg']
g2 = [
    'mpxz',
    'abcd',
    'wlmf'
]
g3 = [
    'abc',
    'hjk',
    'mpq',
    'rtv'
]
print(gridChallenge(g3))