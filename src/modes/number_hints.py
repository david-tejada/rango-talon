from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.rango_number_hints
"""


@ctx.capture("user.rango_hint", rule="<user.number_string>")
def rango_hint(m) -> str:
    return "".join(m)


@ctx.capture("user.rango_target", rule="<user.rango_hint> (plus <user.rango_hint>)*")
def rango_target(m) -> list[str]:
    return m.rango_hint_list
