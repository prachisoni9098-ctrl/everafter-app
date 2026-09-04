import streamlit as st
import random
import math

# Page Configurations
st.set_page_config(page_title="EverAfter App", page_icon="💘")
st.title("💘 EverAfter App")
st.markdown("### Gen-Z & Millennial Relationship Data Engine")
st.write("Welcome Prachi! This is your live app dashboard.")
st.write("---")

# Questions List
QUESTIONS = [
    "Family Setup: I prefer living with a Joint Family rather than a Nuclear Setup.",
    "Location Choice: I want to settle in a Tier-1 Metro City in the future.",
    "Money Management: I believe in maintaining a shared investment pool with my partner.",
    "Conflict Resolution: When an argument happens, I prefer solving it immediately."
]

name1 = st.text_input("Partner 1 Name:", placeholder="e.g., Prachi")
name2 = st.text_input("Partner 2 Name:", placeholder="e.g., Rahul")

if name1 and name2:
    st.write("### 📝 Rate from 1 (Disagree) to 5 (Agree)")
    p1_ans = []
    p2_ans = []
    
    for idx, q in enumerate(QUESTIONS, 1):
        st.markdown(f"**Q{idx}. {q}**")
        p1_ans.append(st.slider(f"{name1}'s Rating", 1, 5, 3, key=f"p1_{idx}"))
        p2_ans.append(st.slider(f"{name2}'s Rating", 1, 5, 3, key=f"p2_{idx}"))
        st.write("")
        
    if st.button("Calculate Compatibility"):
        # Data Science Logic: Weighted Euclidean Distance
        weights = [0.30, 0.25, 0.25, 0.20]
        total_weighted_diff = 0
        max_possible_diff = 0
        
        for i in range(len(QUESTIONS)):
            diff = (p1_ans[i] - p2_ans[i]) ** 2
            total_weighted_diff += diff * weights[i]
            max_possible_diff += 16 * weights[i]
            
        distance = math.sqrt(total_weighted_diff)
        max_distance = math.sqrt(max_possible_diff)
        compatibility_score = round((1 - (distance / max_distance)) * 100, 2)
        
        st.write("---")
        st.success(f"🎯 Dynamic Core Compatibility Index: **{compatibility_score}%**")
        
        if compatibility_score >= 85:
            st.balloons() # This throws balloons on screen!
            st.markdown(f"### 💍 STATUS: {name1} & {name2} are an Exceptionally High Match!")
        elif 60 <= compatibility_score < 85:
            st.markdown(f"### ⚖️ STATUS: Stable Foundations (Moderate Compatibility).")
        else:
            st.markdown(f"### 🚨 STATUS: Friction Points Detected in Background/Values.")
            
    # 📸 NEW FEATURE: THE MEMORY VAULT (PHOTO UPLOADER)
    st.write("---")
    st.subheader("📸 The EverAfter Memory Vault")
    st.write("Upload your favorite couple pictures and good moments here to lock your memories forever!")
    
    uploaded_file = st.file_uploader("Choose a favorite picture...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Display the uploaded image on the app
        st.image(uploaded_file, caption=f"Captured Moment by {name1} & {name2} ❤️", use_column_width=True)
        st.success("✨ Image loaded successfully into the local vault memory!")
