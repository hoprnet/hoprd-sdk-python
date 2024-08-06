# hoprd_sdk.SessionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](SessionApi.md#create_client) | **POST** /api/v3/session | Creates a new client session returing a dedicated session listening port.

# **create_client**
> SessionClientResponse create_client(body)

Creates a new client session returing a dedicated session listening port.

Once the port is bound, it is possible to use the socket for bidirectional read and write communication. Various services require diffrent types of socket communications. This is set by the capabilities field.  TODO: The prototype implementation does not support UDP sockets yet and forces the usage of a TCP socket. Such a restriction is not ideal and should be removed in the future.

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
api_instance = hoprd_sdk.SessionApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.SessionClientRequest() # SessionClientRequest | Creates a new client HOPR session that will start listening on a dedicated port. Once the port is bound, it is possible to use the socketfor bidirectional read and write communication.

try:
    # Creates a new client session returing a dedicated session listening port.
    api_response = api_instance.create_client(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionClientRequest**](SessionClientRequest.md)| Creates a new client HOPR session that will start listening on a dedicated port. Once the port is bound, it is possible to use the socketfor bidirectional read and write communication. | 

### Return type

[**SessionClientResponse**](SessionClientResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

