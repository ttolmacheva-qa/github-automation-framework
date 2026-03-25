def test_check_example_domain_title(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"