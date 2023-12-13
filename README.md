# Dynamic-Flashcards-for-Learning
* Dataset by - Kaggle
* Analyzed the data of 3000+ students and implemented a machine learning algorithm in order to adjust the frequency of flashcards based on the user's proficiency in each subject or topic. This helps reinfroce weaker areas.
* The Flashcard Application is created through Python streamlit library.

## Problem Statement:  
Implement a flashcard application that dynamically adjusts the frequency of presenting flashcards based on the user’s proficiency in each topic.

## Machine Learning Techniques:  
To achieve dynamic adaptability, an unsupervised learning algorithm, specifically K-Means Clustering algorithm, was employed. This machine learning technique allowed the application to categorize flashcards based on user performance, ensuring a customized learning path.

## Brief Summary of the Solution:
* In order to categorize the student records, the data was trained using machine learning algorithm, K-Means clustering algorithm in which student marks were divided into 3 clusters. These clusters were then utilized to identify and display remarks on subjects where improvement was needed.

* To provide a user-friendly interface, an application was developed using the Streamlit library in Python. This application interprets user-entered data, including marks for each subject and corresponding Student IDs, identifying which students need improvement. It dynamically analyzes this information and promptly presents insights on subjects improvement, accompanied by specific remarks. This streamlined and personalized approach ensures a targeted and effective learning experience for users of the flashcard application.
