from invoke import task


@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def database(ctx):
    ctx.run("sqlite3 data/database.sqlite ", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def init_database(ctx):
    ctx.run("python3 src/initialize_database.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)