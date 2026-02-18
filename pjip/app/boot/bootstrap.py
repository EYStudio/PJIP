import ctypes
import os
import re
import sys
import time

from pjip.app.constants import IS_E_CLASSROOM_STUDENTMAIN


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
