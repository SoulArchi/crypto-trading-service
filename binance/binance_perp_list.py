import requests

# Binance 선물 마켓 정보 가져오기
url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
res = requests.get(url).json()

# USDT 무기한 선물 심볼 필터링
usdt_perp_symbols = [
    s["symbol"] for s in res["symbols"]
    if s["contractType"] == "PERPETUAL" and s["quoteAsset"] == "USDT"
]

# 텍스트 파일로 저장
with open("usdt_perp_symbols.txt", "w") as f:
    for symbol in usdt_perp_symbols:
        f.write("BINANCE:" + symbol + "PERP\n")
