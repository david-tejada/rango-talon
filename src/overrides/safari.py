import os
import plistlib
import subprocess
from talon import Context, actions


ctx = Context()
ctx.matches = r"""
tag: browser
app: safari
"""

safari_version = ''

def get_safari_version() -> str:
    global safari_version
    try:
        if safari_version != '':
            return safari_version
        
        paths = subprocess.getoutput(f'mdfind "kMDItemCFBundleIdentifier == com.apple.Safari"').splitlines()
        for path in paths:
            with open(os.path.join(path, "Contents/Info.plist"), "rb") as f:
                plist = plistlib.load(f)
                safari_version = plist['CFBundleShortVersionString']
    except Exception as e:
        safari_version = 'unknown'
        print('Exception retrieving safari version:', e.__class__, e)
    finally:
        return safari_version


@ctx.action_class("user")
class UserActions:
    def rango_type_hotkey():
        version = get_safari_version()
        key = "ctrl-shift-keypad_3" if version.startswith('18.') else "ctrl-shift-3"
        actions.key(key)
