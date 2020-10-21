import pytest
from hydra.cli import *
from click.testing import CliRunner

VALID_MODEL_PATH = "d3bug.py"
VALID_REPO_URL = "https://georgian.io/"
VALID_COMMIT_SHA = "m1rr0r1ng"
VALID_FILE_PATH = "ones/and/zer0es"
VALID_GITHUB_TOKEN =  "Georgian"
VALID_PREFIX_PARAMS = "{'epoch': 88}"


def test_train_local(mocker):
    def stub(dummy):
        pass

    mocker.patch(
        "hydra.cli.check_repo",
        return_value=(VALID_REPO_URL, VALID_COMMIT_SHA)
    )
    mocker.patch(
        "hydra.cli.os.path.join",
        return_value=VALID_FILE_PATH
    )
    mocker.patch(
        "hydra.cli.json_to_string",
        return_value=VALID_PREFIX_PARAMS
    )

    mocker.patch(
        'hydra.cli.subprocess.run',
    )

    runner = CliRunner()
    result = runner.invoke(train, ['--model_path', VALID_MODEL_PATH, '--cloud', 'local', '--github_token', VALID_GITHUB_TOKEN])


    subprocess.run.assert_called_once_with(
        ['sh', VALID_FILE_PATH, '-g', VALID_REPO_URL, '-c', VALID_COMMIT_SHA,
        '-o', VALID_GITHUB_TOKEN, '-m', VALID_MODEL_PATH, '-p', VALID_PREFIX_PARAMS])

    assert result.exit_code == 0
