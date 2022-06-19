# Gen Backend

## Models

### License

| Field                 | Data type     | Description |
| --------------------- | ------------- | ----------- |
| id                    | Integer       | Identifier of the license. Every change the licenses can have, instead a new license will be added. |
| name                  | Varchar(256)  | Formal name of the license. |
| description           | Varchar(1024) | Additional information of the license. |
| duration              | Integer       | Duration in seconds. | 
| readable_duration     | Varchar(16)   | Friendlier duration more readable for the user. |
| amount_of_children    | Integer       | Amount of children that this license can generate. |
| previous_license_id   | Integer       | Since the data on this table should be only added and not edited, this id is for knowing that the license comes out from another license. |
| is_active             | Integer       | If this license is currently active. |
| created_at            | Integer       | Creation date of the license. |

### User
| Field | Data type | Description |
| ----- | --------- | ----------- |
| id    |
