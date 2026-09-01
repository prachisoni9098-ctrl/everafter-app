import streamlit as st
import random
import math

st.set_page_config(page_title="EverAfter App", page_icon="💘")
st.title("💘 EverAfter App")
st.write("Welcome Prachi! This is your live app dashboard.")

# Questions
QUESTIONS = [
    "Family Setup: I prefer living with a Joint Family rather than a Nuclear Setup.",
    "Location Choice: I want to settle in a Tier-1 Metro City in the future.",
    "Money Management: I believe in maintaining a shared investment pool with my partner.",
    "Conflict Resolution: When an argument happens, I prefer solving it immediately."
]

name1 = st.text_input("Partner 1 Name:")
name2 = st.text_input("Partner 2 Name:")

if name1 and name2:
    st.write("### Rate from 1 (Disagree) to 5 (Agree)")
    p1_ans = []
    p2_ans = []
    
    for idx, q in enumerate(QUESTIONS, 1):
        st.write(f"**Q{idx}. {q}**")
        p1_ans.append(st.slider(f"{name1}'s Rating", 1, 5, 3, key=f"p1_{idx}"))
        p2_ans.append(st.slider(f"{name2}'s Rating", 1, 5, 3, key=f"p2_{idx}"))
        st.write("")
        
    if st.button("Calculate Compatibility"):
        st.success("App Logic Running Successfully! We will add calculation details next.")
