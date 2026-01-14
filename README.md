Central de Documentos Fiscais (Microsserviço)
Este projeto é um microsserviço independente desenvolvido em Python/Flask para a recuperação automática de documentos fiscais eletrônicos (NF-e e CT-e). Ele integra-se à API do Meu Danfe para buscar e converter dados brutos em arquivos prontos para o usuário.

Objetivo
Facilitar a rotina de departamentos fiscais e logísticos, permitindo o download imediato do arquivo XML (para entrada no ERP) e do PDF (para impressão/conferência) apenas com a chave de acesso de 44 dígitos, eliminando a necessidade de navegação manual em portais governamentais.

Funcionalidades Principais
Integração REST API: Consumo de endpoints para inclusão e recuperação de documentos em tempo real.

Detecção Automática de Modelo: Lógica de parsing que identifica se a chave pertence a uma NF-e ou CT-e com base nos dígitos estruturais.

Processamento de Binários: Conversão de dados codificados em Base64 para arquivos de download físico via io.BytesIO.

Modo de Demonstração (Mock): O sistema detecta a ausência de chaves de API e entra automaticamente em modo Sandbox, permitindo que qualquer pessoa teste o fluxo de download sem custos ou configurações complexas.

Tecnologias Utilizadas
Backend: Python 3.13 / Flask.

Frontend: HTML5, CSS3, Bootstrap 5 e Font Awesome.

Comunicação: Biblioteca requests para chamadas HTTP.

Arquitetura: Modularização por Blueprints e Herança de Templates (Jinja2).

Como Executar
Clone o repositório:

git clone https://github.com/LPaiva0/FISCAL.git
cd FISCAL

Instale as dependências:

pip install -r requirements.txt
Rode o aplicativo:

python app.py
Acesse no navegador: http://127.0.0.1:5000

Configuração
Para utilizar o serviço real em produção, renomeie o arquivo .env.example para .env e insira sua credencial:

Snippet de código

API_KEY_MEU_DANFE=sua_chave_aqui
Caso não configure a chave, o sistema funcionará em Modo Demo.
