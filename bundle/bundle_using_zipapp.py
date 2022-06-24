#!/usr/bin/env python3
import zipapp
import sys
from os import path
import os
import shutil


def is_file_accepted(i_file_path):
    if i_file_path.suffix == ".py":
        return True
    return False


if __name__ == '__main__':
    app_name = "html_auto_2columns"

    main_path = path.dirname(sys.modules['__main__'].__file__)
    main_path = path.join(main_path, '..')
    deploy_path = path.join(main_path, 'deploy')
    app_path = path.join(main_path, 'src')

    if os.path.exists(deploy_path):
        shutil.rmtree(deploy_path)
    os.makedirs(deploy_path)

    zipapp.create_archive(app_path, path.join(deploy_path, app_name + ".pyz"), '/usr/bin/python3',
                          filter=is_file_accepted)

    print(f"wrapping finished! Output file: {app_name}.pyz")
