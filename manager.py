#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from app import create_app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Role



app = create_app('default')
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    app.run(port=9999,debug=True)