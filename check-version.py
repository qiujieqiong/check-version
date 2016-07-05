#!/usr/bin/env python

import os
import sys
import subprocess
import json

def get_data():
    with open('info.json','r') as f:
        info = json.load(f)
        return info


def check_version():
    OS_RELEASE = subprocess.check_output(["cat /etc/os-release|grep VERSION_ID|cut -d '\"' -f 2"], shell=True).decode('utf-8').strip('\n')
    DEEPIN_VERSION = subprocess.check_output(["cat /etc/deepin-version|grep Version|cut -d = -f 2"], shell=True).decode('utf-8').strip('\n')
    LSB_RELEASE = subprocess.check_output(["cat /etc/lsb-release|grep DISTRIB_RELEASE|cut -d = -f 2"], shell=True).decode('utf-8').strip('\n')
    print OS_RELEASE
    print DEEPIN_VERSION
    print LSB_RELEASE
    data = get_data()
    print data['version']
    with open('docker.result', 'w') as f:
        if OS_RELEASE == data['version']:
            f.write(data['caseID'][0]+' Pass\n')
        else:
            f.write(data['caseID'][0]+' Fail\n')
        if DEEPIN_VERSION == data['version']:
            f.write(data['caseID'][1]+' Pass\n')
        else:
            f.write(data['caseID'][1]+' Fail\n')
        if LSB_RELEASE == data['version']:
            f.write(data['caseID'][2]+' Pass\n')
        else:
            f.write(data['caseID'][2]+' Fail\n')
    f.close()
if __name__ == '__main__':
    check_version()
