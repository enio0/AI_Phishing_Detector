
import re
import ipaddress
from urllib.parse import urlparse


# Extract URLs from an email
def extract_urls(email):
    pattern = r'https?://[^\s<>"\']+'
    urls = re.findall(pattern, email)
    return urls


def get_domain(url):
    domain = urlparse(url).hostname
    return domain



def check_fake_domain(url):
    domain = get_domain(url)

    if domain is None:
        return False

    if "paypal.com" in domain and not (
        domain == "paypal.com" or domain.endswith(".paypal.com")
    ):
        return True

    if "micros0ft" in domain:
        return True

    return False

def check_at_symbol(url):
    return "@" in urlparse(url).netloc


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


