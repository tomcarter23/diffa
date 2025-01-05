import pytest
import os
import subprocess


@pytest.mark.parametrize("sbs", [True, False])
def test_smoke_cli(sbs):
    tmp_output = "./tests/tmp/tmp.out.html"
    if sbs:
        subprocess.run(["diffa", "./tests/data/file1.txt", "./tests/data/file2.txt",
                        tmp_output, "--side-by-side"])
    else:
        subprocess.run(["diffa", "./tests/data/file1.txt", "./tests/data/file2.txt", tmp_output, "--side-by-side"])

    assert os.path.isfile(tmp_output)

    os.remove("./tests/tmp/tmp.out.html")
