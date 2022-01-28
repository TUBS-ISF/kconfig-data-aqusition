import os
import subprocess

# param systems_path absolute path to systems directory

# return system_path absolute path to system directory
# return extra_path_to_kconfig_model relative path from system path to kconfig model path

def prepare(systems_path):
    # create relative path to directory where the kconfig model is located
    extra_path_to_kconfig_model = "" # os.path.join("extra", "path", "to", "model")
    
    # create path to system directory
    system_path = os.path.join(systems_path, 'example_system')

    # change to system directory
    os.chdir(system_path)

    # execute nessecary commands
    subprocess.call(['make', 'alldefconfig']) 

    # return system_path and extra_path_to_kconfig_model
    return system_path, extra_path_to_kconfig_model
