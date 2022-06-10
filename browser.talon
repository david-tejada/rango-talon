tag: browser
-
click <user.letters>: user.rango_click_hint(letters)
blank <user.letters>: user.rango_open_in_new_tab(letters)
stash <user.rango_hints>: user.rango_open_in_new_background_tab(rango_hints)
copy link <user.letters>: user.rango_copy_link(letters)
show <user.letters>: user.rango_show_link(letters)
hover <user.letters>: user.rango_hover_hint(letters)
hover fix <user.letters>: user.rango_fixed_hover_hint(letters)
dismiss: user.rango_unhover()
hint bigger: user.rango_increase_hint_size()
hint smaller: user.rango_decrease_hint_size()
hint {user.rango_hint_styles}: user.rango_set_hint_style(user.rango_hint_styles)
hint weight {user.rango_hint_weights}: user.rango_set_hint_weight(user.rango_hint_weights)
hints toggle: user.rango_toggle_hints()
hints on [{user.rango_hints_toggle_levels}]: 
  user.rango_execute_simple_command("showHints{rango_hints_toggle_levels or ''}")
hints off [{user.rango_hints_toggle_levels}]: 
  user.rango_execute_simple_command("hideHints{rango_hints_toggle_levels or ''}")

rango explicit:  user.rango_disable_direct_clicking()
rango direct:  user.rango_enable_direct_clicking()
