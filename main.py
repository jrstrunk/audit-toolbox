import modules.git_complexity
import modules.ext_interface

input_dirs = [
    # "",
]

# Change to the directory
with open("audit.txt", "w") as report:
    for d in input_dirs:
        os.chdir(d)

        # Get the list of files tracked by Git
        files = subprocess.check_output(['git', 'ls-files']).decode('utf-8').split('\n')

        for f in [f for f in files if ".sol" in f]:
            git_info = git_complexity.get_git_file_info(f)
            interface = get_solidity_interface(f)
