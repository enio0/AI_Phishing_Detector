
import re
import ipaddress
from urllib.parse import urlparse


# Extract URLs from an email
def extract_urls(email):
    pattern = r'https?://[^\s<>"\']+'
    urls = re.findall(pattern, email)

    clean_urls = []

    for url in urls:
        url = url.rstrip(".,;!?")
        clean_urls.append(url)

    return clean_urls


def get_domain(url):
    domain = urlparse(url).hostname
    return domain



def check_fake_domain(url):
    domain = get_domain(url)

    if domain is None:
        return False

    # Known brand domains
    brands = {
        "paypal": "paypal.com",
        "google": "google.com",
        "microsoft": "microsoft.com"
    }

    for brand, official in brands.items():
        if brand in domain:
            if domain != official and not domain.endswith("." + official):
                return True

    # Common imitation examples
    if "paypa1" in domain or "micros0ft" in domain:
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


print(check_fake_domain("https://paypa1.example"))
print(check_fake_domain("https://paypal-login.example"))
print(check_fake_domain("https://google.com.attacker.example"))
print(check_fake_domain("https://www.paypal.com"))