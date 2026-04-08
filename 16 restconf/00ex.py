# Import libraries
import requests, urllib3

# Disable Self-Signed Cert warning for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setup base variable for request
restconf_headers = {"Accept": "application/yang-data+json"}

ip="10.5.5.19"
r = requests.get(f"http://{ip}:3000/rpc/get-software-information",
        headers = restconf_headers,
        auth=("sntuser", "Ilovenetworks99"),
        verify=False)

print(r.status_code)

# Print returned data
print("GET DATA:")
print(r.text)

