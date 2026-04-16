import requests
import os
from dotenv import load_dotenv


load_dotenv()

mx_api = os.getenv("MXTOOLBOX_API_KEY")

def check_domain(domain):
    # Use the 'mx' command for MX lookup as an example
    url = f"https://api.mxtoolbox.com/api/v1/lookup/mx/?argument={domain}"
    headers = {"Authorization": mx_api}
    resp = requests.get(url, headers=headers)
    try:
        return resp.json()
    except Exception as e:
        return {"error": str(e), "status_code": resp.status_code, "text": resp.text}