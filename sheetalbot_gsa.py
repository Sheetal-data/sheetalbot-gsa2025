import streamlit as st

# Page setup
st.set_page_config(
    page_title="SheetalBot – Google Student Ambassador 2025",
    page_icon="🤖",
    layout="centered"
)

# Custom Google-style CSS
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
            font-family: "Google Sans", "Segoe UI", sans-serif;
        }
        h1 {
            color: #4285F4;
            font-size: 2.5rem;
            text-align: center;
        }
        .stChatInputContainer {
            background-color: #f1f3f4;
        }
        .stMarkdown {
            font-size: 1rem;
        }
        .footer {
            text-align: center;
            color: #555;
            margin-top: 50px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🤖 SheetalBot – Your Google Student Ambassador 2025")
st.markdown("""
<div style="color:#0F9D58; font-size:18px;">
Hi, I’m <strong>SheetalBot</strong> – the virtual version of <strong>Sheetal Dubey</strong> 👩‍💻  
Ask me anything about Google tools, AI, community work, or why I’m the perfect fit to be your <strong>Google Student Ambassador 2025</strong>!
</div>
""", unsafe_allow_html=True)

st.divider()

# Response logic
def generate_reply(user_input):
    user_input = user_input.lower()

    if "best fit" in user_input or "why" in user_input:
        return (
            "I'm excited to be a Google Student Ambassador because of the work I’ve already done at the intersection of tech, education, and community impact.\n\n"
            "👩‍🏫 **Community Leadership**: I’ve organized health education events to raise awareness in underserved communities — this shows my ability to lead, educate, and create real-world impact.\n\n"
            "💻 **Tech Educator**: I’ve mentored over 50+ peers, helping them gain hands-on skills in Google Sheets, Gemini, Meet, and other digital tools. I’ve led workshops on data analytics, AI, automation, and problem-solving — empowering others with confidence and clarity.\n\n"
            "🌍 **Diverse Work Experience**: From working at Collegedunia to Evolent Health and freelance roles, I’ve tackled real business challenges, automated workflows, and visualized insights — always bringing value and innovation.\n\n"
            "🚀 **AI & Google Tools Advocate**: I actively help people integrate Google tools and AI (like Gemini) into their daily lives — from resume writing to automation — in ways that are responsible and impactful.\n\n"
            "💡 **My Mission as a GSA**: I want to make digital literacy and AI skills accessible to every student — especially those from non-tech backgrounds or underserved regions.\n\n"
            "**That’s why I believe I’m not just a good fit — I’m the right fit to represent students as a Google Student Ambassador 2025.**"
        )

    elif "who are you" in user_input or "your name" in user_input:
        return "I’m SheetalBot – your friendly tech guide, built by Sheetal Dubey, a community-first, data-driven GSA aspirant! 😊"

    elif "experience" in user_input:
        return ("I've worked with Collegedunia, Evolent Health, and freelance clients. I’ve created dashboards, automated ETL pipelines, and supported data privacy. "
                "I've also hosted workshops and community sessions to spread awareness of health, data, and digital empowerment.")

    elif "tools" in user_input:
        return "I love Google Sheets, Docs, Forms, Meet, and Gemini! I use them for mentoring, reporting, automating, and teaching."

    elif "ai" in user_input or "gemini" in user_input:
        return "I'm passionate about AI! I guide students in using Gemini for smarter research, automation, idea generation, and personal growth."

    elif "sessions" in user_input or "events" in user_input:
        return "I’ve led workshops on Google Sheets, data scraping, AI tools, and digital problem solving. I also organized community education events in health and wellness."

    elif "hi" in user_input or "hello" in user_input:
        return "Hello! 👋 I’m SheetalBot. Ask me anything about Sheetal Dubey’s journey or tools she uses to drive impact!"

    elif "bye" in user_input:
        return "Thanks for chatting! Hope to connect again — maybe through the GSA network! 🌐"

    else:
        return "I'm still learning! Try asking about my experience, tools, sessions, or why I'm the best fit for GSA."

# Auto-show intro Q&A
if "chat_history" not in st.session_state:
    auto_q = "Why is Sheetal Dubey the best fit to be a Google Student Ambassador?"
    st.session_state.chat_history = [
        ("You", auto_q),
        ("SheetalBot", generate_reply(auto_q))
    ]

# Chat input
user_input = st.chat_input("Ask SheetalBot anything...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    response = generate_reply(user_input)
    st.session_state.chat_history.append(("SheetalBot", response))

# Show chat + voice
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div style='color:#EA4335;'><strong>You:</strong> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color:#4285F4;'><strong>🤖 SheetalBot:</strong> {message}</div>", unsafe_allow_html=True)

        # 🎤 Bot speaks using browser's Web Speech API
        st.markdown(f"""
            <script>
                var msg = new SpeechSynthesisUtterance({repr(message)});
                msg.pitch = 1;
                msg.rate = 1;
                msg.volume = 1;
                msg.lang = 'en-IN';
                window.speechSynthesis.speak(msg);
            </script>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
Made with ❤️ using Streamlit · Powered by Google inspiration · Sheetal Dubey for GSA 2025
</div>
""", unsafe_allow_html=True)
