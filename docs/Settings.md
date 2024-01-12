# Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_recipient** | **bool** | Prepends your address to all messages so that receiver of the message can know that you sent that message. | [optional] 
**strategy** | **str** | By default, hoprd runs in **passive** mode, this means that your node will not attempt to open or close any channels automatically. When you set your strategy to **promiscuous** mode, your node will attempt to open channels to a _randomly_ selected group of nodes which you have a healthy connection to. At the same time, your node will also attempt to close channels that are running low on balance or are unhealthy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

