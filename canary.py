#!/usr/bin/env python

'''
Author: Dustin Grady
Function: Alert user if VPN/ service provider modifies canary notice
Status: Working/ Tested
'''

import os
import sys
import requests
import subprocess
import configparser
if sys.platform == 'win32':
    import win32api
if sys.platform == 'darwin':
    from easygui import msgbox


'''Lookup sysarg and corresponding vpn_link/ vpn_canary in .ini file'''
def lookup(arg):
    arg = arg.strip('-').upper()
    if arg == 'HELP':
        print('To run: "python canary.py -<flag>\nValid flags:\n-nord\n-vpnsecure\n-slickvpn\n-ivpn\n-proxy.sh\n-proton\n-spyoff\n-azire\n-liquid\n-ace\n-cloudflare\n-vpnht')
        sys.exit(0)

    config = configparser.ConfigParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config.read(dir_path + '/info.ini')

    try:
        link = config[arg]['link']
        canary = list(config[arg]['canary'].split('\n'))
        check_canary(link, canary)
    except KeyError:
        print('Error reading value. Did you provide a valid flag?')

'''Check appropriate website for statements'''
def check_canary(vpn_link, vpn_canary):
    res = requests.get(vpn_link)
    res_text = res.text
    platform = sys.platform
    for statement in vpn_canary:
        if statement not in res_text:
            if platform == 'linux' or platform == 'linux2':  # Linux
                title = "VPN Canary Alert!"
                body = "The following has been modified on your VPNs Canary page:\n" + statement
                subprocess.call(['notify-send', title, body])

            elif platform == 'darwin':  # Mac
                title = "VPN Canary Alert!"
                body = "The following has been modified on your VPNs Canary page:\n" + statement
                msgbox(body, title)

            elif platform == 'win32':  # Windows
                win32api.MessageBox(0, 'The following has been modified on your VPNs Canary page:\n' + statement, 'VPN Canary Alert!')


try:
    lookup(sys.argv[1])
except IndexError:
    print("Please provide a valid argument, or run 'python canary.py -help' for more info")
