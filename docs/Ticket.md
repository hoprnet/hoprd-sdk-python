# Ticket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | [**ChannelId**](ChannelId.md) |  | [optional] 
**amount** | **str** | The ticket&#x27;s value in HOPR. Only relevant if ticket is a win. | [optional] 
**index** | **str** | Each ticket is labeled by an ongoing serial number named ticket index i and its current value is stored in the smart contract. | [optional] 
**index_offset** | **str** | Offset by which the on-chain stored ticket index gets increased when redeeming the ticket. Used to aggregate tickets. | [optional] 
**channel_epoch** | **str** | Payment channels might run through multiple open and close sequences, this epoch tracks the sequence. | [optional] 
**win_prob** | **str** | The ticket&#x27;s winning probability, going from 0.0 to 1.0 where 0.0 ~&#x3D; 0% winning probability and 1.0 equals 100% winning probability. | [optional] 
**signature** | [**Signature**](Signature.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

