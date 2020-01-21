# readme-dash-core

## Readme API use

Requires getting an API key from ```https://dash.readme.io/project/<project-name>/<project-version>/api-key```
and exporting it as an environment variable (`DASH_CORE_README_API_KEY`).

### Search for a term

Example (search for "0.14.1" in version `0.15.0` of the project):
``` shell
curl --request POST \
  --url 'https://dash.readme.io/api/v1/docs/search?search=0.14.1' \
  --header 'x-readme-version: 0.15.0' \
  -u $DASH_CORE_README_API_KEY:
```
