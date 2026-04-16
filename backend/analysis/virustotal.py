import re
import requests
import os
from dotenv import load_dotenv

load_dotenv()


vt_api_key = os.getenv("VIRUSTOTAL_API_KEY ")

def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

def scan_urls(text):
    urls = extract_urls(text)
    results = []
    for url in urls:
        try:
            resp = requests.post(
                "https://www.virustotal.com/api/v3/urls",
                headers={"x-apikey": vt_api_key},
                data={"url": url},
                timeout=10
            )
            if resp.status_code == 200:
                results.append(resp.json())
            else:
                results.append({"error": f"VirusTotal API error: {resp.status_code}", "url": url})
        except Exception as e:
            results.append({"error": str(e), "url": url})
    return results