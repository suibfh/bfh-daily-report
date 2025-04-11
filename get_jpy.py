import requests
import json
from datetime import datetime

APP_ID = "fe65b781026b40a3b884b042fbcfca66"  # ←あなたのApp ID

url = f"https://openexchangerates.org/api/latest.json?app_id={APP_ID}&symbols=JPY"

try:
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()

    if "rates" in data and "JPY" in data["rates"]:
        jpy = data["rates"]["JPY"]
        output = {
            "date": datetime.utcnow().isoformat() + "Z",
            "rate": round(jpy, 4),
            "source": "openexchangerates.org"
        }
        print("✅ 為替取得成功:", output)
    else:
        output = {
            "date": datetime.utcnow().isoformat() + "Z",
            "rate": None,
            "error": "JPY not found in response"
        }
        print("⚠️ JPYレートが取得できませんでした。")

    with open("usd_jpy.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

except Exception as e:
    print("❌ 為替取得に失敗しました:", e)
    exit(1)
