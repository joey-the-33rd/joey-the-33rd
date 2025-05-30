# We want to retrieve their username from memory if possible;
# if not, we’ll prompt for a username and store it in 
# username.json for next time. 


from pathlib import Path
import json
path = Path('username.json')

if path.exists():
    contents = path.read_text() 
    username = json.loads(contents) 
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")