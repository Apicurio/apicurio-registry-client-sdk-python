## Service Registry SDK Examples

Directory contains examples for APIcurio service registry.

## Basic example



1. Create env variable for registry server url.
For example when using Managed Service Registry
```
SERVICE_REGISTRY_URL=https://3.serviceregistry.rhcloud.com/t/f21a297d-e6ea-49de-99b9-2a231018b7c5
```

1.If you are using service registy instance that requires authentication you need to specify
username and password for authentication:

```
SERVICE_ACCOUNT_CLIENT_ID=srvc-acct-0
SERVICE_ACCOUNT_CLIENT_SECRET=b288da06-57ee-46c0-b708
```

1. Review example group and artifact ID and change it's values to the ones you have in your registy.

1. Run example

```
python3 api/basic.py
```

## RHOAS specific 

rhoas service-registry artifact create --artifact-id=message examples/example-schema.json 