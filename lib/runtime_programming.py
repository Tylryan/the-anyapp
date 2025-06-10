
# DESCRIPTION
#   
print("Loading Function: runtime_programming(None) -> None.")

define("runtime_programming", True)
def runtime_programming():
    print("Starting the heart of the anyapp.")
    module: str = "helpers"
    if is_defined(module) is False:
        load(f"lib/{module}.py")
    help()

    # This drops the user into an interpreter that can also
    # update the runtime of your deck application.
    while True:
        try:
            cmd = input("> ")
            exec(cmd)
        except EOFError:
            halt(1)
        except KeyboardInterrupt:
            halt(1)
        except NameError:
            print(f"Undefined command: '{cmd}'.")
        except Exception as unhandled_exception:
            print("Unhandled exception. See below for more information.\n",
                  unhandled_exception)
