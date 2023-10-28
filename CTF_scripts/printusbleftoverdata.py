import os

# Input PCAPNG file
input_pcapng_file = "send.pcapng"

# Create a directory to save extracted data
output_directory = "extracted_data"
os.makedirs(output_directory, exist_ok=True)

# Run tshark to extract usb.capdata and redirect the output to a text file
os.system(f'tshark -r {input_pcapng_file} -Y "usb.capdata" -T fields -e usb.capdata > usb_capdata.txt')

# Read the usb.capdata text file
with open('usb_capdata.txt', 'r') as usb_capdata_file:
    usb_capdata = usb_capdata_file.read()

# Split the hex streams by newline
hex_streams = usb_capdata.splitlines()

# Create separate text files for each hex stream
for i, hex_stream in enumerate(hex_streams):
    filename = os.path.join(output_directory, f"hex_stream_{i}.txt")
    with open(filename, 'w') as output_file:
        output_file.write(hex_stream)

print("Hex streams extracted and saved to individual text files.")
