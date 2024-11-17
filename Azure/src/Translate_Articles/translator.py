import requests

def translate_text(text, source_language, target_language, endpoint, key):
    """
    Traduz um texto utilizando a API do Azure Translator Text.

    Args:
        text (str): Texto a ser traduzido.
        source_language (str): Código do idioma de origem.
        target_language (str): Código do idioma de destino.
        endpoint (str): Endpoint da API do Azure Translator Text.
        key (str): Chave de acesso da API.

    Returns:
        str: Texto traduzido.
    """

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Content-Type': 'application/json'
    }

    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': target_language
    }

    body = [{'text': text}]

    try:
        response = requests.post(endpoint, headers=headers, params=params, json=body)
        response.raise_for_status()
        return response.json()[0]['translations'][0]['text']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao traduzir: {e}")
        return None