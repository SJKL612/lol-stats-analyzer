# lol-stats-analyzer
League of Legends stats analyzer


### Part 1
 - [x] Work with Riot's official API to get stats of certain summoner(s)
 - [x] Learn and apply: create and code an isolated python environment for this project (IntelliJ already does it but I need to know why) -- venv for this project
 - [x] Simple python code (for loops, f-strings, etc.) to print out basic stats
 - [x] Learn/review JSON and run code in Terminal/CLI to ensure output

#### E/B (errors and bugs) fix -- see Try comments
1. Riot's api key is time-sensitive. When it's expired, go to Riot's Developer page and generate a new key (remember to update .env as well!).
2. Try4's api error: realized that it was caused by (me) trying to look up a key in a dict that does not exist.
    
    - source: Terminal error meg --
   ```
   KeyError: slice(None, 10, None)
   for match_id in match_ids[:10]:
                ~~~~~~~~~^^^^^
   ```
 -> KeyError + python's `[:10]` slicing that returns first 10 items
 -> list supports slicing but dict does ==not== support slicing

   - conclusion:
    If `match_ids` is a list: `match_ids[:10]` works fine (slicing returns first 10 items)
    If `match_ids` is a dict: `match_ids[:10]` treats `[:10]` as a dictionary key, which fails

3. I should print out whatever stats/result I got to see if there's an error in that block (and it's easier to debug!).

