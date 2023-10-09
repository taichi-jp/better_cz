import questionary
from prompt_toolkit.history import FileHistory
from pathlib import Path


class CommitPrompt:
    def __init__(self) -> None:
        self.commit_type = ""
        self.scope = ""
        self.subject = ""

    def ask_commit_type(self):
        self.commit_type = questionary.select(
            "Select the type of change:",
            choices=["feat", "fix", "test", "chore"],
        ).unsafe_ask()

    def ask_scope(self):
        history_file_path = str(Path.home() / ".better_cz_history")
        scope_history = FileHistory(history_file_path)
        self.scope = questionary.text(
            "Select the scope this component affects:", history=scope_history
        ).unsafe_ask()

    def ask_subject(self):
        self.subject = questionary.text(
            "Write a short description of the change:"
        ).unsafe_ask()

    def full_message(self):
        if len(self.scope) > 0:
            return f"{self.commit_type}({self.scope}): {self.subject}"
        else:
            return f"{self.commit_type}: {self.subject}"
