from talon import Module, Context, actions, clip
import json
import time
from typing import Any

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: browser
"""

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

def execute_command(msg: Any):
  json_message = json.dumps(msg)

  with clip.revert():
    clip.set_text(json_message)
    actions.key("alt-shift-p")
    response = read_json_response_with_timeout()

@mod.action_class
class Actions:
  def browser_click_text(text: str):
    """Clicks on a link with a given text"""

@ctx.action_class('user')
class UserActions:
  def browser_click_text(text: str):
    command = {
      "type": "request",
      "action": {
        "type": "click",
        "target": text
      }
    }
    execute_command(command)

