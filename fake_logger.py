import time
import random
import sys

lines = [
    '[INFO]: Today\'s fact: The technical term for "hairball" is "bezoar."',
    "[INFO]: Today's fact: Abraham Lincoln kept four cats in the White House.",
    "[INFO]: Today's fact: Adult cats only meow to communicate with humans.",
    "[ERR]: The user has unsubscribed from cat facts!",
    "[ERR]: 0 users are subscribed",
    "[WARN]: shutting down.",
    "[WARN]: A new user subscribed to cat facts!",
]


if __name__ == '__main__':
    filename = sys.argv[1]
    while True:
        time.sleep(2)
        with open(filename, 'a') as f:
            line = random.choice(lines)
            f.write(line + '\n')
