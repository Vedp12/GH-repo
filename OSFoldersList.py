# * Modules
import fnmatch
import os


# * organize all directory and files in one function
def files_list(
    allFilesList,
    depth=0,
    excludes_path=None,
    excludes_pattern=None,
    file_structure=None,
):
    indent = "  " * depth
    # ! Exclude particular patters and path to list in our files
    if excludes_pattern is None:
        excludes_pattern = [
            ".git",
            ".venv",
            "__pycache__",
            ".idea",
            ".pyc",
            ".tmp",
            ".log",
            "*.jpg",
            "*.jpeg",
            "*.png",
            "*.svg",
            "structure.txt",
        ]
    if excludes_path is None:
        excludes_path = {
            os.path.abspath("src"),
            os.path.abspath(".github"),
            os.path.abspath("test"),
        }
    # * Here it blocked all the not required paths
    allFilesList = os.path.abspath(allFilesList)
    if allFilesList in excludes_path:
        return
    if not os.path.exists(allFilesList):
        raise FileNotFoundError(f"{allFilesList} file do not exist ")
    if not os.path.isdir(allFilesList):
        raise NotADirectoryError(f"{allFilesList} directory do not exist ")
    file_structure.write(f"{indent}{os.path.basename(allFilesList)}/\n")

    allfilesList = []
    # * iterate every files in directory with the contains in it
    for file in os.listdir(allFilesList):
        path = os.path.join(allFilesList, file)
        if any(fnmatch.fnmatch(file, pattern) for pattern in excludes_pattern):
            continue
        if os.path.abspath(path) in excludes_path:
            continue
        if os.path.isfile(path):
            file_structure.write(f"{indent}  |-- {file}\n")
            allfilesList.append(path)
    # * iterate every folders in directory with the contains in it
    for file in os.listdir(allFilesList):
        path = os.path.join(allFilesList, file)
        if any(fnmatch.fnmatch(file, pattern) for pattern in excludes_pattern):
            continue
        if os.path.abspath(path) in excludes_path:
            continue
        if os.path.isdir(path):
            files_list(path, depth + 1, excludes_path, excludes_pattern, file_structure)
    return allfilesList


if __name__ == "__main__":
    current_file = r"/home/tux_106/Documents/PyProj"
    with open(f"{os.path.basename(current_file)}-structure.txt", "w") as file_structure:
        files_list(current_file, file_structure=file_structure)
