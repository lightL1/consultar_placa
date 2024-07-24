import requests
import sys

# API Key (substitua pela sua chave de API se necessário)
API_KEY = "ab682c9f720ed1c86ccebc57c1ffecc9426fec18986e0a6a5d6e17eee6401974"
BASE_URL = "https://api-dh.ciphers.systems/api/v1/vehicle/plate/"

def consultar_placa(placa):
    response = requests.get(f"{BASE_URL}?plate={placa}&apikey={API_KEY}")

    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python placa.py <placa>")
        sys.exit(1)

    placa = sys.argv[1]
    resultado = consultar_placa(placa)

    if resultado is None:
        print(f"Não foi possível obter informações para a placa {placa}.")
    else:
        print("Informações do veículo:")
        print(resultado)
