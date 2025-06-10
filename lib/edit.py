# DESCRIPTION
#   
print("Loading Function: edit(path: str) -> None.")
# Define. If already defined, override it.
define("edit", True)

def edit(path: str) -> None:
    system(f"nvim {path}")
