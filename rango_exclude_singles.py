from talon import Context

ctx = Context()

ctx.matches = r"""
tag: browser
and tag: user.rango_exclude_singles_tag
"""


@ctx.capture(rule="<user.letter> <user.letter>")
def rango_hint(m) -> str:
    return "".join(m.letter_list)
