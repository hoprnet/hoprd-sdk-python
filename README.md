# hoprd-sdk
This Rest API enables developers to interact with a hoprd node programatically.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0.0
- Package version: 2.0.0-rc.1
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import hoprd_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hoprd_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to */api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_get_address**](docs/AccountApi.md#account_get_address) | **GET** /account/address | 
*AccountApi* | [**account_get_addresses**](docs/AccountApi.md#account_get_addresses) | **GET** /account/addresses | 
*AccountApi* | [**account_get_balances**](docs/AccountApi.md#account_get_balances) | **GET** /account/balances | 
*AccountApi* | [**account_withdraw**](docs/AccountApi.md#account_withdraw) | **POST** /account/withdraw | 
*AliasesApi* | [**aliases_get_alias**](docs/AliasesApi.md#aliases_get_alias) | **GET** /aliases/{alias} | 
*AliasesApi* | [**aliases_get_aliases**](docs/AliasesApi.md#aliases_get_aliases) | **GET** /aliases/ | 
*AliasesApi* | [**aliases_remove_alias**](docs/AliasesApi.md#aliases_remove_alias) | **DELETE** /aliases/{alias} | 
*AliasesApi* | [**aliases_set_alias**](docs/AliasesApi.md#aliases_set_alias) | **POST** /aliases/ | 
*ChannelsApi* | [**channels_aggregate_tickets**](docs/ChannelsApi.md#channels_aggregate_tickets) | **POST** /channels/{channelid}/tickets/aggregate | 
*ChannelsApi* | [**channels_close_channel**](docs/ChannelsApi.md#channels_close_channel) | **DELETE** /channels/{channelid}/ | 
*ChannelsApi* | [**channels_fund_channel**](docs/ChannelsApi.md#channels_fund_channel) | **POST** /channels/{channelid}/fund | 
*ChannelsApi* | [**channels_get_channel**](docs/ChannelsApi.md#channels_get_channel) | **GET** /channels/{channelid}/ | 
*ChannelsApi* | [**channels_get_channels**](docs/ChannelsApi.md#channels_get_channels) | **GET** /channels/ | 
*ChannelsApi* | [**channels_get_tickets**](docs/ChannelsApi.md#channels_get_tickets) | **GET** /channels/{channelid}/tickets | 
*ChannelsApi* | [**channels_open_channel**](docs/ChannelsApi.md#channels_open_channel) | **POST** /channels/ | 
*ChannelsApi* | [**channels_redeem_tickets**](docs/ChannelsApi.md#channels_redeem_tickets) | **POST** /channels/{channelid}/tickets/redeem | 
*CheckHealthinessApi* | [**check_node_healthy**](docs/CheckHealthinessApi.md#check_node_healthy) | **GET** /healthyz/ | 
*CheckReadyApi* | [**check_node_ready**](docs/CheckReadyApi.md#check_node_ready) | **GET** /readyz/ | 
*CheckStartedApi* | [**check_node_started**](docs/CheckStartedApi.md#check_node_started) | **GET** /startedz/ | 
*MessagesApi* | [**messages_delete_messages**](docs/MessagesApi.md#messages_delete_messages) | **DELETE** /messages/ | 
*MessagesApi* | [**messages_get_size**](docs/MessagesApi.md#messages_get_size) | **GET** /messages/size | 
*MessagesApi* | [**messages_peek_all_message**](docs/MessagesApi.md#messages_peek_all_message) | **GET** /messages/peek-all | 
*MessagesApi* | [**messages_peek_message**](docs/MessagesApi.md#messages_peek_message) | **GET** /messages/peek | 
*MessagesApi* | [**messages_pop_all_message**](docs/MessagesApi.md#messages_pop_all_message) | **POST** /messages/pop-all | 
*MessagesApi* | [**messages_pop_message**](docs/MessagesApi.md#messages_pop_message) | **POST** /messages/pop | 
*MessagesApi* | [**messages_send_message**](docs/MessagesApi.md#messages_send_message) | **POST** /messages/ | 
*MessagesApi* | [**messages_websocket**](docs/MessagesApi.md#messages_websocket) | **GET** /messages/websocket | 
*NodeApi* | [**node_get_entry_nodes**](docs/NodeApi.md#node_get_entry_nodes) | **GET** /node/entryNodes | 
*NodeApi* | [**node_get_info**](docs/NodeApi.md#node_get_info) | **GET** /node/info | 
*NodeApi* | [**node_get_metrics**](docs/NodeApi.md#node_get_metrics) | **GET** /node/metrics | 
*NodeApi* | [**node_get_peers**](docs/NodeApi.md#node_get_peers) | **GET** /node/peers | 
*NodeApi* | [**node_get_version**](docs/NodeApi.md#node_get_version) | **GET** /node/version | 
*PeerInfoApi* | [**peer_info_get_peer_info**](docs/PeerInfoApi.md#peer_info_get_peer_info) | **GET** /peers/{peerid}/ | 
*PeersApi* | [**peers_ping_peer**](docs/PeersApi.md#peers_ping_peer) | **POST** /peers/{peerid}/ping | 
*SettingsApi* | [**settings_get_settings**](docs/SettingsApi.md#settings_get_settings) | **GET** /settings/ | 
*SettingsApi* | [**settings_set_setting**](docs/SettingsApi.md#settings_set_setting) | **PUT** /settings/{setting} | 
*TicketsApi* | [**tickets_get_statistics**](docs/TicketsApi.md#tickets_get_statistics) | **GET** /tickets/statistics | 
*TicketsApi* | [**tickets_get_ticket_price**](docs/TicketsApi.md#tickets_get_ticket_price) | **GET** /tickets/price | 
*TicketsApi* | [**tickets_get_tickets**](docs/TicketsApi.md#tickets_get_tickets) | **GET** /tickets/ | 
*TicketsApi* | [**tickets_redeem_tickets**](docs/TicketsApi.md#tickets_redeem_tickets) | **POST** /tickets/redeem | 
*TokensApi* | [**tokens_create**](docs/TokensApi.md#tokens_create) | **POST** /tokens/ | 
*TokensApi* | [**tokens_delete**](docs/TokensApi.md#tokens_delete) | **DELETE** /tokens/{id} | 
*TokensApi* | [**tokens_get_token**](docs/TokensApi.md#tokens_get_token) | **GET** /token | 

## Documentation For Models

 - [AccountWithdrawBody](docs/AccountWithdrawBody.md)
 - [AliasesBody](docs/AliasesBody.md)
 - [Channel](docs/Channel.md)
 - [ChannelId](docs/ChannelId.md)
 - [ChannelStatus](docs/ChannelStatus.md)
 - [ChannelTopology](docs/ChannelTopology.md)
 - [ChannelidFundBody](docs/ChannelidFundBody.md)
 - [ChannelsBody](docs/ChannelsBody.md)
 - [Currency](docs/Currency.md)
 - [Error](docs/Error.md)
 - [HoprAddress](docs/HoprAddress.md)
 - [HoprBalance](docs/HoprBalance.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2002Connected](docs/InlineResponse2002Connected.md)
 - [InlineResponse2002Heartbeats](docs/InlineResponse2002Heartbeats.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse403](docs/InlineResponse403.md)
 - [InlineResponse409](docs/InlineResponse409.md)
 - [InlineResponse422](docs/InlineResponse422.md)
 - [InlineResponse4221](docs/InlineResponse4221.md)
 - [InlineResponseMap200](docs/InlineResponseMap200.md)
 - [MessageBody](docs/MessageBody.md)
 - [MessageTag](docs/MessageTag.md)
 - [MessagesBody](docs/MessagesBody.md)
 - [MessagesPeekBody](docs/MessagesPeekBody.md)
 - [MessagesPeekallBody](docs/MessagesPeekallBody.md)
 - [MessagesPopBody](docs/MessagesPopBody.md)
 - [MessagesPopallBody](docs/MessagesPopallBody.md)
 - [MultiAddress](docs/MultiAddress.md)
 - [NativeAddress](docs/NativeAddress.md)
 - [NativeBalance](docs/NativeBalance.md)
 - [ReceivedMessage](docs/ReceivedMessage.md)
 - [RequestStatus](docs/RequestStatus.md)
 - [Settings](docs/Settings.md)
 - [SettingsSettingBody](docs/SettingsSettingBody.md)
 - [Signature](docs/Signature.md)
 - [Ticket](docs/Ticket.md)
 - [Token](docs/Token.md)
 - [TokenCapability](docs/TokenCapability.md)
 - [TokenCapabilityLimit](docs/TokenCapabilityLimit.md)
 - [TokenCapabilityLimitConditions](docs/TokenCapabilityLimitConditions.md)
 - [TokensBody](docs/TokensBody.md)
 - [TransactionReceipt](docs/TransactionReceipt.md)

## Documentation For Authorization


## keyScheme

- **Type**: API key
- **API key parameter name**: x-auth-token
- **Location**: HTTP header

## passwordScheme

- **Type**: HTTP basic authentication


## Author

tech@hoprnet.org
