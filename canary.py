'''
Author: Dustin Grady
Function: Alert user if VPN provider modifies Canary notice
Status: In development
'''

import sys
import requests
import configparser
if sys.platform == 'linux':
    import notify2  # Linux
elif sys.platform == 'win32':
    import win32api  # Windows


'''Lookup sysarg and corresponding vpn_link/ vpn_canary in .ini file'''
def lookup(arg):
    arg = arg.strip('-').upper()

    if arg == 'HELP':
        print('To run: "python canary.py -<flag>\nValid flags:\n-nord\n-vpnsecure\n-lokun\n-slickvpn\n-ivpn\n-proxy.sh')
        sys.exit(0)

    config = configparser.ConfigParser()
    config.read('info.ini')

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

    for statement in vpn_canary:
        if statement not in res_text:
            if sys.platform == 'linux':
                print("ALERT! " + statement +" is missing!")
                notify2.init("Notification")
                n = notify2.Notification("Canary Alert!",
                                         "The following has been removed from your VPNs Canary page:\n" + statement,
                                         "notification-message-im")
                n.show()
            elif sys.platform == 'win32':
                win32api.MessageBox(0, 'The following has been removed from your VPNs Canary page:\n' + statement, 'Canary Alert!')


try:
    lookup(sys.argv[1])
except IndexError:
    print("Please provide a valid argument, or run 'canary.py -help' for more info")
