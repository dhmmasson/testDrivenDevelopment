import sys
import os
import glob


def strip_md_links(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        updated_content = content.replace('.md)', ')')
        file.seek(0)
        file.write(updated_content)
        file.truncate()


if __name__ == '__main__':
    # Get the file paths from the command line arguments
    file_paths = sys.argv[1:]

    # Process each file
    for file_path in file_paths:
        if os.path.isfile(file_path):
            strip_md_links(file_path)
            print(f'Successfully processed {file_path}')
        else:
            print(f'File {file_path} does not exist')
            # Process each file recursively
            for file_path in file_paths:
                if os.path.isfile(file_path):
                    strip_md_links(file_path)
                    print(f'Successfully processed {file_path}')
                elif os.path.isdir(file_path):
                    # Get all .md files recursively inside the folder and subfolders
                    md_files = glob.glob(
                        file_path + '/**/*.md', recursive=True)
                    for md_file in md_files:
                        strip_md_links(md_file)
                        print(f'Successfully processed {md_file}')
                else:
                    print(
                        f'Path {file_path} is neither a file nor a directory')
