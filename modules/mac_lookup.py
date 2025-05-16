def lookup(mac):
    vendor_prefix = mac.upper().replace(":", "")[:6]
    mac_vendors = {
        "00163E": "Apple Inc.",
        "3C5A37": "Samsung Electronics",
        "A4B197": "Huawei Technologies",
        "D850E6": "Intel Corporate",
        "FCF5C4": "Dell Inc."
    }
    return mac_vendors.get(vendor_prefix, "Unknown Vendor")
