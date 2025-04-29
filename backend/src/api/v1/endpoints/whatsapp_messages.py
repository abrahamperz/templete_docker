import json
import logging
from dotenv import load_dotenv
import os
import requests
from fastapi import APIRouter, HTTPException

logger = logging.getLogger(__name__)

router = APIRouter()

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
RECIPIENT_WAID = os.getenv("RECIPIENT_WAID")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERSION = os.getenv("VERSION")


@router.post("/send-whatsapp-template/")
def send_whatsapp_template():
    """
    Send a WhatsApp template message.
    """
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN,
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_WAID,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        logger.error(f"Error sending template message: {response.json()}")
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()


def get_text_message_input(recipient, text):
    """
    Format the body of a custom text message for WhatsApp.
    """
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )


@router.post("/send-whatsapp-text/")
def send_whatsapp_text(recipient: str, text: str):
    """
    Send a custom text message synchronously via WhatsApp.
    """
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    data = get_text_message_input(recipient, text)
    response = requests.post(url, data=data, headers=headers)
    if response.status_code != 200:
        logger.error(f"Error sending custom text message: {response.json()}")
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()


@router.post("/send-whatsapp-sync/")
def send_whatsapp_sync(recipient: str, text: str):
    """
    Send a custom text message synchronously via WhatsApp.
    """
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    data = json.loads(get_text_message_input(recipient, text))
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            logger.error(f"Error sending synchronous custom text message: {response.json()}")
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Connection error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Connection Error: {str(e)}")
