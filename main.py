import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        state_file = 'estado_sessao.json'
        
        if os.path.exists(state_file):
            print("Carregando sessão existente...")
            context = await browser.new_context(storage_state=state_file)
        else:
            print("Criando nova sessão e salvando...")
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto('https://blaze1.space/pt/?modal=auth&tab=login')
            await asyncio.sleep(5)

            await page.fill('//*[@id="auth-modal"]/div/form/div[1]/div/input', 'USUARIO')
            await page.fill('//*[@id="auth-modal"]/div/form/div[2]/div/input', 'SENHA')
            await page.click('//*[@id="auth-modal"]/div/form/div[4]/button')

            await asyncio.sleep(5)

            await context.storage_state(path=state_file)

        page = await context.new_page()
        await page.goto('https://blaze1.space/pt/games/double')

asyncio.run(main())
