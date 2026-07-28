import re

STATUS_KEYWORDS = {
    "Applied": [
        "application received",
        "thanks for applying",
        "application submitted",
        "received your application",
        "application has been received",
        "thank you for your application",
    ],

    "Interview": [
        "interview",
        "technical interview",
        "interview invitation",
        "technical round",
        "coding round",
        "online assessment",
        "assessment",
        "hackerrank",
        "schedule interview",
        "interview scheduled",
        "choose your slot",
        "next round",
        "virtual interview",
    ],

    "Selected": [
        "offer letter",
        "job offer",
        "offer accepted",
        "welcome aboard",
        "pleased to offer",
        "final selection",
        "you have been selected",
        "employment offer",
    ],

    "Rejected": [
        "unfortunately",
        "regret to inform",
        "application unsuccessful",
        "other candidates",
        "position has been filled",
        "unable to proceed",
        "not selected",
        "rejected",
    ]
}


def detect_status(text):

    text = text.lower()
    text = re.sub(r"\s+", " ", text)

    scores = {
        "Applied": 0,
        "Interview": 0,
        "Selected": 0,
        "Rejected": 0,
    }

    for status, keywords in STATUS_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                scores[status] += 1

    best_status = max(scores, key=scores.get)
    best_score = scores[best_status]

    if best_score == 0:
        return {
            "status": "Unknown",
            "confidence": 0,
            "scores": scores
        }

    confidence = round(best_score / sum(scores.values()) * 100)

    return {
        "status": best_status,
        "confidence": confidence,
        "scores": scores
    }


if __name__ == "__main__":

    email = """
    Congratulations!

    We are pleased to invite you to the Technical Interview.

    Please schedule your interview.
    """

    result = detect_status(email)

    print(result)