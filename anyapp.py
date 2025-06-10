# You can extend this program to become whatever you want it
# to be --- so long as you don't crash it --- bo doing the
# following:
# 1. Write python program in another file in another terminal
#    and save it as "extended.py".
# 2. Come back to this one and run `exec("extended.py")`.

print("Version -1000")
from glob import glob
import os
import time



global Defines
Defines = set()

print("Manifesting Function: is_defined(string: str) -> bool.")
def is_defined(string: str) -> bool:
    return string in Defines

print("Manifesting Function: define(string: str) -> bool.")
def define(string: str, overwrite = False) -> bool:
    """Given a definition, this function will declare it. To the world.
    If it was already declared, then by default this function will not
    overwrite the previous declaration. However, if you wish to overwrite
    the previous declaration, then set overwrite = True.
    """

    global Defines
    defined = is_defined(string)
    if defined is False:
        Defines.add(string)
    elif defined and overwrite:
        Defines.add(string)


    return defined

print("Manifesting Function: read_file(path: str) -> str.")
def read_file(path: str) -> str:
    f = open(path, "r")
    c = f.read()
    f.close()
    return c

print("Manifesting Function: load(path: str) -> None.")
def load(path: str) -> None:
    contents: str = read_file(path)
    exec(contents, globals())
    return None

print("Manifesting Function: unload(name: str) -> bool.")
def unload(name: str) -> str:
    if name in Defines:
        del globals()[name]
        Defines.remove(name)
        return True

    print(f"[error]: Failed to undefine: `{name}`.")
    return False
    # Unset a global function/variable

def init():
    # Loading Libs
    print("Loading Libs.")

    lib_path: list[str] = glob("lib/*")
    [ load(x) for x in lib_path ]

    # Loading Application Information
    load("decks/deck.py")


    # User Initializer for their own
    # rc.
    load("initialize.py")
    # Drops you into a session.
    runtime_programming()

if __name__ == "__main__":
    # After the user executes this program, it can be indefinitely
    # extended to become whatever a user desires.
    init()
