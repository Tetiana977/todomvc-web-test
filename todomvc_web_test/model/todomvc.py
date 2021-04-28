from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import have


class TodoMvc:

    def __init__(self):
        self.todos = ss('#todo-list>li')
        self.clear_completed_button = s('#clear-completed')

    def visit(self):
        download_page = "return $._data($('#clear-completed')[0],"\
                        "'events').hasOwnProperty('click')"

        browser.open('https://todomvc4tasj.herokuapp.com')
        browser.should(have.js_returned(True, download_page))

        return self

    def add(self, *names: str):
        for name in names:
            s('#new-todo').type(name).press_enter()
        return self

    def visit_with(self, *names: str):
        self.visit()
        self.add(*names)
        return self

    def start_editing(self, name: str, new_name):
        self.todos.element_by(have.exact_text(name)).double_click()
        return self.todos.element_by(have.css_class('editing'))\
            .element('.edit').with_(set_value_by_js=True).set_value(new_name)

    def cancel_editing(self, name: str, new_name):
        self.start_editing(name, new_name).press_escape()
        return self

    def edit_by_enter(self, name: str, new_name):
        self.start_editing(name, new_name).press_enter()
        return self

    def edit_by_tab(self, name: str, new_name):
        self.start_editing(name, new_name).press_tab()
        return self

    def delete(self, name: str):
        self.todos.element_by(have.exact_text(name)).hover()\
            .element('.destroy').click()
        return self

    def toggle(self, name: str):
        self.todos.element_by(have.exact_text(name)).element('.toggle').click()
        return self

    def toggle_all(self):
        s('#toggle-all').click()
        return self

    def clear_completed(self):
        self.clear_completed_button.click()
        return self

    def list_should_be(self, *names: str):
        self.todos.should(have.exact_texts(*names))
        return self

    def list_should_be_empty(self):
        self.list_should_be()
        return self

    def completed_todos_should_be(self, *names: str):
        self.todos.filtered_by(have.css_class('completed'))\
            .should(have.exact_texts(*names))
        return self

    def active_todos_should_be(self, *names: str):
        self.todos.filtered_by(have.css_class('active'))\
            .should(have.exact_texts(*names))
        return self

    def clear_completed_should_be_hidden(self):
        self.clear_completed_button.should(be.not_.visible)
        return self

    def clear_completed_should_be_visible(self):
        self.clear_completed_button.should(be.visible)
        return self

    def items_left_should_be(self, amount: int):
        s('#todo-count>strong').should(have.exact_text(str(amount)))
        return self
