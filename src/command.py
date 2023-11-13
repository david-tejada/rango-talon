from talon import Module, actions
from typing import Union

mod = Module()


@mod.action_class
class Actions:
    def rango_command_with_target(
        actionType: str,
        target: Union[str, list[str]],
        arg: Union[str, float, None] = None,
    ):
        """Executes a Rango command with target"""
        if isinstance(target, str):
            target = [target]
        action = {"type": actionType, "target": target}
        if arg:
            action["arg"] = arg
        return actions.user.rango_run_command(action)

    def rango_command_without_target(
        actionType: str,
        arg: Union[str, float, None] = None,
        arg2: Union[str, None] = None,
    ):
        """Executes a Rango command without a target"""
        action = {"type": actionType}
        if arg:
            action["arg"] = arg
        if arg2:
            action["arg2"] = arg2
        return actions.user.rango_run_command(action)
