# Exchange Currencies Without Any Fees
GET API Format: https://ccyconverttrigger.azurewebsites.net/api/ccyconverttrigger?from_ccy={3 letter from currency code}&to_ccy={3 letter to currency code}&amount={amount to be converted}

API key to be used in the header: 'x-functions-key:RD_RNS7Kf7fiKMbP4sysWeQnjxOgE3uMYuOnMQ-aTo47AzFumfU9Sg=='

# How to deploy manually
1. func azure functionapp publish CcyConvertTrigger
1. curl -X GET -H 'x-functions-key:RD_RNS7Kf7fiKMbP4sysWeQnjxOgE3uMYuOnMQ-aTo47AzFumfU9Sg==' https://ccyconverttrigger.azurewebsites.net/api/ccyconverttrigger\?from_ccy=JPY\&to_ccy=GBP\&amount=63
# How to test locally
1. func start
1. curl -X GET http://localhost:7071/api/CcyConvertTrigger?from_ccy=GBP&to_ccy=USD&amount=15
