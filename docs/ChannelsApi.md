# swagger_client.ChannelsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_close_channel**](ChannelsApi.md#channels_close_channel) | **DELETE** /channels/{peerid}/{direction}/ | 
[**channels_fund_channels**](ChannelsApi.md#channels_fund_channels) | **POST** /fundmulti/ | 
[**channels_get_channel**](ChannelsApi.md#channels_get_channel) | **GET** /channels/{peerid}/{direction}/ | 
[**channels_get_channels**](ChannelsApi.md#channels_get_channels) | **GET** /channels/ | 
[**channels_get_tickets**](ChannelsApi.md#channels_get_tickets) | **GET** /channels/{peerid}/tickets | 
[**channels_open_channel**](ChannelsApi.md#channels_open_channel) | **POST** /channels/ | 
[**channels_redeem_tickets**](ChannelsApi.md#channels_redeem_tickets) | **POST** /channels/{peerid}/tickets/redeem | 

# **channels_close_channel**
> InlineResponse20011 channels_close_channel(peerid, direction)



Close a opened channel between this node and other node. Once you've initiated channel closure, you have to wait for a specified closure time, it will show you a closure initiation message with cool-off time you need to wait.   Then you will need to send the same command again to finalize closure. This is a cool down period to give the other party in the channel sufficient time to redeem their tickets.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
peerid = 'peerid_example' # str | 
direction = 'direction_example' # str | Specify which channel should be fetched, incoming or outgoing.

try:
    api_response = api_instance.channels_close_channel(peerid, direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_close_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**|  | 
 **direction** | **str**| Specify which channel should be fetched, incoming or outgoing. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_fund_channels**
> InlineResponse2011 channels_fund_channels(body=body)



Fund one or two payment channels between this node and the counter party provided.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FundmultiBody() # FundmultiBody |  (optional)

try:
    api_response = api_instance.channels_fund_channels(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_fund_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FundmultiBody**](FundmultiBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_get_channel**
> list[Channel] channels_get_channel(peerid, direction)



Returns information about the channel between this node and provided peerId.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
peerid = swagger_client.HoprAddress() # HoprAddress | Counterparty peerId assigned to the channel you want to fetch.
direction = 'direction_example' # str | Specify which channel should be fetched, incoming or outgoing.

try:
    api_response = api_instance.channels_get_channel(peerid, direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_get_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | [**HoprAddress**](.md)| Counterparty peerId assigned to the channel you want to fetch. | 
 **direction** | **str**| Specify which channel should be fetched, incoming or outgoing. | 

### Return type

[**list[Channel]**](Channel.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_get_channels**
> InlineResponse2005 channels_get_channels(including_closed=including_closed, full_topology=full_topology)



Lists all active channels between this node and other nodes on the Hopr network. By default response will contain all incomming and outgoing channels that are either open, waiting to be opened, or waiting to be closed. If you also want to receive past channels that were closed, you can pass `includingClosed` in the request url query.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
including_closed = 'including_closed_example' # str | When includingClosed is passed the response will include closed channels which are ommited by default. (optional)
full_topology = 'full_topology_example' # str | Get the full payment channel graph indexed by the node. (optional)

try:
    api_response = api_instance.channels_get_channels(including_closed=including_closed, full_topology=full_topology)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_get_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **including_closed** | **str**| When includingClosed is passed the response will include closed channels which are ommited by default. | [optional] 
 **full_topology** | **str**| Get the full payment channel graph indexed by the node. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_get_tickets**
> list[Ticket] channels_get_tickets(peerid)



Get tickets earned by relaying data packets by your node for the particular channel.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
peerid = 'peerid_example' # str | 

try:
    api_response = api_instance.channels_get_tickets(peerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_get_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**|  | 

### Return type

[**list[Ticket]**](Ticket.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_open_channel**
> InlineResponse2012 channels_open_channel(body=body)



Opens a payment channel between this node and the counter party provided. This channel can be used to send messages between two nodes using other nodes on the network to relay the messages. Each message will deduce its cost from the funded amount to pay other nodes for relaying your messages. Opening a channel can take a little bit of time, because it requires some block confirmations on the blockchain.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelsBody() # ChannelsBody |  (optional)

try:
    api_response = api_instance.channels_open_channel(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_open_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelsBody**](ChannelsBody.md)|  | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_redeem_tickets**
> channels_redeem_tickets(peerid)



Redeems your tickets for this channel. Redeeming will change your tickets into Hopr tokens if they are winning ones. You can check how much tickets given channel has by calling /channels/{peerid}/tickets endpoint. Do this before channel is closed as neglected tickets are no longer valid for redeeming.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
peerid = 'peerid_example' # str | 

try:
    api_instance.channels_redeem_tickets(peerid)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_redeem_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

