
import sys
input = sys.stdin.readline


board = {
    'E' : {
        'O.\n.P' : 'T',
        '.P\nI.' : 'F',
        '.P\nO.' : 'Lz'
    },
    'W' : {
        'P.\n.O' : 'T',
        '.I\nP.' : 'F',
        '.O\nP.' : 'Lz'
    },
    'S' : {
        '.O\nP.' : 'T',
        'I.\n.P' : 'F',
        'O.\n.P' : 'Lz'
    },
    'N' : {
        '.P\nO.' : 'T',
        'P.\n.I' : 'F',
        'P.\n.O' : 'Lz'
    }
}


arrow = input().rstrip()

step = ''

for _ in range(2):
    step += input()

step = step.rstrip()

if step in board[arrow]:
    print(board[arrow][step])
else:
    print('?')

