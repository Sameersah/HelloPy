import pytest
from io import StringIO
from contextlib import redirect_stdout
from src.app import main


def test_main():
    """
    Test the main function to ensure it prints 'Hello, World!'.
    """
    # Redirect stdout to capture the print output
    output = StringIO()
    with redirect_stdout(output):
        main()
    assert output.getvalue().strip() == "Hello World!\n3"
