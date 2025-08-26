# app.py
import streamlit as st
import pandas as pd
import time
import random

# Custom CSS for professional styling
st.markdown("""
<style>
    .header {
        background: linear-gradient(135deg, #1f77b4 0%, #003f5c 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #1f77b4 0%, #003f5c 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
    }
    
    [data-testid=stSidebar] {
        background-color: #f8f9fa;
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
        from PIL import Image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded X-ray", use_container_width=True)
        
        # Model Integration Placeholder
        st.info("MODEL INTEGRATION PLACEHOLDER: Replace with actual model prediction code")
        
        # Simulate AI analysis
        with st.spinner("Analyzing X-ray with ScITODel-CNN..."):
            time.sleep(2)
            
        # Results display
        st.markdown("### Analysis Results")
        col1, col2, col3 = st.columns(3)
        
        # Mock prediction results
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
    
    st.info("Normal and COVID-19 X-ray images would be displayed here")
    
    # Annotation tools
    st.markdown("### Annotation Tools")
    annotation_mode = st.radio("Select Tool", ["Select Region", "Draw ROI", "Measure Distance"])
    
    # Heatmap overlay simulation
    st.markdown("### AI Heatmap Overlay")
    st.info("AI-detected abnormal regions would be highlighted here")
    
    # Model Performance Metrics Section
    st.markdown("### Model Performance Metrics")
    st.info("MODEL EVALUATION INTEGRATION PLACEHOLDER")
    
    # Detailed metrics using tables
    st.markdown("### Performance Statistics")
    
    # Metrics data as table
    metrics_data = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC'],
        'Value': ['94.2%', '92.8%', '95.1%', '93.9%', '96.7%']
    }
    metrics_df = pd.DataFrame(metrics_data)
    st.table(metrics_df)
    
    # Confusion matrix as table
    st.markdown("### Confusion Matrix")
    confusion_data = pd.DataFrame(
        [[850, 25], [30, 895]], 
        index=['Actual Normal', 'Actual COVID'],
        columns=['Predicted Normal', 'Predicted COVID']
    )
    st.table(confusion_data)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Policy Maker View
else:
    st.markdown("## Policy Dashboard")
    
    # Key metrics overview
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Key Performance Indicators")
    
    st.info("REAL-TIME DATA INTEGRATION PLACEHOLDER")
    
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
    
    # Regional data as table
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Regional Case Distribution")
    
    regional_data = pd.DataFrame({
        'Region': ['North', 'South', 'East', 'West', 'Central'],
        'Cases': [2847, 2156, 3201, 1987, 2356],
        'Recovery Rate (%)': [87, 82, 89, 85, 91]
    })
    
    st.table(regional_data)
    
    # System performance data
    st.markdown("### System Performance Data")
    dates = pd.date_range('2024-01-01', periods=10, freq='D')
    performance_data = pd.DataFrame({
        'Date': dates.strftime('%Y-%m-%d'),
        'Accuracy (%)': [94.2, 93.8, 94.5, 94.1, 94.7, 94.3, 94.8, 94.2, 94.6, 94.4],
        'Response Time (s)': [2.3, 2.5, 2.1, 2.4, 2.0, 2.2, 1.9, 2.3, 2.1, 2.2]
    })
    
    st.table(performance_data)
    
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
