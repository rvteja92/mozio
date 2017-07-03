'''Fabric script to deploy to server'''
import os
import time
import datetime

from functools import wraps

from fabric.decorators import hosts
from fabric.api import cd, prefix, sudo, run, task
from fabric.colors import yellow, green, blue


def log_call(func):
    @wraps(func)
    def logged(*args, **kawrgs):
        header = "-" * len(func.__name__)
        print(green("\n".join([header, func.__name__, header]), bold=True))
        return func(*args, **kawrgs)
    return logged


def deploy_on_console():
    with cd('/home/ravi/projects/mozio'):
        print('Moved to directory ' + blue(os.getcwd()))
        # Clean and pull repo
        # run('git fetch origin vishwash')
        # run('git reset --hard FETCH_HEAD')
        # run('git clean -df')
        run('git fetch --all')
        run('git reset --hard origin/master')
        # run('git pull --no-edit origin vishwash')
        run('pip install -r requirements.txt')

        # Build frontend modules
        # with cd('staticfiles/myproject/src/'):
        #     run('npm install')
        #     run('bower install')
        #     run('grunt minify')

    with cd('/home/ravi/projects/mozio/project'):
        print('Moved to directory ' + blue(os.getcwd()))
        # Build Django project
        with prefix("source /home/ravi/.virtualenvs/mozio/bin/activate"):
            run('python manage.py migrate')
            run('python manage.py collectstatic --noinput')

        sudo("supervisorctl update")
        sudo("supervisorctl restart all")
        timestr = datetime.datetime.now().strftime(
            '%a, %d-%b-%Y %I:%M:%S ' + '%s' % (time.tzname[0]))
        print('Deployed at ' + yellow(timestr))


@task
@hosts('139.59.67.138')
@log_call
def deploy():
    # with on_console():
    deploy_on_console()
