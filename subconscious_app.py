import streamlit as st

# Set page config
st.set_page_config(page_title="The Inner Code", page_icon="🌀", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    text-align: center;
    color: #2E86AB;
    margin-bottom: 30px;
}
.result-box {
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
}
.block-result {
    background-color: #ffebee;
    border-left: 5px solid #f44336;
}
.partial-result {
    background-color: #fff3e0;
    border-left: 5px solid #ff9800;
}
.aligned-result {
    background-color: #e8f5e8;
    border-left: 5px solid #4caf50;
}
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🌀 The Inner Code: Subconscious Test</h1>', unsafe_allow_html=True)

st.markdown("---")

# Area selection
st.subheader("🎯 Choose Your Focus Area")
area = st.selectbox(
    "Which area would you like to explore?", 
    ["Money", "Love", "Self-Worth", "Health", "Spiritual Connection"],
    help="Select the life area you'd like to examine for subconscious blocks"
)

st.markdown("---")

# Questions
st.subheader("📝 Rate Each Statement (0 = Strongly Disagree, 10 = Strongly Agree)")

col1, col2 = st.columns([3, 1])

with col1:
    st.write("**1. I feel I deserve good things in life**")
with col2:
    q1 = st.slider("", 0, 10, 5, key="q1", label_visibility="collapsed")

with col1:
    st.write("**2. I easily receive support from others**")
with col2:
    q2 = st.slider("", 0, 10, 5, key="q2", label_visibility="collapsed")

with col1:
    st.write("**3. I trust life/the divine to guide me**")
with col2:
    q3 = st.slider("", 0, 10, 5, key="q3", label_visibility="collapsed")

st.markdown("---")

# Calculate score
score = (q1 + q2 + q3) / 3

# Show current score
st.write(f"**Current Score: {score:.1f}/10**")

# Results
if st.button("🔮 Reveal My Inner Pattern", type="primary"):
    st.markdown("### 🎭 Your Results")
    
    # Create session data
    session_data = f"""The Inner Code: Subconscious Test Results
    
Area Explored: {area}
Overall Score: {score:.1f}/10

Individual Responses:
• I feel I deserve good things: {q1}/10
• I easily receive support: {q2}/10  
• I trust life/the divine to guide me: {q3}/10

Analysis:"""

    if score < 4:
        st.markdown("""
        <div class="result-box block-result">
            <h4>🌑 Core Block Detected</h4>
            <p><strong>Pattern:</strong> "I am not worthy of receiving"</p>
            <p><strong>✨ Belief Rewrite:</strong> "I am a divine being, worthy of infinite good"</p>
            <p><strong>💬 Daily Affirmation:</strong> "I now receive with ease, grace, and gratitude"</p>
        </div>
        """, unsafe_allow_html=True)
        
        session_data += "\n\n🌑 Core Block: 'I am not worthy of receiving'\n✨ Belief Rewrite: 'I am a divine being, worthy of infinite good'\n💬 Affirmation: 'I now receive with ease, grace, and gratitude'"
        
    elif score < 7:
        st.markdown("""
        <div class="result-box partial-result">
            <h4>🌕 Partial Block Detected</h4>
            <p><strong>Pattern:</strong> You sometimes resist receiving. You're learning to trust.</p>
            <p><strong>✨ Belief Rewrite:</strong> "I am open to guidance and support in all forms"</p>
            <p><strong>💡 Focus:</strong> Practice accepting compliments and help from others</p>
        </div>
        """, unsafe_allow_html=True)
        
        session_data += "\n\n🌕 Partial Block: Learning to trust and receive\n✨ Belief Rewrite: 'I am open to guidance and support in all forms'"
        
    else:
        st.markdown("""
        <div class="result-box aligned-result">
            <h4>🌟 Beautifully Aligned!</h4>
            <p><strong>Pattern:</strong> Your beliefs are supporting abundance and flow</p>
            <p><strong>✨ Keep doing:</strong> Trust your intuition and stay open to receiving</p>
            <p><strong>🎯 Next level:</strong> Share your positive energy with others</p>
        </div>
        """, unsafe_allow_html=True)
        
        session_data += "\n\n🌟 Aligned: Your beliefs are supporting abundance!"

    # Download button
    st.download_button(
        "📄 Download My Session Results",
        data=session_data,
        file_name=f"InnerCode_{area}_{score:.1f}.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8em;'>
    <p>💫 Remember: Awareness is the first step to transformation</p>
    <p>✨ Your subconscious patterns can be reprogrammed with consistent practice</p>
</div>
""", unsafe_allow_html=True)