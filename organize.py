import os
import shutil

# Define source directory and destination directories for different file types
source_dir = "D:\document sem 3-1\AI"
destination_dirs = {
    "Documents": "/path/to/destination/Documents",
    "Images": "/path/to/destination/Images",
    "Others": "/path/to/destination/Others"
}

# Function to organize files
def organize_files(source_dir, destination_dirs):
    # Create destination directories if they don't exist
    for dir_path in destination_dirs.values():
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            # Determine file type based on extension
            file_ext = filename.split(".")[-1].lower()

            # Move file to appropriate destination directory
            if file_ext in ("pdf", "doc", "docx", "txt", "ppt", "xls", "xlsx"):
                shutil.move(file_path, destination_dirs["Documents"])
            elif file_ext in ("jpg", "jpeg", "png", "gif", "bmp"):
                shutil.move(file_path, destination_dirs["Images"])
            else:
                shutil.move(file_path, destination_dirs["Others"])

    print("Files organized successfully.")

# Call the function to organize files
organize_files(source_dir, destination_dirs)
