# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://shashi-1234.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0qzP3LsxDiCbFwTmYB6VMjj1LPLVuoiALkx8OUFqH1FgkbKLru_CaHEhTry6GaWbXVvocLX4M8yMd8Gw-FWXkvO8SDle02tzmB2Jh4ijIEzyhTOJcczC8C9TyhWiMrtTo5jFggYyUWxMNhX0tywaG7AwDXi-iHet6H9SsnuwpgBI=058EDCB5"

auth = HTTPBasicAuth("2303a52291@sru.edu.in", API_TOKEN)
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "1"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))