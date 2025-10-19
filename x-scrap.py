import asyncio
from twikit import Client
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.environ.get('USERNAME')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


# Initialize client
# Using a proxy is recommended to avoid being blocked by Cloudflare.
# The proxy URL is retrieved from the 'PROXY' environment variable.
proxy = os.environ.get('PROXY')
client = Client('en-US', proxy=proxy, verify=False)

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD,
        cookies_file='cookies.json'
    )

asyncio.run(main())