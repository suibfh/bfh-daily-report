import requests
import json
from datetime import datetime

url = "https://api.exchangerate.host/latest?base=USD&symbols=JPY"

try:
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    jpy = data["rates"]["JPY"]
    output = {
        "date": datetime.utcnow().isoformat() + "Z",
        "rate": round(jpy, 4)
    }

    with open("usd_jpy.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("✅ 取得成功:", output)

except Exception as e:
    print("❌ 為替取得に失敗しました:", e)
    exit(1)
