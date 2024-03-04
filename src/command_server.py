from talon import Module, clip, actions
import json
import time
from typing import Union, Any

mod = Module()

MINIMUM_SLEEP_TIME_SECONDS = 0.0005


# This doesn't wait for the extension to respond to avoid creating an infinite
# loop if the extension is not responsive
def send_request_timed_out():
    message = {"version": 1, "type": "request", "action": {"type": "requestTimedOut"}}
    json_message = json.dumps(message)
    clip.set_text(json_message)
    actions.user.rango_type_hotkey()
    actions.sleep("200ms")


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
            if message["type"] == "response":
                return message
        # We make sure the message is valid JSON. For example, if a click command
        # results in something being copied to the clipboard and we check the clipboard
        # before Rango has time to copy the response to the clipboard.
        except ValueError as error:
            if initial_raw_text == raw_text:
                # Sanity check to make sure the initial request was valid JSON
                raise ValueError("The request message wasn't valid JSON")

        actions.sleep(sleep_time)

        time_left = timeout_time - time.perf_counter()

        if time_left < 0:
            send_request_timed_out()
            raise Exception("Timed out waiting for response")

        # NB: We use minimum sleep time here to ensure that we don't spin with
        # small sleeps due to clock slip
        sleep_time = max(min(sleep_time * 2, time_left), MINIMUM_SLEEP_TIME_SECONDS)


def send_request_and_wait(action: dict) -> Any:
    message = {"version": 1, "type": "request", "action": action}
    json_message = json.dumps(message)
    with clip.revert():
        clip.set_text(json_message)
        actions.user.rango_type_hotkey()
        response = read_json_response_with_timeout(3.0)

    return response


def handle_response(response: Any, request_action: dict):
    response_actions = response.get("actions")
    if actions == None:
        actions.app.notify(
            "Rango-talon is ahead of the Rango extension. Restart the browser to update the Rango extension"
        )

        return

    result = None

    for action in response_actions:
        match action["name"]:
            case "focusPageAndResend":
                try:
                    actions.browser.focus_page()
                except NotImplementedError:
                    actions.browser.focus_address()
                    actions.key("esc:3")

                response = send_request_and_wait(request_action)
                result = handle_response(response, request_action)

            case "copyToClipboard":
                actions.clip.set_text(action["textToCopy"])

            case "typeTargetCharacters":
                actions.insert(request_action["target"][0])

            case "focusPage":
                try:
                    actions.browser.focus_page()
                except NotImplementedError:
                    actions.browser.focus_address()
                    actions.key("esc:3")

            case "key":
                actions.key(action["key"])

            case "editDelete":
                actions.edit.delete()

            case "sleep":
                if "ms" in action:
                    actions.sleep(f"{action['ms']}ms")
                else:
                    actions.sleep("200ms")

            case "responseValue":
                result = action["value"]

            case "openInNewTab":
                actions.app.tab_open()
                actions.browser.go(action["url"])

    return result


@mod.action_class
class Actions:
    def rango_type_hotkey():
        """Presses the rango hotkey to read the command from the clipboard"""
        actions.key("ctrl-shift-insert")

    def rango_run_command(action: dict):
        """Sends a request to the Rango extension, waits for the response and handles it"""
        response = send_request_and_wait(action)
        return handle_response(response, action)
