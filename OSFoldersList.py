# * Modules
import os
import fnmatch


# * organize all directory and files in one place
def files_list(allfiles, depth=0, excludes_path=None, excludes_pattern=None):
    indent = "  " * depth
    print(f"{indent}{os.path.basename(allfiles)}/")
    # ! Exlude particular patters and path to list in our files
    if excludes_pattern is None:
        excludes_pattern = {
            ".git",
            ".venv",
            "__pycache__",
            ".idea",
            ".pyc",
            ".tmp",
            ".log",
            "jpg",
            "jpeg",
        }
    # !
    if excludes_path is None:
        excludes_path = {
            os.path.abspath("/src"),
            os.path.abspath(".github"),
            os.path.abspath("/test"),
        }

    allfiles = os.path.abspath(allfiles)
    # * Here it blocked all the not required paths
    if allfiles in excludes_path:
        return 1
    if not os.path.exists(allfiles):
        raise FileNotFoundError(f"{allfiles} file do not exist ")
    if not os.path.isdir(allfiles):
        raise NotADirectoryError(f"{allfiles} directory do not exist ")
    allfilesList = []
    # * iterate every files in directory with the contions in it
    for file in os.listdir(allfiles):
        path = os.path.join(allfiles, file)
        if any(fnmatch.fnmatch(file, pattern) for pattern in excludes_pattern):
            continue
        if os.path.abspath(path) in excludes_path:
            continue
        if os.path.isfile(path):
            print(f"{indent}       |~~ {file}")
            allfilesList.append(path)
    # * iterate every folders in directory with the contions in it
    for file in os.listdir(allfiles):
        path = os.path.join(allfiles, file)
        if any(fnmatch.fnmatch(file, pattern) for pattern in excludes_pattern):
            continue
        if os.path.abspath(path) in excludes_path:
            continue
        if os.path.isdir(path):
            files_list(path, depth + 2)
    return allfilesList


if __name__ == "__main__":
    current_file = os.getcwd()
    files_list(current_file)
