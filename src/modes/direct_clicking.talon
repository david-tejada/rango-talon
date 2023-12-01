tag: browser
and tag: user.rango_direct_clicking
and not tag: user.rango_explicit_clicking
-

^<user.rango_target>$: user.rango_command_with_target("directClickElement", rango_target)
