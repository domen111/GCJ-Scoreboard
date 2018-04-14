import json
import sys
from prettytable import PrettyTable
from config import *

board_file = sys.argv[1]
with open(board_file, 'r') as file:
    board = json.loads(file.read())

friends_board = list(filter(lambda user: user['displayname'] in friends, board))
friends_board = sorted(friends_board, key=lambda user: user['score_1'], reverse=True)

table = PrettyTable(['User', 'Rank', 'Score'])
for user in friends_board:
	table.add_row([user['displayname'], user['rank'], user['score_1']])
print(table)
