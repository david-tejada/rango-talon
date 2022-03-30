from talon import Module, Context, actions
from pathlib import Path
import os
from tempfile import gettempdir
from typing import Any, List
import json

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: browser
"""

def get_communication_dir_path():
    """Returns directory that is used by command-server for communication

    Returns:
        Path: The path to the communication dir
    """
    suffix = ""

    # NB: We don't suffix on Windows, because the temp dir is user-specific
    # anyways
    if hasattr(os, "getuid"):
        suffix = f"-{os.getuid()}"

    return Path(gettempdir()) / f"browser-command-server{suffix}"

communication_dir_path = get_communication_dir_path()
if not communication_dir_path.exists():
  communication_dir_path.mkdir(parents=True, exist_ok=True)
request_path = communication_dir_path / "request.json"
response_path = communication_dir_path / "response.json"

def write_json_exclusive(path: Path, body: Any):
    """Writes jsonified object to file, failing if the file already exists

    Args:
        path (Path): The path of the file to write
        body (Any): The object to convert to json and write
    """
    with path.open("x") as out_file:
        out_file.write(json.dumps(body))

@mod.action_class
class Actions:
  def browser_click_text(text: str):
    """Clicks on a link with a given text"""

@ctx.action_class('user')
class UserActions:
  def browser_click_text(text: str):
    actions.key("ctrl-alt-p")
    action = {
      "action": "click",
      "type": "text",
      "target": text
    }
    write_json_exclusive(response_path, action)
