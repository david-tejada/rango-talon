tag: browser
-

click <user.rango_target>: user.rango_execute_command("clickElement", rango_target)
blank <user.rango_target>: user.rango_execute_command("openInNewTab", rango_target)
stash <user.rango_target>: 
  user.rango_execute_command("openInBackgroundTab", rango_target)
copy link <user.rango_target>: user.rango_execute_command("copyLink", rango_target)
copy text <user.rango_target>: user.rango_execute_command("copyTextContent", rango_target)
show <user.rango_target>: user.rango_execute_command("showLink", rango_target)
hover <user.rango_target>: user.rango_execute_command("hoverElement", rango_target)
dismiss: user.rango_execute_command("unhoverAll")
hint bigger: user.rango_execute_command("increaseHintSize")
hint smaller: user.rango_execute_command("decreaseHintSize")
hint {user.rango_hint_styles}: user.rango_execute_command("setHintStyle", user.rango_hint_styles)
hint weight {user.rango_hint_weights}: user.rango_execute_command("setHintWeight", user.rango_hint_weights)
hints refresh: user.rango_execute_command("refreshHints")
hints toggle: user.rango_execute_command("toggleHints")
hints on [{user.rango_hints_toggle_levels}]: 
  user.rango_execute_command("showHints{rango_hints_toggle_levels or ''}")
hints off [{user.rango_hints_toggle_levels}]: 
  user.rango_execute_command("hideHints{rango_hints_toggle_levels or ''}")

rango explicit:  user.rango_disable_direct_clicking()
rango direct:  user.rango_enable_direct_clicking()
