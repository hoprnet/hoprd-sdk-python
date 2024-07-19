# hoprd_sdk.NetworkApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**price**](NetworkApi.md#price) | **GET** /api/v3/network/price | Obtains the current ticket price.

# **price**
> TicketPriceResponse price()

Obtains the current ticket price.

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
api_instance = hoprd_sdk.NetworkApi(hoprd_sdk.ApiClient(configuration))

try:
    # Obtains the current ticket price.
    api_response = api_instance.price()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->price: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TicketPriceResponse**](TicketPriceResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

