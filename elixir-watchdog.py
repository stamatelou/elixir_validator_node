import subprocess
import time
import datetime

restart_command = "docker restart ev"
log_command = "docker logs --since 30s ev"

restart_counter = 0
last_restart_time = "NONE YET"

def get_logs():
    logs = subprocess.run(log_command.split(), capture_output=True, text=True).stdout
    return logs

while True:
    logs = get_logs()
    lines = logs.strip().split("\n")
    count = 0
    for line in lines:
        print(line)
        if "Market data is delayed. Please make sure your connection is stable." in line:
            count += 1
    if count >= 20:
        restart_counter += 1
        print(f"{datetime.datetime.now()} Restarting container... (Total # of restarts: {restart_counter})")
        last_restart_time = datetime.datetime.now()
        subprocess.run(restart_command.split())
    print(f"\n")
    print(f"\n")
    print(f"{datetime.datetime.now()} Total number of occurrences found:", count)
    print(f"{datetime.datetime.now()} Total # of restarts: {restart_counter} - Last restart was at: {last_restart_time}")
    print(f"\n")
    print(f"\n")
    time.sleep(15)
