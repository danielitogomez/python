import sys
import subprocess


def install_packages():
    with open("requirements.txt") as file:
        output_file = file.read()
        output_file_split = output_file.splitlines()
        print(f" {output_file_split}  \n")
    for i in output_file_split:
        output = subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
        if output == 0:
            print("Package installed!!!")
        else:
            print("Some packages with error!!!")
            exit()


