## Description
This is a simple python script built with selenium library.

## Goal
Automate targeted post/reel sharing to multiple users.

## How to use?

### For Windows
1. Download [Python](https://www.python.org/downloads/)

2. Download this [application](https://github.com/Leoxhiu/InstaAuto/archive/refs/heads/main.zip) as zip
3. Move your file to Desktop for easier configuration

4. Open .env with notepad

5. Adjust configuration in .env based on your preference, replace _italic words_ directly
    - INSTA_USERNAME=_(your instagram account username)_
    - INSTA_PASSWORD=_(your instagram account password)_
    - TARGET_POST=_(url/link of post/reel to be shared)_
    - USER_PER_BATCH=_(number of users to share post with at one time)_
    - REST_AFTER_BATCH=_(minutes for program rest after running one batch)_

6. Launch CMD

7. Type and enter
    > cd Desktop/InstaAuto-main

8. Type and enter
    > .\env\Scripts\activate

9. Type and enter
    > pip install -r requirements.txt

10. Type and enter
    > python main.py

11. The application is successfully launched!
12. For future launch, you can double click on **main.py**.

### For MAC
Currently unavailable

## File description
### main.py
Main program file to be run.

### users.txt
File that stored the usernames to share post with.
