import re
# CYBR472 - Part 3 - Liv Fletcher
# Write a script to automate the process of extracting images from the attathed Thumbs.zip file.

# Take in the Thumbs file and read the binary 
with open('Thumbs.db', 'rb') as file:
    hex_image = file.read().hex()
    
    # Setting the header/footer variables to their corresponding hex values
    jpg_headers = re.finditer('ffd8ffe0', hex_image, re.IGNORECASE)
    jpg_footers = re.finditer('ffd9', hex_image, re.IGNORECASE)

    # Iterate through until a match for a JPG header and footer have been found
    # Implementing the zip function within the enumrate to process the header and footer iterable values together
    for i, (header_match, footer_match) in enumerate(zip(jpg_headers, jpg_footers)):

        # Setting the start and end of the JPG block for extraction
        header_offset = header_match.start()
        footer_offset = footer_match.end()

        # Saving the block hex data of the JPG image 
        image_data = bytes.fromhex(hex_image[header_offset:footer_offset])

        # Save the image block to current directory with iteration number 
        # (first iteration - image_0.jpg, second - image_1.jpg etc)
        image_path = f'image_{i}.jpg'

        print(f"Found Image, saving: image_{i}.jpg")
        
        # Save the contents into a JPG format within the current path
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
