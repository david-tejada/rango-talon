from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: browser
app: chrome
app: brave
app: vivaldi
app: microsoft_edge
app: opera
app: safari
app: firefox
"""

@ctx.action_class("browser")
class BrowserActions:
    def go_back():
        try:
            actions.user.rango_command_without_target_short_timeout("historyGoBack")
        except:
            actions.next()

    def go_forward():
        try:
            actions.user.rango_command_without_target_short_timeout("historyGoForward")
        except:
            actions.next()