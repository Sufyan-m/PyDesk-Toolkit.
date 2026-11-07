# Day 01 - Bulk File Renamer 🐍

A simple Python project that renames multiple JPG images in a folder automatically using `pathlib`.

## ✨ Features

- Automatically scans a folder for JPG images.
- Renames images with sequential numbering.
- Supports uppercase and lowercase `.jpg` extensions.
- Keeps renamed images in the same folder.
- Displays each renamed filename.
- Shows a completion message.

## 🛠️ Built With

- Python 3
- pathlib (built-in Python module)

## 📂 Example

**Before:**

```text
image/
├── download.jpg
├── picture.jpg
└── wallpaper.jpg
```

**After:**

```text
image/
├── image_1.jpg
├── image_2.jpg
└── image_3.jpg
```

## 🚀 How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open `Bulk-Renamer.py`.
4. Change the source folder path to your own folder.
5. Run the script:

```bash
python Bulk-Renamer.py
```

## 📌 Important

- This version works with `.jpg` files only.
- Original filenames are replaced.
- Test with copies of your images first.
- Make sure the folder path is correct.

##
