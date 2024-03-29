# hoprd_sdk.AccountApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get_address**](AccountApi.md#account_get_address) | **GET** /account/address | 
[**account_get_addresses**](AccountApi.md#account_get_addresses) | **GET** /account/addresses | 
[**account_get_balances**](AccountApi.md#account_get_balances) | **GET** /account/balances | 
[**account_withdraw**](AccountApi.md#account_withdraw) | **POST** /account/withdraw | 

# **account_get_address**
> InlineResponse20010 account_get_address()



Get node's HOPR and native addresses. HOPR address is also called PeerId and can be used by other node owner to interact with this node.

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))

try:
    api_response = api_instance.account_get_address()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_address: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_addresses**
> InlineResponse20010 account_get_addresses()



Get node's HOPR and native addresses. HOPR address is also called PeerId and can be used by other node owner to interact with this node.

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))

try:
    api_response = api_instance.account_get_addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_balances**
> InlineResponse2009 account_get_balances()



Get node's and associated Safe's HOPR and native balances as well as the allowance for HOPR tokens to be drawn by HoprChannels from Safe. HOPR tokens from the Safe balance is used to fund payment channels between this node and other nodes on the network. NATIVE balance of the Node is used to pay for the gas fees for the blockchain.

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))

try:
    api_response = api_instance.account_get_balances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_balances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_withdraw**
> InlineResponse2008 account_withdraw(body=body)



Withdraw funds from this node to your ethereum wallet address. You can choose whitch currency you want to withdraw, NATIVE or HOPR.

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.AccountWithdrawBody() # AccountWithdrawBody |  (optional)

try:
    api_response = api_instance.account_withdraw(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_withdraw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountWithdrawBody**](AccountWithdrawBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

