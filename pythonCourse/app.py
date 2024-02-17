"""Module focused on python course of Alura"""

from src.models.application import Application
from src.challenges.main import run_challenges
from src import app_sequential_version

app = Application()


def main():
    """The main Function"""
    app.run()
    app.bump_version(bump_type="PATCH")
    print(app)
    app_sequential_version.main()
    run_challenges()


if __name__ == "__main__":
    main()
