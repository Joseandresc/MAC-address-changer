
import subprocess
import optparse
import re

def get_arguments():
    # parser object is created here
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        #handle error
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC, use --help for more info")
    return options
def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    regexMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if regexMac:
        return regexMac.group(0)
    else:
        print("Could not find MAC address")

options = get_arguments()
change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
print("Current MAC " + str(current_mac))

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC address was successfully change to " + current_mac)
else:
    print("MAC address did not change")
