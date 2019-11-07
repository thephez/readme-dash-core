import requests
from requests.auth import HTTPBasicAuth
import json
import os

API_KEY = os.environ.get("DASH_CORE_README_API_KEY")
VERSION = 'v0.14.1'
CATEGORIES = ['core-reference', 'core-api-reference', 'core-examples', 'additional-resources']

def api_get(url, headers=None):
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(API_KEY,''))
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
    print(filename)
    with open(filename, "w") as md_file:
        md_file.write(data)


results = []
for c in CATEGORIES:
    results.append(get_docs_in_category(c))

#print(json.dumps(results, indent=2))

slugs = []
for result in results:
    for r in result:
        slugs.append(r['slug'])
        #print(r)
        #print('{} ({})'.format(r['title'], r['slug']))
        doc = get_doc_by_slug(r['slug'], VERSION)
        #print(json.dumps(doc, indent=2))
        if 'children' in r:
            for child in r['children']:
                #print('{} ({})'.format(child['title'], child['slug']))
                slugs.append(child['slug'])


for slug in slugs:
    #print('Slug: {}'.format(slug))
    doc = get_doc_by_slug(slug, VERSION)
    filename = "{}.md".format(slug)
    write_to_file(filename, doc['body'])

