
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


    def test_url_punctuation(self):
        email = "Visit https://example.com/login. Thank you!"
        urls = extract_urls(email)
        self.assertEqual(urls[0], "https://example.com/login")





    def test_improved_fake_domains(self):
        self.assertTrue(check_fake_domain("https://paypa1.example"))
        self.assertTrue(check_fake_domain("https://paypal-login.example"))
        self.assertTrue(check_fake_domain("https://google.com.attacker.example"))
        self.assertFalse(check_fake_domain("https://www.paypal.com"))


    
    def test_uppercase_domain(self):
        self.assertTrue(
            check_fake_domain("https://PAYPAL-LOGIN.example")
        )

    def test_misleading_google_url(self):
        url = "https://google.com@attacker.example/login"

        self.assertEqual(get_domain(url), "attacker.example")
        self.assertTrue(check_at_symbol(url))

    def test_multiple_url_extraction(self):
        email = """
        Visit https://google.com.
        Or http://192.0.2.10/login!
        """

        urls = extract_urls(email)

        self.assertEqual(urls, [
            "https://google.com",
            "http://192.0.2.10/login"
    ])

    def test_combined_url_checks(self):
        url = "https://paypal-login.example@google.com/account"

        self.assertEqual(get_domain(url), "google.com")
        self.assertTrue(check_at_symbol(url))
        self.assertFalse(check_fake_domain(url))
        self.assertFalse(check_ip_address(url))


if __name__ == "__main__":
    unittest.main()
