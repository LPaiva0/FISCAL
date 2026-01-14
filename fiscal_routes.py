from flask import Blueprint, render_template, request, jsonify, send_file
import io
import base64

fiscal_bp = Blueprint('fiscal', __name__, template_folder='templates')

# --- MOCK SERVICE (Simula a API MeuDanfe) ---
class MeuDanfeMock:
    def adicionar_por_chave(self, chave):
        # Simula resposta de sucesso para qualquer chave de 44 dígitos
        return {'status': 'OK'}

    def download_pdf_por_chave(self, chave):
        # Gera um PDF fake em Base64 para demonstração
        pdf_demo = b"%PDF-1.4 %Mock PDF Content for Portfolio"
        return {'data': base64.b64encode(pdf_demo).decode('utf-8')}

    def download_xml_por_chave(self, chave):
        # Gera um XML fake para demonstração
        xml_demo = f"<nfeProc><chNFe>{chave}</chNFe><info>Mock XML</info></nfeProc>"
        return {'data': xml_demo}

danfe_service = MeuDanfeMock()

# --- ROTAS ---

@fiscal_bp.route('/fiscal/central_downloads')
def central_downloads():
    """Tela principal para inserção de chaves e download"""
    return render_template('Fiscal/CentralDownloadsFiscal.html')

@fiscal_bp.route('/fiscal/api/buscar_documento', methods=['POST'])
def buscar_documento_api():
    data = request.get_json()
    chave = data.get('chave', '')
    
    if not chave or len(chave) != 44:
        return jsonify({'sucesso': False, 'mensagem': 'Chave inválida (deve ter 44 dígitos)'}), 400

    try:
        resp = danfe_service.adicionar_por_chave(chave)
        status = resp.get('status')
        
        if status == 'OK':
            modelo = chave[20:22]
            tipo = "NF-e" if modelo == '55' else ("CT-e" if modelo == '57' else "Documento")
            return jsonify({'sucesso': True, 'tipo': tipo, 'status_api': status})
        return jsonify({'sucesso': False, 'mensagem': f'Status: {status}'})
    except Exception as e:
        return jsonify({'sucesso': False, 'mensagem': str(e)}), 500

@fiscal_bp.route('/fiscal/download/pdf/<chave>')
def download_pdf(chave):
    try:
        resp = danfe_service.download_pdf_por_chave(chave)
        pdf_bin = base64.b64decode(resp['data'])
        return send_file(
            io.BytesIO(pdf_bin),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f"{chave}.pdf"
        )
    except Exception as e:
        return f"Erro ao gerar PDF: {e}", 500

@fiscal_bp.route('/fiscal/download/xml/<chave>')
def download_xml(chave):
    try:
        resp = danfe_service.download_xml_por_chave(chave)
        xml_str = resp['data']
        return send_file(
            io.BytesIO(xml_str.encode('utf-8')),
            mimetype='text/xml',
            as_attachment=True,
            download_name=f"{chave}.xml"
        )
    except Exception as e:
        return f"Erro ao gerar XML: {e}", 500
