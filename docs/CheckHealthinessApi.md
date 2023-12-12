# hoprd_sdk.CheckHealthinessApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_node_healthy**](CheckHealthinessApi.md#check_node_healthy) | **GET** /healthyz/ | 

# **check_node_healthy**
> object check_node_healthy()



Check whether the node is healthy

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
api_instance = hoprd_sdk.CheckHealthinessApi(hoprd_sdk.ApiClient(configuration))

try:
    api_response = api_instance.check_node_healthy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckHealthinessApi->check_node_healthy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

