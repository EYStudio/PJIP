import datetime
from pjip.config.build_info import VERSION, WIN_FILEVER, PROJECT_NAME_ABBREVIATION

START_YEAR = 2024
CURRENT_YEAR = datetime.datetime.now().year

if CURRENT_YEAR == START_YEAR:
    COPYRIGHT = f"Copyright (C) {START_YEAR} Errorsia"
else:
    COPYRIGHT = f"Copyright (C) {START_YEAR}-{CURRENT_YEAR} Errorsia"

file_vers = f"{WIN_FILEVER[0]}, {WIN_FILEVER[1]}, {WIN_FILEVER[2]}, {WIN_FILEVER[3]}"
prod_vers = f"{WIN_FILEVER[0]}, {WIN_FILEVER[1]}, {WIN_FILEVER[2]}, {WIN_FILEVER[3]}"

PROGRAM_FILE_NAME = '_'.join([PROJECT_NAME_ABBREVIATION, ('v' + VERSION), 'x64'])
PROGRAM_FILE_NAME_LITE = '_'.join([PROJECT_NAME_ABBREVIATION, ('v' + VERSION), 'x64', 'Lite'])

version_text = f"""
# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({file_vers}),
    prodvers=({prod_vers}),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable(
        '040904B0',
        [
          StringStruct('CompanyName', 'Errorsia'),
          StringStruct('FileDescription', f'{PROJECT_NAME_ABBREVIATION} Application'),
          StringStruct('FileVersion', f'{VERSION}'),
          StringStruct('ProductVersion', f'{VERSION}'),
          StringStruct('InternalName', f'{PROJECT_NAME_ABBREVIATION}'),
          StringStruct('OriginalFilename', f'{PROGRAM_FILE_NAME_LITE}.exe'),
          StringStruct('ProductName', f'{PROJECT_NAME_ABBREVIATION}'),
          StringStruct('LegalCopyright', f'{COPYRIGHT}'),
          StringStruct('LegalTrademarks', f'{PROJECT_NAME_ABBREVIATION} is a trademark of Errorsia'),
          StringStruct('License', 'GPLv3'),
        ]
      )
    ]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
"""

print(__file__)

import os

SCRIPT_DIR = os.path.dirname(__file__)
VERSION_FILE = os.path.join(SCRIPT_DIR, "version.txt")

print(VERSION_FILE)

with open(VERSION_FILE, "w", encoding="utf-8") as f:
    f.write(version_text)
