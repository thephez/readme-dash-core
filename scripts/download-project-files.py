#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
import json
import os
import sys

# Necessary for Travis
reload(sys)
sys.setdefaultencoding('utf-8')

API_KEY = os.environ.get("DASH_CORE_README_API_KEY")
VERSION = 'v0.15.0'
CATEGORIES = ['core-reference', 'core-api-reference', 'core-guides', 'core-examples', 'additional-resources']

def api_get(url, headers=None):
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(API_KEY,''))
    # Raise exception for errors (4xx, 5xx)
    response.raise_for_status()
    return response.json()

# Categories
def get_docs_in_category(category_name):
    url = '{}/{}/docs'.format("https://dash.readme.io/api/v1/categories", category_name)
    headers = {'x-readme-version': VERSION}
    return api_get(url, headers)

# Docs
def get_doc_by_slug(slug, doc_version):
    url = '{}/{}'.format("https://dash.readme.io/api/v1/docs", slug)
    headers = {'x-readme-version': doc_version}
    return api_get(url, headers)

# Errors
def get_errors():
    url = "https://dash.readme.io/api/v1/errors"
    print(url)
    return api_get(url)


def write_to_file(filename, data):
    #print('Writing to: {}'.format(filename))
    with open(filename, "w") as md_file:
        md_file.write(data)


def main():
    results = []
    for c in CATEGORIES:
        results.append(get_docs_in_category(c))

    slugs = []
    for result in results:
        for r in result:
            slugs.append(r['slug'])
            #print('{} ({})'.format(r['title'], r['slug']))
            doc = get_doc_by_slug(r['slug'], VERSION)

            if 'children' in r:
                for child in r['children']:
                    slugs.append(child['slug'])

    for slug in slugs:
        print('Processing slug: {}'.format(slug))
        doc = get_doc_by_slug(slug, VERSION)
        filename_markdown_content = "markdown/{}.md".format(slug)
        filename_full_content = "full-json/{}.json".format(slug)
        filename_html_content = "html/{}.html".format(slug)
        write_to_file(filename_markdown_content, doc['body'])
        write_to_file(filename_full_content, json.dumps(doc, indent=1))
        #write_to_file(filename_html_content, doc['body_html'])

if __name__ == '__main__':
    main()
