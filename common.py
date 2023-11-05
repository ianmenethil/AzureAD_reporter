# Description: Common.py contains Common classes used in python files. Contents:
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit import prompt
import typer

class Choices:
    @staticmethod
    def custom_selection_dialog(title, options):
        bindings = KeyBindings()
        selected_index = 0

        @bindings.add(Keys.Up)
        def move_up(_):
            nonlocal selected_index
            selected_index = (selected_index - 1) % len(options)

        @bindings.add(Keys.Down)
        def move_down(_):
            nonlocal selected_index
            selected_index = (selected_index + 1) % len(options)

        @bindings.add(Keys.Enter)
        def select(event):
            event.app.exit()

        def get_prompt_text():
            text = title + "\n"
            for i, option in enumerate(options):
                if i == selected_index:
                    text += f"[{i}] > {option[0]} <\n"
                else:
                    text += f"[{i}]   {option[0]}\n"
            return text
        prompt(get_prompt_text, key_bindings=bindings, refresh_interval=0.1)
        return selected_index

    @staticmethod
    def get_selection(console, title, options, exit_message):
        selected_index = Choices.custom_selection_dialog(title, options)
        if selected_index is None:
            console.print(exit_message, style="bold red")
            raise typer.Exit(code=1)
        selected_index = int(selected_index)
        console.print(f"{title} selected: {options[selected_index][0]}", style="bold blue")
        return selected_index

    @staticmethod
    def get_userType(console):
        """Get the user type from the selection dialog."""
        options = [("All", 0), ("Guest", 1), ("Member", 2)]
        return Choices.get_selection(console, "Select user type to process", options, "No user type selected. Exiting.")

    @staticmethod
    def get_license(console):
        options = [("No", 0), ("Yes", 1)]
        return Choices.get_selection(console, "Do you want to get licenses and plans for users?", options, "No option selected for licenses. Exiting.")

    @staticmethod
    def get_accountEnabled(console):
        options = [("Enabled Accounts Only", 0), ("All", 1)]
        return Choices.get_selection(console, "Please choose an account:", options, "No account selected. Exiting.")

    @staticmethod
    def get_job(console):
        options = [
            ("Get User last sign-in data", 0),
            ("Get Suspicious User Audits[NOT YET IMPLEMENTED]", 1),
            ("User plans and licenses[NOT YET IMPLEMENTED]", 2),
            ("Get Password and MFA details[NOT YET IMPLEMENTED]", 2)]
        selected_index = Choices.custom_selection_dialog("Please select what to execute:", options)
        console.print(f"Please select what to execute: Selected option: {options[selected_index][0]}", style="bold blue")
        return selected_index
