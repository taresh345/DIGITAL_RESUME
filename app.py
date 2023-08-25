import json
from pathlib import Path
import streamlit as st
import requests  # pip install requests

from PIL import Image
# from streamlit_lottie import st_lottie

# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)


# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()


# hire_me=load_lottieurl('https://lottie.host/7ef8bb9d-4b92-48e7-8756-4abec8064f43/IwPQKRHXIA.json')
# lottie_two=load_lottieurl('https://lottie.host/0d4e041a-8f52-4d99-86b7-9e6f94805143/x7ZQC5TqYA.json')




# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume for data analyst job.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Taresh Gupta"
PAGE_ICON = ":wave:"
NAME = "Taresh Gupta"
DESCRIPTION = """
 I am an aspiring and enthusiastic Web Developer who is also interested in Sports/Data analytics driven by a passion for JavaScriptand python development. I bring a wealth of expertise in front-end development, backed by hands-on involvement in several personal projects. I am now seeking to elevate my burgeoning tech career as a Software Development Engineer within a dynamic and competitive setting.
Rooted in a background of Mechanical Engineering, I possess the inherent ability to autonomously grasp a wide array of subjects. This skill is vividly demonstrated through my accomplished mastery of front-end development.
 
"""
EMAIL = "taresh345@gmail.com"
SOCIAL_MEDIA = {
    # "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/taresh-gupta-b26022168/",
    "GitHub": "https://github.com/taresh345",
    # "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Olympics Dataset Analysis - Insights from Olympics games from 1896 to 2016": "https://olympic-analysis-project.streamlit.app/",
    "🏆FIFA WC analysis  -  Interactive analysis on possible metrics and stats about fifa wc matches 1930-1956": "https://tare-fifawc.streamlit.app/",
    "🏆TIC TAC TOE- Javascript powered tic tac toe game which have the ability to detect the winner of the game and precursors of the player turn marks":"https://replit.com/join/njfvlknett-tareshgupta" ,
    "🏆WEATHER APP - In this project, I conceived and developed a dynamic Weather App that provides real-time weather information for any city in the world. The app employs a combination of HTML, CSS, and JavaScript, utilizing "
    "the OpenWeather API to fetch and display weather data, including temperature, weather conditions, and more.": " https://replit.com/join/loldboqtbq-tareshgupta",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2= st.columns(2, gap="small")
with col1:
    st.title("  HEY I AM")
    # st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python,Excel,HTML,CSS,JAVASCRIPT
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
# col1,col2=st.columns(2,gap="small")
# with col1:
#     st_lottie(lottie_two,
#               speed=1,
#               reverse=False,
#               loop=True,
#               quality="low",  # medium ; high
#               # renderer="svg",  # canvas
#               height=None,
#               width=None,
#               key=None,
#               )
# with col2:
st.write('\n')
st.subheader("Hard Skills")
st.write(
        """
    - 👩‍💻 Programming: Python (Numpy, Pandas),Scikit-learn,javascript ,html,css
    - 📊 Data Visulization: PowerBi, Plotly
    - 📚 Modeling: Logistic regression, linear regression,KNN.
    - 🗄️ Databases: MySQL
    """
)


# --- Projects & Accomplishments ---
st.write('\n\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



# st_lottie(hire_me,
#           speed=1,
#           reverse=False,
#           loop=True,
#           quality="low",  # medium ; high
#           # renderer="svg",  # canvas
#           height=None,
#           width=None,
#           key=None,
#           )
