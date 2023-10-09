from commit_prompt import CommitPrompt
import subprocess


def cz():
    commit_prompt = CommitPrompt()

    try:
        commit_prompt.ask_commit_type()
        print(commit_prompt.full_message())

        commit_prompt.ask_scope()
        print(commit_prompt.full_message())

        commit_prompt.ask_subject()

        subprocess.run(
            ["git", "commit", "-m", commit_prompt.full_message()], check=True
        )
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    cz()
