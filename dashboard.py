# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import time
import random

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main background and text colors */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff7f0e;
        --success-color: #2ca02c;
        --warning-color: #d62728;
        --dark-bg: #0e1117;
        --light-bg: #f0f2f6;
    }
    
    /* Main container styling */
    .main {
        background-color: #ffffff;
    }
    
    /* Header styling */
    .header {
        background: linear-gradient(135deg, #1f77b4 0%, #003f5c 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #1f77b4 0%, #003f5c 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(31, 119, 180, 0.4);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background-color: #2ca02c;
    }
    
    /* Sidebar styling */
    [data-testid=stSidebar] {
        background-color: #f8f9fa;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #e9ecef;
        border-radius: 8px 8px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #1f77b4;
        color: white;
    }
    
    /* Custom icons using CSS */
    .icon-header::before {
        content: "●";
        color: #1f77b4;
        margin-right: 10px;
    }
    
    .icon-metric::before {
        content: "■";
        color: #2ca02c;
        margin-right: 8px;
    }
    
    .icon-chart::before {
        content: "▲";
        color: #ff7f0e;
        margin-right: 8px;
    }
    
    /* Code block styling for model integration notes */
    .model-note {
        background-color: #e9f7fe;
        border-left: 4px solid #1f77b4;
        padding: 15px;
        margin: 15px 0;
        border-radius: 0 8px 8px 0;
        font-family: monospace;
        font-size: 14px;
    }
    
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="header">
    <h1>ScITODel-COVID-19 Detection System</h1>
    <p>AI-Powered X-ray Analysis for Rapid COVID-19 Detection</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    role = st.selectbox("Select Role", ["Doctor", "Radiologist", "Policy Maker"])
    st.markdown("---")
    st.info("System Status: Operational")
    st.success("Last Update: Just now")

# Doctor View
if role == "Doctor":
    st.markdown("## Doctor Dashboard")
    
    # Patient Information Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Patient Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        patient_name = st.text_input("Patient Name", "John Doe")
    with col2:
        # Fixed: Removed minimum age restriction
        patient_age = st.number_input("Age", min_value=0, max_value=120, value=35)
    with col3:
        patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    
    symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Shortness of Breath", "Fatigue", "Loss of Taste/Smell"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # X-ray Upload Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("X-ray Analysis")
    
    uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded X-ray", use_container_width=True)
        
        # Model Integration Placeholder - START
        st.markdown('<div class="model-note">', unsafe_allow_html=True)
        st.markdown("**MODEL INTEGRATION PLACEHOLDER**")
        st.markdown("Replace this section with actual model prediction code:")
        st.code('''
# Example model integration code:
# import your_model_module
# prediction_result = your_model.predict(image)
# confidence_score = your_model.get_confidence(image)
# risk_level = your_model.calculate_risk(image)
        ''', language='python')
        st.markdown('</div>', unsafe_allow_html=True)
        # Model Integration Placeholder - END
        
        # Simulate AI analysis
        with st.spinner("Analyzing X-ray with ScITODel-CNN..."):
            time.sleep(2)
            
        # Results display
        st.markdown("### Analysis Results")
        col1, col2, col3 = st.columns(3)
        
        # Mock prediction results - REPLACE WITH ACTUAL MODEL OUTPUT
        prediction = random.choice(["COVID-19 Positive", "Normal"])
        confidence = random.uniform(85, 98)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Diagnosis", prediction)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Confidence", f"{confidence:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Risk Level", "High" if "Positive" in prediction else "Low")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Confidence progress bar
        st.progress(confidence/100)
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Send to Radiologist"):
                st.success("Case sent to radiologist for review!")
        with col2:
            if st.button("Confirm Diagnosis"):
                st.success("Diagnosis confirmed and recorded!")
                
    else:
        st.info("Please upload a chest X-ray image to begin analysis")
    st.markdown('</div>', unsafe_allow_html=True)

# Radiologist View
elif role == "Radiologist":
    st.markdown("## Radiologist Viewer")
    
    # Image comparison section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("X-ray Comparison")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/NormalChestXRay.jpg/300px-NormalChestXRay.jpg", 
                caption="Normal Chest X-ray", use_container_width=True)
    with col2:
        st.image("https://www.cdc.gov/coronavirus/2019-ncov/images/COVID-19-Chest-Imaging-Example.jpg", 
                caption="COVID-19 Positive X-ray", use_container_width=True)
    
    # Annotation tools
    st.markdown("### Annotation Tools")
    annotation_mode = st.radio("Select Tool", ["Select Region", "Draw ROI", "Measure Distance"])
    
    # Heatmap overlay simulation
    st.markdown("### AI Heatmap Overlay")
    st.info("AI-detected abnormal regions highlighted in red overlay")
    st.image("https://miro.medium.com/max/1400/1*JN9t0U0I6YFVZcsjM4V75A.gif", 
             caption="AI Heatmap Visualization (Simulated)", use_container_width=True)
    
    # Model Performance Metrics Section
    st.markdown("### Model Performance Metrics")
    st.markdown('<div class="model-note">', unsafe_allow_html=True)
    st.markdown("**MODEL EVALUATION INTEGRATION PLACEHOLDER**")
    # st.markdown("Replace this section with actual model evaluation metrics:")
#     st.code('''
# # Example model evaluation integration:
# # metrics = your_model.get_performance_metrics()
# # confusion_matrix = your_model.get_confusion_matrix()
# # roc_curve_data = your_model.get_roc_data()
#         ''', language='python')
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Detailed metrics
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Performance Statistics")
    
    # Metrics data - REPLACE WITH ACTUAL MODEL METRICS
    metrics_data = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC'],
        'Value': [94.2, 92.8, 95.1, 93.9, 96.7]
    }
    metrics_df = pd.DataFrame(metrics_data)
    
    fig = px.bar(metrics_df, x='Metric', y='Value', 
                 color='Metric',
                 color_discrete_sequence=px.colors.sequential.Viridis)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Confusion matrix
    st.markdown("### Confusion Matrix")
    confusion_data = [[850, 25], [30, 895]]
    fig = go.Figure(data=go.Heatmap(
        z=confusion_data,
        x=['Predicted Normal', 'Predicted COVID'],
        y=['Actual Normal', 'Actual COVID'],
        colorscale='Blues'
    ))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Policy Maker View
else:
    st.markdown("## Policy Dashboard")
    
    # Key metrics overview
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Key Performance Indicators")
    
    # Model Integration Note
    st.markdown('<div class="model-note">', unsafe_allow_html=True)
    st.markdown("**REAL-TIME DATA INTEGRATION PLACEHOLDER**")
    st.markdown("Replace mock data with actual system metrics from your models:")
#     st.code('''
# # Example real-time data integration:
# # total_cases = database.get_total_cases()
# # accuracy_rate = model_monitor.get_current_accuracy()
# # response_time = system_monitor.get_avg_response_time()
# # uptime = system_monitor.get_uptime_percentage()
#         ''', language='python')
#     st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Cases", "12,547", "+12%")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Accuracy Rate", "94.2%", "+2.1%")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Avg. Response Time", "2.3s", "-0.5s")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("System Uptime", "99.8%", "+0.1%")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Regional data visualization
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Regional Case Distribution")
    
    # Mock regional data - REPLACE WITH ACTUAL DATA FROM DATABASE
    regional_data = pd.DataFrame({
        'Region': ['North', 'South', 'East', 'West', 'Central'],
        'Cases': [2847, 2156, 3201, 1987, 2356],
        'Recovery Rate': [87, 82, 89, 85, 91]
    })
    
    fig = px.bar(regional_data, x='Region', y='Cases', 
                 color='Cases', 
                 color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)
    
    # Recovery rate chart
    fig2 = px.line(regional_data, x='Region', y='Recovery Rate', 
                   markers=True, title="Recovery Rates by Region")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # System performance
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("System Performance")
    
    # Timeline data - REPLACE WITH ACTUAL SYSTEM METRICS
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    performance_data = pd.DataFrame({
        'Date': dates,
        'Accuracy': np.random.normal(94, 2, 30),
        'Response_Time': np.random.normal(2.5, 0.5, 30)
    })
    
    tab1, tab2 = st.tabs(["Accuracy Trend", "Response Time"])
    
    with tab1:
        fig3 = px.line(performance_data, x='Date', y='Accuracy',
                       title="Model Accuracy Over Time")
        fig3.add_hline(y=92, line_dash="dash", line_color="red", 
                       annotation_text="Minimum Threshold")
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab2:
        fig4 = px.line(performance_data, x='Date', y='Response_Time',
                       title="System Response Time (seconds)")
        st.plotly_chart(fig4, use_container_width=True)
    
    # Export options
    st.markdown("### Export Data")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export Report (PDF)"):
            st.success("Report exported successfully!")
    with col2:
        if st.button("Export Data (CSV)"):
            st.success("Data exported successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>Powered by ScITODel-CNN - IoT-Enabled COVID-19 Detection System</p>
    <p>© 2025 Medical AI Research Team</p>
</div>
""", unsafe_allow_html=True)