import re

from getsitemap import get_individual_sitemap
from google.oauth2 import service_account
from googleapiclient.discovery import build

SITEMAP = "https://example.com/sitemap.xml"
MATCHING_REGEXES = [r"/example/"]
REQUEST_TYPE = "URL_UPDATED"

urls = get_individual_sitemap(SITEMAP)[SITEMAP]

credentials = service_account.Credentials.from_service_account_file("secret.json")

service = build("indexing", "v3", credentials=credentials)

batch = service.new_batch_http_request()

eligible_urls = [url for url in urls if any(re.match(regex, url) for regex in MATCHING_REGEXES)]

batches = [eligible_urls[i : i + 100] for i in range(0, len(eligible_urls), 100)]


def callback(_, response, exception):
    if exception is not None:
        print("Error")
        print(exception)
    else:
        print("Success")
        print(response)


for batch_urls in batches:
    for url in batch_urls:
        request = {"url": url, "type": REQUEST_TYPE}
        batch.add(service.urlNotifications().publish(body=request), callback=callback)

    batch.execute()
    batch = service.new_batch_http_request()

print("Done ✨")
