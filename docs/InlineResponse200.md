# InlineResponse200

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unredeemed** | **float** | Number of tickets that wait to be redeemed as for Hopr tokens. | [optional] 
**unredeemed_value** | **str** | Total value of all unredeemed tickets in Hopr tokens. | [optional] 
**redeemed** | **float** | Number of tickets already redeemed on this node. | [optional] 
**redeemed_value** | **str** | Total value of all redeemed tickets in Hopr tokens. | [optional] 
**losing_tickets** | **float** | Number of tickets that didn&#x27;t win any Hopr tokens. To better understand how tickets work read about probabilistic payments (https://docs.hoprnet.org/core/probabilistic-payments) | [optional] 
**win_proportion** | **float** | Proportion of number of winning tickets vs loosing tickets, 1 means 100% of tickets won and 0 means that all tickets were losing ones. | [optional] 
**neglected** | **float** | Number of tickets that were not redeemed in time before channel was closed. Those cannot be redeemed anymore. | [optional] 
**neglected_value** | **str** | Total value of all neglected tickets in Hopr tokens. | [optional] 
**rejected** | **float** | Number of tickets that were rejected by the network by not passing validation. In other words tickets that look suspicious and are not eligible for redeeming. | [optional] 
**rejected_value** | **str** | Total value of rejected tickets in Hopr tokens | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

