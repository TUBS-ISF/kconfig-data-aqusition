import os
import subprocess

def prepare(systems_path):
    extra_path_to_kconfig_model = ""
    system_path = os.path.join(systems_path, 'soletta')

    os.chdir(system_path)
    subprocess.call(['make', 'alldefconfig'])

    return system_path, extra_path_to_kconfig_model
