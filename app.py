import yaml

HOST = "0.0.0.0"                  # B104 (MEDIUM -15): เปิดรับทุก Interface
def load_cfg(text):
    return yaml.load(text) 