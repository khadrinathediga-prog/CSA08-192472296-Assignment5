
# B2 - Sentiment Analysis with Negation Handling

positive_words = {
    "good", "excellent", "clean", "safe", "fresh",
    "improved", "happy", "clear", "better"
}

negative_words = {
    "bad", "poor", "dirty", "unsafe", "polluted",
    "unhealthy", "angry", "worse", "terrible"
}

negation_words = {"not", "never", "no", "hardly"}


def sentiment_score(text):
    words = text.lower().replace(".", "").replace(",", "").split()

    score = 0
    negate_next = False

    for word in words:
        if word in negation_words:
            negate_next = not negate_next
            continue

        if word in positive_words:
            score += -1 if negate_next else 1
            negate_next = False

        elif word in negative_words:
            score += 1 if negate_next else -1
            negate_next = False

    if score > 0:
        return "Positive", score
    elif score < 0:
        return "Negative", score
    else:
        return "Neutral", score


# Test cases
complaints = [
    "The air quality is good",
    "The air quality is terrible",
    "The air is not good",
    "The air is not bad",
    "The air is not not good",
    "The city is clean but the air is polluted",
    "Great! Another day of terrible air quality",
    "The air quality is excellent and safe"
]

print("SENTIMENT ANALYSIS RESULTS\n")

for complaint in complaints:
    result, score = sentiment_score(complaint)

    print("Complaint:", complaint)
    print("Sentiment:", result)
    print("Score:", score)
    print("-" * 45)

print("\nSentiment testing completed!")
