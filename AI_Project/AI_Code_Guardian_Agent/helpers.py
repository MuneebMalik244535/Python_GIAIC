import datetime
import re

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def sanitize_filename(name: str) -> str:
    return re.sub(r'[^\w\-_\. ]', '_', name)
