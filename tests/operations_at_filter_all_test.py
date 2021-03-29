from todomvc_web_test.model import given, then, when


def test_create():
    given.visit()

    when.add()

    then.list_should_be_empty()

    when.add('a')

    then.list_should_be('a')\
        .items_left_should_be(1)

    when.add('b', 'c')

    then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)


def test_edit_by_enter():
    given.visit_with('a', 'b', 'c')

    when.edit_by_enter('b', 'b edited')

    then.list_should_be('a', 'b edited', 'c')\
        .items_left_should_be(3)


def test_edit_by_focus_change():
    given.visit_with('a', 'b', 'c')

    when.edit_by_tab('b', 'b edited')

    then.list_should_be('a', 'b edited', 'c')\
        .items_left_should_be(3)


def test_cancel_edit_by_escape():
    given.visit_with('a', 'b', 'c')

    when.cancel_editing('b', 'b edited')

    then.list_should_be('a', 'b', 'c')\
        .items_left_should_be(3)


def test_complete():
    given.visit_with('a', 'b', 'c')

    when.toggle('b')

    then.completed_todos_should_be('b')\
        .active_todos_should_be('a', 'c')\
        .items_left_should_be(2)\
        .clear_completed_should_be_visible()


def test_complete_all_with_some_completed():
    given.visit_with('a', 'b', 'c')\
        .toggle('b')

    when.toggle_all()

    then.completed_todos_should_be('a', 'b', 'c')\
        .active_todos_should_be()\
        .items_left_should_be(0)


def test_activate():
    given.visit_with('a', 'b', 'c')\
        .toggle_all()

    when.toggle('b')

    then.completed_todos_should_be('a', 'c')\
        .active_todos_should_be('b')\
        .items_left_should_be(1)

    when.toggle('a')\
        .toggle('c')

    then.active_todos_should_be('a', 'b', 'c')\
        .completed_todos_should_be()\
        .items_left_should_be(3)\
        .clear_completed_should_be_hidden()


def test_activate_all():
    given.visit_with('a', 'b', 'c')\
        .toggle_all()

    when.toggle_all()

    then.active_todos_should_be('a', 'b', 'c')\
        .completed_todos_should_be()\
        .items_left_should_be(3)\
        .clear_completed_should_be_hidden()


def test_delete():
    given.visit_with('a', 'b', 'c')

    when.delete('b')

    then.list_should_be('a', 'c')\
        .items_left_should_be(2)


def test_delete_by_edit():
    given.visit_with('a', 'b', 'c')

    when.edit_by_enter('a', '')

    then.list_should_be('b', 'c')\
        .items_left_should_be(2)

    when.edit_by_tab('b', '')

    then.list_should_be('c')\
        .items_left_should_be(1)


def test_clear_completed():
    given.visit_with('a', 'b', 'c', 'd')\
        .toggle('b')\
        .toggle('d')

    when.clear_completed()

    then.list_should_be('a', 'c')\
        .items_left_should_be(2)\
        .clear_completed_should_be_hidden()
