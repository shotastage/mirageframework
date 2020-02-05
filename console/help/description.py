"""
MIRAGE Console
description.py

Created by Shota Shimazu on 2019/1/27

Copyright (c) 2018-2020 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""


from console import version


@property
def usage_docstring() -> str:
    return """
MIRAGE v{0}

Usage:
    mg [action] option <--sub-option> <inputs>

    mg [action]:[subaction] option <--sub-option> <inputs>



[Create Project]

new                                         Create a new Django project.
new:react                                   Create a new Django API project with React.js front-end.
new:ng                                      Create a new Django API project with Angular.
                         --nebular          Create a new Angular project with Nebular.
                         --material         Create a new Angular project with Material theme.

[Utilities]

b             app         <app name>        Backup exsiting app.
browser                   <URL>             Launch browser set as default by system.
conf                      <config type>     Generate miragefile or reconfig mirage.
f                                           Create a new Python source file with copyrights doc string.


[Console]

c                                           Launch Django Python shell.
c:db                                        Launch databse shell.


[Database]

db:migrate                                  Make migrations and apply migrations.
db:merge                                    Discard & recreate migrations.
db:reset                                    Reset all database. ( Only debugging SQLite is supported. )


[Generator]

g             app         <app names...>    Create multiple Django apps at once.
g             model       <model class>     Create Django model class.
g             module      <module bane>     Create a new Python module with __init__.py


[Heroku]

heroku        configure                     Configure setting files for deploing to heroku.


[Management]

m             test                          Run test of Django application.
m             superuser                     Create super user for Django admin.
m             <manage.py command>           Run manage.py command.


[Server]

s                                           Launch debugging server.


[Help]

h                                           Show usage of Mirage.
v                                           Print version information.
?             update                        Check update.
?             system                        Check platform and Python version.

""".format(version.__version__)


@property
def version_docstring() -> str:
    return """
MIRAGE Version {0}

https://github.com/shotastage/mirageframework

Copyright (c) 2017-2020 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
""".format(version.__version__)
