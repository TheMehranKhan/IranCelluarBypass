import os
import shutil
import uuid
from google.colab import files
import zipfile

# Step 1: Uninstall the conflicting pathlib package
!pip uninstall -y pathlib

# Step 2: Install necessary libraries
!pip install pyinstaller

# Function to clear the directory of all files
def clear_directory(path='.'):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            shutil.rmtree(os.path.join(root, name))

clear_directory()

# Define the generate_new_uuid function
def generate_new_uuid():
    new_uuid = str(uuid.uuid4())
    print(f"UUID Generator Output: {new_uuid}")
    return new_uuid

# Function to replace UUID in the template content
def replace_uuid_in_file(template_content, new_uuid):
    return template_content.replace('aa9c5023-3f0e-4d0f-904b-5fbc5da0c9bd', new_uuid.strip())

# Create the configuration file content
template_content = '''
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ConsentText</key>
    <dict>
        <key>default</key>
        <string>برگشت آنتن</string>
    </dict>
    <key>DDNAProfileProperties</key>
    <dict>
        <key>IsNewProfile</key>
        <true/>
        <key>PayloadType</key>
        <string></string>
        <key>PlatformFilters</key>
        <array>
            <string>ios</string>
        </array>
    </dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>APNs</key>
            <array>
                <dict>
                    <key>AllowedProtocolMask</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInDomesticRoaming</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInRoaming</key>
                    <integer>1</integer>
                    <key>AuthenticationType</key>
                    <string>CHAP</string>
                    <key>DefaultProtocolMask</key>
                    <integer>1</integer>
                    <key>EnableXLAT464</key>
                    <true/>
                    <key>Name</key>
                    <string>mcinet</string>
                </dict>
                <dict>
                    <key>AllowedProtocolMask</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInDomesticRoaming</key>
                    <integer>1</integer>
                    <key>AllowedProtocolMaskInRoaming</key>
                    <integer>1</integer>
                    <key>AuthenticationType</key>
                    <string>PAP</string>
                    <key>DefaultProtocolMask</key>
                    <integer>1</integer>
                    <key>EnableXLAT464</key>
                    <false/>
                    <key>Name</key>
                    <string>mtnirancell</string>
                    <key>ProxyPort</key>
                    <integer>8181</integer>
                    <key>ProxyServer</key>
                    <string>11.131.26.138</string>
                </dict>
            </array>
            <key>PayloadDisplayName</key>
            <string>Cellular</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.cellular.743E468A-10AF-49A9-B9EE-7D0A9DBD532F</string>
            <key>PayloadType</key>
            <string>com.apple.cellular</string>
            <key>PayloadUUID</key>
            <string>aa9c5023-3f0e-4d0f-904b-5fbc5da0c9bd</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>All Operators</string>
    <key>PayloadIdentifier</key>
    <string>1e8dc475-ac7e-4ec2-aeeb-948c19a51b0d</string>
    <key>PayloadOrganization</key>
    <string></string>
    <key>PayloadRemovalDisallowed</key>
    <false/>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b82e890e-4fcd-4dfd-a6d9-ad3808251e91</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
'''

# Network configurations
network_configs = {
    "All Network": {},
    "Hamrah Aval": {},
    "Irancel": {},
    "Rightel": {},
}

# Select configuration
print("Please select a configuration:")
for index, config_name in enumerate(network_configs.keys(), start=1):
    print(f"{index}. {config_name}")

selected_index = int(input("Enter the number of your desired configuration: "))
selected_config_name = list(network_configs.keys())[selected_index - 1]
selected_config = network_configs[selected_config_name]

# Proxy settings
need_proxy = input("Do you need proxy settings? (yes/no): ").strip().lower()
if need_proxy == "yes":
    proxy_server = input("Please enter the proxy server address: ")
    proxy_port = int(input("Please enter the proxy port: "))
else:
    proxy_server = ""
    proxy_port = 0

# Create unique IDs using the uuid library
unique_ids = [str(uuid.uuid4()) for _ in range(5)]

# Add unique IDs to the configuration
selected_config["UniqueIDs"] = unique_ids

# Add proxy settings if needed
if need_proxy == "yes":
    selected_config["ProxyServer"] = proxy_server
    selected_config["ProxyPort"] = proxy_port

# Display the final configuration
print("\nFinal configuration:")
print(selected_config)

# Prompt user for a single custom profile name
custom_name = input("Enter the custom name for the generated profiles: ")

# List of template files
templates = [
    "Alloprators-template.mobileconfig",
    "HamrahAval-template.mobileconfig",
    "Irancell-template.mobileconfig",
    "irancell+mci.mobileconfig",
    "Rightel-template.mobileconfig"
]

output_files = []

# Process each template
for template in templates:
    new_uuid = generate_new_uuid()
    output_content = replace_uuid_in_file(template_content, new_uuid)
    output_path = f"{custom_name}-{template}"
    with open(output_path, 'w') as f:
        f.write(output_content)
    output_files.append(output_path)

# Print the paths of the generated configuration files
print("\nGenerated configuration files:")
for output_file in output_files:
    print(output_file)

# Create a zip file containing all the generated files
zip_filename = f"{custom_name}_profiles.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for output_file in output_files:
        zipf.write(output_file)

# Trigger file download in the Colab interface
files.download(zip_filename)