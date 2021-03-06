import os
import zipfile
from zipfile import ZipFile
from pathlib import Path
from shutil import move

download_directory = Path("/Users/jobe/Downloads")
dir_name = "/Users/jobe/Downloads"
extension = ".zip"

for i in range(1, 3):
    for p in download_directory.rglob("*"):
        folder_name = p.stem.rsplit("_", 1)[-1]
        p.rename(download_directory / p.name)

    for item in os.listdir(dir_name):  # loop through items in dir
        if item.endswith(extension):  # check for ".zip" extension
            file_name = dir_name + "/" + item  # get full path of files
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(dir_name)  # extract file to dir
            zip_ref.close()  # close file
            os.remove(file_name)  # delete zipped file

    for p in download_directory.rglob('*'):
        if p.is_dir() and len(list(p.iterdir())) == 0:
            os.removedirs(p)

    def get_dir(filename):
        ext = filename.suffix[1:]
        return dirs.get(ext, "Misc")

    dirs = {
        # Images
        "jpeg": "Images",
        "png": "Images",
        "jpg": "Images",
        "tiff": "Images",
        "gif": "Images",
        "HDAC": "Images",

        # Videos
        "mp4": "Videos",
        "mkv": "Videos",
        "mov": "Videos",
        "webm": "Videos",
        "flv": "Videos",

        # Music
        "mp3": "Music",
        "ogg": "Music",
        "wav": "Music",
        "flac": "Music",

        # Program Files

        "sh": "Program Files",
        "iso": "Program Files",
        "dmg": "Program Files",

        # Documents
        "pdf": "Documents",
        "doc": "Documents",
        "docx": "Documents",
        "txt": "Documents",
        "ppt": "Documents",
        "ods": "Documents",
        "csv": "Documents",

        # Code
        "h": "Code",
        "cpp": "Code",
        "py": "Code",
        "js": "Code",
        "html": "Code",
        "css": "Code",
        "c": "Code",
    }

    # Directory Path
    PATH = Path("/Users/jobe/Downloads")

    for filename in PATH.iterdir():

        path_to_file = filename.absolute()

        if path_to_file.is_file():
            destination = PATH / get_dir(filename)

            if not destination.exists():
                destination.mkdir()

            move(str(path_to_file), str(destination))
    i += 1
