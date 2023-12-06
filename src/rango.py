from talon import Module, Context, actions
from typing import Union

mod = Module()
ctx = Context()


@mod.capture(rule="<user.letter> (twice | second)")
def rango_hint_double(m) -> str:
    return m.letter + m.letter


@mod.capture(rule="<user.letter> | <user.letter> <user.letter> | <user.rango_hint_double>")
def rango_hint(m) -> str:
    return "".join(m)


@mod.capture(rule="<user.rango_hint> (and <user.rango_hint>)*")
def rango_target(m) -> list[str]:
    return m.rango_hint_list


@mod.capture(rule="<user.letter> | <user.letter> <user.letter>")
def rango_tab_marker(m) -> str:
    return "".join(m)


@mod.action_class
class Actions:
    def rango_toggle_hints():
        """It toggles the Rango hints globally on or off"""
        actions.user.rango_command_without_target("toggleHints")

    def rango_try_to_focus_and_check_is_editable(target: Union[str, list[str]]):
        """Tries to focus an element marked with a hint (clicking if it's not a link) and returns true if the active element is editable"""
        return actions.user.rango_command_with_target(
            "tryToFocusElementAndCheckIsEditable", target
        )

    def rango_insert_text_to_input(
        text: str, target: Union[str, list[str]], pressEnter: bool
    ):
        """Inserts a given text to an input marked with the target hint"""
        if actions.user.rango_try_to_focus_and_check_is_editable(target):
            actions.edit.select_all()
            actions.edit.delete()
            actions.user.paste(text)
            if pressEnter:
                # Here we insert a wait in case that, for example, some results
                # list needs to be populated (e.g. react.dev)
                actions.sleep("400ms")
                actions.key("enter")

    def rango_clear_input(target: Union[str, list[str]]):
        """Removes the contents of an input"""
        if actions.user.rango_try_to_focus_and_check_is_editable(target):
            actions.edit.select_all()
            actions.edit.delete()

    def rango_run_action_on_reference(command: str, reference: str):
        """Runs a Rango command on a mark"""
        actions.user.rango_command_without_target(
            "runActionOnReference", command, reference
        )

    def rango_force_explicit_clicking():
        """Forces Rango explicit clicking"""
        ctx.tags = ["user.rango_explicit_clicking_forced"]

    def rango_force_direct_clicking():
        """Forces Rango direct clicking"""
        ctx.tags = ["user.rango_direct_clicking_forced"]
