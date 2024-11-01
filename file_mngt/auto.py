# cd /Users/tuyennguyen/automation/file_mngt
# python auto.py
import os
import shutil
# Define the path to your Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")
# Define folder names for different file types
folders = {
    'pdf': 'pdfs',
    'jpg': 'imgs',
    'jpeg': 'imgs',
    'png': 'imgs',
    'txt': 'docs',
    'docx': 'docs',
    'xlsx': 'docs',
    'c' : 'codes',
    'h' : 'codes',
}
# Create the folders if they don't exist
for folder in folders.values():
    os.makedirs(os.path.join(downloads_folder, folder), exist_ok=True)
# Sort the files in the Downloads folder
for filename in os.listdir(downloads_folder):
    file_extension = filename.split('.')[-1].lower()
    # Check if the file extension is in the predefined folders
    if file_extension in folders:
        # Move the file to the corresponding folder
        source = os.path.join(downloads_folder, filename)
        destination = os.path.join(downloads_folder, folders[file_extension], filename)
        shutil.move(source, destination)
        print(f'Move: {filename} to {folders[file_extension]}')
print("all files sorted")

