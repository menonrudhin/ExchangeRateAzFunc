from flask import Flask, request
import urllib.request
import re

app = Flask(__name__)
pattern = r'class="BNeawe iBp4i AP7Wnd">[0-9,]+.?[0-9]* [a-zA-Z ]+<\/div>'

# Converts from-currency to to-currency as per the current exchange rate (as per Google)
# Not intended for production usage
@app.route('/fx-rate')
def getFxRate():
    FROM_CCY=request.args.get('from_ccy')
    TO_CCY=request.args.get('to_ccy')
    AMOUNT=request.args.get('amount')

    result = urllib.request.urlopen(f'https://www.google.com/search?q={AMOUNT}+{FROM_CCY}+to+{TO_CCY}&oq={AMOUNT}+{FROM_CCY}+to+{TO_CCY}');

    raw_text = str(result.read());
    matches = re.finditer(pattern, raw_text)
    for match in matches:
        start = match.start()
        end = raw_text.index('<',start)

        ret_val = raw_text[start + 28:end]
        print(ret_val)

    return ret_val

if __name__ == '__main__':
    app.run()