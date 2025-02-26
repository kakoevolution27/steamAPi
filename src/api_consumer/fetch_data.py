from api_client import SteamApi
import pandas as pd
import json
import os
StmAPi = SteamApi()


game_names = StmAPi.get_app_id() 


game_names_json = json.dumps(game_names, indent=4, ensure_ascii=False) 

with open("game_names.json", "w", encoding="utf-8") as f:
    json.dump(game_names, f, indent=4, ensure_ascii=False)


