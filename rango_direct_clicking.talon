tag: browser
and tag: user.rango_direct_clicking
-

^<user.rango_target>$: user.rango_command_with_target("directClickElement", rango_target)
^<user.rango_hint_double> (twice | second)$: user.rango_command_with_target("directClickElement", rango_hint_double)