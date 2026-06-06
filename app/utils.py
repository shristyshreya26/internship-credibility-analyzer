import re

urgency_words = [
    "urgent",
    "apply now",
    "limited",
    "immediately",
    "guaranteed",
    "fast hiring"
]

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def urgency_count(text):

    text = text.lower()

    return sum(
        word in text
        for word in urgency_words
    )

def capital_ratio(text):

    total_letters = sum(
        c.isalpha()
        for c in text
    )

    if total_letters == 0:
        return 0

    capital_letters = sum(
        c.isupper()
        for c in text
    )
    return capital_letters / total_letters
    
def extract_features(text):
    

    text_lower = text.lower()

    has_whatsapp_apply = int(
        "whatsapp" in text_lower
    )

    has_registration_fee = int(
        any(
            phrase in text_lower
            for phrase in [
                "registration fee",
                "application fee",
                "processing fee"
            ]
        )
    )

    has_company_email = int(
        "@" in text
    )

    has_duration_mentioned = int(
        any(
            phrase in text_lower
            for phrase in [
                "month",
                "months",
                "week",
                "weeks"
            ]
        )
    )

    has_no_interview = int(
        any(
            phrase in text_lower
            for phrase in [
                "no interview",
                "without interview"
            ]
        )
    )

    has_earn_daily = int(
        any(
            phrase in text_lower
            for phrase in [
                "earn daily",
                "daily earning",
                "daily income"
            ]
        )
    )

    text_length = len(text)

    return [
        has_whatsapp_apply,
        has_registration_fee,
        has_company_email,
        has_duration_mentioned,
        has_no_interview,
        has_earn_daily,
        text_length
    ]
    