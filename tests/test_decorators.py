import os

from src.decorators import log


def test_log_to_console_success(capsys):
    @log()
    def test_function_success_console(x, y):
        return x + y
        test_function_success_console(1, 2)
        captured = capsys.readouterr()
        assert "test_function_success_console ok" in captured.out


def test_log_to_file_success():
    @log(filename="test_log.txt")
    def test_function_success(x, y):
        return x + y

    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    test_function_success(1, 2)

    with open("test_log.txt", "r") as log_file:
        lines = log_file.readlines()

    assert len(lines) == 1
    assert lines[0].strip() == "test_function_success ok"
