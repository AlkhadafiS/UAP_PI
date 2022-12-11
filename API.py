import requests, json

url = "https://cuaca-gempa-rest-api.vercel.app/"
gempa = "https://cuaca-gempa-rest-api.vercel.app/quake"
cuaca = "https://cuaca-gempa-rest-api.vercel.app/weather/"

class API_Gempa:
    def __init__(self, gempa):
        self.gempa = gempa

    def cariGempaTerkini(gempa):
        return gempa

class API_Cuaca_Kabupaten:

    def __init__(self, provinsi, kabupaten):
        self.provinsi = provinsi
        self.kabupaten = kabupaten

    def cariCuacaKabupaten(provinsi, kabupaten):
        hasilCuacaKabupaten = cuaca + provinsi + "/" + kabupaten
        hasilCuacaKabupaten = requests.get(hasilCuacaKabupaten)
        return hasilCuacaKabupaten

class API_Cuaca_Provinsi:
    def __init__(self, provinsi):
        self.provinsi = provinsi

    def cariCuacaProvinsi(provinsi):
        hasilCuacaProvinsi = cuaca + provinsi
        hasilCuacaProvinsi = requests.get(hasilCuacaProvinsi)
        return hasilCuacaProvinsi
