# InlineResponse2002Connected

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_id** | [**HoprAddress**](HoprAddress.md) |  | [optional] 
**peer_address** | [**NativeAddress**](NativeAddress.md) |  | [optional] 
**multi_addr** | [**MultiAddress**](MultiAddress.md) |  | [optional] 
**heartbeats** | [**InlineResponse2002Heartbeats**](InlineResponse2002Heartbeats.md) |  | [optional] 
**last_seen** | **float** | Timestamp on when the node was last seen (in milliseconds) | [optional] 
**last_seen_latency** | **float** | Latency recorded the last time a node was measured when seen (in milliseconds) | [optional] 
**quality** | **float** | A float between 0 (completely unreliable) and 1 (completely reliable) estimating the quality of service of a peer&#x27;s network connection | [optional] 
**backoff** | **float** |  | [optional] 
**is_new** | **bool** | True if the node is new (no heartbeats sent yet). | [optional] 
**reported_version** | **str** | HOPR protocol version as determined from the successful ping in the Major.Minor.Patch format or \&quot;unknown\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

