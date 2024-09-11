import os
import pytesseract
from PIL import Image

# Define the folder path containing the images
folder_path = r'dataset\data\unprepared\lined'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        
        # Open the image file
        with Image.open(file_path) as img:
            # Use Tesseract to extract text from the image
            text = pytesseract.image_to_string(img,lang='nep')
        
        # Create a new .gt.txt file for each image
        gt_filename = f"{os.path.splitext(filename)[0]}.gt.txt"
        gt_file_path = os.path.join(folder_path, gt_filename)
        
        # Write the extracted text into the .gt.txt file
        with open(gt_file_path, 'w', encoding='utf-8') as gt_file:
            gt_file.write(text)

print("Text extraction and file creation completed.")