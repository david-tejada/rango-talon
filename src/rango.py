from typing import Union

from talon import Context, Module, actions

mod = Module()
ctx = Context()


@mod.action_class
class Actions:
    def rango_click_element(target: dict):
        """Clicks an element"""
        actions.user.rango_run_command({"name": "clickElement", "target": target})

    def rango_direct_click_element(target: dict):
        """Clicks an element using direct clicking"""
        actions.user.rango_run_command({"name": "directClickElement", "target": target})

    def rango_focus_element(target: dict):
        """Focuses an element"""
        actions.user.rango_run_command({"name": "focusElement", "target": target})

    def rango_focus_first_input():
        """Focuses the first input element on the page"""
        actions.user.rango_run_command({"name": "focusFirstInput"})

    def rango_activate_tab(tab_target: dict):
        """Switches to a tab using its hint"""
        actions.user.rango_run_command({"name": "activateTab", "target": tab_target})

    def rango_refresh_tab_hints():
        """Refreshes the tab hints"""
        actions.user.rango_run_command({"name": "refreshTabMarkers"})

    def rango_toggle_hints():
        """It toggles the Rango hints globally on or off"""
        actions.user.rango_run_command({"name": "toggleHints"})

    def rango_try_to_focus_and_check_is_editable(target: dict):
        """Tries to focus an element marked with a hint (clicking if it's not a link) and returns true if the active element is editable"""
        return actions.user.rango_run_command(
            {"name": "tryToFocusElementAndCheckIsEditable", "target": target}
        )

    def rango_insert_text_to_input(text: str, target: dict, pressEnter: bool = False):
        """Inserts a given text to an input marked with the target hint"""
        if actions.user.rango_try_to_focus_and_check_is_editable(target):
            actions.edit.select_all()
            actions.edit.delete()
            actions.user.paste(text)
            if pressEnter:
                # Here we insert a wait in case that, for example, some results
                # list needs to be populated (e.g. react.dev)
                actions.sleep("400ms")
                actions.key("enter")

    def rango_clear_input(target: Union[str, list[str]]):
        """Removes the contents of an input"""
        if actions.user.rango_try_to_focus_and_check_is_editable(target):
            actions.edit.select_all()
            actions.edit.delete()

    def rango_run_action_on_reference(actionName: str, referenceName: str):
        """Runs a Rango command on a mark"""
        actions.user.rango_run_command(
            {
                "name": actionName,
                "target": {
                    "type": "primitive",
                    "mark": {"type": "elementReference", "value": referenceName},
                },
            }
        )

    def rango_run_action_on_text_matched_element(
        actionName: str, text: str, prioritize_viewport: Union[bool, None] = False
    ):
        """Runs a Rango command on a hintable element found using fuzzy search"""
        actions.user.rango_run_command(
            {
                "name": actionName,
                "target": {
                    "type": "primitive",
                    "mark": {
                        "type": "fuzzyText",
                        "value": text,
                        "prioritizeViewport": prioritize_viewport,
                    },
                },
            }
        )

    def rango_save_reference(target: dict, referenceName: str):
        """Saves a reference to an element"""
        actions.user.rango_run_command(
            {"name": "saveReference", "target": target, "referenceName": referenceName}
        )

    def rango_save_reference_for_active_element(referenceName: str):
        """Saves a reference for the currently active element"""
        actions.user.rango_run_command(
            {"name": "saveReferenceForActiveElement", "referenceName": referenceName}
        )

    def rango_show_references():
        """Shows all saved references"""
        actions.user.rango_run_command({"name": "showReferences"})

    def rango_remove_reference(referenceName: str):
        """Removes a saved reference"""
        actions.user.rango_run_command(
            {"name": "removeReference", "referenceName": referenceName}
        )

    def rango_copy_link(target: dict):
        """Copies a link address"""
        actions.user.rango_run_command({"name": "copyLink", "target": target})

    def rango_copy_markdown_link(target: dict):
        """Copies a link in markdown format"""
        actions.user.rango_run_command({"name": "copyMarkdownLink", "target": target})

    def rango_copy_element_text(target: dict):
        """Copies the text content of an element"""
        actions.user.rango_run_command(
            {"name": "copyElementTextContent", "target": target}
        )

    def rango_set_selection_before(target: dict):
        """Sets the cursor position before an element"""
        actions.user.rango_run_command({"name": "setSelectionBefore", "target": target})

    def rango_set_selection_after(target: dict):
        """Sets the cursor position after an element"""
        actions.user.rango_run_command({"name": "setSelectionAfter", "target": target})

    def rango_copy_location_property(property: str):
        """Copies a property of the current page location"""
        actions.user.rango_run_command(
            {"name": "copyLocationProperty", "property": property}
        )

    def rango_copy_current_tab_markdown_url():
        """Copies the current tab's URL in markdown format"""
        actions.user.rango_run_command({"name": "copyCurrentTabMarkdownUrl"})

    def rango_increase_hint_size():
        """Increases the size of hints"""
        actions.user.rango_run_command({"name": "increaseHintSize"})

    def rango_decrease_hint_size():
        """Decreases the size of hints"""
        actions.user.rango_run_command({"name": "decreaseHintSize"})

    def rango_display_extra_hints():
        """Displays extra hints"""
        actions.user.rango_run_command({"name": "displayExtraHints"})

    def rango_display_excluded_hints():
        """Displays excluded hints"""
        actions.user.rango_run_command({"name": "displayExcludedHints"})

    def rango_display_less_hints():
        """Displays fewer hints"""
        actions.user.rango_run_command({"name": "displayLessHints"})

    def rango_include_extra_selectors(target: dict):
        """Includes extra selectors for hints"""
        actions.user.rango_run_command(
            {"name": "includeExtraSelectors", "target": target}
        )

    def rango_exclude_extra_selectors(target: dict):
        """Excludes extra selectors for hints"""
        actions.user.rango_run_command(
            {"name": "excludeExtraSelectors", "target": target}
        )

    def rango_exclude_all_hints():
        """Excludes all hints"""
        actions.user.rango_run_command({"name": "excludeAllHints"})

    def rango_include_or_exclude_more_selectors():
        """Includes or excludes more selectors"""
        actions.user.rango_run_command({"name": "includeOrExcludeMoreSelectors"})

    def rango_include_or_exclude_less_selectors():
        """Includes or excludes fewer selectors"""
        actions.user.rango_run_command({"name": "includeOrExcludeLessSelectors"})

    def rango_confirm_selectors_customization():
        """Confirms the customization of selectors"""
        actions.user.rango_run_command({"name": "confirmSelectorsCustomization"})

    def rango_reset_custom_selectors():
        """Resets custom selectors"""
        actions.user.rango_run_command({"name": "resetCustomSelectors"})

    def rango_refresh_hints():
        """Refreshes all hints"""
        actions.user.rango_run_command({"name": "refreshHints"})

    def rango_toggle_hints():
        """Toggles hints visibility"""
        actions.user.rango_run_command({"name": "toggleHints"})

    def rango_enable_hints(level: str = "global"):
        """Enables hints at specified level"""
        actions.user.rango_run_command({"name": "enableHints", "level": level})

    def rango_disable_hints(level: str = "global"):
        """Disables hints at specified level"""
        actions.user.rango_run_command({"name": "disableHints", "level": level})

    def rango_reset_toggle_level(level: str):
        """Resets hint toggle at specified level"""
        actions.user.rango_run_command({"name": "resetToggleLevel", "level": level})

    def rango_display_toggles_status():
        """Displays the status of all toggles"""
        actions.user.rango_run_command({"name": "displayTogglesStatus"})

    def rango_toggle_tab_hints():
        """Toggles tab hints"""
        actions.user.rango_run_command({"name": "toggleTabMarkers"})

    def rango_toggle_keyboard_clicking():
        """Toggles keyboard clicking"""
        actions.user.rango_run_command({"name": "toggleKeyboardClicking"})

    def rango_open_settings_page():
        """Opens the settings page"""
        actions.user.rango_run_command({"name": "openSettingsPage"})

    def rango_open_page_in_new_tab(page: str):
        """Opens a specific page in a new tab"""
        actions.user.rango_run_command({"name": "openPageInNewTab", "url": url})

    def rango_scroll_page(direction: str, factor: float = 1):
        """Scrolls the page in the given direction by the specified factor"""
        command = f"scroll{direction.capitalize()}Page"
        actions.user.rango_run_command({"name": command, "factor": factor})

    def rango_scroll_sidebar(side: str, direction: str, factor: float = 1):
        """Scrolls a sidebar up or down"""
        command = f"scroll{direction}{side}Aside"
        actions.user.rango_run_command({"name": command, "factor": factor})

    def rango_scroll_at_element(direction: str, target: dict, factor: float = 1):
        """Scrolls at an element in the given direction"""
        command = f"scroll{direction.capitalize()}AtElement"
        actions.user.rango_run_command(
            {"name": command, "target": target, "factor": factor}
        )

    def rango_scroll_at_element_again(direction: str):
        """Repeats the previous scroll at element command"""
        command = f"scroll{direction.capitalize()}AtElement"
        actions.user.rango_run_command({"name": command})

    def rango_scroll_element_to_position(position: str, target: dict):
        """Scrolls an element to the specified position (top/bottom/center)"""
        command = f"scrollElementTo{position.capitalize()}"
        actions.user.rango_run_command({"name": command, "target": target})

    def rango_focus_next_tab_with_sound():
        """Focuses the next tab that is producing sound"""
        actions.user.rango_run_command({"name": "focusNextTabWithSound"})

    def rango_focus_next_audible_tab():
        """Focuses the next audible tab. This tab might be muted and not currently producing sound"""
        actions.user.rango_run_command({"name": "focusNextAudibleTab"})

    def rango_focus_next_muted_tab():
        """Focuses the next muted tab"""
        actions.user.rango_run_command({"name": "focusNextMutedTab"})

    def rango_focus_tab_last_sounded():
        """Focuses the tab that last started to play sound"""
        actions.user.rango_run_command({"name": "focusTabLastSounded"})

    def rango_mute_current_tab():
        """Mutes the current tab"""
        actions.user.rango_run_command({"name": "muteCurrentTab"})

    def rango_unmute_current_tab():
        """Unmutes the current tab"""
        actions.user.rango_run_command({"name": "unmuteCurrentTab"})

    def rango_mute_next_tab_with_sound():
        """Mutes the next tab that has sound"""
        actions.user.rango_run_command({"name": "muteNextTabWithSound"})

    def rango_unmute_next_muted_tab():
        """Unmutes the next muted tab"""
        actions.user.rango_run_command({"name": "unmuteNextMutedTab"})

    def rango_mute_tab(tab_target: dict):
        """Mutes a tab using its hint"""
        actions.user.rango_run_command({"name": "muteTab", "target": tab_target})

    def rango_unmute_tab(tab_target: dict):
        """Unmutes a tab using its hint"""
        actions.user.rango_run_command({"name": "unmuteTab", "target": tab_target})

    def rango_mute_all_tabs_with_sound():
        """Mutes all tabs that have sound"""
        actions.user.rango_run_command({"name": "muteAllTabsWithSound"})

    def rango_unmute_all_muted_tabs():
        """Unmutes all muted tabs"""
        actions.user.rango_run_command({"name": "unmuteAllMutedTabs"})

    def rango_close_tab(tab_target: dict):
        """Closes a tab using its hint"""
        actions.user.rango_run_command({"name": "closeTab", "target": tab_target})

    def rango_open_in_new_tab(target: dict):
        """Opens a link in a new tab"""
        actions.user.rango_run_command({"name": "openInNewTab", "target": target})

    def rango_open_in_background_tab(target: dict):
        """Opens a link in a background tab"""
        actions.user.rango_run_command(
            {"name": "openInBackgroundTab", "target": target}
        )

    def rango_close_other_tabs():
        """Closes all other tabs in the window"""
        actions.user.rango_run_command({"name": "closeOtherTabsInWindow"})

    def rango_close_tabs_to_left():
        """Closes all tabs to the left in the window"""
        actions.user.rango_run_command({"name": "closeTabsToTheLeftInWindow"})

    def rango_close_tabs_to_right():
        """Closes all tabs to the right in the window"""
        actions.user.rango_run_command({"name": "closeTabsToTheRightInWindow"})

    def rango_close_tabs_left_end(amount: int = 1):
        """Closes a number of tabs from the left end"""
        actions.user.rango_run_command(
            {"name": "closeTabsLeftEndInWindow", "amount": amount}
        )

    def rango_close_tabs_right_end(amount: int = 1):
        """Closes a number of tabs from the right end"""
        actions.user.rango_run_command(
            {"name": "closeTabsRightEndInWindow", "amount": amount}
        )

    def rango_close_previous_tabs(amount: int = 1):
        """Closes a number of tabs to the left of current tab"""
        actions.user.rango_run_command(
            {"name": "closePreviousTabsInWindow", "amount": amount}
        )

    def rango_close_next_tabs(amount: int = 1):
        """Closes a number of tabs to the right of current tab"""
        actions.user.rango_run_command(
            {"name": "closeNextTabsInWindow", "amount": amount}
        )

    def rango_clone_current_tab():
        """Clones the current tab"""
        actions.user.rango_run_command({"name": "cloneCurrentTab"})

    def rango_focus_previous_tab():
        """Focuses the previously active tab"""
        actions.user.rango_run_command({"name": "focusPreviousTab"})

    def rango_focus_or_create_tab_by_url(url: str):
        """Focuses an existing tab with the given URL or creates a new one"""
        actions.user.rango_run_command({"name": "focusOrCreateTabByUrl", "url": url})

    def rango_focus_tab_by_text(text: str):
        """Focuses a tab matching the given text"""
        actions.user.rango_run_command({"name": "focusTabByText", "text": text})

    def rango_cycle_tabs_by_text(step: int):
        """Cycles through tabs matching the current search text"""
        actions.user.rango_run_command({"name": "cycleTabsByText", "step": step})

    def rango_navigate_to_page_root():
        """Navigates to the root of the current page"""
        actions.user.rango_run_command({"name": "navigateToPageRoot"})

    def rango_navigate_to_next_page():
        """Navigates to the next page"""
        actions.user.rango_run_command({"name": "navigateToNextPage"})

    def rango_navigate_to_previous_page():
        """Navigates to the previous page"""
        actions.user.rango_run_command({"name": "navigateToPreviousPage"})

    def rango_move_tab_to_new_window():
        """Moves the current tab to a new window"""
        actions.user.rango_run_command({"name": "moveCurrentTabToNewWindow"})

    def rango_unhover_all():
        """Removes all hover effects"""
        actions.user.rango_run_command({"name": "unhoverAll"})

    def rango_show_link(target: dict):
        """Shows the address of a link"""
        actions.user.rango_run_command({"name": "showLink", "target": target})

    def rango_hide_hint(target: dict):
        """Hides a specific hint"""
        actions.user.rango_run_command({"name": "hideHint", "target": target})

    def rango_hover_element(target: dict):
        """Hovers over an element"""
        actions.user.rango_run_command({"name": "hoverElement", "target": target})

    def rango_get_bare_title() -> str:
        """Returns the title of the currently focused tab without including the decorations"""
        return actions.user.rango_run_command({"name": "getBareTitle"})
