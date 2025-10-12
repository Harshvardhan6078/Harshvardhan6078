import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import os

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# File paths
DATA_FILE = "student_performance.csv"
IMAGE_FILE = "captain7888.jpg"

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    return df

df = load_data()

# Subject columns
ACADEMIC = ["Math", "Science", "English", "History"]
NON_ACAD = ["Attendance", "Participation", "Projects", "Discipline", "Creativity"]

df["Academic Score"] = df[ACADEMIC].mean(axis=1)
df["Non-Academic Score"] = df[NON_ACAD].mean(axis=1)

# Sidebar
st.sidebar.title("Student Performance System")
if os.path.exists(IMAGE_FILE):
    st.sidebar.image(IMAGE_FILE, use_container_width=True)

role = st.sidebar.radio("Select Role", ["Teacher", "Student"])

# Teacher view
if role == "Teacher":
    st.title("Teacher Dashboard")
    st.subheader("Student Dataset")
    st.dataframe(df)

    st.markdown("---")
    st.subheader("Top Performers per Subject")
    top_cols = st.columns(len(ACADEMIC))
    for col, subject in zip(top_cols, ACADEMIC):
        top5 = df[["Name", subject]].nlargest(5, subject).set_index("Name")
        with col:
            st.markdown(subject)
            st.bar_chart(top5)

    st.markdown("---")
    st.subheader("Class Summary")
    total_students = len(df)
    passed = (~(df[ACADEMIC] <= 50).any(axis=1)).sum()
    failed = total_students - passed
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Students", total_students)
    c2.metric("Passed", passed)
    c3.metric("Failed", failed)

    st.markdown("---")
    st.subheader("Score Distributions")
    dist_cols = st.columns(len(ACADEMIC))
    for col, subject in zip(dist_cols, ACADEMIC):
        fig, ax = plt.subplots()
        df[subject].plot.hist(bins=10, ax=ax, color="skyblue")
        ax.set_title(f"{subject} Distribution")
        ax.set_xlim(0, 100)
        with col:
            st.pyplot(fig)

    st.markdown("---")
    st.subheader("Boxplots")
    box_cols = st.columns(len(ACADEMIC))
    for col, subject in zip(box_cols, ACADEMIC):
        fig, ax = plt.subplots()
        sns.boxplot(y=df[subject], ax=ax, color="lightgreen")
        ax.set_title(f"{subject} Boxplot")
        ax.set_ylim(0, 100)
        with col:
            st.pyplot(fig)

    st.markdown("---")
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(df[ACADEMIC + NON_ACAD].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.markdown("---")
    st.subheader("PCA Projection")
    features = ACADEMIC + NON_ACAD
    pca = PCA(n_components=2)
    comps = pca.fit_transform(df[features])
    df_pca = pd.DataFrame(comps, columns=["PC1", "PC2"])
    df_pca["Name"] = df["Name"]
    fig = px.scatter(df_pca, x="PC1", y="PC2", text="Name", title="PCA of Student Performance")
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

# Student view
else:
    st.title("Student Portal")
    student_name = st.sidebar.selectbox("Select Your Name", df["Name"].unique())
    student_roll = st.sidebar.number_input("Enter Your Roll No", min_value=1, step=1)
    login_btn = st.sidebar.button("Login")

    if login_btn:
        roll_number = int(student_roll)
        matched = df[df["Roll No"] == roll_number]

        if matched.empty or student_name not in matched["Name"].values:
            st.error("Name and Roll No do not match. Please check and try again.")
            st.stop()

        student = matched[matched["Name"] == student_name].iloc[0]
        st.success("Login Successful")

        st.header(f"{student['Name']} (Roll No: {student['Roll No']})")
        st.subheader("Your Record")
        st.write(student)

        st.markdown("---")
        st.subheader("Subject Performance")
        pie_cols = st.columns(len(ACADEMIC))
        for col, subject in zip(pie_cols, ACADEMIC):
            score = student[subject]
            fig, ax = plt.subplots()
            ax.pie([score, 100 - score],
                   labels=["Achieved", "Remaining"],
                   autopct="%1.1f%%",
                   startangle=90,
                   colors=["green", "red"])
            ax.set_title(subject)
            ax.axis("equal")
            with col:
                st.pyplot(fig)

        avg_score = student[ACADEMIC].mean()
        st.markdown(f"Average Score: {avg_score:.2f}")

        df["Rank"] = df[ACADEMIC].mean(axis=1).rank(ascending=False)
        rank = int(df[df["Name"] == student["Name"]]["Rank"].iloc[0])
        st.markdown(f"Class Rank: {rank} of {len(df)}")

        st.markdown("---")
        st.subheader("Performance Clustering")
        km = KMeans(n_clusters=3, random_state=42)
        df["Cluster"] = km.fit_predict(df[["Academic Score", "Non-Academic Score"]])
        fig2 = px.scatter(df, x="Academic Score", y="Non-Academic Score",
                          color="Cluster", hover_name="Name", title="Clustering Overview")
        fig2.add_trace(go.Scatter(
            x=[student["Academic Score"]],
            y=[student["Non-Academic Score"]],
            mode="markers+text",
            text=[student["Name"]],
            marker=dict(size=15, color="red"),
            textposition="top center",
            showlegend=False
        ))
        st.plotly_chart(fig2, use_container_width=True)
