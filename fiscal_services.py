import base64
import os
import requests

class MeuDanfeAPI:
    """Integração com a API v2 do Meu Danfe (com Modo de Demonstração para Portfólio)"""
    BASE_URL = "https://api.meudanfe.com.br/v2"

    def __init__(self):
        self.api_key = os.getenv('API_KEY_MEU_DANFE', '')
        # Se não houver chave, o sistema opera em modo MOCK para o GitHub
        self.is_demo = not self.api_key
        
        self.headers = {
            "Api-Key": self.api_key,
            "Accept": "application/json"
        }

    def adicionar_por_chave(self, chave_acesso):
        if self.is_demo:
            return {'status': 'OK'} # Simula sucesso no GitHub
            
        url = f"{self.BASE_URL}/fd/add/{chave_acesso}"
        response = requests.put(url, headers=self.headers, timeout=10)
        return response.json()

    def download_pdf_por_chave(self, chave_acesso):
        if self.is_demo:
            # Retorna um PDF fake em Base64 para demonstração
            pdf_fake = b"%PDF-1.4 %Conteudo Simulado para Portfolio"
            return {'data': base64.b64encode(pdf_fake).decode('utf-8')}

        url = f"{self.BASE_URL}/fd/get/da/{chave_acesso}"
        response = requests.get(url, headers=self.headers, timeout=15)
        return response.json()

    def download_xml_por_chave(self, chave_acesso):
        if self.is_demo:
            # Retorna um XML fake para demonstração
            xml_fake = f"<nfe><chNFe>{chave_acesso}</chNFe><status>MOCK</status></nfe>"
            return {'data': xml_fake}

        url = f"{self.BASE_URL}/fd/get/xml/{chave_acesso}"
        response = requests.get(url, headers=self.headers, timeout=15)
        return response.json()
