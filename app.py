import streamlit as st
import pandas as pd
import pickle
import base64
st.set_page_config(
    page_title="🏗️ Construction Cost Estimation",
    page_icon="🏗️",
    layout="wide"
)
model = pickle.load(open("model.pkl", "rb"))
st.markdown("""
<div class="main-title">
🏗️ Construction Project Cost Estimation System
</div>
""", unsafe_allow_html=True)
st.markdown("### Predict the estimated construction cost using Machine Learning")
st.markdown("---")
#---------------------------------
#background image
#---------------------------------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
img = get_base64("background.jpg")

st.markdown(f"""
<style>
.stApp {{
    background: url("data:image/jpeg;base64,{img}") no-repeat center center fixed;
    background-size: cover;}}
[data-testid="stHeader"] {{background: rgba(0,0,0,0);}}
[data-testid="stToolbar"] {{background: rgba(0,0,0,0);}}
.main > div {{background-color: rgba(0,0,0,0.55);padding:20px;border-radius:15px;}}
h1,h2,h3,p,label,span {{ color:white !important;}}
</style>
""", unsafe_allow_html=True)

left,right=st.columns(2)
with left:
    st.subheader("🏠 Building Details")
    area=st.number_input("Area (sq.ft)",500,10000,1500)
    floors=st.selectbox("Floors",[1,2,3,4,5])
    bedrooms=st.selectbox("Bedrooms",[1,2,3,4,5,6])
    bathrooms=st.selectbox("Bathrooms",[1,2,3,4,5])
    material_quality=st.selectbox(
        "Material Quality",
        ["Low","Medium","High"]
    )
    location=st.selectbox(
        "Location",
        ["Urban","Suburban","Rural"]
    )
with right:
    st.subheader("🏢 Project Details")
    project_type=st.selectbox(
        "Project Type",
        ["Residential","Commercial"]
    )
    labor_cost=st.number_input("Labor Cost",100000,5000000,300000)
    cement_price=st.number_input("Cement Price",200,600,380)
    steel_price=st.number_input("Steel Price",30,120,65)
    construction_time=st.slider("Construction Time",4,36,12)
    contractor_rating=st.slider("Contractor Rating",1,5,3)
if st.button("💰 Estimate Construction Cost"):
    input_data = pd.DataFrame({
    "Material_Quality": [material_quality],
    "Location": [location],
    "Project_Type": [project_type],
    "Area_sqft": [area],
    "Floors": [floors],
    "Bedrooms": [bedrooms],
    "Bathrooms": [bathrooms],
    "Labor_Cost": [labor_cost],
    "Cement_Price": [cement_price],
    "Steel_Price": [steel_price],
    "Construction_Time": [construction_time],
    "Contractor_Rating": [contractor_rating]
     })
    prediction = model.predict(input_data)[0]
    st.markdown(f"""
    <div class="result-card">
    <div class="cost-title">💰 Estimated Construction Cost</div>
    <div class="cost-value">₹ {prediction:,.2f}</div></div>""", unsafe_allow_html=True)
    st.subheader("📋 Project Summary")
    st.write(f"**Area:** {area} sq.ft")
    st.write(f"**Floors:** {floors}")
    st.write(f"**Bedrooms:** {bedrooms}")
    st.write(f"**Bathrooms:** {bathrooms}")
    st.write(f"**Material Quality:** {material_quality}")
    st.write(f"**Location:** {location}")
    st.write(f"**Project Type:** {project_type}")
    st.write(f"**Construction Time:** {construction_time} Months")
    st.write(f"**Contractor Rating:** ⭐ {contractor_rating}")
st.markdown(f"""
<style>

/* ================= Background ================= */
.stApp {{
    background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
                url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Remove header background */
[data-testid="stHeader"] {{
    background: transparent;
}}
[data-testid="stToolbar"] {{
    background: transparent;
}}

/* ================= Main Container ================= */
.main > div {{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding:25px;
    border-radius:20px;
}}

/* ================= Headings ================= */
.main-title{{
    font-size:58px;
    font-weight:900;
    color:#FFFFFF;
    text-align:center;
    letter-spacing:1px;
    text-shadow:0px 4px 12px rgba(0,0,0,0.6);
}}
h2 {{
    color:#FFD54F !important;
    font-weight:700 !important;
}}
h3 {{
    color:#FFFFFF !important;
    font-weight:600 !important;
}}
p, label, span {{
    color:white !important;
    font-size:18px;
}}
strong {{
    color:#FFD54F;
}}

/* ================= Sidebar ================= */
[data-testid="stSidebar"] {{
    background:rgba(15,23,42,0.95);
}}
[data-testid="stSidebar"] * {{
    color:white !important;
}}
[data-testid="stSidebar"] .stExpander {{
    background:rgba(255,255,255,0.08);
    border-radius:10px;
}}

/* ================= Inputs ================= */

.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stTextInput input {{
    background:white !important;
    color:black !important;
    border-radius:10px;
}}

/* ================= Slider ================= */

.stSlider label {{
    color:white !important;
}}
.stSlider span {{
    color:white !important;
}}
/* ================= Button ================= */
.stButton>button{{
    width:100%;
    height:70px;
    font-size:48px;
    font-weight:bold;
    color:white;
    border:none;
    border-radius:18px;
    background:linear-gradient(90deg,#FF9800,#F44336);
}}
.stButton>button:hover{{
    background:linear-gradient(90deg,#F44336,#E91E63);
    transform:scale(1.03);
}}

/* ================= Metric Card ================= */
.result-card{{
    background:linear-gradient(135deg,#1565C0,#42A5F5);
    padding:25px;
    border-radius:20px;
    text-align:center;
}}

/* Cost title */
.cost-title{{
    font-size:50px !important;
    font-weight:800;
    color:#FFE082 !important;
    margin-bottom:30px;
}}

/* Predicted amount */
.cost-value{{
    font-size:48px !important;
    font-weight:700;
    color:white !important;
    letter-spacing:2px;
}}
""", unsafe_allow_html=True)
# ===========================
# Sidebar
# ===========================
st.sidebar.image("construction.webp",use_container_width=True)
st.sidebar.title("Navigation")
st.sidebar.markdown("""
<h3 style="font-size:30px; color:white;">
🏗️ Construction Cost Estimation
</h3>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.markdown("""
<style>

/* Increase sidebar width */
section[data-testid="stSidebar"]{
    width: 420px !important;
}

section[data-testid="stSidebar"] > div{
    width: 420px !important;
}

</style>
""", unsafe_allow_html=True)
st.sidebar.info("""
**Machine Learning Project**

Predict the estimated construction cost using
Random Forest Regression.
""")

st.sidebar.markdown("---")

with st.sidebar.expander("📌 Project Objective"):
    st.write("""
- Predict construction project cost.
- Reduce manual estimation.
- Improve accuracy.
- Provide quick cost estimation.
""")

with st.sidebar.expander("⚙️ Technologies Used"):
    st.write("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Streamlit
""")

with st.sidebar.expander("🤖 Machine Learning Model"):
    st.write("""
**Algorithm Used**

✅ Random Forest Regressor
""")

with st.sidebar.expander("📊 Input Features"):
    st.write("""
- Area (sq.ft)
- Floors
- Bedrooms
- Bathrooms
- Material Quality
- Location
- Project Type
- Labor Cost
- Cement Price
- Steel Price
- Construction Time
- Contractor Rating
""")

with st.sidebar.expander("🎯 Output"):
    st.write("""
Estimated Total Construction Cost (₹)
""")

with st.sidebar.expander("✨ Advantages"):
    st.write("""
- Fast Prediction
- User Friendly
- Accurate Estimation
- Saves Time
- Easy Planning
""")

with st.sidebar.expander("🏢 Applications"):
    st.write("""
- Construction Companies
- Civil Engineers
- Contractors
- Architects
- Real Estate Developers
""")

with st.sidebar.expander("🚀 Future Scope"):
    st.write("""
- Live Material Price API
- Cost Breakdown
- PDF Report
- Cloud Deployment
- User Login System
""")

st.sidebar.markdown("---")
st.caption("Developed by Snehal Kolekar using Machine Learning (Random Forest Regression) & Streamlit")
