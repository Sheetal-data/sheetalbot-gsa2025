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
Hi, I’m <strong>SheetalBot</strong> – the virtual version of <strong>Sheetal Pandey</strong> 👩‍💻  
Ask me anything about Google tools, AI, community work, or why I’m the perfect fit to be your <strong>Google Student Ambassador 2025</strong>!
</div>
""", unsafe_allow_html=True)

st.divider()

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chatbot reply logic
def generate_reply(user_input):
    user_input = user_input.lower()

    if "who are you" in user_input or "your name" in user_input:
        return "I’m SheetalBot – your friendly tech guide, built by Sheetal Pandey, a passionate, community-driven data professional applying to be your Google Student Ambassador 2025! 😊"

    elif "why gsa" in user_input or "ambassador" in user_input:
        return ("My journey began with organizing health education events that built awareness in local communities. That experience taught me how to lead, communicate, and drive impact. "
                "Later, at Collegedunia and Evolent Health, and as a freelance analyst, I mentored over 50 peers in using Google Sheets, Gemini, and Meet to solve real-world problems like automation, analysis, and reporting. "
                "As a Student Ambassador, I want to combine my passion for outreach and my technical expertise to make digital tools approachable, inclusive, and empowering for every student.")

    elif "experience" in user_input or "what have you done" in user_input:
        return ("I've worked at Collegedunia, Evolent Health, and freelanced with Highbrow Tech and others. I’ve built dashboards, automated ETL pipelines, and supported privacy-compliant data analysis. "
                "I’ve also hosted community education drives and tech workshops — helping students and professionals alike become confident with data and AI tools.")

    elif "favorite google tool" in user_input or "fav tool" in user_input:
        return "Google Sheets! 📊 I use it to teach automation, create visual dashboards, and simplify complex reporting workflows. It’s powerful, accessible, and a great teaching tool."

    elif "ai" in user_input or "gemini" in user_input:
        return ("I love introducing students to AI tools like Gemini. I’ve helped peers write better resumes, brainstorm project ideas, and automate everyday work using Gemini responsibly and creatively.")

    elif "tools" in user_input:
        return ("I regularly use Google Sheets, Docs, Meet, Forms, and Gemini. I’ve integrated them into workshops, personal projects, and mentoring sessions to show how even basic tools can create big impact.")

    elif "sessions" in user_input or "events" in user_input:
        return ("I’ve led sessions on web scraping, Sheets automation, and using Gemini for students. Previously, I also conducted health education events in underserved areas — showing my long-standing commitment to empowering others.")

    elif "real" in user_input:
        return "Well, I’m a bot — but Sheetal Pandey is very real. And she’s driven, community-minded, and ready to represent students as a GSA 2025. 🚀"

    elif "hi" in user_input or "hello" in user_input:
        return "Hey there! 👋 Ready to chat about tech, community, and why I’d love to be your Google Student Ambassador."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! I hope we connect again soon — maybe through the GSA community! 💙💛💚❤️"

    else:
        return "I’m still learning! Try asking about Google tools, AI, community work, or what makes Sheetal Pandey the right fit for GSA 2025."

# Chat input
user_input = st.chat_input("Ask SheetalBot anything...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = generate_reply(user_input)
    st.session_state.chat_history.append(("SheetalBot", bot_reply))

# Display the conversation
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div style='color:#EA4335;'><strong>You:</strong> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color:#4285F4;'><strong>🤖 SheetalBot:</strong> {message}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
Made with ❤️ using Streamlit · Inspired by Google's mission to make information universally accessible & useful
</div>
""", unsafe_allow_html=True)
