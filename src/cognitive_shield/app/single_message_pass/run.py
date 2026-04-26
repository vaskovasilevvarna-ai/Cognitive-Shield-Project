"""
Executable entry point for the single-message analytical pass shell.
"""

from .pipeline import run_pipeline


def main() -> None:
    """
    Minimal Sprint 0 entry point.
    """
    run_pipeline()


if __name__ == "__main__":
    main()
