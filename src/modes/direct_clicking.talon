tag: browser
and not tag: user.rango_disabled
and tag: user.rango_direct_clicking
and not tag: user.rango_explicit_clicking
and not tag: user.rango_explicit_clicking_forced
tag: browser
and not tag: user.rango_disabled
and tag: user.rango_direct_clicking_forced
-

^<user.rango_direct_clicking_target>$: user.rango_direct_click_element(rango_direct_clicking_target)
