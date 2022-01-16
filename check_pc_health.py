#!/usr/bin/env

import sys
import shutil
import os


def check_reboot():
    """Return True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_gb, min_percentage):
    """Return True if there isn't enough disk space. Return False otherwise"""
    du = shutil.disk_usage(disk)
    # To calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # To calculate how many free gigabytes
    free_gigabytes = du.free / 2 ** 30
    if percent_free < min_percentage or free_gigabytes < min_gb:
        return True
    return False


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percentage=10):
        print("# WARNING: Disk full.\nResolve this with any of the below tasks.")
        print("1. Get yourself a spare Disk.\n2. Delete unused apps and files.")
        print("Check pc health again after performing any of the above tasks.")
        sys.exit(1)

    print("Everything is ok!")
    sys.exit(0)


main()

