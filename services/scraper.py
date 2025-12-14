from playwright.async_api import async_playwright

async def scrape_linkedin_page(page_id: str):
    url = f"https://www.linkedin.com/company/{page_id}/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            await page.goto(url, timeout=15000)
            await page.wait_for_timeout(3000)
            try:
                name = await page.locator("h1").inner_text()
            except:
                name = page_id
        except:
            name = page_id

        await browser.close()

        return {
            "page_id": page_id,
            "name": name,
            "url": url,
            "followers": 0
        }
