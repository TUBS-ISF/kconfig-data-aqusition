import os
import subprocess

def prepare(systems_path):
    extra_path_to_kconfig_model = ""
    system_path = os.path.join(systems_path, 'toybox')

    os.chdir(system_path)
    subprocess.call(['make', 'defconfig'])

    return system_path, extra_path_to_kconfig_model
