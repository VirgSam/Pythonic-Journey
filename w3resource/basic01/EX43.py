# 43. Write a Python program to get OS name, platform and release information

import os
print(f" OS Name: {os.name}")
import platform
print(f" Platform: {platform.system()}")
print(f" Release info: {platform.release()}")

# Alternative approach

import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release()) # one can also concatenate with commas
