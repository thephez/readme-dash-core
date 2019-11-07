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

def get_project_versions():
    url = "https://dash.readme.io/api/v1/version"
    return api_get(url)

def get_project_version_dump(version_id):
    url = '{}:{}'.format("https://dash.readme.io/api/v1/version", "versionId")
    print(url)
    return api_get(url)

def get_errors():
    url = "https://dash.readme.io/api/v1/errors"
    print(url)
    return api_get(url)


print(json.dumps(get_project_metadata(), indent=2))
print(json.dumps(get_project_versions(), indent=2))

# Not working
#print(json.dumps(get_project_version_dump('5daf2e65f4109c0040fd51e5'), indent=2))

print(json.dumps(get_errors(), indent=2))

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
