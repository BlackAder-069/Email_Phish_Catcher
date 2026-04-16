from fastapi import FastAPI
import requests
import re
from analysis.virustotal import scan_urls
from analysis.mxtoolbox import check_domain
from analysis.yara_scan import yara_match

MAILHOG_API = "http://localhost:8025/api/v2/messages"

app = FastAPI()

@app.get("/analyze")
def analyze_emails():
    resp = requests.get(MAILHOG_API)
    emails = resp.json().get("items", [])
    results = []
    for email in emails:
        content = email['Content']['Body']
        urls = re.findall(r'https?://[^\s]+', content)  # Extract URLs directly here
        vt_results = scan_urls(content)  # Scan all URLs in the email body at once
        domains = [url.split('/')[2] for url in urls if '://' in url]
        mx_results = [check_domain(domain) for domain in domains]
        yara_results = yara_match(content)
        results.append({
            "subject": email['Content']['Headers'].get('Subject', [''])[0],
            "urls": urls,
            "virustotal": vt_results,
            "mxtoolbox": mx_results,
            "yara": yara_results
        })
    return results