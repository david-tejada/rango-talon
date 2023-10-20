tag: user.talon
-
# Helpers to make scripting using references easier
click rango mark <user.word>: "user.rango_run_action_on_reference(\"clickElement\", \"{word}\")"
focus rango mark <user.word>: "user.rango_run_action_on_reference(\"focusElement\", \"{word}\")"
hover rango mark <user.word>: "user.rango_run_action_on_reference(\"hoverElement\", \"{word}\")"
