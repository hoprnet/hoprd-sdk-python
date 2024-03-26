# hoprd_sdk.ConfigurationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration**](ConfigurationApi.md#configuration) | **GET** /node/configuration | Get the configuration of the running node.

# **configuration**
> str configuration()

Get the configuration of the running node.

Get the configuration of the running node.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.ConfigurationApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get the configuration of the running node.
    api_response = api_instance.configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

