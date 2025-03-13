import azure.functions as func
import datetime
import json
import logging
import urllib.request
import re

app = func.FunctionApp()
pattern = r'class="BNeawe iBp4i AP7Wnd">[0-9,]+.?[0-9]* [a-zA-Z ]+<\/div>'

@app.route(route="ccy-convert", auth_level=func.AuthLevel.FUNCTION)
def CcyConvertTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #name = req.params.get('name')

    FROM_CCY=req.params.get('from_ccy')
    TO_CCY=req.params.get('to_ccy')
    AMOUNT=req.params.get('amount')

    if FROM_CCY and TO_CCY and AMOUNT:
        result = urllib.request.urlopen(f'https://www.google.com/search?q={AMOUNT}+{FROM_CCY}+to+{TO_CCY}&oq={AMOUNT}+{FROM_CCY}+to+{TO_CCY}');
        raw_text = str(result.read());
        matches = re.finditer(pattern, raw_text)
        for match in matches:
            start = match.start()
            end = raw_text.index('<',start)

            ret_val = raw_text[start + 28:end]
            print(ret_val)
        return func.HttpResponse(f"{ret_val}")
    else:
        return func.HttpResponse(
             "Pass from_ccy, to_ccy, and amount as parameters",
             status_code=200
        )
