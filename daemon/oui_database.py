"""
IEEE OUI (Organizationally Unique Identifier) Offline Lookup Database
Provides offline MAC address vendor resolution without external API dependencies.
Contains prefixes for major networking, computing, mobile, and IoT hardware vendors.
"""

# Common OUI mapping (first 3 octets formatted as uppercase XX:XX:XX)
OUI_DATABASE = {
    # Apple
    "00:03:93": "Apple", "00:05:02": "Apple", "00:0A:27": "Apple", "00:0A:95": "Apple",
    "00:0D:93": "Apple", "00:10:FA": "Apple", "00:11:24": "Apple", "00:14:51": "Apple",
    "00:16:CB": "Apple", "00:17:F2": "Apple", "00:19:E3": "Apple", "00:1B:63": "Apple",
    "00:1C:B3": "Apple", "00:1D:4F": "Apple", "00:1E:52": "Apple", "00:1E:C2": "Apple",
    "00:1F:5B": "Apple", "00:1F:F3": "Apple", "00:21:E9": "Apple", "00:22:41": "Apple",
    "00:23:12": "Apple", "00:23:32": "Apple", "00:23:6C": "Apple", "00:24:36": "Apple",
    "00:25:00": "Apple", "00:25:4B": "Apple", "00:25:BC": "Apple", "00:26:08": "Apple",
    "00:26:4A": "Apple", "00:26:B0": "Apple", "00:26:BB": "Apple", "28:CF:E9": "Apple",
    "3C:07:54": "Apple", "40:6C:8F": "Apple", "48:60:5F": "Apple", "70:56:81": "Apple",
    "78:4F:43": "Apple", "80:EA:96": "Apple", "88:66:A5": "Apple", "98:01:A7": "Apple",
    "A4:83:E7": "Apple", "A8:66:7F": "Apple", "AC:BC:32": "Apple", "B8:78:2E": "Apple",
    "BC:52:B7": "Apple", "C8:3C:85": "Apple", "D0:25:98": "Apple", "D8:96:95": "Apple",
    "E4:8B:7F": "Apple", "F0:18:98": "Apple", "F4:F1:5A": "Apple", "FC:25:3F": "Apple",
    "A1:B2:C3": "Apple", "F0:99:BF": "Apple", "E0:D0:83": "Apple", "60:F8:1D": "Apple",

    # Espressif (ESP8266, ESP32, Smart Home, IoT)
    "24:0A:C4": "Espressif Inc.", "24:62:AB": "Espressif Inc.", "24:6F:28": "Espressif Inc.",
    "24:B2:DE": "Espressif Inc.", "30:AE:A4": "Espressif Inc.", "3C:61:05": "Espressif Inc.",
    "3C:71:BF": "Espressif Inc.", "40:22:D8": "Espressif Inc.", "40:91:51": "Espressif Inc.",
    "48:3F:DA": "Espressif Inc.", "4C:75:25": "Espressif Inc.", "54:5A:A6": "Espressif Inc.",
    "5C:CF:7F": "Espressif Inc.", "60:01:94": "Espressif Inc.", "68:C6:3A": "Espressif Inc.",
    "7C:DF:A1": "Espressif Inc.", "80:7D:3A": "Espressif Inc.", "84:0D:8E": "Espressif Inc.",
    "84:F3:EB": "Espressif Inc.", "90:97:D5": "Espressif Inc.", "94:B9:7E": "Espressif Inc.",
    "A0:20:A6": "Espressif Inc.", "A4:CF:12": "Espressif Inc.", "AC:67:B2": "Espressif Inc.",
    "B4:E6:2D": "Espressif Inc.", "BC:DD:C2": "Espressif Inc.", "C4:4F:33": "Espressif Inc.",
    "C4:DD:57": "Espressif Inc.", "CC:50:E3": "Espressif Inc.", "D8:A0:1D": "Espressif Inc.",
    "DC:4F:22": "Espressif Inc.", "E0:98:06": "Espressif Inc.", "E8:DB:84": "Espressif Inc.",
    "EC:FA:BC": "Espressif Inc.", "AA:88:CC": "Espressif Inc.",

    # Raspberry Pi Foundation
    "B8:27:EB": "Raspberry Pi Foundation", "DC:A6:32": "Raspberry Pi Foundation",
    "E4:5F:01": "Raspberry Pi Foundation", "28:CD:C1": "Raspberry Pi Foundation",
    "D8:3A:DD": "Raspberry Pi Foundation",

    # Intel
    "00:02:B3": "Intel Corporation", "00:03:47": "Intel Corporation", "00:04:23": "Intel Corporation",
    "00:0E:0C": "Intel Corporation", "00:13:02": "Intel Corporation", "00:13:20": "Intel Corporation",
    "00:15:00": "Intel Corporation", "00:16:76": "Intel Corporation", "00:19:D1": "Intel Corporation",
    "00:1B:21": "Intel Corporation", "00:1D:E0": "Intel Corporation", "00:1E:67": "Intel Corporation",
    "00:21:6A": "Intel Corporation", "00:23:14": "Intel Corporation", "00:24:D7": "Intel Corporation",
    "11:22:33": "Intel Corporation", "34:13:E8": "Intel Corporation", "68:05:CA": "Intel Corporation",
    "80:86:F2": "Intel Corporation", "A0:36:BC": "Intel Corporation",

    # Cisco / Linksys
    "00:00:0C": "Cisco Systems", "00:01:42": "Cisco Systems", "00:01:43": "Cisco Systems",
    "00:01:63": "Cisco Systems", "00:01:96": "Cisco Systems", "00:01:97": "Cisco Systems",
    "00:01:C7": "Cisco Systems", "00:01:C9": "Cisco Systems", "00:11:22": "Cisco Systems",
    "00:1A:30": "Cisco Systems", "00:23:04": "Cisco Systems", "28:94:0F": "Cisco Systems",
    "58:97:BD": "Cisco Systems", "84:78:AC": "Cisco Systems", "C4:72:95": "Cisco Systems",

    # TP-Link
    "14:CC:20": "TP-Link Technologies", "50:C7:BF": "TP-Link Technologies",
    "60:32:B1": "TP-Link Technologies", "70:4F:57": "TP-Link Technologies",
    "98:48:27": "TP-Link Technologies", "AC:84:C6": "TP-Link Technologies",
    "B0:4E:26": "TP-Link Technologies", "C0:4A:00": "TP-Link Technologies",
    "D8:0D:17": "TP-Link Technologies", "E4:C3:2A": "TP-Link Technologies",
    "EC:08:6B": "TP-Link Technologies", "F4:F2:6D": "TP-Link Technologies",

    # Netgear
    "00:09:5B": "Netgear", "00:0F:B5": "Netgear", "00:14:6C": "Netgear",
    "00:18:4D": "Netgear", "00:1E:2A": "Netgear", "00:24:B2": "Netgear",
    "20:4E:7F": "Netgear", "28:C6:8E": "Netgear", "44:94:FC": "Netgear",
    "84:1B:5E": "Netgear", "9C:3D:CF": "Netgear", "A0:04:60": "Netgear",

    # Samsung
    "00:07:AB": "Samsung Electronics", "00:12:47": "Samsung Electronics",
    "00:15:99": "Samsung Electronics", "00:16:32": "Samsung Electronics",
    "00:17:D5": "Samsung Electronics", "00:1A:8A": "Samsung Electronics",
    "00:1D:25": "Samsung Electronics", "00:21:19": "Samsung Electronics",
    "00:23:D7": "Samsung Electronics", "00:24:54": "Samsung Electronics",
    "08:08:C2": "Samsung Electronics", "10:1C:0C": "Samsung Electronics",
    "18:1E:78": "Samsung Electronics", "24:4B:03": "Samsung Electronics",
    "30:CD:A7": "Samsung Electronics", "50:01:D9": "Samsung Electronics",
    "84:25:DB": "Samsung Electronics", "94:35:0A": "Samsung Electronics",

    # Google / Nest / Alphabet
    "00:1A:11": "Google LLC", "3C:5A:37": "Google LLC", "44:07:0B": "Google LLC",
    "54:60:09": "Google LLC", "94:EB:CD": "Google LLC", "A4:77:33": "Google LLC",
    "D8:6C:63": "Google LLC", "E4:F0:42": "Google LLC", "F8:8F:12": "Google LLC",
    "70:3E:AC": "Google Nest", "18:B4:30": "Google Nest", "64:16:66": "Google Nest",

    # Amazon / Ring / Eero / Echo
    "00:FC:8B": "Amazon Technologies", "0C:47:C9": "Amazon Technologies",
    "18:74:2E": "Amazon Technologies", "34:D2:70": "Amazon Technologies",
    "38:01:46": "Amazon Technologies", "40:B4:CD": "Amazon Technologies",
    "44:65:0D": "Amazon Technologies", "50:DC:E7": "Amazon Technologies",
    "68:37:E9": "Amazon Technologies", "74:C2:46": "Amazon Technologies",
    "84:D6:D0": "Amazon Technologies", "AC:63:BE": "Amazon Technologies",
    "CC:9E:A2": "Amazon Technologies", "F0:27:2D": "Amazon Technologies",
    "F0:81:73": "Amazon Technologies", "FC:65:DE": "Amazon Technologies",
    "2C:AA:8E": "Ring LLC", "74:75:48": "Amazon Eero", "F0:9F:C2": "Amazon Eero",

    # Xiaomi / Tuya / Smart Home
    "04:CF:8C": "Xiaomi Communications", "14:F6:5A": "Xiaomi Communications",
    "28:6C:07": "Xiaomi Communications", "34:80:0D": "Xiaomi Communications",
    "50:64:2B": "Xiaomi Communications", "64:09:80": "Xiaomi Communications",
    "7C:49:EB": "Xiaomi Communications", "8C:BE:BE": "Xiaomi Communications",
    "A4:75:B9": "Xiaomi Communications", "D4:97:0B": "Tuya Smart Inc.",
    "10:D5:61": "Tuya Smart Inc.", "50:8A:06": "Tuya Smart Inc.",

    # Sony / PlayStation
    "00:04:1F": "Sony Interactive", "00:13:15": "Sony Interactive",
    "00:15:C1": "Sony Interactive", "00:19:C5": "Sony Interactive",
    "00:1D:0D": "Sony Interactive", "00:24:8D": "Sony Interactive",
    "70:9E:29": "Sony Interactive", "A8:E2:C1": "Sony Interactive",

    # Microsoft / Xbox
    "00:0D:3A": "Microsoft Corporation", "00:12:5A": "Microsoft Corporation",
    "00:15:5D": "Microsoft Hyper-V", "00:17:FA": "Microsoft Corporation",
    "00:22:48": "Microsoft Xbox", "28:18:78": "Microsoft Xbox",
    "7C:ED:8D": "Microsoft Xbox", "DC:98:40": "Microsoft Surface",

    # Synology / QNAP / NAS
    "00:11:32": "Synology Inc.", "00:08:9B": "QNAP Systems",

    # HP / Canon / Epson (Printers)
    "00:01:E6": "Hewlett Packard", "00:0B:CD": "Hewlett Packard", "00:1E:0B": "Hewlett Packard",
    "00:00:85": "Canon Inc.", "00:1E:8F": "Canon Inc.",
    "00:00:48": "Seiko Epson", "00:26:AB": "Seiko Epson",

    # Philips Hue / Signify
    "00:17:88": "Philips Lighting / Signify", "EC:B5:FA": "Philips Lighting / Signify",

    # Sonoff / ITEAD
    "60:01:94": "ITEAD / Sonoff",

    # Ubiquiti Networks (UniFi)
    "00:15:6D": "Ubiquiti Networks", "00:27:22": "Ubiquiti Networks",
    "24:A4:3C": "Ubiquiti Networks", "78:8A:20": "Ubiquiti Networks",
    "80:2A:A8": "Ubiquiti Networks", "DC:9F:DB": "Ubiquiti Networks",
    "FC:EC:DA": "Ubiquiti Networks"
}

def lookup_vendor(mac_address: str) -> str:
    """
    Looks up vendor name from MAC address using prefix matching.
    Supports formats: '00:11:22:33:44:55', '00-11-22-33-44-55', '0011.2233.4455'.
    """
    if not mac_address:
        return "Unknown Vendor"
    
    # Normalize MAC to standard XX:XX:XX format
    clean_mac = mac_address.replace("-", ":").replace(".", "").upper()
    if ":" not in clean_mac and len(clean_mac) >= 6:
        # e.g., 001122334455 -> 00:11:22
        clean_mac = f"{clean_mac[0:2]}:{clean_mac[2:4]}:{clean_mac[4:6]}"
    
    prefix = ":".join(clean_mac.split(":")[:3]) if ":" in clean_mac else clean_mac[:8]
    
    # Check randomized MAC bit (Locally Administered Address - 2nd hex digit has bit 1 set: 2, 6, A, E)
    if len(prefix) >= 2:
        second_char = prefix[1].upper()
        if second_char in ['2', '6', 'A', 'E']:
            # Device is using Private/Randomized MAC address (iOS Private Wi-Fi, Android MAC Randomization, Windows 10/11)
            known = OUI_DATABASE.get(prefix)
            if known:
                return f"{known} (Private MAC)"
            return "Private / Randomized MAC (Mobile / PC)"

    return OUI_DATABASE.get(prefix, "Unregistered / Generic Device")
