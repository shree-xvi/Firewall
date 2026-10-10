#in this file, we have a simple firewall simulation that generates random IP addresses and checks them against predefined firewall rules. The code consists of three main functions: `generate_random_ip`, `check_firewall_rules`, and `main`.

import __main__
import random


def generate_random_ip(): #used to generate random IP addresses in the range of 192.168.1.1 to 192.168.1.20
    return f"192.168.1.{random.randint(1, 20)}"

def check_firewall_rules(ip,rules): #used to check if the generated IP address is in the firewall rules and return the corresponding action (block or allow)
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "block"

def main(): 
    firewall_rules = {
         "192.168.1.1": "allow",
        "192.168.1.4": "allow",
        "192.168.1.9": "allow",
        "192.168.1.13": "allow",
        "192.168.1.16": "allow",
        "192.168.1.19": "allow"
    } #this dictionary contains the firewall rules, where the keys are the IP addresses and the values are the corresponding actions (block or allow)

    for _ in range(12):
        ip_address = generate_random_ip() #here we generate a random IP address using the generate_random_ip function
        action = check_firewall_rules(ip_address, firewall_rules) #here we check if the generated IP address is in the firewall rules using the check_firewall_rules function and get the corresponding action (block or allow)
        random_number = random.randint(0, 999) #here we generate a random number between 0 and 999 using the random.randint function
        print(f"IP Address: {ip_address}, Action: {action}, Random: {random_number}")#here we print the generated IP address, the corresponding action (block or allow), and the random number using an f-string

if __name__ == "__main__":
    main()