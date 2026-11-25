import subprocess

def run_cmd(user_input):
    subprocess.run(f"echo {user_input}", shell=True)    # B602 (HIGH -25)
    subprocess.Popen(f"dir {user_input}", shell=True)   # B602 (HIGH -25)