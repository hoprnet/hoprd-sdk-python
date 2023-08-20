# MessagesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**MessageTag**](MessageTag.md) |  | 
**body** | [**MessageBody**](MessageBody.md) |  | 
**peer_address** | **str** | The recipient HOPR peer id, to which the message is sent. | 
**path** | **list[str]** | The path is ordered list of peer ids through which the message should be sent. If no path is provided, a path which covers the nodes minimum required hops will be determined automatically. | [optional] 
**hops** | **int** | Number of required intermediate nodes. This parameter is ignored if path is set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

