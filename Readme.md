# How to deploy manually
1. func azure functionapp publish CcyConvertTrigger
1. curl -X GET -H 'x-functions-key:<API-KEY-HERE>' https://ccyconverttrigger.azurewebsites.net/api/ccyconverttrigger\?from_ccy=JPY\&to_ccy=GBP\&amount=63
# How to test locally
1. func start
1. curl -X GET http://localhost:7071/api/CcyConvertTrigger?from_ccy=GBP&to_ccy=USD&amount=15

# Generate JSON credentials for Github Action
1. az ad sp create-for-rbac --name CcyConvertTrigger --role contributor --scopes /subscriptions/<SUBSCRIPTION-ID-HERE> --sdk-auth
