import streamlit as st

st.set_page_config(page_title="Influencer Skincare Dashboard", layout="wide")

st.title("Influencer Marketing Impact on Skincare Sales in Dubai")

tabs = ["Data Visualization", "Classification", "Clustering", "Association Rule Mining", "Regression"]
selected_tab = st.sidebar.selectbox("Select a Tab", tabs)

if selected_tab == "Data Visualization":
    st.header("🔍 Data Visualization")
    st.write("This tab will provide descriptive visual insights.")
elif selected_tab == "Classification":
    st.header("🧠 Classification Models")
    st.write("This tab will let you apply KNN, Decision Tree, Random Forest, and GBRT.")
elif selected_tab == "Clustering":
    st.header("🔗 Customer Segmentation (Clustering)")
    st.write("Use K-means clustering to define customer segments.")
elif selected_tab == "Association Rule Mining":
    st.header("🔁 Association Rule Mining")
    st.write("Apply Apriori algorithm to find associations in consumer preferences.")
elif selected_tab == "Regression":
    st.header("📈 Regression Analysis")
    st.write("Apply Linear, Ridge, Lasso, and Decision Tree Regressors.")
