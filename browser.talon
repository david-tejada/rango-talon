tag: browser
-

# Click
click <user.rango_target>:
  user.rango_command_with_target("clickElement", rango_target)

# Open in a new tab
blank <user.rango_target>:
  user.rango_command_with_target("openInNewTab", rango_target)
stash <user.rango_target>:
  user.rango_command_with_target("openInBackgroundTab", rango_target)

# Hover
hover <user.rango_target>:
  user.rango_command_with_target("hoverElement", rango_target)
dismiss: user.rango_command_with_target("unhoverAll")

# Show link address
show <user.rango_target>:
  user.rango_command_with_target("showLink", rango_target)

# Scroll
upper: user.rango_command_without_target("scrollUpPage")
downer: user.rango_command_without_target("scrollDownPage")
upper <user.rango_target>:
  user.rango_command_with_target("scrollUpAtElement", rango_target)
downer <user.rango_target>:
  user.rango_command_with_target("scrollDownAtElement", rango_target)
up again: user.rango_command_without_target("scrollUpAtElement")
down again: user.rango_command_without_target("scrollDownAtElement")

# Copy target information
copy [link] <user.rango_target>:
  user.rango_command_with_target("copyLink", rango_target)
copy mark <user.rango_target>:
  user.rango_command_with_target("copyMarkdownLink", rango_target)
copy text <user.rango_target>:
  user.rango_command_with_target("copyElementTextContent", rango_target)

# Copy current url information
copy page {user.rango_page_location_property}:
  user.rango_command_without_target("copyLocationProperty", rango_page_location_property)
copy mark address:
  user.rango_command_without_target("copyCurrentTabMarkdownUrl")

# Modify hints appearance
hint bigger: user.rango_command_without_target("increaseHintSize")
hint smaller: user.rango_command_without_target("decreaseHintSize")
hint {user.rango_hint_styles}: 
  user.rango_command_without_target_with_arg("setHintStyle", user.rango_hint_styles)
hint weight {user.rango_hint_weights}:
  user.rango_command_without_target_with_arg("setHintWeight", user.rango_hint_weights)

# Show and hide hints
hints refresh: user.rango_command_without_target("refreshHints")
hints toggle: user.rango_command_without_target("toggleHints")
hints on [{user.rango_hints_toggle_levels}]: 
  user.rango_command_without_target_with_arg("enableHints", rango_hints_toggle_levels or "global")
hints off [{user.rango_hints_toggle_levels}]: 
  user.rango_command_without_target_with_arg("disableHints", rango_hints_toggle_levels or "global")

# Enable or disable showing the url in the title
address in title on: user.rango_command_without_target("enableUrlInTitle")
address in title off: user.rango_command_without_target("disableUrlInTitle")

# Switch modes
rango explicit:  user.rango_disable_direct_clicking()
rango direct:  user.rango_enable_direct_clicking()
