from playwright.sync_api import sync_playwright


def kun_uz():
    url = 'https://kun.uz/news/category/jahon'
    with sync_playwright() as play:
        browser = play.firefox.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        r = page.query_selector_all('.top-news__big')
        page.screenshot(path=f'example-{play.firefox.name}.png')
        for i in r:
            info1 = i.text_content().split()[2][10:]
            info2 = i.text_content().split()[3:]
            year = i.text_content().split()[2][0:10]
            date = i.text_content().split()[0]
        data_dict = {
            "date": date,
            "year": year,
            "info1": info1,
            "info2": info2
        }
    return data_dict
