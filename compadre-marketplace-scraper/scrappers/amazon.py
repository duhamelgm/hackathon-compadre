import asyncio
from playwright.async_api import async_playwright, Playwright
import urllib.parse

async def run(playwright: Playwright, query: str):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=True)
    context = await browser.new_context(
      user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
      color_scheme=r"light",
      locale=r"en-US,en;q=0.9",
      storage_state={},
      extra_http_headers={}
    )
    context.set_default_timeout(5000)
    page = await context.new_page()
    await page.goto(f"https://www.amazon.ca/s?k={urllib.parse.quote_plus(query)}&ref=nb_sb_noss", timeout=30000)

    products = page.locator("//div[starts-with(@data-cel-widget, 'search_result_') and translate(substring(@data-cel-widget, string-length('search_result_') + 1), '0123456789', '') = '']")
    result = []
    for i in range(min(await products.count(), 10)):
      try:        
        product = products.nth(i)
        product_result = {
          'source': 'amazon'
        }

        print(await product.get_attribute('class'))

        title = product.locator("h2 a").first
        if title:
          product_result['title'] = await title.text_content()
          product_result["link"] = "amazon.ca" + await title.get_attribute("href")

        price = ""
        price_whole = product.locator(".a-price-whole").first
        if price_whole:
          price += await price_whole.text_content()
        
        price_fraction = product.locator(".a-price-fraction").first
        if price_fraction:
          price += await price_fraction.text_content()

        product_result['price'] = price

        img = product.locator("img").first
        if img:
          product_result['image'] = await img.get_attribute('src')

        result.append(product_result)
      except Exception as e:
        print(e)

    # other actions...
    await browser.close()

    return result[:10]

async def scrap(query: str):
    async with async_playwright() as playwright:
        return await run(playwright, query)