# API Reference
## ConfirmTagCreation
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/CreateTag
```json
{
  "Author_ID": "<User_ID>",
  "Tag_Name": "<Tag name>",
  "Tag_Desc": "<Tag desc>"
}
```
Response: [Tags](TagsSrcLink)/[ConfirmTagCreation](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagCreation) 
```json
{
  "Tag_ID": "<TAG_ID>",
  "Status code": "HTTP status code",
  "Created at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
## ConfirmTagUpdate
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/UpdateTag
```json
{
  "Tag_ID": "<TAG_ID>",
  "Tag_name": "<New_Tag-name> OR NULL",
  "Tag_desc": "<New_Tag-desc> OR NULL" 
}
```
Response: [Tags](TagsSrcLink)/[ConfirmTagUpdate](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagUpdate) 
```json
{
  "Status code": "HTTP status code",
  "Updated at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
## ConfirmTagDelete
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/DeleteTag
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
Response: [Tags](TagsSrcLink)/[ConfirmTagDelete](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagDelete) 
```json
{
  "Status code": "HTTP status code",
  "deleted_at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
## ReturnTag
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/RequestTag
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
Response: [Tags](TagsSrcLink)/[ReturnTag](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ReturnTag) 
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
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/RequestTagsForPost
```json
{
  "Post_ID": "<Post_ID>"
}
```
Response: [Tags](TagsSrcLink)/[ReturnTagsForPost](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ReturnTagsForPost) 
```json
{
  "Tag_IDs": ["<Tag-ID1>", "<Tag-ID2>", "..."]
}
```
