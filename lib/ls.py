
# DESCRIPTION
#   
print("Loading Function: ls(path: str | None) -> None.")

define("ls", True)
def ls(path: str | None = None) -> list[str]:

    if path is None:
        path = "."

    contents: list[str] = os.listdir(path)
    print(contents)
    return contents
