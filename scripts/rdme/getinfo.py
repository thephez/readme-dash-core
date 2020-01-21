import requests
from requests.auth import HTTPBasicAuth
import json
import os

API_KEY = os.environ.get("DASH_CORE_README_API_KEY")
VERSION = 'v0.15.0'
CATEGORIES = ['core-reference', 'core-api-reference', 'core-examples', 'additional-resources', 'core-guides']

def api_get(url, headers=None):
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(API_KEY,''))
    return response.json()

# Categories
def get_category(category_name):
    url = '{}/{}'.format("https://dash.readme.io/api/v1/categories", category_name)
    headers = {'x-readme-version': VERSION}
    return api_get(url, headers)

def get_docs_in_category(category_name):
    url = '{}/{}/docs'.format("https://dash.readme.io/api/v1/categories", category_name)
    headers = {'x-readme-version': VERSION}
    return api_get(url, headers)


# Docs
def get_doc_by_slug(slug, doc_version):
    url = '{}/{}'.format("https://dash.readme.io/api/v1/docs", slug)
    headers = {'x-readme-version': doc_version}
    return api_get(url, headers)


# Projects
def get_project_metadata():
    url = "https://dash.readme.io/api/v1/"
    return api_get(url)

# Version
def get_project_versions():
    url = "https://dash.readme.io/api/v1/version"
    return api_get(url)

def get_project_version_dump(version_id):
    url = '{}:{}'.format("https://dash.readme.io/api/v1/version", "versionId")
    print(url)
    return api_get(url)

# Errors
def get_errors():
    url = "https://dash.readme.io/api/v1/errors"
    print(url)
    return api_get(url)


def write_to_file(filename, data):
    print(filename)
    with open(filename, "w") as md_file:
        md_file.write(data)


#print(json.dumps(get_project_metadata(), indent=2))
#print(json.dumps(get_project_versions(), indent=2))

# Not working
#print(json.dumps(get_project_version_dump('5daf2e65f4109c0040fd51e5'), indent=2))

#print(json.dumps(get_errors(), indent=2))

# Known categories: core-reference, core-api-reference, core-examples, test
# Unknown: core guides category name
category = "core-guides"
print(json.dumps(get_category(category), indent=2))
print(json.dumps(get_docs_in_category(category), indent=2))

results = []
for c in CATEGORIES:
    results.append(get_docs_in_category(c))

print(json.dumps(results, indent=2))

for r in results:
    for x in r:
        print(x)
        print('{} ({})'.format(x['title'], x['slug']))
        doc = get_doc_by_slug(x['slug'], VERSION)
        print(json.dumps(doc, indent=2))
        #print(doc['body'])
        filename = "{}.md".format(x['slug'])
        #write_to_file(filename, doc['body'])
        if 'children' in doc:
            for child in doc['children']:
                print('Child doc: {}'.format(child))
