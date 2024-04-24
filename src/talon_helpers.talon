code.language: talon
-
# Helpers to make scripting easier

# Using references
click rango mark <user.word>: "user.rango_run_action_on_reference(\"clickElement\", \"{word}\")"
focus rango mark <user.word>: "user.rango_run_action_on_reference(\"focusElement\", \"{word}\")"
hover rango mark <user.word>: "user.rango_run_action_on_reference(\"hoverElement\", \"{word}\")"

# Using fuzzy search with the text of the element
click rango text <user.text>: "user.rango_run_action_on_text_matched_element(\"clickElement\", \"{text}\")"
focus rango text <user.text>: "user.rango_run_action_on_text_matched_element(\"focusElement\", \"{text}\")"
hover rango text <user.text>: "user.rango_run_action_on_text_matched_element(\"hoverElement\", \"{text}\")"