# swagger_client.PeerInfoApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peer_info_get_peer_info**](PeerInfoApi.md#peer_info_get_peer_info) | **GET** /peerInfo/{peerid} | 

# **peer_info_get_peer_info**
> InlineResponse20010 peer_info_get_peer_info(peerid)



Get information about this peer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PeerInfoApi(swagger_client.ApiClient(configuration))
peerid = swagger_client.HoprAddress() # HoprAddress | 

try:
    api_response = api_instance.peer_info_get_peer_info(peerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerInfoApi->peer_info_get_peer_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | [**HoprAddress**](.md)|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

