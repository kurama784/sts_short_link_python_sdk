import os
from short_link_sdk import sdk

client = sdk.ShortLinkClient(os.getenv("SHORT_LINK_TOKEN"))
resp = client.create_link("https://google.com")

print(resp['Url'])