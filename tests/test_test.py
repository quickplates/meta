from pathlib import Path

import copier
import pytest
from helpers.utils import CWD, SandboxedGitRepo
from plumbum import local


@pytest.fixture()
def data() -> dict[str, str]:
    """Return a dictionary with the data to be used in the template."""

    return {
        "username": "quickplates",
        "projectname": "template",
        "description": "Template",
    }


@pytest.fixture()
def copied_template_directory(
    tmp_path_factory: pytest.TempPathFactory,
    cloned_template_directory: Path,
    data: dict[str, str],
) -> Path:
    """Return a temporary directory with a copied template."""

    prefix = "copied-template-"

    with tmp_path_factory.mktemp(prefix) as tmp_path:
        copier.run_copy(
            str(cloned_template_directory),
            str(tmp_path),
            defaults=True,
            data=data,
            vcs_ref="HEAD",
            quiet=True,
        )

        with SandboxedGitRepo(tmp_path):
            local.cmd.git("add", ".")
            local.cmd.git("commit", "--message", "Initial commit")
            yield tmp_path


def test_test(copied_template_directory: Path) -> None:
    """Test that the template's own tests pass."""

    with CWD(copied_template_directory):
        local.cmd.nix(
            "develop",
            ".#test",
            "--command",
            "--",
            "task",
            "test",
        )
