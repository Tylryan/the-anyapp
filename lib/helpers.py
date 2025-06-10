
# DESCRIPTION
#   
define("help")
print("Loading Function: help(None) -> None.")
def help():
    print("""USAGE
    $ python this-script.py
DESCRIPTION
    This is an example of how to write an "Any Application". An Any Application 
    (AnyApp) is an application that is designed to be extending by the USER
    even after runtime.

    I was trying to figure out how to make a program like Emacs in a sense.

STARTERS
    1. Print The Deck       : > print(deck)
    2. Append To The Deck   : > deck.append(Card('front', 'back'))
    3. Add the Clear Command: > load("lib/clear.py")
    4. Clear the Screen     : > clear()
    5. Exit the App         : > exit()
    """)
