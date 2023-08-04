import requests
import json


######NOT WORKING Still work in progress

###Update SNMP String v2

AUTHToken="Enter Auth Token"
TenantID="Enter Tenant ID"
SiteID="Enter Site ID"
ElementID="Enter Element ID"
New_V2_String="New V2 String"

url = "https://api.elcapitan.cloudgenix.com/v2.1/api/tenants/{}/sites/{}/elements/{}/snmpagents".format(TenantID, SiteID, ElementID)

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-auth-token': AUTHToken
}

####Get the WAN Interface Config
GET_WAN_INT_CONFIG = requests.request("GET", url, headers=headers)

###Convert to DICTIONARY
Jsonformatted = GET_WAN_INT_CONFIG.json()
print(Jsonformatted)

###Add changed value
#NestedValue = {'community':'Newstring'}
#WANInterfaceUpdate = {'v2_config': {'enabled': True, 'community': 'NewString'}},
Jsonformatted['v2_config'][['community'] : New_V2_String],

##Format back to type to import back in
Serialized_JSON_DATA = json.dumps(Jsonformatted)


##PUTTING DATA BACK
response = requests.request("PUT", url, headers=headers, data=Serialized_JSON_DATA)

print(response.text)
