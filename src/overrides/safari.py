from talon import Context, actions
from ..overrides import safari_version


ctx = Context()
ctx.matches = r"""
tag: browser
app: safari
"""

@ctx.action_class("user")
class UserActions:
    def rango_type_hotkey():
        version = safari_version.get()
        key = "ctrl-shift-keypad_3" if version.startswith('18.') else "ctrl-shift-3"
        actions.key(key)