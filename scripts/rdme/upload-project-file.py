import requests
from requests.auth import HTTPBasicAuth
import json
import os

API_KEY = os.environ.get("DASH_CORE_README_API_KEY")
VERSION = 'v0.15.0'

def api_put(url, payload, headers=None):
    response = requests.put(url, data=payload, headers=headers, auth=HTTPBasicAuth(API_KEY,''))
    # Raise exception for errors (4xx, 5xx)
    response.raise_for_status()
    return response.json()

def read_json_from_file(filename):
    print('Reading from: {}/{}'.format(os.getcwd(), filename))
    with open(filename, "r") as f:
        content = json.load(f)

    return content

def read_from_file(filename):
    print('Reading from: {}/{}'.format(os.getcwd(), filename))
    with open(filename, "r") as f:
        content = f.readlines()

    return content


def main():
    filename = 'api-upload-test'

    # Contains title, category, slug info
    json_data = read_json_from_file(('full-json/{}.json'.format(filename))

    # Text content
    markdown_data = read_from_file('markdown/{}.md'.format(filename))
    full_text = ''.join(markdown_data)
    
    # Construct payload for Readme.io
    payload = {}
    payload['title'] = json_data['title']
    payload['type'] = json_data['type']
    payload['category'] = json_data['category']
    payload['body'] = full_text

    slug = json_data['slug']

    url = '{}/{}'.format("https://dash.readme.io/api/v1/docs", slug)
    headers = {'x-readme-version': 'v0.15.0'}
    
    response = api_put(url, payload, headers)
    print('Updated: "{}" ({})'.format(payload['title'], url))
    #if response['body'] == payload['body']:
    #    print('Successfully updated: "{}"'.format(payload['title']))
    #else:
        #print('Update failed for: "{}"'.format(payload['title']))
        #print(response)
        #print(full_text)

if __name__ == '__main__':
    main()
