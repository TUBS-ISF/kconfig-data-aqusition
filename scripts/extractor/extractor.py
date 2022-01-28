import argparse
import os
import sys
import git
import datetime
from glob import glob
import subprocess
import stat
import shutil
import importlib

kconfig_file_name = "Kconfig"

date_format = '%Y-%m-%d'
start_date = '1970-12-31'
end_date = '2099-12-31'

def init_dirs():
    # change to main directory
    os.chdir(os.path.dirname(__file__))

    os.chdir('../..')

    # set main diretory
    global main_path
    main_path = os.getcwd()

    # create data directory
    global data_path
    data_path = os.path.join(main_path, 'data')
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    # create systems directory
    global systems_path
    systems_path = os.path.join(main_path, 'systems')
    if not os.path.exists(systems_path):
        os.makedirs(systems_path)

    # check repo directory exists
    global repo_path
    repo_path = os.path.join(systems_path, system_name)
    if not os.path.isdir(repo_path):
        print("The system specified does not exist")
        sys.exit()

    # check system specific lib
    global system_lib
    system_lib = importlib.import_module("systems." + system_name.replace('-', ''))
    if not system_lib:
        print("system module not found")
        sys.exit()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('System',
                       metavar='system',
                       type=str,
                       help='the name of the system directory')
    parser.add_argument('--config', help='kconfig file')
    parser.add_argument('--start', help='start date')
    parser.add_argument('--end', help='end date')
    args = parser.parse_args()

    if args.config:
        global kconfig_file_name
        kconfig_file_name = args.config

    if args.start:
        try:
            datetime.datetime.strptime(args.start, date_format)
            global start_date
            start_date = args.start
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            sys.exit()
    if args.end:
        try:
            datetime.datetime.strptime(args.end, date_format)
            global end_date
            end_date = args.end
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            sys.exit()

    # set system_name
    global system_name
    system_name = args.System

    # init directories
    init_dirs()
    
    all_commits = getAllCommits()

    unique_paths = findAllUniquePaths(all_commits)

    relevant_commits = getRelevantCommity(unique_paths)
    
    """
    # create output path if not exists
    output_path = os.path.join(data_path, system_name, 'data')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    with open(os.path.join(output_path, 'relevant_commits.out')) as f:
        relevant_commits = [line.rstrip() for line in f]
    """

    extractModels(relevant_commits)

def findAllUniquePaths(all_commits):
    files = []
    for commit in all_commits:
        g = git.Git(repo_path)
        g.reset('--hard')
        g.clean('-fxd')
        g.checkout(commit)
        print(commit)
        for dir,_,_ in os.walk(repo_path):
            files.extend(glob(os.path.join(dir, kconfig_file_name)))
    
    # convert each absolute path to a relative path
    unique_paths = []
    for file_name in files:
        unique_paths.append(os.path.relpath(os.path.join(file_name), repo_path))

    # remove duplicates from list
    unique_paths = list(set(unique_paths))

    # create output path if not exists
    output_path = os.path.join(data_path, system_name, 'data')
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # save unique paths
    with open(os.path.join(output_path, 'unique_paths.out'), 'w', encoding = 'utf-8') as f:
        for unique_path in unique_paths:
            f.write(unique_path + "\n")

    return unique_paths

def getRelevantCommity(unique_paths):
    # get git repository
    g = git.Git(repo_path)

    # reset to master
    g.fetch('origin')
    g.reset('--hard', 'origin/master')

    log_with_time = []
    log_without_time = []

    for unique_path in unique_paths:
        # get relevant commits as hash values
        log_with_time.extend(g.log('--after='+start_date, '--before='+end_date, '--pretty=format:"%H;%ci"', '--follow', '--', unique_path).replace('"', '').splitlines())
        log_without_time.extend(g.log('--after='+start_date, '--before='+end_date, '--pretty=format:"%H"', '--follow', '--', unique_path).replace('"', '').splitlines())

    # create output path if not exists
    output_path = os.path.join(data_path, system_name, 'data')
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # remove duplicates from list
    log_with_time = list(set(log_with_time))
    log_without_time = list(set(log_without_time))

    # save hash values
    with open(os.path.join(output_path, 'relevant_commits_time.out'), 'w', encoding = 'utf-8') as f:
        for line in log_with_time:
            f.write(line + "\n")
    
    with open(os.path.join(output_path, 'relevant_commits.out'), 'w', encoding = 'utf-8') as f:
        for line in log_without_time:
            f.write(line + "\n")

    # return hash values
    return log_without_time

def getAllCommits():
    # get git repository
    g = git.Git(repo_path)

    # reset to master
    g.fetch('origin')
    g.reset('--hard', 'origin/master')

    # get all commits as hash values
    log_with_time = g.log('--after='+start_date, '--before='+end_date, '--pretty=format:"%H;%ci"').replace('"', '').splitlines()
    log_without_time = g.log('--after='+start_date, '--before='+end_date, '--pretty=format:"%H"').replace('"', '').splitlines()

    # create output path if not exists
    output_path = os.path.join(data_path, system_name, 'data')
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # save hash values
    with open(os.path.join(output_path, 'all_commits_time.out'), 'w', encoding = 'utf-8') as f:
        for line in log_with_time:
            f.write(line + "\n")
    
    with open(os.path.join(output_path, 'all_commits.out'), 'w', encoding = 'utf-8') as f:
        for line in log_without_time:
            f.write(line + "\n")

    # return hash values
    return log_without_time

def extractModels(relevant_commits):
    # create models path if not exists
    models_path = os.path.join(data_path, system_name, 'models')
    if not os.path.exists(models_path):
        os.makedirs(models_path)

    # get git repository
    g = git.Git(repo_path)

    for commit in relevant_commits:
        print("start extracting model from revision " + commit)

        # switch git revision
        g.reset('--hard')
        g.clean('-fxd')
        g.checkout(commit)

        # get commit message
        commit_message = g.show('--pretty=format:"%ci"')
        first_line = commit_message.splitlines()[0].replace('"', '')
        parts_of_line = first_line.split(' ')
        commit_date = parts_of_line[0]
        commit_time = parts_of_line[1].replace(':', '-')

        # create output path if not exists
        output_path = os.path.join(models_path, commit_date.split('-')[0], commit_date + '_' + commit_time)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # save commit message in log file
        with open(os.path.join(output_path, commit + '.log'), 'w', encoding = 'utf-8') as f:
            f.write(commit_message.encode('ascii', 'ignore').decode('utf-8'))

        # execute system specific commands
        system_path, extra_path_to_kconfig_model = system_lib.prepare(systems_path)

        # change to scripts directory
        os.chdir(os.path.dirname(__file__))

        # copy scripts
        shutil.copyfile('check_dep', os.path.join(system_path, 'check_dep'))
        shutil.copyfile('dimacs.py', os.path.join(system_path, 'dimacs.py'))
        shutil.copyfile('dimacs2xml.jar', os.path.join(system_path, 'dimacs2xml.jar'))
        
        # change to system directory
        os.chdir(system_path)

        # set file permissions
        st = os.stat('check_dep')
        os.chmod('check_dep', st.st_mode | stat.S_IEXEC)

        # execute check_dep and save output
        with open(os.path.join(output_path, 'kconfig.kmax'), 'w', encoding = 'utf-8') as kmax_file:
            check_dep_process = subprocess.run([
                    './check_dep', 
                    '--dimacs', 
                    os.path.join(system_path, extra_path_to_kconfig_model, kconfig_file_name)],
                stdout=kmax_file)

        # execute dimacs.py and save output
        with open(os.path.join(output_path, 'kconfig.kmax'), 'rb', 0) as kmax_file, open(os.path.join(output_path, 'kconfig.dimacs'), 'w', encoding = 'utf-8') as dimacs_file:
            dimacs_process = subprocess.run([
                    'python',
                    'dimacs.py',
                    '-d',
                    '--include-nonvisible-bool-defaults', 
                    '--remove-orphaned-nonvisibles'],
                stdout=dimacs_file, 
                stdin=kmax_file)

        # execute dimacs2xml.jar
        dimacs2xml_process = subprocess.run([
            'java', 
            '-jar', 
            'dimacs2xml.jar', 
            os.path.join(output_path, 'kconfig.dimacs'), 
            os.path.join(output_path, 'clean.dimacs'), 
            os.path.join(output_path, 'model.xml')])

if __name__ == "__main__":
    main()
