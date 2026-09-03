import json
with open("out.json", encoding="utf-8") as f:
    data = json.load(f)

import pandas as pd
df = pd.read_json("out.json")
