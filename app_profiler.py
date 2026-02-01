import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Karabo Makofane | Data Profile",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
body {
    background-color: #fff0f5;
    color: #4b004b;
}
h1, h2, h3, h4, h5, h6 {
    color: #d63384;
}
.stButton>button {
    background-color: #ff66b3;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #ff3385;
    transform: scale(1.05);
    transition: all 0.2s ease-in-out;
}
.stDataFrame table {
    border-collapse: collapse;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


st.title("🌸 Personal Research & Data Profile 🌸")
st.subheader("Karabo Makofane | Aspiring Data Scientist & Analyst")

#Image from GitHub URL
image_url = "https://github.com/KaraboMakofane16/streamlit.css/blob/main/karabopic.jpeg"

col1, col2 = st.columns([1,2])
with col1:
    st.image(image_url, caption="Karabo Makofane", use_container_width=True)
with col2:
    st.markdown("""
    **Name:** Karabo Makofane  
    **Field of Interest:** Data Science & Analytics  
    **Institution:** University of Mpumalanga  
    """)

#my profile summary
st.markdown("### Professional Summary")
st.info("""
I am an aspiring Data Scientist and Analyst with a completed Bachelor of
Information and Communication Technology degree from the University of Mpumalanga.
I have two years of experience as a university tutor, supporting students across
data science, statistics, programming, and project-based modules.

I am passionate about data-driven problem solving, analytics, and continuous learning,
and I enjoy working in structured and collaborative environments.
""")

st.markdown("### Technical Skills")
skills = [
    "🐍 Python Programming",
    "📊 R Programming",
    "🗄 SQL",
    "🤖 Machine Learning",
    "📈 Statistics",
    "📊 Power BI",
    "🎨 Data Visualisation",
    "☁️ Azure Services",
    "📝 Agile & Scrum",
    "📂 Project Management",
    "💻 Microsoft Office"
]
cols = st.columns(3)
for i, skill in enumerate(skills):
    cols[i % 3].write(skill)


st.markdown("### Experience")
st.success("University Tutor – University of Mpumalanga (March 2024 – Nov 2025)")
st.write("""
- Supported students in Web Development, Databases, Project Management, and Agile & Scrum  
- Transitioned into Data Science tutoring covering Statistics, Python, AI, and Machine Learning  
- Assisted with assignments, quizzes, and capstone projects  
- Worked closely with lecturers to support at-risk students and maintain academic standards
""")


st.markdown("### Sample Data Exploration")
sample_data = pd.DataFrame({
    "Project": [
        "Data Analysis",
        "Machine Learning Model",
        "Dashboard Visualisation",
        "Statistical Modelling"
    ],
    "Tools Used": [
        "Python, SQL",
        "Python, ML",
        "Power BI",
        "R"
    ],
    "Level": [
        "Intermediate",
        "Advanced",
        "Intermediate",
        "Advanced"
    ]
})
st.dataframe(sample_data, use_container_width=True)

level = st.selectbox("Filter Projects by Level", ["All", "Intermediate", "Advanced"])
if level != "All":
    st.dataframe(sample_data[sample_data["Level"] == level], use_container_width=True)


st.markdown("### Contact Information")
st.markdown("""
📧 **Email:** Karabomakofane13@gmail.com  
📍 **Location:** Gauteng, Randburg  
📞 **Phone:** +27 82 049 9163
""")


st.markdown("### 🎲 Data Career Quiz")
st.write("Answer a few questions and we’ll predict if you’re more suited for Data Science or Data Analytics!")

questions = {
    "Do you enjoy building predictive models with data?": ["Yes", "No"],
    "Do you prefer exploring data and visualizing insights?": ["Yes", "No"],
    "Are you comfortable with programming and algorithms?": ["Yes", "No"],
    "Do you enjoy creating dashboards for decision-making?": ["Yes", "No"],
    "Do you like experimenting with machine learning models?": ["Yes", "No"]
}

score_ds = 0
score_da = 0
answers = {}

for q, options in questions.items():
    ans = st.radio(q, options, key=q)
    answers[q] = ans
    if q in ["Do you enjoy building predictive models with data?", "Are you comfortable with programming and algorithms?", "Do you like experimenting with machine learning models?"]:
        if ans == "Yes":
            score_ds += 1
    else:
        if ans == "Yes":
            score_da += 1

if st.button("Get Prediction!"):
    st.markdown("### 🧠 Result:")
    if score_ds > score_da:
        st.success("You are more suited for **Data Science**! 🌟")
    elif score_da > score_ds:
        st.success("You are more suited for **Data Analytics**! 📊")
    else:
        st.warning("You have a balanced interest in both Data Science and Data Analytics! 🎯")
