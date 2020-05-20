""" Entry point for tsrc log """

import argparse

import cli_ui as ui

import tsrc
import tsrc.cli


def main(args: argparse.Namespace) -> None:
    workspace = tsrc.cli.get_workspace(args)
    all_ok = True
    for unused_index, repo, full_path in workspace.enumerate_repos():
        colors = ["green", "reset", "yellow", "reset", "bold blue", "reset"]
        log_format = "%m {}%h{} - {}%d{} %s {}<%an>{}"
        log_format = log_format.format(*("%C({})".format(x) for x in colors))
        cmd = [
            "log",
            "--color=always",
            "--pretty=format:%s" % log_format,
            "%s...%s" % (args.from_, args.to),
        ]
        rc, out = tsrc.git.run_captured(full_path, *cmd, check=False)
        if rc != 0:
            all_ok = False
        if out:
            ui.info(ui.bold, repo.dest)
            ui.info(ui.bold, "-" * len(repo.dest))
            ui.info(out)
    if not all_ok:
        raise tsrc.Error()
