import subprocess
import requests

def enumerate_with_gobuster(domain):
  subprocess.run(["gobuster", "dns", "-d", domain, "-w", "wordlist.txt", "-o", f"{domain}_gobuster.txt", "-t", "50"])

def enumerate_with_subfinder(domain):
  subprocess.run(["subfinder", "-d", domain, "-o", f"{domain}_subfinder.txt"])

def enumerate_with_sublist3r(domain):
  subprocess.run(["sublist3r", "-d", domain, "-o", f"{domain}_sublist3r.txt"])

def send_notification(domain):
  webhook_url = "https://hooks.slack.com/services/{ID}"
  message = f"Enumeration complete for {domain}"
  requests.post(webhook_url, json={"text": message})

# Read in the domain list
with open("domain_list.txt", "r") as f:
  domain_list = f.read().splitlines()

# Enumerate subdomains for each domain using each tool
for domain in domain_list:
  enumerate_with_gobuster(domain)
  enumerate_with_subfinder(domain)
  enumerate_with_sublist3r(domain)

  # Send notification for completed enumeration
  send_notification(domain)
