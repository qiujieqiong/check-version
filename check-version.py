#!/usr/bin/env python

import os
import sys
import subprocess

def check_version():
    version = sys.argv[1]
    OS_RELEASE = subprocess.check_output(["cat /etc/os-release|grep VERSION_ID|cut -d '\"' -f 2"], shell=True).decode('utf-8').strip('\n')
    DEEPIN_VERSION = subprocess.check_output(["cat /etc/deepin-version|grep Version|cut -d = -f 2"], shell=True).decode('utf-8').strip('\n')
    LSB_RELEASE = subprocess.check_output(["cat /etc/lsb-release|grep DISTRIB_RELEASE|cut -d = -f 2"], shell=True).decode('utf-8').strip('\n')
    print OS_RELEASE
    print DEEPIN_VERSION
    print LSB_RELEASE
    with open('docker.result', 'w') as f:
        if OS_RELEASE == version:
            f.write('1 Pass\n')
        else:
            f.write('1 Fail\n')
        if DEEPIN_VERSION == version:
            f.write('2 Pass\n')
        else:
            f.write('2 Fail\n')
        if LSB_RELEASE == version:
            f.write('3 Pass\n')
        else:
            f.write('3 Fail\n')
    f.close()
if __name__ == '__main__':
    check_version()
