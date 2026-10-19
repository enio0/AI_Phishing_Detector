
import re
import ipaddress
from urllib.parse import urlparse


# Extract URLs from an email
def extract_urls(email):
    pattern = r'https?://[^\s<>"\']+'
    urls = re.findall(pattern, email)
    return urls


# Check if a URL uses an IP address
def check_ip_address(url):
    domain = urlparse(url).hostname

    if domain is None:
        return False

    try:
        ipaddress.ip_address(domain)
        return True
    except ValueError:
        return False
