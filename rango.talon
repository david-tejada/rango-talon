tag: browser
-
settings():
  user.rango_start_with_direct_clicking = 1
  user.rango_exclude_singles = 0

# Click
click <user.rango_target>:
  user.rango_command_with_target("clickElement", rango_target)

# Focus
focus <user.rango_target>:
  user.rango_command_with_target("focusElement", rango_target)

go input:
  user.rango_command_without_target("focusFirstInput")

# Focus and Enter
flick <user.rango_target>:
  user.rango_command_with_target("focusElement", rango_target)
  key(enter)

# Focus tab
(go tab | slot) <user.rango_target>:
  user.rango_command_with_target("activateTab", rango_target)
tab marker refresh: user.rango_command_without_target("refreshTabMarkers")

# Open in a new tab
blank <user.rango_target>:
  user.rango_command_with_target("openInNewTab", rango_target)
stash <user.rango_target>:
  user.rango_command_with_target("openInBackgroundTab", rango_target)

# Navigation
go root: user.rango_command_without_target("navigateToPageRoot")
page next: user.rango_command_without_target("navigateToNextPage")
page last: user.rango_command_without_target("navigateToPreviousPage")

# Move current tab to a new window
tab split: user.rango_command_without_target("moveCurrentTabToNewWindow")

# Focus previous tab
tab back: user.rango_command_without_target("focusPreviousTab")

# Close tabs
tab close other: user.rango_command_without_target("closeOtherTabsInWindow")
tab close left: user.rango_command_without_target("closeTabsToTheLeftInWindow")
tab close right: user.rango_command_without_target("closeTabsToTheRightInWindow")
tab close first [<number_small>]:
  user.rango_command_without_target("closeTabsLeftEndInWindow", number_small or 1)
tab close final [<number_small>]:
  user.rango_command_without_target("closeTabsRightEndInWindow", number_small or 1)
tab close previous [<number_small>]:
  user.rango_command_without_target("closePreviousTabsInWindow", number_small or 1)
tab close next [<number_small>]:
  user.rango_command_without_target("closeNextTabsInWindow", number_small or 1)

# Clone tab
tab clone: user.rango_command_without_target("cloneCurrentTab")

# Hover
hover <user.rango_target>:
  user.rango_command_with_target("hoverElement", rango_target)
dismiss: user.rango_command_without_target("unhoverAll")

# Show link address
show <user.rango_target>:
  user.rango_command_with_target("showLink", rango_target)

# Scroll
upper: user.rango_command_without_target("scrollUpPage")
upper <number>: user.rango_command_without_target("scrollUpPage", number)
upper all: user.rango_command_without_target("scrollUpPage", 9999)
tiny up: user.rango_command_without_target("scrollUpPage", 0.2)

downer: user.rango_command_without_target("scrollDownPage")
downer <number>: user.rango_command_without_target("scrollDownPage", number)
downer all: user.rango_command_without_target("scrollDownPage", 9999)
tiny down: user.rango_command_without_target("scrollDownPage", 0.2)

scroll left: user.rango_command_without_target("scrollLeftPage")
scroll left all: user.rango_command_without_target("scrollLeftPage", 9999)
tiny left: user.rango_command_without_target("scrollLeftPage", 0.2)

scroll right: user.rango_command_without_target("scrollRightPage")
scroll right all: user.rango_command_without_target("scrollRightPage", 9999)
tiny right: user.rango_command_without_target("scrollRightPage", 0.2)

# Scroll the left or right asides
upper left: user.rango_command_without_target("scrollUpLeftAside")
upper left all: user.rango_command_without_target("scrollUpLeftAside", 9999)

downer left: user.rango_command_without_target("scrollDownLeftAside")
downer left all: user.rango_command_without_target("scrollDownLeftAside", 9999)

upper right: user.rango_command_without_target("scrollUpRightAside")
upper right all: user.rango_command_without_target("scrollUpRightAside", 9999)

downer right: user.rango_command_without_target("scrollDownRightAside")
downer right all: user.rango_command_without_target("scrollDownRightAside", 9999)

# Scroll the scrolling container that contains the target
upper <user.rango_target>:
  user.rango_command_with_target("scrollUpAtElement", rango_target)
tiny up <user.rango_target>:
  user.rango_command_with_target("scrollUpAtElement", rango_target, 0.2)

downer <user.rango_target>:
  user.rango_command_with_target("scrollDownAtElement", rango_target)
tiny down <user.rango_target>:
  user.rango_command_with_target("scrollDownAtElement", rango_target, 0.2)

scroll left <user.rango_target>:
  user.rango_command_with_target("scrollLeftAtElement", rango_target)
tiny left <user.rango_target>:
  user.rango_command_with_target("scrollLeftAtElement", rango_target, 0.1)

scroll right <user.rango_target>:
  user.rango_command_with_target("scrollRightAtElement", rango_target)
tiny right <user.rango_target>:
  user.rango_command_with_target("scrollRightAtElement", rango_target, 0.1)

# Repeat previous scroll
up again: user.rango_command_without_target("scrollUpAtElement")
down again: user.rango_command_without_target("scrollDownAtElement")
left again: user.rango_command_without_target("scrollLeftAtElement")
right again: user.rango_command_without_target("scrollRightAtElement")

# Snap scroll
crown <user.rango_target>:
  user.rango_command_with_target("scrollElementToTop", rango_target)
bottom <user.rango_target>:
  user.rango_command_with_target("scrollElementToBottom", rango_target)
center <user.rango_target>:
  user.rango_command_with_target("scrollElementToCenter", rango_target)

# Copy target information
copy [link] <user.rango_target>:
  user.rango_command_with_target("copyLink", rango_target)
copy mark <user.rango_target>:
  user.rango_command_with_target("copyMarkdownLink", rango_target)
copy text <user.rango_target>:
  user.rango_command_with_target("copyElementTextContent", rango_target)

# Paste
paste to <user.rango_target>:
  user.rango_insert_text_to_input(clip.text(), rango_target, 0)

# Insert text to field
insert <user.text> to <user.rango_target>:
  user.rango_insert_text_to_input(text, rango_target, 0)
enter <user.text> to <user.rango_target>:
  user.rango_insert_text_to_input(text, rango_target, 1)

# Cursor position
pre <user.rango_target>:
  user.rango_command_with_target("setSelectionBefore", rango_target)
post <user.rango_target>:
  user.rango_command_with_target("setSelectionAfter", rango_target)

# Clear field
change <user.rango_target>:
  user.rango_clear_input(rango_target)

# Copy current url information
copy page {user.rango_page_location_property}:
  user.rango_command_without_target("copyLocationProperty", rango_page_location_property)
copy mark address:
  user.rango_command_without_target("copyCurrentTabMarkdownUrl")

# Modify hints appearance
hint bigger: user.rango_command_without_target("increaseHintSize")
hint smaller: user.rango_command_without_target("decreaseHintSize")

# Exclude or include single letter hints
hint exclude singles: user.rango_command_without_target("excludeSingleLetterHints")
hint include singles: user.rango_command_without_target("includeSingleLetterHints")

# Extra hints
hint extra: user.rango_command_without_target("displayExtraHints")
hint more: user.rango_command_without_target("displayExcludedHints")
hint less: user.rango_command_without_target("displayLessHints")
include <user.rango_target>: user.rango_command_with_target("includeExtraSelectors", rango_target)
exclude <user.rango_target>: user.rango_command_with_target("excludeExtraSelectors", rango_target)
some more: user.rango_command_without_target("includeOrExcludeMoreSelectors")
some less: user.rango_command_without_target("includeOrExcludeLessSelectors")
custom hints save: user.rango_command_without_target("confirmSelectorsCustomization")
custom hints reset: user.rango_command_without_target("resetCustomSelectors")

# Show and hide hints
hints refresh: user.rango_command_without_target("refreshHints")
hints (toggle | switch): user.rango_command_without_target("toggleHints")
hints on [{user.rango_hints_toggle_levels}]: 
  user.rango_command_without_target("enableHints", rango_hints_toggle_levels or "global")
hints off [{user.rango_hints_toggle_levels}]: 
  user.rango_command_without_target("disableHints", rango_hints_toggle_levels or "global")
hints reset {user.rango_hints_toggle_levels}: 
  user.rango_command_without_target("resetToggleLevel", rango_hints_toggle_levels)
toggle show:
  user.rango_command_without_target("displayTogglesStatus")

# Toggle keyboard clicking
keyboard (toggle | switch): user.rango_command_without_target("toggleKeyboardClicking")

# Enable or disable showing the url in the title
address in title on: user.rango_command_without_target("enableUrlInTitle")
address in title off: user.rango_command_without_target("disableUrlInTitle")

# Switch modes
rango explicit:  user.rango_disable_direct_clicking()
rango direct:  user.rango_enable_direct_clicking()

# Setting page
rango settings: user.rango_command_without_target("openSettingsPage")

# Pages
rango open {user.rango_page}: user.rango_command_without_target("openPageInNewTab", rango_page)