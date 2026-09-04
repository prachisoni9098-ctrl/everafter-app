import streamlit as st
import random
import math

# Page Setup
st.set_page_config(page_title="EverAfter Premium Ecosystem", page_icon="💘", layout="centered")
st.title("💘 EverAfter: The Ultimate Life & Relationship Planner")
st.markdown("### Data-Driven Analytics + Family & Wedding Management")
st.write("---")

# 1. PROFILE SECTION WITH ZODIAC SIGNS
st.subheader("👤 User Profiles & Astro Metrics")
col_name1, col_name2 = st.columns(2)
with col_name1:
    name1 = st.text_input("Partner 1 Name:", placeholder="e.g., Prachi")
    zodiac1 = st.selectbox("Partner 1 Zodiac Sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
with col_name2:
    name2 = st.text_input("Partner 2 Name:", placeholder="e.g., Rahul")
    zodiac2 = st.selectbox("Partner 2 Zodiac Sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

# 2. CORE STATEMENT QUESTIONS
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
        # Math calculation
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
        
        # 🌟 ASTROLOGY MATCH OVERLAY
        st.subheader("🌌 Cosmic & Shubh Muhurat Report")
        st.info(f"✨ Match analysis generated for **{zodiac1}** and **{zodiac2}**. Astro Element Harmony is structurally locked.")
        st.write("📅 **Upcoming Shubh Muhurat Dates Found for You:**")
        st.write("- 🌸 November 18, 2026 (Rohini Nakshatra)")
        st.write("- 🌸 November 23, 2026 (Uttara Phalguni)")
        st.write("- 🌸 December 05, 2026 (Anuradha Nakshatra)")
        
        # 👑 DYNAMIC ROUTING & CONDITIONS
        if compatibility_score >= 75:
            st.balloons()
            st.markdown("### 💍 STATUS: High Match Matrix! Unlocking Event Modules.")
            
            # 🏰 FEATURE 2: WEDDING PLANNER DESK
            st.write("---")
            st.subheader("🏰 EverAfter Premium Wedding Planner & Destination Desk")
            st.write("Since your compatibility score is elite, explore destination themes handpicked for your lifestyle metrics:")
            
            col_wed1, col_wed2, col_wed3 = st.columns(3)
            with col_wed1:
                st.metric("Royal Heritage", "Udaipur, RJ")
                st.caption("✨ Palaces & Vintage Style")
            with col_wed2:
                st.metric("Serene Beachfront", "Goa / Havelock")
                st.caption("🌊 Sunset Vows & Minimalist")
            with col_wed3:
                st.metric("Mountain Ecstasy", "Mussoorie, UK")
                st.caption("🌲 Cozy Fog & Luxury Resorts")
                
            st.text_input("Enter Estimated Guest Count:", value="300")
            st.slider("Budget Metric Allocation (INR in Lakhs):", 10, 100, 35)
            
        else:
            st.markdown("### ⚖️ STATUS: Structural Differences Detected.")
            st.info("💡 Projections indicate lifestyle variations. Activating Support Infrastructure.")
            
        # 🧠 FEATURE 3: PSYCHOLOGIST & RELATIONSHIP WELLNESS HELP DESK
        st.write("---")
        st.subheader("🧠 EverAfter Relationship Wellness Desk")
        st.write("Relationships need active communication and professional scaffolding. Feel free to access our support network:")
        
        st.warning("⚠️ Feeling overwhelmed or going through a rough patch? Talking to an expert can clear things up.")
        
        col_psy1, col_psy2 = st.columns(2)
        with col_psy1:
            st.write("👩‍⚕️ **Dr. Ananya Sharma (Senior Relationship Counselor)**")
            st.write("💬 *Specialization: Pre-Marital Value Alignment & Communication Gaps*")
            if st.button("📅 Secure Instant Session Slot with Dr. Ananya"):
                st.success("Slot Held! Connecting securely to the counseling dashboard...")
        with col_psy2:
            st.write("👨‍⚕️ **Dr. Rohan Verma (Cognitive Behavior & Wellness Expert)**")
            st.write("💬 *Specialization: Emotional Processing & Stress Management*")
            if st.button("📅 Secure Instant Session Slot with Dr. Rohan"):
                st.success("Slot Held! Connecting securely to the counseling dashboard...")

    # 📸 PHOTO VAULT (Always active)
    st.write("---")
    st.subheader("📸 The EverAfter Memory Vault")
    uploaded_file = st.file_uploader("Choose a favorite picture...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption=f"Captured Moment by {name1} & {name2} ❤️", use_column_width=True)
        st.success("✨ Image locked successfully into the local vault memory!")

