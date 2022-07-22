from graphqlclient import GraphQLClient

import json

def create_group(client: GraphQLClient, name: str):
    _result = client.execute('''
    {
      groups {
        list { name }
      }
    }
    ''')
    if name in _result:
        return
    # result = json.loads(result)
    # result["groups"]["list"]
    #print(type(result))

    # TODO: Implement error checks
    _result = client.execute('''
    mutation Group($name: String!) {
      groups {
         create(name: $name) {
          responseResult {
            succeeded,
            errorCode,
            slug,
            message
          },
          group {
            id
            createdAt
            name
          }
        }
      }
    }
    ''', variables={'name': name})
    print(_result)
    return _result["data"]["groups"]["create"]["group"]["id"]

def sync_users(client: GraphQLClient, name: str, users: list):
    # TODO: Sync users
    yield

def assign_user(client: GraphQLClient, group_id: int, user_id: int):
    _result = client.execute('''
        mutation AssignUser($groupId: Int!, $userId: Int!) {
            groups {
                assignUser(groupId: $groupId, userId: $userId) {
                responseResult {
                succeeded,
                errorCode,
                slug,
                message
              }
            }
          }
    }''', variables={'groupId': group_id, 'userId': user_id})
    print(_result)

def retrieve_users(client: GraphQLClient):
    _result = client.execute('''
    {
        users {
            list {
                id
                email
            }
        }
    }''')
    _result = json.loads(_result)
    print(_result)
    return _result["data"]["users"]["list"]