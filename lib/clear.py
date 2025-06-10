
# DESCRIPTION
#   

print("Loading Function: clear() -> None.")
if define("clear", 
          overwrite = True):
    print(f"Info: Function Overwritten: `clear`.")

def clear() -> None:
    assert os is not None

    os.system("clear")

