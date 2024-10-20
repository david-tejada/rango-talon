from talon import Context, actions
from ..overrides import safari_version  # only relative imports work

ctx = Context()
ctx.matches = r"""
tag: browser
app: safari
"""

_SAFARI_VERSION = safari_version.get()
_HOTKEY = "ctrl-shift-keypad_3" if _SAFARI_VERSION.startswith("18.") else "ctrl-shift-3"


@ctx.action_class("user")
class UserActions:
    def rango_type_hotkey():
        actions.key(_HOTKEY)
