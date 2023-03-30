import pytest
import os

@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, "test.txt")
    with open(target_file, 'w') as file:
        lines = ["2 USA 9834000km^2 331000000\n",
                 "3 Britain 243610km^2 67000000\n",
                 "10 France 551695km^2 68000000\n"
                 ]
        file.writelines(lines)
    return target_file