import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


st.set_page_config(layout='wide')

st.sidebar.title('students performance and analysis system')
st.sidebar.image('captain7888.jpg')
profession = st.sidebar.selectbox('please select your profession',['teacher','students'])



if profession == 'teacher':
    df = pd.read_csv('student_performance.csv')
    st.dataframe(df)
    
    df = pd.read_csv('student_performance.csv')
    
    # Example usage in a Streamlit app:
    subject = st.selectbox("Select Subject", df.columns[1:])  # Skip 'Name' column
   

    def topper(subject):
        if subject == "Name":
            return st.subheader("choose another column sir")
        elif subject not in df.columns:
            st.error(f"Subject '{subject}' not found in the dataset.")
            return

        # Sort and select top 5 scores with names
        toppe = df[['Name', subject]].sort_values(by=subject, ascending=False).head(5)

        # Set 'Name' as index for chart display
        toppe = toppe.set_index('Name')

        st.subheader(f"Top 5 Students in {subject}")
        st.bar_chart(toppe)
    
    st.metric('total students are',str(df.shape[0]))
    
    def passed(subject):
        p=0
        f=0
        for i in df:
            if i <=50:
                p = p+1
            else:
                f = f+1
        return 'passed =',p ,'and failed are',f
        
    
    
         
    coll1 , coll2 = st.columns(2)  
    coll3 , coll4 = st.columns(2)
    with coll1:
        topper(subject="English")
    with coll2:
        topper(subject="Math")
    with coll3:
        topper(subject="Science")
    with coll4:
        topper(subject="History")

elif profession == 'students':
    
    df = pd.read_csv('student_performance.csv')
    # Let the user select a student
    student = st.sidebar.selectbox("select your id", df["Name"].unique())   
    
    # name = st.sidebar.selectbox("Select your ID", df["Name"].unique(), key="student_selectbox")

    num = st.number_input('please enter roll no')
    # Date = st.date_input('please enter your date')
    gender = st.selectbox('select_gender',['male','female','dont want to maintion'])

    btn = st.button('login please')
    
    if btn:
        if not df[(df["Name"] == student) & (df["Roll No"] == num)].empty:
            
            
            time.time()
            print('good to go')
            st.session_state['authenticated'] = True
            st.success('good buddy')
            st.balloons()
            time.sleep(.9)
            st.balloons()
            time.sleep(.9)
            st.balloons()
            #st.write('got it you are'+ ' ' + gender)
            if student:
                
                # Retrieve the selected student's data
                st.markdown('# student performance portal')
                
                student_data = df[df["Name"] == student].iloc[0]

                # Display student's complete record
                st.header(f"Details for {student}")
                st.write(student_data)

                # Extract scores for key subjects to visualize
                subjects = ["Math", "Science", "English", "History"]
                student_scores = student_data[subjects]
                total = 100
            
                col1,col2 = st.columns(2)
                col3,col4 = st.columns(2)
                
                def piee(selected_subject):
                    
                    # Create a pie chart for the subject scores
                    # Replace this with the chosen subject
                    student_score = student_data[selected_subject]  # Get the score for the selected subject

                    # Calculate achieved marks and remaining marks
                    achieved1 = student_score
                    remaining1 = 100 - student_score
                    avg = (student_data['Math']+student_data['Science']+student_data['English']+student_data['History'])/5
                
                    
                    fig, ax = plt.subplots(figsize=(3,3),dpi = 100)
                    ax.pie([achieved1, remaining1], 
                    labels=["Achieved Marks", "Remaining Marks"], 
                    autopct='%1.1f%%', 
                    startangle=90, 
                    colors=["green", "red"])
                    ax.axis('equal')  # Ensures the pie chart is a circle
                    ax.set_title(f"{selected_subject} Performance for {student}")
                    # Display the pie chart in Streamlit
                    st.header(f"Pie Chart for {selected_subject} (Student: {student})")
                    return st.pyplot(fig)
                    
                with col1:
                    piee('History')
                with col2:
                    piee('Science')
                with col3:
                    piee('Math')
                with col4:
                    piee('English')
                avg = (student_data['Math']+student_data['Science']+student_data['English']+student_data['History'])/5
                st.markdown(f"<h2><b>Your average score is {avg}</b></h2>", unsafe_allow_html=True)

                        
                        
                        
                
        else:
            # print('mind on your own business')
            st.error('bhai apna kam kar na')

        #if st.session_state.get('authenticated'):
        #   pass
            
        

