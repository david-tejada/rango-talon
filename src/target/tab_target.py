from talon import Module

mod = Module()


@mod.capture(rule="<user.letter> | <user.letter> <user.letter>")
def rango_tab_hint(m) -> str:
    return "".join(m)


@mod.capture(rule="<user.rango_tab_hint>")
def rango_primitive_tab_target(m) -> dict:
    return {
        "type": "primitive",
        "mark": {"type": "tabHint", "value": m.rango_tab_hint},
    }


@mod.capture(
    rule="<user.rango_primitive_tab_target> (and <user.rango_primitive_tab_target>)+"
)
def rango_list_tab_target(m) -> dict:
    return {
        "type": "list",
        "items": m.rango_primitive_tab_target_list,
    }


@mod.capture(rule="<user.rango_primitive_tab_target> | <user.rango_list_tab_target>")
def rango_tab_target(m) -> dict:
    return m[0]
