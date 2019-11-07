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


def get_category(category_name):
    url = '{}{}'.format("https://dash.readme.io/api/v1/categories/", category_name)
    headers = {'x-readme-version': VERSION}
    return api_get(url, headers)

def get_docs_in_category(category_name):
    url = '{}/{}/docs'.format("https://dash.readme.io/api/v1/categories", category_name, "docs")
    headers = {'x-readme-version': VERSION}
    return api_get(url, headers)


def get_project_metadata():
    url = "https://dash.readme.io/api/v1/"
    return api_get(url)


# Known categories: core-reference, core-api-reference, core-examples, test
# Unknown: core guides category name
category = "core-examples"
#print(json.dumps(get_category(category), indent=2))
#print(json.dumps(get_docs_in_category(category), indent=2))

results = []
for c in CATEGORIES:
    #print(json.dumps(get_category(c), indent=2))
    results.append(get_docs_in_category(c))

print(json.dumps(results, indent=2))
