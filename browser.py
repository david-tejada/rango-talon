from talon import Module, Context, actions, clip, settings
import json
import time
from typing import Any

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: browser
"""

mod.tag(
    "rango_direct_clicking",
    desc="Commands for direct clicking with the extension rango",
)
ctx.tags = ["user.rango_direct_clicking"]

rango_start_with_direct_clicking = mod.setting(
    "rango_direct_clicking",
    type=bool,
    default=True,
    desc="Rango direct clicking mode setting",
)


def update_clicking_mode(setting_value):
    if setting_value == 1:
        ctx.tags = ["user.rango_direct_clicking"]
    else:
        ctx.tags = []


settings.register("user.rango_direct_clicking", update_clicking_mode)

mod.list("rango_hint_styles", desc="list of Rango hint styles")
mod.list("rango_hint_weights", desc="list of Rango hint weights")
mod.list("rango_hints_toggle_levels", desc="list of Rango hints toggle levels")

ctx.lists["user.rango_hint_styles"] = {"boxed": "boxed", "subtle": "subtle"}
ctx.lists["user.rango_hint_weights"] = {
    "bold": "bold",
    "normal": "normal",
    "auto": "auto",
}
ctx.lists["user.rango_hints_toggle_levels"] = {
    "tab": "Tab",
    "host": "Host",
    "path": "Path",
}


@mod.capture(rule="<user.letters> | <user.letters> (and <user.letters>)+")
def rango_hints(m) -> str:
    return m.letters_list


RANGO_COMMAND_TIMEOUT_SECONDS = 3.0
MINIMUM_SLEEP_TIME_SECONDS = 0.0005


def read_json_response_with_timeout() -> Any:
    """Repeatedly tries to read a json object from the clipboard, waiting
    until the message type is "response"

    Raises:
        Exception: If we timeout waiting for a response

    Returns:
        Any: The json-decoded contents of the file
    """
    timeout_time = time.perf_counter() + RANGO_COMMAND_TIMEOUT_SECONDS
    sleep_time = MINIMUM_SLEEP_TIME_SECONDS
    while True:
        raw_text = clip.text()
        message = json.loads(raw_text)

        if message["type"] == "response":
            break

        actions.sleep(sleep_time)

        time_left = timeout_time - time.perf_counter()

        if time_left < 0:
            raise Exception("Timed out waiting for response")

        # NB: We use minimum sleep time here to ensure that we don't spin with
        # small sleeps due to clock slip
        sleep_time = max(min(sleep_time * 2, time_left), MINIMUM_SLEEP_TIME_SECONDS)

    return json.loads(raw_text)


@mod.action_class
class Actions:
    def rango_execute_simple_command(
        actionType: str, target: str = None, directClicked: bool = False
    ):
        """Function for executing Rango commands more succinctly"""

    def rango_execute_command(action: dict[str, Any], directClicked: bool = False):
        """Executes a Rango command"""

    def rango_click_hint(hintText: str, directClicked: bool = False):
        """Clicks on a link with a given hint"""

    def rango_open_in_new_tab(hintText: str):
        """Clicks on a link with a given hint"""

    def rango_open_in_new_background_tab(hints: list):
        """Open links in a non focused tab"""

    def rango_copy_link(hintText: str):
        """Copies a link with a given hint"""

    def rango_show_link(hintText: str):
        """Shows the link address with a given hint"""

    def rango_hover_hint(hintText: str):
        """Hovers on a link with a given hint"""

    def rango_fixed_hover_hint(hintText: str):
        """Hovers on a link with a given hint with no automatic unhover"""

    def rango_unhover():
        """Unhover all hovered elements"""

    def rango_toggle_hints():
        """Toggle hints on and off"""

    def rango_increase_hint_size():
        """Increase the size of the hints"""

    def rango_decrease_hint_size():
        """Decrease the size of the hints"""

    def rango_set_hint_style(value: str):
        """Change the style of the hints"""

    def rango_set_hint_weight(value: str):
        """Change the weight of the hints"""

    def rango_enable_direct_clicking():
        """Enables rango direct mode so that the user doesn't have to say 'click' before the hint letters"""

    def rango_disable_direct_clicking():
        """Disables rango direct mode"""


@ctx.action_class("user")
class UserActions:
    def rango_execute_simple_command(
        actionType: str, target: str = None, directClicked: bool = False
    ):
        action = {"type": actionType}
        if target:
            action["target"] = target
        actions.user.rango_execute_command(action, directClicked)

    def rango_execute_command(action: dict[str, Any], directClicked: bool = False):
        message = {"version": 1, "type": "request", "action": action}

        json_message = json.dumps(message)
        response = None
        with clip.revert():
            clip.set_text(json_message)
            actions.key("ctrl-shift-insert")
            response = read_json_response_with_timeout()

        if response["action"]["type"] == "copyToClipboard":
            clip.set_text(response["action"]["textToCopy"])

        if directClicked and response["action"]["type"] == "noHintFound":
            actions.insert(action.target)

    def rango_click_hint(hintText: str, directClicked: bool = False):
        actions.user.rango_execute_simple_command(
            "clickElement", hintText, directClicked
        )

    def rango_open_in_new_tab(hintText: str):
        actions.user.rango_execute_simple_command("openInNewTab", hintText)

    def rango_open_in_new_background_tab(hints: list):
        print(hints)
        actions.user.rango_execute_command(
            {"type": "openInBackgroundTab", "target": hints}
        )

    def rango_copy_link(hintText: str):
        actions.user.rango_execute_simple_command("copyLink", hintText)

    def rango_show_link(hintText: str):
        actions.user.rango_execute_simple_command("showLink", hintText)

    def rango_hover_hint(hintText: str):
        actions.user.rango_execute_simple_command("hoverElement", hintText)

    def rango_fixed_hover_hint(hintText: str):
        actions.user.rango_execute_simple_command("fixedHoverElement", hintText)

    def rango_unhover():
        actions.user.rango_execute_simple_command("unhoverAll")

    def rango_toggle_hints():
        actions.user.rango_execute_simple_command("toggleHints")

    def rango_increase_hint_size():
        actions.user.rango_execute_simple_command("increaseHintSize")

    def rango_decrease_hint_size():
        actions.user.rango_execute_simple_command("decreaseHintSize")

    def rango_set_hint_style(value: str):
        actions.user.rango_execute_simple_command("setHintStyle", value)

    def rango_set_hint_weight(value: str):
        actions.user.rango_execute_simple_command("setHintWeight", value)

    def rango_enable_direct_clicking():
        ctx.settings["user.rango_direct_clicking"] = True

    def rango_disable_direct_clicking():
        ctx.settings["user.rango_direct_clicking"] = False
