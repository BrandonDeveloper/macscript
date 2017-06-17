import os
interface1 = "eth0"
interface2 = "wlan0"
interface3 = "wl01"
normal_mac = "Normal MAC"
print("interface1 is if you are using eth0")
print("interface2 is if you are using wlan0")
print("interface3 is if you are using wl01")
print("normal_mac is if you want your normal mac address back")
interface_option = input("interface1 interface2 or interface3 or normal_mac: ")
if interface_option == interface1:
	os.system('macchanger -r eth0')
if interface_option == interface2:
	os.system('macchanger -r wlan0')
if interface_option == interface3:
	os.system('macchanger -r wl01')
if interface_option == normal_mac:
	what_interface = input("What is your interface interface1 interface2 or interface3: ")
	if what_interface == interface1:
		os.system('macchanger -p eth0')
	if what_interface == interface2:
		os.system('macchanger -p wlan0')
	if what_interface == interface3:
		os.system('macchanger -p wl01')

