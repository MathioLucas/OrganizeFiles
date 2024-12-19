import os
import shutil

# Define the desktop path (adjust if needed)
desktop = os.path.expanduser("~/Desktop")

# Define target folders and file extensions
folders = {
    "Downloads": [".zip", ".exe", ".dmg", ".torrent"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Screenshots": ["Screenshot"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
}

# Define a fallback folder for unclassified files
other_folder = "Others"

def organize_files():
    # Create folders if they don't exist
    for folder in folders.keys():
        os.makedirs(os.path.join(desktop, folder), exist_ok=True)
    os.makedirs(os.path.join(desktop, other_folder), exist_ok=True)

    # Iterate through files on the desktop
    for file_name in os.listdir(desktop):
        file_path = os.path.join(desktop, file_name)

        # Skip if it's a folder or system file
        if os.path.isdir(file_path) or file_name.startswith("."):
            continue

        # Move the file to the appropriate folder
        moved = False
        for folder, extensions in folders.items():
            if file_name.startswith("Screenshot") and folder == "Screenshots":
                shutil.move(file_path, os.path.join(desktop, folder, file_name))
                moved = True
                break
            if file_name.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(desktop, folder, file_name))
                moved = True
                break

        # If the file doesn't match any category, move it to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(desktop, other_folder, file_name))

    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_files()
