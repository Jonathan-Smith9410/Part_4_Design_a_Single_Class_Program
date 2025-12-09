# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem


As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToDo:

    def __init__(self):
        # Parameters:
        # None
        # Side effects:
        # Initialise dict to store todo items
        pass
    
    def add(self, item):
        # Parameters:
        # item: string representing a task
        # Side effects:
        # Add item to dict as a value with a sequential int as a key
        pass
    
    def show_list(self):
        # Parameters:
        # None
        # Side effects:
        # None
        # Returns:
        # dict
        pass
    
    def remove_item(self, key):
        # Parameters:
        # key: an int representing a key value in the todo list
        # Side effects:
        # None
        # Returns:
        # dict
        pass


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
add() adds the item to the dict
"""
todo = Todo()
todo.add("Walk the dog")
todo.show_list() # => {1: "Walk the dog"}

"""
Given a task with no contents
add() raises an exception
"""
todo = Todo()
todo.add("") # raises an error with the message "No task present to add."

"""
Given an empty dictionary
show_list() raises an exception
"""
todo = Todo()
todo.show_list() # raises an error with the message "No tasks present in list."

"""
Given an dictionary with more than one item present
show_list() returns the contents
"""
todo = Todo()
todo.add("Walk the dog")
todo.add("Do the shopping")
todo.show_list() # => {1: "Walk the dog", 2: "Do the shopping"}

"""
Given an dictionary with more than one item present
remove_item(key) deletes the entry at the key integer value
"""
todo = Todo()
todo.add("Walk the dog")
todo.add("Do the shopping")
todo.remove_item(1)
todo.show_list() # => {2: "Do the shopping"}


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
