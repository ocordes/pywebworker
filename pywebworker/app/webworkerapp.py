# -*- coding: utf-8 -*-
"""

written by: Oliver Cordes 2019-06-16
changed by: Oliver Cordes 2019-06-16
"""

import click

import os, sys
import traceback
import importlib


from pywebworker.workerapp import WebWorkerApp


# some exceptions
class NoAppException(click.UsageError):
    """Raised if an application cannot be found or loaded."""


def prepare_import(path):
    """Given a filename this will try to calculate the python path, add it
    to the search path and return the actual module name that is expected.
    """
    path = os.path.realpath(path)

    if os.path.splitext(path)[1] == '.py':
        path = os.path.splitext(path)[0]

    if os.path.basename(path) == '__init__':
        path = os.path.dirname(path)

    module_name = []

    # move up until outside package structure (no __init__.py)
    while True:
        path, name = os.path.split(path)
        module_name.append(name)

        if not os.path.exists(os.path.join(path, '__init__.py')):
            break

    if sys.path[0] != path:
        sys.path.insert(0, path)

    return '.'.join(module_name[::-1])


def import_script(module_name, raise_if_not_found=True):
    __traceback_hide__ = True

    try:
        #__import__(module_name)
        module = importlib.import_module(module_name)
    except ImportError:
        # Reraise the ImportError if it occurred within the imported module.
        # Determine this by checking whether the trace has a depth > 1.
        if sys.exc_info()[-1].tb_next:
            raise NoAppException(
                'While importing "{name}", an ImportError was raised:'
                '\n\n{tb}'.format(name=module_name, tb=traceback.format_exc())
            )
        elif raise_if_not_found:
            raise NoAppException(
                'Could not import "{name}".'.format(name=module_name)
            )
        else:
            return None

    return module


def locate_app(module):
    app = None

    # Search for the most common names first.
    for attr_name in ('app', 'application'):
        app = getattr(module, attr_name, None)

        if isinstance(app, WebWorkerApp):
            return app

    return app


def load_app(script):
    # update names and path for module loading
    import_name = prepare_import(script)
    module = import_script(import_name)
    if module is None:
        raise NoAppException(
            'Module is none.'
        )

    app = locate_app(module)

    return app



@click.group()
def cli():
    """WebWorker program loader"""
    #click.echo('Hello World2!')
    #click.echo(script)


@cli.command()
@click.argument('pyscript', envvar='PYWEBWORKER_APP')
def run(pyscript):
    """Runs a pywebworker script """
    app = load_app(pyscript)
    if app is None:
        click.echo('WebWorker application not found!')
    else:
        click.echo('WebWorker application found ...')

    app.run()


if __name__ == '__main__':
    cli()
