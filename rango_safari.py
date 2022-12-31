from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
app: safari
"""

@ctx.action_class("user")
class UserActions:
    def rango_type_hotkey():
        actions.key("ctrl-shift-3")