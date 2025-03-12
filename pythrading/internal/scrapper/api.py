import requests

url = "https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw"
response = requests.get(url)

import json
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

class KorbitResponse:
    def __init__(self, response_data):
        self.timestamp = response_data.get('timestamp')
        self.last = float(response_data.get('last', 0))
        self.open = float(response_data.get('open', 0)) 
        self.bid = float(response_data.get('bid', 0))
        self.ask = float(response_data.get('ask', 0))
        self.low = float(response_data.get('low', 0))
        self.high = float(response_data.get('high', 0))
        self.volume = float(response_data.get('volume', 0))
        
korbit_data = KorbitResponse(response.json())
print(f"타임스탬프: {korbit_data.timestamp}")
print(f"현재가: {korbit_data.last}")
print(f"시가: {korbit_data.open}")
print(f"매수가: {korbit_data.bid}")
print(f"매도가: {korbit_data.ask}")
print(f"최저가: {korbit_data.low}")
print(f"최고가: {korbit_data.high}")
print(f"거래량: {korbit_data.volume}")
