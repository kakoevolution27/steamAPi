import requests

class APIClient:
    #Cliente genérico para requisições a APIs
    def __init__(self,base_url,headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, endpoint,params=None):
        response = requests.get(f'{self.base_url}{endpoint}', params=params,headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=data,headers=self.headers)
        response.raise_for_status()
        return response.json()
    
class SteamAPI(APIClient):
    #Cliente especializado para consumir a API steam
    def __init__(self, api_key:str):
        super().__init__("https://store.steampowered.com/")
        self.api_key = api_key

    def get_game_details(self, app_id:int):
        return self.get(f"api/appdetails?appids={app_id}")
    
    def get_game_reviews(self, app_id:int,language:str,num_per_pages:int):
        return self.get(f"appreviews/{app_id}?json=1&language={language}&num_per_page={num_per_pages}")
    
    