tag: browser
-
click <user.letters>: user.browser_click_hint(letters, 0)
blank <user.letters>: user.browser_click_hint(letters, 1)
hover <user.letters>: user.browser_hover_hint(letters)
hover fix <user.letters>: user.browser_fixed_hover_hint(letters)
dismiss: user.browser_unhover()
hints toggle: user.browser_toggle_hints()

rango default:  user.browser_disable_direct_clicking()
rango direct:  user.browser_enable_direct_clicking()