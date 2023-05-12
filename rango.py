from talon import Module, Context, actions, clip, settings, app
import json
import time
from typing import Any, Union

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: browser
"""

mod.tag(
    "rango_direct_clicking",
    desc="Tag for enabling direct clicking in Rango",
)
mod.tag(
    "rango_exclude_singles_tag",
    desc="Tag for enabling using only double letter hints in Rango",
)

rango_start_with_direct_clicking = mod.setting(
    "rango_start_with_direct_clicking",
    type=bool,
    default=True,
    desc="Rango direct clicking mode setting",
)
rango_exclude_singles = mod.setting(
    "rango_exclude_singles",
    type=bool,
    default=False,
    desc="Setting for excluding single letter hints in Rango",
)


def update_clicking_mode(setting_value):
    tags = set(ctx.tags)

    if setting_value == 1:
        tags.add("user.rango_direct_clicking")
    else:
        tags.discard("user.rango_direct_clicking")

    ctx.tags = tags


def update_exclude_singles(setting_value):
    tags = set(ctx.tags)

    if setting_value == 1:
        tags.add("user.rango_exclude_singles_tag")
    else:
        tags.discard("user.rango_exclude_singles_tag")

    ctx.tags = tags


settings.register("user.rango_start_with_direct_clicking", update_clicking_mode)
settings.register("user.rango_exclude_singles", update_exclude_singles)

mod.list("rango_hints_toggle_levels", desc="list of Rango hints toggle levels")
mod.list(
    "rango_page_location_property",
    desc="list of properties to be found in window.location",
)
mod.list("rango_page", desc="A Rango-related page")

toggle_levels = ["everywhere", "global", "tab", "host", "page", "now"]
ctx.lists["user.rango_hints_toggle_levels"] = {k: k for k in toggle_levels}
ctx.lists["user.rango_page_location_property"] = {
    "address": "href",
    "host name": "hostname",
    "host": "host",
    "origin": "origin",
    "path": "pathname",
    "port": "port",
    "protocol": "protocol",
}
ctx.lists["user.rango_page"] = {
    "sponsor": "https://github.com/sponsors/david-tejada",
    "read me": "https://github.com/david-tejada/rango/blob/main/readme.md",
    "issues": "https://github.com/david-tejada/rango/issues",
    "new issue": "https://github.com/david-tejada/rango/issues/new",
    "changelog": "https://github.com/david-tejada/rango/blob/main/CHANGELOG.md",
}


@mod.capture(rule="<user.letter> | <user.letter> <user.letter>")
def rango_hint(m) -> str:
    return "".join(m.letter_list)


@mod.capture(rule="<user.letter>")
def rango_hint_double(m) -> str:
    return m.letter + m.letter


@mod.capture(rule="<user.rango_hint> (and <user.rango_hint>)*")
def rango_target(m) -> list[str]:
    return m.rango_hint_list


MINIMUM_SLEEP_TIME_SECONDS = 0.0005


def read_json_response_with_timeout(timeout_seconds) -> Any:
    """Repeatedly tries to read a json object from the clipboard, waiting
    until the message type is "response"

    Raises:
        Exception: If we timeout waiting for a response

    Returns:
        Any: The json-decoded contents of the file
    """
    timeout_time = time.perf_counter() + timeout_seconds
    sleep_time = MINIMUM_SLEEP_TIME_SECONDS
    message = None
    initial_raw_text = clip.text()
    while True:
        raw_text = clip.text()
        try:
            message = json.loads(raw_text)
        # We make sure the message is valid JSON. For example, if a click command
        # results in something being copied to the clipboard and we check the clipboard
        # before Rango has time to copy the response to the clipboard.
        except ValueError as error:
            if initial_raw_text != raw_text:
                continue
            else:
                # Sanity check to make sure the initial request was valid JSON
                raise ValueError("The request message wasn't valid JSON")

        if message["type"] == "response":
            break

        actions.sleep(sleep_time)

        time_left = timeout_time - time.perf_counter()

        if time_left < 0:
            raise Exception("Timed out waiting for response")

        # NB: We use minimum sleep time here to ensure that we don't spin with
        # small sleeps due to clock slip
        sleep_time = max(min(sleep_time * 2, time_left), MINIMUM_SLEEP_TIME_SECONDS)

    return message


def send_request_and_wait_for_response(action: dict, timeout_seconds: float = 3.0):
    message = {"version": 1, "type": "request", "action": action}
    json_message = json.dumps(message)
    with clip.revert():
        clip.set_text(json_message)
        actions.user.rango_type_hotkey()
        response = read_json_response_with_timeout(timeout_seconds)

    response_actions = response.get("actions")

    if response_actions == None:
        actions.app.notify(
            "Rango-talon is ahead of the Rango extension. Restart the browser to update the Rango extension"
        )
        return

    for response_action in response_actions:
        name = response_action["name"]

        if name == "copyToClipboard":
            actions.clip.set_text(response_action["textToCopy"])

        if name == "typeTargetCharacters":
            actions.insert(action["target"][0])

        if name == "focusPage":
            try:
                actions.browser.focus_page()
            except NotImplementedError:
                actions.browser.focus_address()
                actions.key("esc:3")

        if name == "key":
            actions.key(response_action["key"])

        if name == "editDelete":
            actions.edit.delete()

        if name == "sleep":
            if "ms" in response_action:
                actions.sleep(f"{response_action['ms']}ms")
            else:
                actions.sleep("200ms")


@mod.action_class
class Actions:
    def rango_type_hotkey():
        """Presses the rango hotkey to read the command from the clipboard"""

    def rango_command_with_target(
        actionType: str,
        target: Union[str, list[str]],
        arg: Union[str, float, None] = None,
    ):
        """Executes a Rango command"""

    def rango_command_without_target(
        actionType: str, arg: Union[str, float, None] = None
    ):
        """Executes a Rango command without a target"""

    def rango_toggle_hints():
        """It toggles the Rango hints globally on or off"""

    def rango_enable_direct_clicking():
        """Enables rango direct mode so that the user doesn't have to say 'click' before the hint letters"""

    def rango_disable_direct_clicking():
        """Disables rango direct mode"""


@ctx.action_class("user")
class UserActions:
    def rango_type_hotkey():
        actions.key("ctrl-shift-insert")

    def rango_command_with_target(
        actionType: str,
        target: Union[str, list[str]],
        arg: Union[str, float, None] = None,
    ):
        if isinstance(target, str):
            target = [target]
        action = {"type": actionType, "target": target}
        if arg:
            action["arg"] = arg
        send_request_and_wait_for_response(action)

    def rango_command_without_target(
        actionType: str, arg: Union[str, float, None] = None
    ):
        action = {"type": actionType}
        if arg:
            action["arg"] = arg
        send_request_and_wait_for_response(action)

    # Necessary for talon_hud
    def rango_toggle_hints():
        actions.user.rango_command_without_target("toggleHints")

    def rango_enable_direct_clicking():
        ctx.tags = ["user.rango_direct_clicking"]

    def rango_disable_direct_clicking():
        ctx.tags = []
