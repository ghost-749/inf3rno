import subprocess
import re

def extract():
    """
    Extract stored Wi-Fi passwords on a Windows system.
    Returns:
        dict: Dictionary of Wi-Fi SSIDs and their passwords
    """
    results = {}
    try:
        # Get list of Wi-Fi profiles
        profiles_output = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"],
            encoding='utf-8',
            errors='ignore'
        )
        profiles = re.findall(r"All User Profile\s*:\s*(.+)", profiles_output)

        for profile in profiles:
            profile = profile.strip()
            # Get detailed info for each profile
            details_output = subprocess.check_output(
                ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                encoding='utf-8',
                errors='ignore'
            )
            # Extract password (Key Content)
            key_match = re.search(r"Key Content\s*:\s*(.+)", details_output)
            if key_match:
                password = key_match.group(1).strip()
                results[profile] = password
                print(f"[+] SSID: {profile}, Password: {password}")
            else:
                results[profile] = "No password found"

        return results if results else "No Wi-Fi profiles found."

    except subprocess.CalledProcessError as e:
        return f"Error executing netsh: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"