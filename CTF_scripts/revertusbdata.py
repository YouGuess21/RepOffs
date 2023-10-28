import os

# Input directory containing the text files with hex streams
input_directory = "extracted_data"

# Create a directory to save the reverted data
output_directory = "reverted_data"
os.makedirs(output_directory, exist_ok=True)

# Function to revert hex data and save it as a file
def revert_and_save_hex(hex_data, file_number):
    byte_data = bytes.fromhex(hex_data)
    filename = os.path.join(output_directory, f"reverted_data_{file_number}")
    with open(filename, 'wb') as output_file:
        output_file.write(byte_data)

# Iterate through the text files in the input directory
for file_number, filename in enumerate(os.listdir(input_directory)):
    with open(os.path.join(input_directory, filename), 'r') as input_file:
        hex_stream = input_file.read()
        revert_and_save_hex(hex_stream, file_number)

print("Hex streams reverted and saved as individual files.")
