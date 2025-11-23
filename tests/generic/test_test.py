from pathlib import Path

import copier
import pytest
from plumbum import local

from tests.utils import CWD, SandboxedGitRepo


@pytest.fixture
def data() -> dict[str, str]:
    """Return a dictionary with the data to be used in the template."""
    return {
        "type": "generic",
        "accountname": "foo",
        "reponame": "foo",
        "repourl": "https://github.com/foo/foo",
        "description": "Example template",
        "example": "false",
    }


@pytest.fixture
def copied_template_directory(
    tmp_path_factory: pytest.TempPathFactory,
    cloned_template_directory: Path,
    data: dict[str, str],
) -> Path:
    """Return a temporary directory with a copied template."""
    tmp_path = tmp_path_factory.mktemp("copied-template-")

    copier.run_copy(
        str(cloned_template_directory),
        str(tmp_path),
        data=data,
        vcs_ref="HEAD",
        quiet=True,
    )

    with SandboxedGitRepo(tmp_path):
        local.cmd.git("add", "./")
        local.cmd.git("commit", "--message", "Initial commit")
        yield tmp_path


def test_test(copied_template_directory: Path) -> None:
    """Test that the template's own tests pass."""
    with CWD(copied_template_directory):
        local.cmd.nix(
            "develop",
            "./#test",
            "--command",
            "--",
            "task",
            "test",
        )
