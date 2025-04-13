
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px

st.set_page_config(page_title="SmartRoutes", layout="wide")

page = st.sidebar.selectbox("Navigate", ["Home", "Route Dashboard", "Traffic Prediction", "SACCO Login", "Planner Zone", "Contact"])

@st.cache_data
def load_sample_data():
    data = pd.DataFrame({
        'Latitude': [-1.2921, -1.2833, -1.2762],
        'Longitude': [36.8219, 36.8167, 36.8148],
        'Stop': ['CBD', 'Upper Hill', 'Ngong Rd']
    })
    return data

if page == "Home":
    st.title("SmartRoutes – AI-Powered Matatu Route Optimizer")
    st.markdown("""
    **Making Nairobi's public transport smoother using data science**
    
    - Saves commuters' time
    - Helps SACCOs reduce fuel waste
    - Supports SDG 11: Sustainable Cities & Communities
    
    This tool uses GPS data, commuter demand, and traffic patterns to recommend better matatu routes.
    """)

elif page == "Route Dashboard":
    st.title("📍 Matatu Route Dashboard")
    df = load_sample_data()
    m = folium.Map(location=[-1.29, 36.82], zoom_start=13)
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['Stop']).add_to(m)
    folium_static(m)

elif page == "Traffic Prediction":
    st.title("📈 Traffic & Demand Forecast")
    traffic_data = pd.DataFrame({
        "Hour": list(range(6, 21)),
        "Predicted Congestion Level": [10, 18, 25, 40, 50, 70, 80, 90, 60, 40, 30, 20, 15, 10, 8]
    })
    fig = px.line(traffic_data, x="Hour", y="Predicted Congestion Level", markers=True,
                  title="Traffic Congestion Forecast by Hour")
    st.plotly_chart(fig, use_container_width=True)

elif page == "SACCO Login":
    st.title("👥 SACCO Operator Portal")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success("Logged in successfully (demo only)")
        uploaded_file = st.file_uploader("Upload Matatu GPS Data (CSV)", type="csv")
        if uploaded_file:
            data = pd.read_csv(uploaded_file)
            st.write("### Uploaded Route Data", data.head())

elif page == "Planner Zone":
    st.title("🧠 Urban Planner Dashboard")
    area_data = pd.DataFrame({
        "Region": ["CBD", "Westlands", "Ngong Rd", "Embakasi"],
        "Avg Delay (min)": [12, 18, 30, 25],
        "Demand Index": [80, 65, 95, 70]
    })
    fig = px.bar(area_data, x="Region", y="Avg Delay (min)", color="Demand Index", title="Average Delays and Demand")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Contact":
    st.title("📬 Contact & Collaborate")
    st.markdown("""
    Are you a SACCO, government planner, or transport tech enthusiast?

    **We'd love to collaborate!**

    📧 Email: smartroutes@project.ai  
    🌐 LinkedIn: SmartRoutes Team  
    📝 Fill out this form to get in touch.
    """)
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Submit")
