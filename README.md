# Google Code Jam Friends' Scoreboard

Google Code Jam 2018 doesn't not have "friend" feature itself. So I created this script to dump the data from GCJ and filter the status of friends.

## Usage

First, create `config.py` (see `config-sample.py`). Then:
```bash
python3 dump-data.py > board.json # Get the data from GCJ
python3 find-friends.py board.json
```

