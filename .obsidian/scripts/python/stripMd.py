import sys
import os
import glob
import getopt


def strip_md_links(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        # Remove .md from the links, link can be in the format [link](path.md#something)
        updated_content = content.replace('.md#', '#').replace(
            '.md)', ')').replace('.md"', '"')
        # has the file been modified ?
        if content == updated_content:
            return 0
        file.seek(0)
        file.write(updated_content)
        file.truncate()
        return 1


def usage():
    print("Usage: python strip.md.py [-v] [-q] root <files>")


def main(argv):
    verbose = False
    quiet = False
    fileProcessed = 0
    fileModified = 0
    root_folder = ''
    try:
        opts, args = getopt.getopt(argv, "vq", ["verbose", "quiet"])
    except getopt.GetoptError:
        print('Invalid command line arguments')
        return
    for opt, arg in opts:
        if opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-q", "--quiet"):
            quiet = True
    # Get the root folder from the first non-option argument
    if args:
        root_folder = args[0]
        if not os.path.isdir(root_folder):
            print(f'Root folder {root_folder} does not exist')
            return
        else:
            os.chdir(root_folder)
    else:
        usage()
        return
    # Get the file paths from the remaining arguments
    file_paths = args[1:]

    # remove empty strings from the file_paths
    file_paths = list(filter(None, file_paths))
    if len(file_paths) == 0:
        file_paths = glob.glob(root_folder + '/**/*.md', recursive=True)
    else:
        # replace folder with all .md files in the folder
        for i in range(len(file_paths)):
            if os.path.isdir(file_paths[i]):
                file_paths[i] = glob.glob(
                    file_paths[i] + '/**/*.md', recursive=True)
            else:
                file_paths[i] = [file_paths[i]]
        file_paths = [item for sublist in file_paths for item in sublist]

    for file_path in file_paths:
        if os.path.isfile(file_path):
            fileProcessed += 1
            fileModified += strip_md_links(file_path)
            if verbose:
                print(f'Successfully processed {file_path}')
        else:
            print(f'File {file_path} does not exist')
    if not quiet:
        print(f'{fileProcessed} files processed')
        print(f'{fileModified} files modified')
    return fileProcessed


if __name__ == '__main__':
    main(sys.argv[1:])
