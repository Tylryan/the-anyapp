# The AnyApp
## What is an AnyApp
This is a simple example of an application that has the "Any
Application" property. An application has the AnyApp property 
when it's source code can be updated using itself and those updates
are reflected in the user's current running instance. In other
words, if an application has this property, then it can be extended 
indefinitely by the user at runtime. There are probably many
examples of AnyApps, but the one that inspired this expirement
was Emacs. See 
[Interactive Programming](https://en.wikipedia.org/wiki/Interactive_programming)
for a Wiki on the topic.

## This AnyApp
The primary goal of this AnyApp is to hold a list of Cards in a global 
variable called "deck" which will be modified by the user at runtime. 
However, the user is not limited to only being able to modify the deck 
at runtime, the application can do anything Python itself can do. 
Based on the description above, this application could be
considered to have the AnyApp property.

Upon startup, the deck has no cards. However, the user can add Cards to 
the deck dynamically at runtime with the following code:
```python
deck.append(Card("<Your Front>", "<Your Back>"))
```

If the user would like to add functionality to the application itself, 
they can write a new feature somewhere and load it into the application 
with the `load` function.
```python
load("path/to/your/extention.py")
```

# Examples
## Loading Modules
The user can dynamically load any Python code into the application. In the
example below, the user will start the application and dynamically load (at
runtime) a prewritten module found in the `lib` directory allowing them to run
the `pwd()` command.
1. `$ python anyapp.py`
2. `> load("lib/pwd.py")`
3. `> pwd()`


## Extending an AnyApp
The user can also write their own modules and load them into this application
at runtime.

In this example, the user would like to add a function that adds a new card
to the deck called `deck_append(c: Card) -> bool`. This module can be found at 
`lib/deck_append`. 

To add this module, the user would run the following commands:
1. `$ python anyapp.py`.
2. `> load("lib/deck_append.py")`
3. `> deck_append(Card("Hvordarn Gar Det?", "How's it going?"))`
4. `> print(deck)`

If you would like to make sure this functionality get's loaded everytime you
start the application, run the following commands:
1. Unload the module's function: `unload("deck_append")`.
2. While the application is running, edit it: `edit("initialize.py")` .
    - Add the `load("lib/deck_append.py")` command to the `init` section.
3. Re-evaluate the initialize.py: `load("initialize.py")`.
4. Test to see if the command was loaded.
5. Restart and test to see if the command was automatically loaded.


## Dynamically Modifying The Source Code
A user could modify the source code of the application and 
re-evaluate the entire application.

For this example, the user will modify the version of the
application and `load` the entire application.

1. `$ python anyapp.py`
2. `> edit("anyapp.py")`: Change the version of the application.
3. `> load("anyapp.py")`: Pay attention to the output at the
   beginning. The new version should be reflected and you never had
   to rerun Python. However, the state of the deck has been lost
   which can be observed when running: `print(deck)`.

> Note that if the application held any state that wasn't saved,
> running `load("anyapp.py")` would reset the state. In our case 
> this means that if a user added cards to the global deck and 
> re-evaluated the main program,
> then their card would no longer be in the deck. If this is a 
> feature the user wants, then they can add (write/load) it 
> whenever they wish.
> An easy work around for this is to not `load("anyapp.py")` and instead use
> a separate "initializer" file.


# Requirements
- Python3
- Make