#/usr/bin/env python

import subprocess

print(" _____               _ _                 _                 ")
print("|_   _|_ _ _ __ ___ (_) |___ _ __  _   _| |__   ___  _   _ ")
print("  | |/ _` | '_ ` _ \| | / __| '_ \| | | | '_ \ / _ \| | | |")
print("  | | (_| | | | | | | | \__ \ |_) | |_| | |_) | (_) | |_| |")
print("  |_|\__,_|_| |_| |_|_|_|___/ .__/ \__, |_.__/ \___/ \__, |")
print("                            |_|    |___/             |___/ ")

print (" BY Lenin Royal :) \n")

interface = raw_input("Enter your wlan interface > ")
new_mac = raw_input("Enter the MAC that you want to change > ")
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("Your new Mac is "+ new_mac)
subprocess.call(["ifconfig", interface])
print("Thankyou for Using our Script :)")