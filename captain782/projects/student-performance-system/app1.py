import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    """Loads the CSV file into a Pandas DataFrame."""
    return pd.read_csv("student_performance.csv")

# Load the student performance data
df = load_data()

st.title("Student Performance Dashboard")

# Let the user select a student
student = st.selectbox("Select a Student", df["Name"].unique())

if student:
    # Retrieve the selected student's data
    student_data = df[df["Name"] == student].iloc[0]

    # Display student's complete record
    st.header(f"Details for {student}")
    st.write(student_data)

    # Extract scores for key subjects to visualize
    subjects = ["Math", "Science", "English", "History"]
    student_scores = student_data[subjects]
    total = 100

    # Create a pie chart for the subject scores
    st.header("Subject Score Distribution")
    fig, ax = plt.subplots(figsize=(2,2))
    ax.pie(student_scores, labels=subjects, autopct='%1.1f%%', startangle=90, 
           colors=["skyblue", "lightgreen", "salmon", "violet"])
    ax.axis('equal')  # Ensures the pie is drawn as a circle
    ax.set_title("Performance Across Subjects")
    st.pyplot(fig)
    
    import matplotlib.pyplot as plt

# Example: Replace 'Math' and student_data with your desired subject and student's data
selected_subject = "Science"  # Replace this with the chosen subject
student_score = student_data[selected_subject]  # Get the score for the selected subject

# Calculate achieved marks and remaining marks
achieved = student_score
remaining = 100 - student_score
col1,col2= st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie([achieved, remaining], 
       labels=["Achieved Marks", "Remaining Marks"], 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=["green", "red"])
    ax.axis('equal')  # Ensures the pie chart is a circle
    ax.set_title(f"{selected_subject} Performance for {student}")
    # Display the pie chart in Streamlit
    st.header(f"Pie Chart for {selected_subject} (Student: {student})")
    st.pyplot(fig)


with col2:
    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie([achieved, remaining], 
       labels=["Achieved Marks", "Remaining Marks"], 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=["green", "red"])


    ax.axis('equal')  # Ensures the pie chart is a circle
    ax.set_title(f"{selected_subject} Performance for {student}")
# Display the pie chart in Streamlit
    st.header(f"Pie Chart for {selected_subject} (Student: {student})")
    st.pyplot(fig)


    
    
# Create a pie chart
fig, ax = plt.subplots(figsize=(2,2))
ax.pie([achieved, remaining], 
       labels=["Achieved Marks", "Remaining Marks"], 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=["green", "red"])
ax.axis('equal')  # Ensures the pie chart is a circle
ax.set_title(f"{selected_subject} Performance for {student}")

# Display the pie chart in Streamlit
st.header(f"Pie Chart for {selected_subject} (Student: {student})")
st.pyplot(fig)

              
import matplotlib.pyplot as plt

# Example: Replace 'Math' and student_data with your desired subject and student's data
selected_subject = "Math"  # Replace this with the chosen subject
student_score = student_data[selected_subject]  # Get the score for the selected subject

# Calculate achieved marks and remaining marks
achieved = student_score
remaining = 100 - student_score

# Create a pie chart
fig, ax = plt.subplots(figsize=(2,2))
ax.pie([achieved, remaining], 
       labels=["Achieved Marks", "Remaining Marks"], 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=["green", "red"])
ax.axis('equal')  # Ensures the pie chart is a circle
ax.set_title(f"{selected_subject} Performance for {student}")

# Display the pie chart in Streamlit
st.header(f"Pie Chart for {selected_subject} (Student: {student})")
st.pyplot(fig)



import matplotlib.pyplot as plt

# Example: Replace 'Math' and student_data with your desired subject and student's data
selected_subject = "History"  # Replace this with the chosen subject
student_score = student_data[selected_subject]  # Get the score for the selected subject

# Calculate achieved marks and remaining marks
achieved = student_score
remaining = 100 - student_score

# Create a pie chart
fig, ax = plt.subplots(figsize=(2,2))
ax.pie([achieved, remaining], 
       labels=["Achieved Marks", "Remaining Marks"], 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=["green", "red"])
ax.axis('equal')  # Ensures the pie chart is a circle
ax.set_title(f"{selected_subject} Performance for {student}")

# Display the pie chart in Streamlit
st.header(f"Pie Chart for {selected_subject} (Student: {student})")
st.pyplot(fig)


import matplotlib.pyplot as plt

# Example: Replace 'Math' and student_data with your desired subject and student's data
selected_subject = "English"  # Replace this with the chosen subject
student_score = student_data[selected_subject]  # Get the score for the selected subject

# Calculate achieved marks and remaining marks
achieved = student_score
remaining = 100 - student_score

# Create a pie chart
fig, ax = plt.subplots(figsize=(2,2))
ax.pie([achieved, remaining], 
       labels=["Achieved Marks", "Remaining Marks"], 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=["green", "red"])
ax.axis('equal')  # Ensures the pie chart is a circle
ax.set_title(f"{selected_subject} Performance for {student}")

# Display the pie chart in Streamlit
st.header(f"Pie Chart for {selected_subject} (Student: {student})")
st.pyplot(fig)

import matplotlib.pyplot as plt

# Example: Replace 'Math' and student_data with your desired subject and student's data
selected_subject = "Attendance"  # Replace this with the chosen subject
student_score = student_data[selected_subject]  # Get the score for the selected subject

# Calculate achieved marks and remaining marks
achieved = student_score
remaining = 100 - student_score

# Create a pie chart
fig, ax = plt.subplots(figsize=(2,2))
ax.pie([achieved, remaining], 
       labels=["Achieved Marks", "Remaining Marks"], 
       autopct='%1.1f%%', 
       startangle=90, 
       colors=["green", "red"])
ax.axis('equal')  # Ensures the pie chart is a circle
ax.set_title(f"{selected_subject} Performance for {student}")

# Display the pie chart in Streamlit
st.header(f"Pie Chart for {selected_subject} (Student: {student})")
st.pyplot(fig)

df['academic_score'] = df[['Math', 'Science', 'English', 'History']].mean(axis=1)
df['nonacademic_score'] = df[['Attendance', 'Participation', 'Projects', 'Discipline', 'Creativity']].mean(axis=1)

# Create a scatter plot for overall performance
import matplotlib.pyplot as plt

fig_overall, ax_overall = plt.subplots(figsize=(7, 5))
# Plot all students (blue dots)
ax_overall.scatter(df['academic_score'], df['nonacademic_score'],
                   color="blue", alpha=0.6, label="Students")
# Highlight the selected/current student (red dot with larger size)
current_student = df[df["Name"] == student]
ax_overall.scatter(current_student['academic_score'], current_student['nonacademic_score'],
                   color="red", s=150, label=f"Current Student: {student}")

# Add labels and title to the axes
ax_overall.set_xlabel("Academic Score (Avg. of Math, Science, English, History)")
ax_overall.set_ylabel("Non-Academic Score (Avg. of Attendance, Participation, Projects, Discipline, Creativity)")
ax_overall.set_title("Overall Performance Scatter Plot")
ax_overall.legend()

st.header("Overall Performance Scatter Plot")
st.pyplot(fig_overall)

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

@st.cache_data
def load_data():
    """Loads the CSV file into a Pandas DataFrame."""
    return pd.read_csv("student_performance.csv")

# Load data
df = load_data()

st.title("Student Performance Dashboard")

# Calculate overall performance metrics:
# Academic Score: Average of Math, Science, English, History
# Non-Academic Score: Average of Attendance, Participation, Projects, Discipline, Creativity
df['academic_score'] = df[['Math', 'Science', 'English', 'History']].mean(axis=1)
df['nonacademic_score'] = df[['Attendance', 'Participation', 'Projects', 'Discipline', 'Creativity']].mean(axis=1)

# Apply K-Means clustering (3 clusters used as an example)
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['academic_score', 'nonacademic_score']])

# Let the user select a student (with a unique key)
selected_student = st.selectbox("Select a Student", sorted(df["Name"].unique()), key="student_selectbox")

# Create an interactive scatter plot with Plotly Express for all students.
# Each dot is colored by its cluster and displays the student's name on hover.
fig = px.scatter(
    df,
    x="academic_score",
    y="nonacademic_score",
    color="cluster",          # Color by cluster label.
    text="Name",              # Set student names (used in hover).
    color_continuous_scale="Viridis",
    labels={
        "academic_score": "Academic Score (Avg. of Math, Science, English, History)",
        "nonacademic_score": "Non-Academic Score (Avg. of Attendance, Participation, Projects, Discipline, Creativity)"
    },
    title="Overall Performance with Clustering",
    width=1200,               # Bigger graph
    height=700
)

# Update hover so that only the student's name is shown.
fig.update_traces(hovertemplate="%{text}<extra></extra>",
                  textposition="top center",
                  textfont=dict(family="Helvetica", size=12, color="black"),
                  marker=dict(line=dict(width=1, color='DarkSlateGrey')))

# Now, create a separate trace for the selected student
# This trace will have a custom marker color (here 'red') and a larger marker size.
df_selected = df[df["Name"] == selected_student]
selected_trace = px.scatter(
    df_selected,
    x="academic_score",
    y="nonacademic_score",
    text="Name"
).update_traces(
    marker=dict(color="red", size=20, line=dict(width=2, color="DarkSlateGrey")),
    hovertemplate="%{text}<extra></extra>",
    showlegend=False  # Hide from the legend if desired
).data[0]

# Add the selected student trace to the overall figure.
fig.add_trace(selected_trace)

# Update layout for a cleaner UI.
fig.update_layout(
    title_font_family="Helvetica",
    title_font_color="darkblue",
    title_font_size=24,
    font=dict(family="Helvetica", size=20, color="black"),
    plot_bgcolor="white",
    paper_bgcolor="skyblue",
    margin=dict(l=50, r=50, t=70, b=50),
    xaxis=dict(
        title="Academic Score (Avg. of Math, Science, English, History)",
        title_font=dict(family="Helvetica", size=16, color="black"),
        tickfont=dict(family="Helvetica", size=14, color="black"),
        gridcolor="lightgrey"
    ),
    yaxis=dict(
        title="Non-Academic Score (Avg. of Attendance, Participation, Projects, Discipline, Creativity)",
        title_font=dict(family="Helvetica", size=16, color="black"),
        tickfont=dict(family="Helvetica", size=14, color="black"),
        gridcolor="lightgrey"
    ),
    legend=dict(
        title="Cluster",
        font=dict(family="Helvetica", size=14, color="black"),
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

st.plotly_chart(fig, use_container_width=True)
