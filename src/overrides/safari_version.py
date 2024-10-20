import os
import subprocess


_safari_version = ''

def get() -> str:
    global _safari_version
    try:
        if _safari_version != '':
            return _safari_version
        
        import plistlib 
        # Not sure how Python handles this cross-platform: 
        # imported inside try-catch to avoid breaking other platforms
        paths = subprocess.getoutput(f'mdfind "kMDItemCFBundleIdentifier == com.apple.Safari"').splitlines()
        for path in paths:
            with open(os.path.join(path, "Contents/Info.plist"), "rb") as f:
                plist = plistlib.load(f)
                _safari_version = plist['CFBundleShortVersionString']
    except Exception as e:
        _safari_version = 'unknown'
        print('Exception retrieving safari version:', e.__class__, e)
    finally:
        return _safari_version