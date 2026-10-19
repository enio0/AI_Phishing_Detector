
import unittest

from url_analyser import (
    extract_urls,
    get_domain,
    check_ip_address,
    check_fake_domain,
    check_at_symbol
)


class TestURLAnalyser(unittest.TestCase):

    def test_extract_urls(self):
        email = "Visit https://google.com and https://example.com"
        urls = extract_urls(email)

        self.assertEqual(len(urls), 2)

    def test_ip_address(self):
        self.assertTrue(check_ip_address("http://192.0.2.10/login"))
        self.assertFalse(check_ip_address("https://google.com"))

    def test_fake_domain(self):
        self.assertTrue(check_fake_domain("https://paypal.com.fake.example"))
        self.assertTrue(check_fake_domain("https://micros0ft-login.example"))
        self.assertFalse(check_fake_domain("https://www.paypal.com"))

    def test_at_symbol(self):
        self.assertTrue(check_at_symbol("https://paypal.com@attacker.example"))
        self.assertFalse(check_at_symbol("https://paypal.com"))

    def test_get_domain(self):
        domain = get_domain("https://paypal.com@attacker.example")
        self.assertEqual(domain, "attacker.example")


if __name__ == "__main__":
    unittest.main()
