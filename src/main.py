import subprocess
from pathlib import Path
import re

# playlist
# Finding files...
# Found files -> List them
# Creating playlist...


l = [  # audios
    ".mp3",
    ".wav",
    ".aac",
    ".flac",
    ".ogg",
    ".m4a",
    ".wma",
    # videos
    ".mp4",
    ".mov",
    ".mkv",
    ".wmv",
    ".avi",
    ".WebM",
]


def natural_sorting(file):
    pass


def files_finder(folder_path):
    """Loops through the directory to find files to make the playlist with.

    Args:
        folder_path (Path): The target folder (working directory)

    Returns:
        list: List of the files
    """
    playlist = []
    files = list(folder_path.iterdir())
    skipped_count = 0
    found_count = 0
    # Checks if there any files
    if not files:
        return playlist
    
        

    # Loops through the files and checks if their extensions are valid
    for file in files:
        if file.suffix.lower() in l:
            playlist.append(file)
            # Number of found files
            found_count += 1

        # Number of skipped files
        else:
            skipped_count += 1
            
    print(f"Found {found_count} playable file(s), Skipped {skipped_count} file(s)")
    return playlist


def main(folder_path):
    # Gets the list of files
    playlist = files_finder(folder_path)

    # Checks if the list is empty
    if not playlist:
        print("No valid items found.")

    # If list isn't empty, it checks if the files are actually valid files or not (not implemented yet)
    else:
        string_paths = []
        for f in playlist:
            print(f"DEBUG: {f}")
            string_paths.append(str(f))

        print(*string_paths)


if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / "test_folder"
    main(path)
