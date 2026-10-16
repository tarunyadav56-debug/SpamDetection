import streamlit as st
import joblib

model=joblib.load('spam_model.pkl')

st.set_page_config(layout='wide')

st.markdown("""
<style>
.banner {
    background: linear-gradient(90deg, #4aaaaa, #000000);
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    color: white;
    font-size: 35px;
    font-weight: bold;
    margin-bottom: 25px;
}
</style>

<div class="banner">
    Sentiment Analysis Project
</div>
""", unsafe_allow_html=True)

st.sidebar.image("flag.jpg")

st.sidebar.title("About us")
st.sidebar.text("We are developing ML projects based on NLP in LN AI Academy")

st.sidebar.title("About Project")
st.sidebar.text("This project predicts whether email is spam or not....")

st.sidebar.title("Contact us")
st.sidebar.text("+919717776422")

sample_review=st.selectbox("Sample Message",options=['Congratulations! Youve won a free iPhone. Click here to claim now!','Your account has been compromised. Verify your password immediately at this link','Thanks for your help with debugging the Streamlit code yesterday'])
if st.button("Predict", key="b1"):
    pred = model.predict([sample_review])
    prob = model.predict_proba([sample_review])
    if pred[0] == 1:
        st.error(f"🐞 Spam detected! ({prob[0][0]:.2f})")
    else:
        st.success(f"No Spam Email ({prob[0][1]:.2f})")
        st.snow()
        
sample_review2=st.text_input("Enter Message")
if st.button("Predict second", key="b2"):
    pred = model.predict([sample_review2])
    prob = model.predict_proba([sample_review2])
    if pred[0] == 1:
        st.error(f"🐞 Spam detected! ({prob[0][0]:.2f})")
    else:
        st.success(f"No Spam Email ({prob[0][1]:.2f})")
        st.snow()

