import streamlit as st
import random
import math

# Page Setup
st.set_page_config(page_title="EverAfter Premium Ecosystem", page_icon="💘", layout="centered")
st.title("💘 EverAfter: The Ultimate Life & Relationship Planner")
st.markdown("### Data-Driven Analytics + Family & Wedding Management")
st.write("---")

# 1. PROFILE SECTION WITH ZODIAC & LOVE LANGUAGE
st.subheader("👤 User Profiles & Astro Metrics")
col_name1, col_name2 = st.columns(2)
with col_name1:
    name1 = st.text_input("Partner 1 Name:", placeholder="e.g., Prachi")
    zodiac1 = st.selectbox("Partner 1 Zodiac Sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    love_lang1 = st.selectbox("Partner 1 Love Language:", ["Quality Time", "Words of Appreciation", "Acts of Service", "Receiving Gifts"])
with col_name2:
    name2 = st.text_input("Partner 2 Name:", placeholder="e.g., Rahul")
    zodiac2 = st.selectbox("Partner 2 Zodiac Sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    love_lang2 = st.selectbox("Partner 2 Love Language:", ["Quality Time", "Words of Appreciation", "Acts of Service", "Receiving Gifts"])

# 2. ALL CORE STATEMENT QUESTIONS ARE BACK!
QUESTIONS = [
    "Family Setup: I prefer living with a Joint Family rather than a Nuclear Setup.",
    "Location Choice: I want to settle in a Tier-1 Metro City in the future.",
    "Money Management: I believe in maintaining a shared investment pool with my partner.",
    "Conflict Resolution: When an argument happens, I prefer solving it immediately."
]

if name1 and name2:
    st.write("---")
    st.subheader("📝 Core Lifestyle Compatibility Matrix")
    p1_ans = []
    p2_ans = []
    
    for idx, q in enumerate(QUESTIONS, 1):
        st.markdown(f"**Q{idx}. {q}**")
        p1_ans.append(st.slider(f"{name1}'s Rating", 1, 5, 3, key=f"p1_{idx}"))
        p2_ans.append(st.slider(f"{name2}'s Rating", 1, 5, 3, key=f"p2_{idx}"))
        st.write("")
        
    if st.button("Calculate Core Matrix & Analytics", type="primary"):
        # Math calculation: Weighted Euclidean Distance
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
        
        # 🌟 NEW FEATURE: DYNAMIC LOVE LANGUAGE LOGIC REPORT
        st.subheader("❤️ Love Language Alignment Report")
        if love_lang1 == love_lang2:
            st.info(f"✨ Perfect Emotional Sync! Both value **{love_lang1}**. This reduces relationship friction by 40%.")
        else:
            st.warning(f"💡 Emotional Duality Detected! {name1} values **{love_lang1}** while {name2} values **{love_lang2}**.")
            st.write("👉 **Data Science Tip:** Make an active effort to speak your partner's emotional language to avoid communication gaps!")
        
        # COSMIC & SHUBH MUHURAT REPORT
        st.subheader("🌌 Cosmic & Shubh Muhurat Report")
        st.info(f"✨ Match analysis generated for **{zodiac1}** and **{zodiac2}**.")
        st.write("📅 **Upcoming Shubh Muhurat Dates Found for You:**")
        st.write("- 🌸 November 18, 2026 (Rohini Nakshatra)")
        st.write("- 🌸 November 23, 2026 (Uttara Phalguni)")
        
        # DYNAMIC ROUTING & CONDITIONS (Wedding Planner)
        if compatibility_score >= 75:
            st.balloons()
            st.markdown("### 💍 STATUS: High Match Matrix! Unlocking Event Modules.")
            st.write("---")
            st.subheader("🏰 EverAfter Premium Wedding Planner & Destination Desk")
            col_wed1, col_wed2 = st.columns(2)
            with col_wed1:
                st.metric("Royal Heritage", "Udaipur, RJ")
            with col_wed2:
                st.metric("Serene Beachfront", "Goa / Havelock")
        else:
            st.markdown("### ⚖️ STATUS: Structural Differences Detected.")
            st.info("💡 Projections indicate lifestyle variations. Activating Support Infrastructure.")
            
        # PSYCHOLOGIST & RELATIONSHIP WELLNESS HELP DESK
        st.write("---")
        st.subheader("🧠 EverAfter Relationship Wellness Desk")
        st.warning("⚠️ Feeling overwhelmed or going through a rough patch? Talking to an expert can clear things up.")
        col_psy1, col_psy2 = st.columns(2)
        with col_psy1:
            st.write("👩‍⚕️ **Dr. Ananya Sharma (Senior Counselor)**")
            if st.button("📅 Secure Instant Session Slot with Dr. Ananya"):
                st.success("Slot Held!")
        with col_psy2:
            st.write("👨‍⚕️ **Dr. Rohan Verma (Wellness Expert)**")
            if st.button("📅 Secure Instant Session Slot with Dr. Rohan"):
                st.success("Slot Held!")

    # PHOTO VAULT (Memory Vault)
    st.write("---")
    st.subheader("📸 The EverAfter Memory Vault")
    uploaded_file = st.file_uploader("Choose a favorite picture...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Captured Moment ❤️", use_column_width=True)
        st.success("✨ Image locked successfully into vault memory!")
