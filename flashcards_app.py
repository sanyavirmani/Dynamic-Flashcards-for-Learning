import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('trained_dataset.csv')

kmeans_english = KMeans(n_clusters=3, random_state=0)
df['EnglishCluster'] = kmeans_english.fit_predict(df[['EnglishScore']])

kmeans_logical = KMeans(n_clusters=3, random_state=0)
df['LogicalReasoningCluster'] = kmeans_logical.fit_predict(df[['LogicalReasoningScore']])

kmeans_quantitative = KMeans(n_clusters=3, random_state=0)
df['QuantitativeAptitudeCluster'] = kmeans_quantitative.fit_predict(df[['QuantitativeAptitudeScore']])

def interpret_english_cluster(cluster):
    if cluster == 0:
        return 'Needs Improvement'
    elif cluster == 1:
        return 'Does Not Need Improvement'
    elif cluster == 2:
        return 'A little more focus'

def interpret_logicalreasoning_cluster(cluster):
    if cluster == 0:
        return 'Needs Improvement'
    elif cluster == 1:
        return 'Does Not Need Improvement'
    elif cluster == 2:
        return 'A little more focus'

def interpret_quantitativeaptitude_cluster(cluster):
    if cluster == 0:
        return 'Needs Improvement'
    elif cluster == 1:
        return 'Does Not Need Improvement'
    elif cluster == 2:
        return 'A little more focus'

def main():
    st.set_page_config(page_title="Flashcards App", page_icon="📘")

    student_id = st.text_input("Enter Student ID:")

    if student_id:
        # User input for the subject scores
        user_english_score = st.number_input("Enter your English score:", min_value=0, max_value=100)
        user_logicalreasoning_score = st.number_input("Enter your Logical Reasoning score:", min_value=0, max_value=100)
        user_aptitude_score = st.number_input("Enter your Quantitative Aptitude score:", min_value=0, max_value=100)

        # Predict the cluster for User's subject score
        user_english_cluster = kmeans_english.predict([[user_english_score]])[0]
        user_logicalreasoning_cluster = kmeans_logical.predict([[user_logicalreasoning_score]])[0]
        user_quantitativeaptitude_cluster = kmeans_quantitative.predict([[user_aptitude_score]])[0]

        # Interpret improvement status
        english_improvement_status = interpret_english_cluster(user_english_cluster)
        logical_improvement_status = interpret_logicalreasoning_cluster(user_logicalreasoning_cluster)
        quantitative_improvement_status = interpret_quantitativeaptitude_cluster(user_quantitativeaptitude_cluster)

        # Display the improvement status in Streamlit
        st.title(f"Flashcards for Student ID {student_id}")
        st.write(f"English Improvement Status: {english_improvement_status}")
        st.write(f"Logical Reasoning Improvement Status: {logical_improvement_status}")
        st.write(f"Quantitative Aptitude Improvement Status: {quantitative_improvement_status}")

if __name__ == "__main__":
    main()
