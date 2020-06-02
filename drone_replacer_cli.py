# -*- coding: utf-8 -*-
import click as click


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help(), color=ctx.color)
    else:
        pass  # act normally


@cli.command(
    name="make-changes",
    help="Make changes in Drone step to enable Git branch deployment",
)
@click.argument("drone_file_path", required=True)
def make_drone_changes(drone_file):
    click.echo("Drone file path is {}".format(drone_file))
