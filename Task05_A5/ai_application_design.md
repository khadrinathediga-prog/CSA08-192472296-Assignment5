# A5 – AI Application Design

## 1. Introduction

The City Air Quality Monitoring Network can use Artificial Intelligence (AI) and Natural Language Processing (NLP) to analyse citizen complaints, generate summaries, and answer questions about air-quality measurements.

Three AI-assisted features are proposed:

1. Sentiment analysis
2. Automatic text summarisation
3. Rule-based chatbot

## 2. Sentiment Analysis

### Objective

Classify citizen complaints into Positive, Negative, or Neutral categories.

### Proposed Algorithm

A lexicon-based approach assigns sentiment scores to words and handles simple negation.

**SIMATS-style Pseudocode**

```text
ALGORITHM Sentiment_Analysis(complaint)

BEGIN
    positive_words ← predefined positive vocabulary
    negative_words ← predefined negative vocabulary
    negation_words ← {not, never, no}

    score ← 0
    negate ← FALSE

    FOR each word IN complaint DO
        IF word is a negation word THEN
            negate ← NOT negate

        ELSE IF word is positive THEN
            IF negate THEN
                score ← score - 1
            ELSE
                score ← score + 1
            END IF
            negate ← FALSE

        ELSE IF word is negative THEN
            IF negate THEN
                score ← score + 1
            ELSE
                score ← score - 1
            END IF
            negate ← FALSE
        END IF
    END FOR

    IF score > 0 THEN
        RETURN Positive
    ELSE IF score < 0 THEN
        RETURN Negative
    ELSE
        RETURN Neutral
    END IF
END
```

## 3. Automatic Text Summarisation

### Objective

Generate short summaries from lengthy citizen complaints.

### Proposed Approach

Use extractive summarisation to select the most important sentences based on keyword frequency.

**Pseudocode**

```text
ALGORITHM Summarise_Complaint(text, k)

BEGIN
    sentences ← Split text into sentences
    words ← Extract meaningful words
    frequencies ← Count word frequencies

    FOR each sentence IN sentences DO
        score ← Sum frequencies of its meaningful words
        Store sentence and score
    END FOR

    selected ← Select top k scoring sentences
    Sort selected sentences by original position

    RETURN Join selected sentences
END
```

**Limitation:** Important information may be missed when sentences use uncommon words or complex language.

## 4. Rule-Based Chatbot

### Objective

Answer questions about monitoring stations and pollution readings.

### Proposed Approach

The chatbot identifies keywords and retrieves relevant information from the SQLite database.

**Pseudocode**

```text
ALGORITHM Air_Quality_Chatbot(question)

BEGIN
    question ← Convert question to lowercase
    station ← Identify requested station

    IF question contains "average PM2.5" THEN
        Execute parameterised SQL query
        RETURN average PM2.5 for station

    ELSE IF question contains "maximum PM10" THEN
        Execute parameterised SQL query
        RETURN maximum PM10 for station

    ELSE IF question contains "readings" THEN
        Execute parameterised SQL query
        RETURN number of readings

    ELSE
        RETURN "Sorry, I cannot answer this question."
    END IF
END
```

## 5. Alternative Approach: Machine Learning

Instead of predefined sentiment dictionaries and chatbot rules, a machine-learning or transformer-based NLP model could be used.

| Feature | Rule-Based Approach | Machine-Learning Approach |
|---|---|---|
| Implementation | Simple | More complex |
| Training data | Not required | Usually required |
| Interpretability | High | Varies |
| Sarcasm handling | Limited | Potentially better |
| Computational cost | Low | Potentially higher |
| Flexibility | Limited vocabulary and rules | Can generalise to varied language |

## 6. Limitations and Risks

- Sarcasm may be classified incorrectly.
- Double negatives and complex sentences can confuse simple sentiment rules.
- Extractive summaries may omit important details.
- Rule-based chatbots cannot answer questions outside their predefined rules.
- Incorrect or incomplete monitoring data can produce misleading responses.
- Parameterised SQL queries should be used to prevent SQL injection.
- Human review should be available for important or uncertain complaints.

## 7. Conclusion

A lexicon-based sentiment analyser, extractive summariser, and rule-based chatbot provide practical starting points for AI-assisted air-quality monitoring.

These methods are relatively simple and interpretable. More advanced NLP models may improve performance, but they require additional testing, resources, and evaluation.