import pytest
import requests
from playwright.sync_api import expect

def test_api_to_ui_flow(page):
    response =requests.get("https://randomuser.me/api/")
    data = response.json()
    first_name = data["results"][0]["name"]["first"]
    last_name = data["results"][0]["name"]["last"]
    full_name = f"{first_name} {last_name}"
    print (f"Ищем человека: {full_name}")

    page.goto("https://en.wikipedia.org/")
    page.locator("#searchInput").fill(full_name)
    page.locator("#searchInput").press("Enter")

    expect(page.locator("#firstHeading")).to_be_visible()