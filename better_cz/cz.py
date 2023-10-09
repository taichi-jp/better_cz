import subprocess
from better_cz.commit_prompt import CommitPrompt


def main():
    prompt = CommitPrompt()

    try:
        prompt.ask_commit_type()
        print(prompt.full_message())

        prompt.ask_scope()
        print(prompt.full_message())

        prompt.ask_subject()

        subprocess.run(["git", "commit", "-m", prompt.full_message()], check=True)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
