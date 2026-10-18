from playwright.sync_api import expect


def test_whitespace_is_trimmed_in_the_browser(page, live_server):
    page.goto(f"{live_server}/cars/new")

    page.get_by_label("Make", exact=True).fill("  Toyota  ")
    page.get_by_label("Model", exact=True).fill(" Corolla ")
    page.get_by_label("Year", exact=True).fill("2024")

    page.get_by_role("button", name="Create car").click()

    expect(page.get_by_role("heading", name="Toyota Corolla", exact=True)).to_be_visible()