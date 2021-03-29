from todomvc_web_test.model import given, then, when


def test_todos_management():

    given.visit()

    when.add('a', 'b', 'c')
    then.list_should_be('a', 'b', 'c')

    when.cancel_editing('c', 'c to be canceled')

    when.delete('c')
    then.list_should_be('a', 'b')

    when.edit_by_tab('a', 'a edited')

    when.toggle('a edited')
    when.clear_completed()
    then.list_should_be('b')
