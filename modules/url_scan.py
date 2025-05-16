import requests
import base64

API_KEY = "20933dda496d6c6dfae3f617d5180cc0394b174d228fa29f4339154145cf99ab"
API_URL = "https://www.virustotal.com/api/v3/urls"

def scan(url):
    headers = {
        "x-apikey": API_KEY,
        "content-type": "application/x-www-form-urlencoded"
    }

    data = f"url={url}"
    response = requests.post(API_URL, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        url_id = result["data"]["id"]

        # Get scan report
        report_url = f"https://www.virustotal.com/api/v3/analyses/{url_id}"
        report_response = requests.get(report_url, headers=headers)

        if report_response.status_code == 200:
            analysis = report_response.json()
            stats = analysis["data"]["attributes"]["stats"]
            return {
                "malicious": stats["malicious"],
                "suspicious": stats["suspicious"],
                "harmless": stats["harmless"],
                "undetected": stats["undetected"]
            }
        else:
            return f"Failed to retrieve scan report: {report_response.status_code}"
    else:
        return f"Failed to submit URL: {response.status_code} - {response.text}"
