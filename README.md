# Caribou Juffair Review Analyzer

This project was created for the Pretrained Model Challenge lab. It uses pretrained Hugging Face models to analyze reviews related to Caribou Coffee on Al Shabab Avenue in Juffair, Bahrain.

## Problem Definition

The purpose of this project is to analyze customer reviews and identify whether each review is Positive, Neutral, or Negative.

The application can process both English and Arabic reviews.

## Dataset

The evaluation dataset contains 60 manually labeled review samples.

Each review includes:

- Review text
- Human sentiment label
- Topic label
- Evaluation rating
- Language
- Source information

The sentiment classes are:

- Positive
- Neutral
- Negative

The topic classes are:

- Drink Quality
- Service
- Atmosphere
- Price
- Cleanliness
- Location
- Waiting Time

## Pretrained Models

The main sentiment model is:

`cardiffnlp/twitter-xlm-roberta-base-sentiment`

This is the same multilingual model demonstrated in the tutor exercise. It supports English and Arabic sentiment analysis.

Two additional sentiment models were evaluated in the notebook:

- `lxyuan/distilbert-base-multilingual-cased-sentiments-student`
- `finiteautomata/bertweet-base-sentiment-analysis`

The project also uses:

- `facebook/bart-large-mnli` for zero-shot topic classification
- `sshleifer/distilbart-cnn-12-6` for summarization

## Model Output

The Streamlit application returns:

- Sentiment label
- Confidence score
- Required metadata

Example:

```python
{
    "label": "Positive",
    "score": 0.95,
    "metadata": "huggingface_AI_model"
}
