# hoprd_sdk.PeersApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peers_ping_peer**](PeersApi.md#peers_ping_peer) | **POST** /peers/{peerid}/ping | 

# **peers_ping_peer**
> InlineResponse20011 peers_ping_peer(peerid)



Pings another node to check its availability.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.PeersApi(hoprd_sdk.ApiClient(configuration))
peerid = 'peerid_example' # str | Peer id that should be pinged

try:
    api_response = api_instance.peers_ping_peer(peerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->peers_ping_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**| Peer id that should be pinged | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

