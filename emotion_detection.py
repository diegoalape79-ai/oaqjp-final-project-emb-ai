"""
Módulo para realizar detección de emociones usando Watson NLP.
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Ejecuta la detección de emociones sobre el texto recibido.

    Args:
        text_to_analyze (str): Texto que será analizado.

    Returns:
        str: Respuesta en formato texto recibida desde el servicio Watson NLP.
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    return response.text