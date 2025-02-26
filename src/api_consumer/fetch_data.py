from api_client import *
import pandas as pd
import json
import os
import time
#StmAPi = SteamApi()


#game_names = StmAPi.get_app_id() 


#game_names_json = json.dumps(game_names, indent=4, ensure_ascii=False) 

#with open("game_names.json", "w", encoding="utf-8") as f:
#   json.dump(game_names, f, indent=4, ensure_ascii=False)
StSAPI = SteamStoreAPI()



with open(r"C:\Users\kakoe\Desktop\steamAPi\data\game_names.json", "r", encoding="utf-8") as f:
    game_names = json.load(f)

rpm = 200  # Limite de requisições por minuto
req = 0  # Contador de requisições
batch = 1  # Contador de arquivos salvos
reqs = []  # Lista para armazenar os resultados

for item in game_names["applist"]["apps"]:
    app_id = item["appid"]
    response = StSAPI.get_game_details(app_id)
    req += 1
    reqs.append(response)

    # Controle de taxa de requisição
    if req == rpm:
        print(f"Aguardando 60 segundos... ({len(reqs)} requisições feitas)")
        time.sleep(60)
        req = 0  

    # Salva os dados a cada 5000 requisições
    if len(reqs) == 5000:
        file_path = rf"C:\Users\kakoe\Desktop\steamAPi\data\game_data_batch_{batch}.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(reqs, f, indent=4, ensure_ascii=False)

        print(f"Arquivo salvo: {file_path}")

        reqs = []  # Reseta a lista de requisições para o próximo lote
        batch += 1  # Incrementa o número do arquivo

# Salva os dados restantes (se houver menos de 5000 no final)
if reqs:
    file_path = rf"C:\Users\kakoe\Desktop\steamAPi\data\game_data_batch_{batch}.json"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(reqs, f, indent=4, ensure_ascii=False)

    print(f"Arquivo final salvo: {file_path}")


    
    

   


