# google-indexing-api

Use the [Google Indexing API](https://developers.google.com/search/apis/indexing-api/v3/quickstart) to submit URLs for indexing to Google Search.

This tool lets you provide a sitemap and send URLs that match any regexes you provide for indexing using the Google Indexing API.

To use this project, first clone this repository and install the required dependencies:

```
git clone https://github.com/capjamesg/google-indexing-api
cd google-indexing-api/
pip3 install -r requirements.txt
```

Then, update the following values in `app.py`:

```
SITEMAP = "https://example.com/sitemap.xml" # the sitemap to crawl
MATCHING_REGEXES = [r"/posts/"] # the regexes of paths you want to crawl
REQUEST_TYPE = "URL_UPDATED" # request type: either URL_UPDATED or URL_DELETED
```

Then, create a Service Account in Google Cloud. Grant access to the Google Indexing API to the Service Account.

Issue OAuth credentials for your Service Account and save them to a file called `secret.json` that is in the same folder as the `app.py` file.

Next, invite the email for your service account to your Google Search Console instance.

Now, you can run the script to request indexing of URLs:

```
python3 app.py
```

At the time of writing this script, Google allows 200 requests per day.

## License

This project is licensed under an [MIT license](LICENSE).
