import ctypes
import os
import re
import sys
import time
import platform
import win32com.client
import subprocess


class PJIPBootStrap:
    def __init__(self):
        self.check_operate_system()
        self.authority_admin = self.is_admin()
        if not self.authority_admin:
            if self.privilege_escalation():
                time.sleep(3)
                sys.exit()
            else:
                print("Run without admin")
        else:
            print('Run as admin')

        self.system_info = self.get_system_info()

    @staticmethod
    def check_operate_system():
        """Check whether OS is Windows nt"""
        if os.name != 'nt':
            sys.exit('UNSUPPORTED SYSTEMS')

    @staticmethod
    def is_admin():
        """Checking whether programme has administrator privilege"""

        authority = ctypes.windll.shell32.IsUserAnAdmin()
        return bool(authority)

    @staticmethod
    def privilege_escalation():
        """
        Try to rerun script as admin
        Uses ShellExecuteW with "runas"
        :return: True if elevation succeeded, False otherwise
        """
        result = ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, ' '.join(sys.argv), None, 1
        )
        return result > 32

    def get_system_info(self):
        """
        Collect system information in a dictionary.

        system: OS name (Windows)
        release: OS release
        version: OS build version
        major: major version number
        minor: minor version number
        build: build number
        platform: platform ID
        service_pack: installed service pack
        architecture: system architecture (64bit, 32bit)
        hotfixes: list of installed hotfixes
        :return: dictionary with system details
        """

        win_ver = sys.getwindowsversion()
        system_info = {
            "system": platform.system(),  # Windows
            "release": platform.release(),  # Major (e.g. 10, 11)
            "version": platform.version(),  # build version
            "major": win_ver.major,  # major version
            "minor": win_ver.minor,  # minor version
            "build": win_ver.build,  # build version
            "platform": win_ver.platform,  # platform ID
            "service_pack": win_ver.service_pack,
            "architecture": platform.architecture(),  # (64bit, 32bit)
            "hotfixes": self.get_hotfixes_winapi()
        }
        return system_info

    @staticmethod
    def get_hotfixes_winapi():
        """
        Retrieve installed Windows hotfixes using the Update API.

        Searches update history, extracts KB identifiers, install dates, and result codes.
        :return: list of dictionaries with hotfix details
        """
        update_session = win32com.client.Dispatch("Microsoft.Update.Session")
        update_searcher = update_session.CreateUpdateSearcher()
        history_count = update_searcher.GetTotalHistoryCount()
        history = update_searcher.QueryHistory(0, history_count)

        hotfixes = []
        for entry in history:
            match = re.search(r"(KB\d+)", entry.Title)
            if match:
                hotfixes.append({
                    "kb": match.group(1),
                    "date": entry.Date,
                    "result": entry.ResultCode
                })
        return hotfixes

    @staticmethod
    def get_hotfixes_powershell():
        cmd = 'powershell "Get-HotFix | Select-Object -Property HotFixID, InstalledOn"'
        output = subprocess.check_output(cmd, shell=True).decode(errors="ignore")
        hotfixes = []
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("kb"):
                parts = line.split(None, 1)
                if len(parts) == 2:
                    hotfixes.append({
                        "KB": parts[0],
                        "InstalledOn": parts[1]
                    })
        return hotfixes