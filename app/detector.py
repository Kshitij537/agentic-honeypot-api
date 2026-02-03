def detect_scam(message: str) -> dict:
    message_lower = message.lower()

    best_match = None
    max_hits = 0

    SCAM_PATTERNS = {
        "upi_refund": [
            "refund", "upi", "reversal", "credited", "failed transaction"
        ],
        "kyc_update": [
            "kyc", "update kyc", "account suspended", "reactivate"
        ],
        "prize_lottery": [
            "lottery", "won", "winner", "prize", "congratulations"
        ],
        "bank_verification": [
            "verify", "bank account", "account blocked", "click link"
        ]
    }

    for scam_type, keywords in SCAM_PATTERNS.items():
        hits = sum(1 for kw in keywords if kw in message_lower)

        if hits > max_hits:
            max_hits = hits
            best_match = scam_type

    # No scam detected
    if max_hits < 2:
        return {
            "is_scam": False,
            "confidence": 0.1
        }

    # Confidence calculation
    confidence = min(0.5 + (0.1 * max_hits), 0.95)

    return {
        "is_scam": True,
        "scam_type": best_match or "generic_scam",
        "confidence": round(confidence, 2)
    }
