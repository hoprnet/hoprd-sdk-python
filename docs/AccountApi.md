# hoprd_sdk.AccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addresses**](AccountApi.md#addresses) | **GET** /api/v3/account/addresses | Get node&#x27;s HOPR and native addresses.
[**balances**](AccountApi.md#balances) | **GET** /api/v3/account/balances | Get node&#x27;s and associated Safe&#x27;s HOPR and native balances as the allowance for HOPR
[**withdraw**](AccountApi.md#withdraw) | **POST** /api/v3/account/withdraw | Withdraw funds from this node to the ethereum wallet address.

# **addresses**
> AccountAddressesResponse addresses()

Get node's HOPR and native addresses.

Get node's HOPR and native addresses.  HOPR address is represented by the P2P PeerId and can be used by other node owner to interact with this node.

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get node's HOPR and native addresses.
    api_response = api_instance.addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountAddressesResponse**](AccountAddressesResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balances**
> AccountBalancesResponse balances()

Get node's and associated Safe's HOPR and native balances as the allowance for HOPR

Get node's and associated Safe's HOPR and native balances as the allowance for HOPR tokens to be drawn by HoprChannels from Safe.  HOPR tokens from the Safe balance are used to fund the payment channels between this node and other nodes on the network. NATIVE balance of the Node is used to pay for the gas fees for the blockchain.

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get node's and associated Safe's HOPR and native balances as the allowance for HOPR
    api_response = api_instance.balances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->balances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountBalancesResponse**](AccountBalancesResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw**
> AccountBalancesResponse withdraw(body)

Withdraw funds from this node to the ethereum wallet address.

Withdraw funds from this node to the ethereum wallet address.  Both NATIVE or HOPR can be withdrawn using this method.

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.WithdrawBodyRequest() # WithdrawBodyRequest | 

try:
    # Withdraw funds from this node to the ethereum wallet address.
    api_response = api_instance.withdraw(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->withdraw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WithdrawBodyRequest**](WithdrawBodyRequest.md)|  | 

### Return type

[**AccountBalancesResponse**](AccountBalancesResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

