
import subprocess
import optparse

parser = optparse.OptionParser()

interface = input("interface >")
new_mac = input("MAC >")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])