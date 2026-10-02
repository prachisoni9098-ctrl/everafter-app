import streamlit as st
import random
import math

# Page Setup
st.set_page_config(page_title="EverAfter Premium", page_icon="💘")
st.title("💘 EverAfter: The Ultimate Life Planner")
st.markdown("### Sem-3 Practical & Core Logic Engine")
st.write("---")

# 1. USER PROFILE SECTION
st.subheader("👤 User Profiles")
col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("Partner 1 Name:", placeholder="e.g., Prachi")
    love_lang1 = st.selectbox("Partner 1 Love Language:", ["Quality Time", "Words of Appreciation", "Acts of Service", "Receiving Gifts"])
with col2:
    name2 = st.text_input("Partner 2 Name:", placeholder="e.g., Rahul")
    love_lang2 = st.selectbox("Partner 2 Love Language:", ["Quality Time", "Words of Appreciation", "Acts of Service", "Receiving Gifts"])

# 2. CORE QUESTIONS
st.write("---")
st.subheader("📝 Core Lifestyle Matrix")
q1 = st.slider("I prefer living with a Joint Family rather than a Nuclear Setup. (1-5)", 1, 5, 3)
q2 = st.slider("When an argument happens, I prefer solving it immediately. (1-5)", 1, 5, 3)

if st.button("Calculate Core Analytics", type="primary"):
    # Statistical Calculation (Distance Math)
    diff = ((q1 - q2) ** 2)
    compatibility = round((1 - (math.sqrt(diff) / 4)) * 100, 2)
    
    st.write("---")
    st.success(f"🎯 Core Compatibility Index: **{compatibility}%**")
    
    # 🌟 NEW FEATURE: DYNAMIC LOVE LANGUAGE LOGIC
    st.subheader("❤️ Love Language Alignment Report")
    if love_lang1 == love_lang2:
        st.balloons() # Throws balloons on screen
        st.info(f"✨ Perfect Emotional Sync! Both value **{love_lang1}**. This reduces relationship friction by 40%.")
    else:
        st.warning(f"💡 Emotional Duality Detected! {name1} values **{love_lang1}** while {name2} values **{love_lang2}**.")
        st.write("👉 **Data Science Tip:** Make an active effort to speak your partner's emotional language to avoid communication gaps!")
