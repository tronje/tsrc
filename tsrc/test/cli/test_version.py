def test_version(tsrc_cli, message_recorder) -> None:
    tsrc_cli.run("version")
    assert message_recorder.find("version")
