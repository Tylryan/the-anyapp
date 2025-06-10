# Assume the os module is imported

print("Loading Function: edit(path: str) -> None.")
# Define. If already defined, override it.
define("pwd", True)
def pwd():
    os.system("pwd")
