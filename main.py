import subprocess
import os
import modules.git_complexity as git_complexity
import modules.ext_interface as ext_interface

only_ext_interface = False

input_dirs = [
    "/home/john/Repos/2024-01-renft/smart-contracts/src/modules",
    "/home/john/Repos/2024-01-renft/smart-contracts/src/packages",
]

with open("report.sol", "w") as report:
    print("// SPDX-License-Identifier: BUSL-1.1", end="\n\n", file=report)
    print("interface Audit {", file=report)

    for d in input_dirs:
        # Change to the directory
        os.chdir(d)

        # Get the list of files tracked by Git
        files = subprocess.check_output(['git', 'ls-files']).decode('utf-8').split('\n')

        for f in [f for f in files if ".sol" in f]:
            git_info = git_complexity.get_git_file_info(f)
            interface = ext_interface.get_solidity_interface(f)

            if not only_ext_interface or len(interface) > 0:

                print("// ###", f, file=report)
                print(
                    "// Git Info -",
                    "Change Ratio:", 
                    git_info["ratio"],
                    "Total Adds:",
                    git_info["adds"],
                    "Total Deletes:", 
                    git_info["dels"],
                    "Total Days:",
                    git_info["days"],
                    "Authors:",
                    git_info["authors"],
                    end="\n\n",
                    file=report,
                )

                for func in interface:
                    print(func, end="\n\n", file=report)
                
                print("", end="\n\n\n", file=report)

    print("}", file=report)
