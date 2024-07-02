## Description
This is a simple python script built with selenium library.

## Goal
Automate targeted post/reel sharing to multiple users.

## How to use?

### For Windows
1. Download [Python](https://www.python.org/downloads/)

2. Move your file to Desktop for easier configuration

3. Open .env with notepad

4. Adjust configuration in .env based on your preference, replace _italic words_ directly
    - USERNAME=_(your instagram account username)_
    - PASSWORD=_(your instagram account password)_
    - TARGET_POST=_(url/link of post/reel to be shared)_
    - USER_PER_BATCH=_(number of users to share post with at one time)_

5. Launch CMD

6. Type and enter
    > cd Desktop/InstaAuto

7. Type and enter
    > ./env/Scripts/activate

8. Type and enter
    > pip install -r .\requirements.txt

9. Type and enter
    > python main.py

### For MAC
Currently unavailable

## File description
### main.py
Main program file to be run.

### users.txt
File that stored the usernames to share post with.
