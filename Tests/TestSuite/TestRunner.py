import pytest
import sys


class MyPlugin:
    def pytest_sessionfinish(self):
        print("\n*** Test run finished  ***")


if __name__ == "__main__":
    sys.exit(pytest.main(["-x", '..\\Scripts'], plugins=[MyPlugin()]))
