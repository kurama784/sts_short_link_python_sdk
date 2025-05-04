import os
from short_link_sdk import sdk

client = sdk.ShortLinkClient(os.getenv("SHORT_LINK_TOKEN"))
short_link = client.create_link("https://google.com")

print(short_link)