# hoprd_sdk.PeerInfoApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peer_info_get_peer_info**](PeerInfoApi.md#peer_info_get_peer_info) | **GET** /peers/{peerid}/ | 

# **peer_info_get_peer_info**
> InlineResponse20011 peer_info_get_peer_info(peerid)



Get information about this peer.

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
api_instance = hoprd_sdk.PeerInfoApi(hoprd_sdk.ApiClient(configuration))
peerid = 'peerid_example' # str | 

try:
    api_response = api_instance.peer_info_get_peer_info(peerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerInfoApi->peer_info_get_peer_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**|  | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

