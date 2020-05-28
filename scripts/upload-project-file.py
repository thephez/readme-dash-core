import requests
from requests.auth import HTTPBasicAuth
import json
import os
import sys

API_KEY = os.environ.get("DASH_CORE_README_API_KEY")
VERSION = 'v0.16.0'

def api_put(url, payload, headers=None):
    response = requests.put(url, data=payload, headers=headers, auth=HTTPBasicAuth(API_KEY,''))
    # Raise exception for errors (4xx, 5xx)
    response.raise_for_status()
    return response.json()

def read_json_from_file(filename):
    #print('Reading from: {}/{}'.format(os.getcwd(), filename))
    with open(filename, "r") as f:
        content = json.load(f)

    return content

def read_from_file(filename):
    #print('Reading from: {}/{}'.format(os.getcwd(), filename))
    with open(filename, "r") as f:
        content = f.readlines()

    return content

def create_payload(json_data, markdown_text):
    # Construct payload for Readme.io
    payload = {}
    payload['title'] = json_data['title']
    payload['type'] = json_data['type']
    payload['category'] = json_data['category']
    payload['body'] = markdown_text

    return payload


def main(args):
    for i in range(1, len(args)):
        filename = args[i] #'api-upload-test'
        print(filename)

        # Contains title, category, slug info
        json_data = read_json_from_file('full-json/{}.json'.format(filename))

        # Text content
        markdown_lines = read_from_file('markdown/{}.md'.format(filename))
        full_text = ''.join(markdown_lines)

        url = '{}/{}'.format("https://dash.readme.io/api/v1/docs", json_data['slug'])
        headers = {'x-readme-version': VERSION}

        # Create payload and send
        payload = create_payload(json_data, full_text)
        try:
            print('Updating: {}'.format(payload['title']))
            response = api_put(url, payload, headers)
            # TODO: add some checking to verify upload succesful
            print('Updated: "{}" ({})'.format(payload['title'], url))
        except requests.HTTPError as e:
            print('--- Exception updating "{}": {} ---'.format(payload['title'], e))
            continue


if __name__ == '__main__':
    # Call like (supports multiple file args):
    #   python3 upload-project-file.py core-api-ref-remote-procedure-calls-dash
    if len(sys.argv) < 2:
        print('Usage: upload-project-file.py <slugname1> <slugname2>')
    else:
        main(sys.argv)
