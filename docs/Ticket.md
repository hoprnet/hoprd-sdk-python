# Ticket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | [**ChannelId**](ChannelId.md) |  | [optional] 
**challenge** | **str** | The ticket&#x27;s challenge which needs to be solved before being able to claim the embedded incentive. | [optional] 
**index** | **str** | Each ticket is labeled by an ongoing serial number named ticket index i and its current value is stored in the smart contract. | [optional] 
**amount** | **str** | The ticket&#x27;s value in HOPR. | [optional] 
**win_prob** | **str** | The ticket&#x27;s winning probability normalized with the common base of Ethereum which is 2^256-1. | [optional] 
**channel_epoch** | **str** | Payment channels might run through multiple open and close sequences, this epoch tracks the sequence. | [optional] 
**signature** | [**Signature**](Signature.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

