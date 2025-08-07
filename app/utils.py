import re


def normalize_persian(text):
    """
    نرمال‌سازی متن فارسی
    """
    if not isinstance(text, str):
        return text

    text = text.replace("ي", "ی").replace("ك", "ک")
    text = re.sub(r"[\u064B-\u065F]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text