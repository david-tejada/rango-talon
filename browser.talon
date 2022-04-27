tag: browser
-
click <user.letters>: user.browser_click_hint(letters)
hover <user.letters>: user.browser_hover_hint(letters)
hover fix <user.letters>: user.browser_fixed_hover_hint(letters)
dismiss: user.browser_unhover()
hints toggle: user.browser_toggle_hints()

# When we click via javascript with target="_blank" or target="new" we get a prompt
# to allow the website to open popups. This command allows the current website to open
# popups. It works in firefox I have to try in chrome to see if it's different
allow popup:
  key(alt-p)
  sleep(200ms)
  key(down)
  key(enter)

rango default:  user.browser_disable_direct_clicking()
rango direct:  user.browser_enable_direct_clicking()