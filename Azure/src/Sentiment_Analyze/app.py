import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()

# Carrega as variáveis do arquivo .env
endpoint = os.getenv('AZURE_ENDPOINT')
key = os.getenv('AZURE_KEY')

# Resto do seu código
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential= AzureKeyCredential(key))

documents = [
    "I love code",
    "I hate fail to code",
    "I love travel"
]



result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)

docs = [doc for doc in result if not doc.is_error]

for idx, doc in enumerate(docs):
    print(f"Documente Text: {documents[idx]}")
    print(f"overall sentiment: {doc.sentiment}")