# python script to zip files
from zipfile import ZipFile
import os


def get_all_file_paths(directory):

    file_paths = []  # empty path list
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def exec():
    # folder name you want to zip
    zipFolderName = input("Enter the folder name to zip : ")

    # get paths from directory
    file_paths = get_all_file_paths(zipFolderName)

    # list of all files to zip
    print('Following files will be zipped : ')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile(f'{zipFolderName}.zip', 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
    print('All files zipped successfully!')


exec()
