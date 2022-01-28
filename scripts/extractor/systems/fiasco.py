import os
import subprocess

def prepare(systems_path):
    extra_path_to_kconfig_model = ""
    system_path = os.path.join(systems_path, 'fiasco')

    os.chdir(system_path)
    subprocess.run(['make', 'BUILDDIR=./mybuild'])

    os.chdir(os.path.join(system_path, 'mybuild'))
    subprocess.run(['make', 'allyesconfig'])

    return os.path.join(system_path, 'mybuild'), extra_path_to_kconfig_model
