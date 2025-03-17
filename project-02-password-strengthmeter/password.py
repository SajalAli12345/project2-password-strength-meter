import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter",page_icon="🔐")

st.title("🔐 Password Strength Meter")
st.markdown("""
## Welcome the Altimate Password Strength Meter!
Use this Simple tool to check the strength of your password and get suggestion on how to make its stronger.
We will give u to useful tips to create **Strong password** 🔒""")

password = st.text_input("Enter your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ password should contain both upper & lower case.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    

    if score == 4:
        feedback.append("✅ Strong Password!🎉")
    elif score == 3:
        feedback.append("⚠️ Your Password is medium strength. It could be stronger.")
    else:
        feedback.append("❌ Your Password is Weak. Please make it strong.")
    
    if feedback:
        st.markdown("## Improvement Suggestions ##")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please Enter your password to get Started")