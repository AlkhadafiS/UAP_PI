import json, requests

url = "https://cuaca-gempa-rest-api.vercel.app/"
gempa = "https://cuaca-gempa-rest-api.vercel.app/quake"
cuaca = "https://cuaca-gempa-rest-api.vercel.app/weather/"

class API_Class:
    def __init__(self, url):
        self.url = url

    API_Success = requests.get(url).json()

    def cariGempaTerkini(self):
        hasilGempaTerkini = requests.get(gempa).json()
        return hasilGempaTerkini

    def cariCuacaKabupaten(self, provinsi, kabupaten):
        hasilCuacaKabupaten = requests.get(cuaca + provinsi + "/" + kabupaten).json()
        return hasilCuacaKabupaten

    def cariCuacaProvinsi(self, provinsi):
        hasilCuacaProvinsi = requests.get(cuaca + provinsi).json()
        return hasilCuacaProvinsi
