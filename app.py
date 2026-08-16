import streamlit as st
from transformers import pipeline


st.set_page_config(
    page_title="Caribou Review Analyzer",
    page_icon="☕"
)

st.title("☕ Caribou Juffair Review Analyzer")
st.write("Analyze an English or Arabic customer review.")


@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="cardiffnlp/twitter-xlm-roberta-base-sentiment"
    )


review = st.text_area(
    "Enter a review",
    placeholder="The coffee was excellent. / القهوة ممتازة"
)


if st.button("Analyze Review"):

    if review.strip() == "":
        st.warning("Please enter a review first.")

    else:
        with st.spinner("Analyzing the review..."):
            pipe = load_model()
            result = pipe([review])[0]

        label = result["label"].capitalize()
        score = result["score"]

        custom_result = {
            "label": label,
            "score": score,
            "metadata": "huggingface_AI_model"
        }

        st.subheader("Prediction")

        if label == "Positive":
            st.success("Positive")
        elif label == "Negative":
            st.error("Negative")
        else:
            st.info("Neutral")

        st.write("Confidence:", f"{score:.2%}")

        st.subheader("Required Output Structure")
        st.write(custom_result)


st.divider()
st.caption(
    "Pretrained model: cardiffnlp/twitter-xlm-roberta-base-sentiment"
)
