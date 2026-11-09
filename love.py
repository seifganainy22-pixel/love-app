import streamlit as st
import time

# إعدادات الصفحة والتصميم
st.set_page_config(page_title="For My Love ❤️", page_icon="💖", layout="centered")

# عنوان رئيسي أنيق
st.title("💖 A Special Message For You 💖")
st.write("---")

# إدخال الاسم لتعطي طابعاً شخصياً
name = st.text_input("Enter your name, beautiful:", placeholder="Type your name here...")

if name:
    st.subheader(f"Welcome to your special place, {name}! ✨")
    
    # سؤال تفاعلي
    answer = st.radio(
        "Do you know how much you mean to me?",
        ("Select an option...", "A little bit 🤏", "A lot! ❤️", "More than words can say! 🌎💖")
    )

    if answer == "A little bit 🤏":
        st.warning("Wrong answer! Try again 😉")
    elif answer == "A lot! ❤️":
        st.info("Close, but it's way more than that! 💕")
    elif answer == "More than words can say! 🌎💖":
        st.success("EXACTLY! You are my absolute world! 🎉🥰")
        st.balloons()  # تأثير بالونات احتفالية!

    st.write("---")
    
    # زر لإظهار رسالة حب خاصة
    if st.button("Click for a secret surprise 💌"):
        with st.spinner("Preparing your surprise..."):
            time.sleep(1)
        st.snow()  # تأثير الثلج المتساقط
        st.markdown("""
        ### 🌹 My Promise To You
        > *"In a world full of variables, you are my only constant.  
        > Thank you for bringing so much warmth, joy, and love into my life.  
        > You make every single day brighter just by being in it."*
        """)
        
        # قائمة بطاقات لطيفة (Expanders)
        with st.expander("3 Reasons Why You Are Amazing 💖"):
            st.write("1. **Your Smile:** It lights up my whole day. 😊")
            st.write("2. **Your Kindness:** You have the sweetest heart. 🌷")
            st.write("3. **Simply You:** Being with you is my favorite thing. ✨")
            