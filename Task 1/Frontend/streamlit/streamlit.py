import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

st.set_page_config(page_title="Iris Classifier Dashboard", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #6EC1E4; font-size: 3rem; margin-bottom: 0.2em;'>
        Iris Flower Classifier
    </h1>
    <h3 style='text-align: center; color: #D4AC0D; font-weight: 500;'>
        Interactive Dashboard for Classification & Insights
    </h3>
    <hr style='border: 1px solid #444;'>
""", unsafe_allow_html=True)



iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
st.subheader("Iris Dataset Overview")
st.markdown("<hr style='border: 1px solid #444;'>", unsafe_allow_html=True)
with st.expander("Show raw dataset"):
    st.dataframe(df)

st.subheader("Feature Statistics")
st.dataframe(df.describe().T)
st.subheader("Feature Relationships")
st.markdown("<hr style='border: 1px solid #444;'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    fig1, ax1 = plt.subplots()
    sns.scatterplot(data=df, x="sepal length (cm)", y="sepal width (cm)", hue="species", ax=ax1)
    ax1.set_title("Sepal Length vs Sepal Width")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x="petal length (cm)", y="petal width (cm)", hue="species", ax=ax2)
    ax2.set_title("Petal Length vs Petal Width")
    st.pyplot(fig2)



st.subheader("Prediction")
st.markdown("<hr style='border: 1px solid #444;'>", unsafe_allow_html=True)
st.write("Enter flower measurements to predict the species and see where it lies visually!")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.1, 0.1)
    petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 1.4, 0.1)
with col2:
    sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.5, 0.1)
    petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 0.2, 0.1)


user_input = [sepal_length, sepal_width, petal_length, petal_width]


if st.button("Predict"):
    try:
        
        response = requests.post("http://backend:5000/predict", json={
    "feature_array": user_input
})

        response.raise_for_status()
        prediction = response.json()["prediction"][0]

        
        classes = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        st.success(f"Predicted Class: **{classes[prediction]}**")

       
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

        
        new_point = pd.DataFrame([user_input], columns=iris.feature_names)
        new_point['species'] = "Your Input"
        df_combined = pd.concat([df, new_point], ignore_index=True)

        fig, ax = plt.subplots()
        sns.scatterplot(data=df_combined,
                        x="petal length (cm)",
                        y="petal width (cm)",
                        hue="species",
                        style="species",
                        s=100)
        ax.set_title("Petal Length vs Width (User Input Highlighted)")
        st.pyplot(fig)

    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the API: {e}")
    except Exception as e:
        st.warning(f"Could not display plot or prediction: {e}")
