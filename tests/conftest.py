import pytest
import os


def pytest_addoption(parser):
    parser.addoption(
        "--collect-tests",
        action="store_true",
        help="Collect tests",
        default=False,
    )


def pytest_collection_modifyitems(config, items):
    tests = set()
    if config.option.collect_tests:
        for item in items:
            item.add_marker(pytest.mark.skipif(True, reason="Skip"))
            path = os.path.relpath(item.module.__file__)
            tests.add("{}\n".format(path))
            test_str = path
            if item.cls:
                test_str += f"::{item.cls.__name__}"
            if item.function:
                test_str += f"::{item.function.__name__}"
            tests.add(f"{test_str}\n")
        with open(".pytest.completion", "w") as file:
            file.writelines(tests)
