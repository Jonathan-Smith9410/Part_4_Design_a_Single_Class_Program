from lib.todo import *
import pytest

def test_adding_item_to_dict():
    todo = ToDo()
    todo.add("Walk the dog")
    assert todo.show_list() == {1: "Walk the dog"}

def test_task_with_no_contents_raises_exception():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.add("")
    error_message = str(e.value)
    assert error_message == "No task present to add."

def test_empty_dict_raises_exception():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.show_list()
    error_message = str(e.value)
    assert error_message == "No tasks present in list."

def test_adding_two_items_to_dict():
    todo = ToDo()
    todo.add("Walk the dog")
    todo.add("Do the shopping")
    assert todo.show_list() == {1: "Walk the dog", 2: "Do the shopping"}

def test_remove_one_item_from_dict():
    todo = ToDo()
    todo.add("Walk the dog")
    todo.add("Do the shopping")
    todo.complete_task(1)
    assert todo.show_list() == {2: "Do the shopping"}