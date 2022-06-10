tag: browser
and tag: user.rango_direct_clicking
-
^<user.letter>$: user.rango_execute_command("directClickElement", letter)
^<user.letter> <user.letter>$: user.rango_execute_command("directClickElement", "{letter_1}{letter_2}")