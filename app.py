import streamlit as st
import joblib
import pandas as pd

model = joblib.load('mobile_price_pipeline.pkl')

st.title("📱 Mobile Price Range Predictor")
st.write("Specifications daalo, model predict karega price range (Low/Medium/High/Very High)")

col1, col2 = st.columns(2)

with col1:
    battery_power = st.slider("Battery Power (mAh)", 500, 2000, 1200)
    blue = st.selectbox("Bluetooth", [0, 1])
    clock_speed = st.slider("Clock Speed (GHz)", 0.5, 3.0, 1.5)
    dual_sim = st.selectbox("Dual SIM", [0, 1])
    fc = st.slider("Front Camera (MP)", 0, 20, 5)
    four_g = st.selectbox("4G", [0, 1])
    int_memory = st.slider("Internal Memory (GB)", 2, 64, 32)
    m_dep = st.slider("Mobile Depth (cm)", 0.1, 1.0, 0.5)
    mobile_wt = st.slider("Mobile Weight (g)", 80, 200, 140)
    n_cores = st.slider("Number of Cores", 1, 8, 4)

with col2:
    pc = st.slider("Primary Camera (MP)", 0, 20, 10)
    px_height = st.slider("Pixel Height", 0, 1960, 800)
    px_width = st.slider("Pixel Width", 500, 2000, 1200)
    ram = st.slider("RAM (MB)", 256, 4000, 2000)
    sc_h = st.slider("Screen Height (cm)", 5, 20, 12)
    sc_w = st.slider("Screen Width (cm)", 0, 18, 7)
    talk_time = st.slider("Talk Time (hrs)", 2, 20, 10)
    three_g = st.selectbox("3G", [0, 1])
    touch_screen = st.selectbox("Touch Screen", [0, 1])
    wifi = st.selectbox("WiFi", [0, 1])

if st.button("Predict Price Range"):
    input_data = pd.DataFrame([[battery_power, blue, clock_speed, dual_sim, fc, four_g,
                                  int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
                                  px_width, ram, sc_h, sc_w, talk_time, three_g,
                                  touch_screen, wifi]],
                                columns=['battery_power','blue','clock_speed','dual_sim','fc',
                                         'four_g','int_memory','m_dep','mobile_wt','n_cores',
                                         'pc','px_height','px_width','ram','sc_h','sc_w',
                                         'talk_time','three_g','touch_screen','wifi'])

    prediction = model.predict(input_data)[0]
    labels = {0: "Low Cost", 1: "Medium Cost", 2: "High Cost", 3: "Very High Cost"}

    st.success(f"Predicted Price Range: **{labels[prediction]}**")
