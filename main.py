import pathlib

# Folder containing original images
path = pathlib.Path(r"D:\OS\image")

# Destination folder (same folder in this version)
destination = pathlib.Path(r"D:\OS\image")

# Create destination folder if it doesn't exist
destination.mkdir(parents=True, exist_ok=True)

# Starting number for filenames
counter = 1

# Loop through every file in the folder
for image in path.iterdir():

    # Check whether the file is a JPG image
    if image.suffix.lower() == ".jpg":

        # Generate a new filename
        name = f"image_{counter}.jpg"

        # Rename the original file
        image.rename(destination / name)

        # Display the new filename
        print(f"Renamed: {name}")

        # Increase the counter
        counter += 1

# Display completion message
print("BULK RENAMING COMPLETE! 😂")