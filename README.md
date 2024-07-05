
# UUID Replacement and Configuration File Generator

This script helps in generating configuration files with unique UUIDs and allows customization of network and proxy settings. It clears the directory of all files, generates new UUIDs, replaces the UUID in a given template, and creates a zip file containing the generated configuration files.

## Features:
- Uninstalls conflicting packages.
- Installs necessary libraries.
- Clears the directory.
- Generates unique UUIDs.
- Replaces UUIDs in template content.
- Customizes network and proxy settings.
- Generates and zips configuration files.
- Triggers download of the generated zip file.

## Usage:
1. Run the script in Google Colab.
2. Follow the prompts to select network configuration and proxy settings.
3. Provide a custom name for the generated profiles.
4. Download the generated zip file containing the configuration files.

## New Update with Website for Getting Free Profiles:
Check out the new update on creating unique profiles and activating antennas on iPhone 14 and 15 without tracking and closure. The documentation provides free and permanent activation tutorials, along with source code and a unique UUID file.

## Creating Unique Profiles:
The code is provided as a template that can be customized for all operators using the UUID generator written in Python. Replace the existing codes with the new ones and save the file. You can easily convert the Python file to an executable (exe) file using the following commands:

```sh
pip install pyinstaller

pyinstaller --onefile --windowed uuid-generator.py
```

In the templates, replace the UUID section with the new code:

```xml
<key>PayloadType</key>
<string>com.apple.cellular</string>
<key>PayloadUUID</key>
<string>NEW_UUID</string>
<key>PayloadVersion</key>
<integer>1</integer>
```

The reason for configuration closures is the use of the same UUID by multiple users. Ensure each device has a unique UUID.

### Steps for Activation:
1. **Download Apple Configurator or Imazing Profile Editor**:
   - Apple Configurator for macOS
   - Imazing Profile Editor for Windows

2. **Create a New Profile**:
   - Open Apple Configurator.
   - Go to "File" and select "New Profile".

3. **Profile Settings**:
   - In "Name", enter a desired name.
   - In "Identifier", either leave it blank or generate a unique code using `uuid-generator.py`.

4. **APN Settings**:
   - Look for "cellular" in the left menu.
   - Set "Configured APN Type" to "mcinet" or "mtnirancell".
   - Set "Data VPN Authentication Type" to "CHAP".
   - Use IP4; switch to IP6 if there are internet issues.

5. **Test and Save**:
   - Save the configuration.
   - If it doesn't work, create a new configuration with a new UUID and test again.

### Upload Profile Steps:
1. Perform a network reset.
2. Send the configuration file to the phone and download it.
3. Click on the configuration file to open it and save it.
4. Go to File Manager and click on the configuration to prompt the installation.
5. In settings, go to VPN and Device Management, select the profile, and install it.
6. Go to Cellular Data, enable Data Roaming and VoLTE on 5G or LTE, and restart the phone.

### Additional Notes:
- Set the network to MCI (Hamrah Aval) for better antenna reception.
- Avoid using dual SIM cards simultaneously.
- If the profile doesn't work, generate a new UUID and test again. For internet access, especially with Irancell, you can set IP settings to IP6.
- Ensure the network is set to 5G.
- If the signal is lost at midnight, switch to 2G as it may auto-recover by morning.
- Remember to delete the old profile before testing a new one.

Special thanks to [AiGptCode on GitHub](https://github.com/AiGptCode/Iphone-14-15-IRAN-Anten) for providing the templates
Adaptation for Google Collab by [Mehran Khan](https://github.com/TheMehranKhan)
