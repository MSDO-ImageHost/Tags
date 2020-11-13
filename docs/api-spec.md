# API Reference
## ConfirmTagCreation
Request: [Gateway](GatewayLink)/CreateTag
```json
{
  "Author_ID": "<User_ID>",
  "Tag_Name": "<Tag name>",
  "Tag_Desc": "<Tag desc>"
}
```
Response: [Tags](TagsSrcLink)/[ConfirmTagCreation](TagsLink#ConfirmTagCreation) 
```json
{
  "Tag_ID": "<TAG_ID>",
  "Status code": "HTTP status code",
  "Created at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
## ConfirmTagUpdate
Request: [Gateway](GatewayLink)/UpdateTag
```json
{
  "Tag_ID": "<TAG_ID>",
  "Tag_name": "<New_Tag-name> OR NULL",
  "Tag_desc": "<New_Tag-desc> OR NULL" 
}
```
Response: [Tags](TagsSrcLink)/[ConfirmTagUpdate](TagsLink#ConfirmTagUpdate) 
```json
{
  "Status code": "HTTP status code",
  "Updated at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
## ConfirmTagDelete
Request: [Gateway](GatewayLink)/DeleteTag
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
Response: [Tags](TagsSrcLink)/[ConfirmTagDelete](TagsLink#ConfirmTagDelete) 
```json
{
  "Status code": "HTTP status code",
  "deleted_at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
## ReturnTag
Request: [Gateway](GatewayLink)/RequestTag
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
Response: [Tags](TagsSrcLink)/[ReturnTag](TagsLink#ReturnTag) 
```json
{
  "Author": "User ID",
  "Tag_Name": "<Tag-name>",
  "Tag_Desc": "<Tag-desc>",
  "Created at": "<ISO8601 timestamp>",
  "Last updated at": "<ISO8601 timestamp>"
}
```
## ReturnTagsForPost
Request: [Gateway](GatewayLink)/RequestTagsForPost
```json
{
  "Post_ID": "<Post_ID>"
}
```
Response: [Tags](TagsSrcLink)/[ReturnTagsForPost](TagsLink#ReturnTagsForPost) 
```json
{
  "Tag_IDs": "[<Tag-ID1>, <Tag-ID2>, ...]"
}
```
