import requests
from constants import bark_url


def send_notifications(message):
    requests.get(f"{bark_url}/{message}")
