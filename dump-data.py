import requests
import base64
import json
import sys
from config import *


def request_data(min_rank):
    r = requests.get("https://codejam.googleapis.com/scoreboard/%s/poll"%contest_id, params =
            { "p": base64.b64encode(b'{"min_rank":%d,"num_consecutive_users":30}' % min_rank) }
        )
    data = json.loads(base64.urlsafe_b64decode(r.text + '==='))
    return data


print("Requesting data of rank %d ~ rank %d" % (1, 30), file = sys.stderr)
page1_data = request_data(1)
full_scoreboard_size = page1_data["full_scoreboard_size"]
user_scores = page1_data["user_scores"]
for i in range(31,full_scoreboard_size,30):
    print("Requesting data of rank %d ~ rank %d" % (i, i + 29), file = sys.stderr)
    user_scores += request_data(i)["user_scores"]
print(json.dumps(user_scores))
