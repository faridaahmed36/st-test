import streamlit as st
import requests
import json

# URL of the Flask API
API_URL = "http://localhost:8000/predict"

# Function to send POST request to Flask API
def predict_risk_level(data):
    try:
        response = requests.post(API_URL, json=data)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Streamlit form for user input
st.title("Risk Level Prediction")
st.write("Fill in the patient data to get the risk level prediction.")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=0, max_value=120, value=25)
temperature = st.number_input("Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)
oxygen = st.number_input("Oxygen Saturation (%)", min_value=0.0, max_value=100.0, value=98.0)
respiration_rate = st.number_input("Respiration Rate (breaths/min)", min_value=0, max_value=50, value=16)
lower_bp = st.number_input("Lower Blood Pressure (mm Hg)", min_value=0, max_value=200, value=80)
upper_bp = st.number_input("Upper Blood Pressure (mm Hg)", min_value=0, max_value=300, value=120)
pulse = st.number_input("Pulse (beats/min)", min_value=0, max_value=200, value=70)

# Symptoms checkboxes
allergy = st.checkbox("Allergy")
asthma = st.checkbox("Asthma")
cardiac_arrest = st.checkbox("Cardiac Arrest")
carditis = st.checkbox("Carditis")
crushing_injury = st.checkbox("Crushing Injury")
dizziness = st.checkbox("Dizziness")
paralysis = st.checkbox("Paralysis")
wheezing = st.checkbox("Wheezing")
bleeding_or_bruising = st.checkbox("Bleeding or Bruising")
arm_injury = st.checkbox("Arm Injury")
facial_injury = st.checkbox("Facial Injury")
leg_injury = st.checkbox("Leg Injury")
hand_injury = st.checkbox("Hand Injury")
unresponsive = st.checkbox("Unresponsive")
trauma = st.checkbox("Trauma")
full_trauma = st.checkbox("Full Trauma")
syncope = st.checkbox("Syncope")
shortness_of_breath = st.checkbox("Shortness of Breath")
rapid_heart_rate = st.checkbox("Rapid Heart Rate")
panic_attack = st.checkbox("Panic Attack")
palpitations = st.checkbox("Palpitations")
pain = st.checkbox("Pain")
numbness = st.checkbox("Numbness")
near_syncope = st.checkbox("Near Syncope")
nausea = st.checkbox("Nausea")
chest_pain = st.checkbox("Chest Pain")
fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
dysrhythmia = st.checkbox("Dysrhythmia")
eye_injury = st.checkbox("Eye Injury")
migraine = st.checkbox("Migraine")
loss_of_consciousness = st.checkbox("Loss of Consciousness")
irregular_heartbeat = st.checkbox("Irregular Heartbeat")
hypotension = st.checkbox("Hypotension")
hypertension = st.checkbox("Hypertension")
hyperglycemia = st.checkbox("Hyperglycemia")
low_blood_sugar_symptoms = st.checkbox("Low Blood Sugar Symptoms")
hemoptysis = st.checkbox("Hemoptysis")
head_laceration = st.checkbox("Head Laceration")
head_injury = st.checkbox("Head Injury")
epistaxis = st.checkbox("Epistaxis")
blurred_vision = st.checkbox("Blurred Vision")

# Collect input data
input_data = {
    "gender": gender,
    "age": age,
    "temperature": temperature,
    "oxygen": oxygen,
    "respiration_rate": respiration_rate,
    "lower_bp": lower_bp,
    "upper_bp": upper_bp,
    "pulse": pulse,
    "allergy": int(allergy),
    "asthma": int(asthma),
    "cardiac_arrest": int(cardiac_arrest),
    "carditis": int(carditis),
    "crushing_injury": int(crushing_injury),
    "dizziness": int(dizziness),
    "paralysis": int(paralysis),
    "wheezing": int(wheezing),
    "bleeding_or_bruising": int(bleeding_or_bruising),
    "arm_injury": int(arm_injury),
    "facial_injury": int(facial_injury),
    "leg_injury": int(leg_injury),
    "hand_injury": int(hand_injury),
    "unresponsive": int(unresponsive),
    "trauma": int(trauma),
    "full_trauma": int(full_trauma),
    "syncope": int(syncope),
    "shortness_of_breath": int(shortness_of_breath),
    "rapid_heart_rate": int(rapid_heart_rate),
    "panic_attack": int(panic_attack),
    "palpitations": int(palpitations),
    "pain": int(pain),
    "numbness": int(numbness),
    "near_syncope": int(near_syncope),
    "nausea": int(nausea),
    "chest_pain": int(chest_pain),
    "fever": int(fever),
    "cough": int(cough),
    "dysrhythmia": int(dysrhythmia),
    "eye_injury": int(eye_injury),
    "migraine": int(migraine),
    "loss_of_consciousness": int(loss_of_consciousness),
    "irregular_heartbeat": int(irregular_heartbeat),
    "hypotension": int(hypotension),
    "hypertension": int(hypertension),
    "hyperglycemia": int(hyperglycemia),
    "low_blood_sugar_symptoms": int(low_blood_sugar_symptoms),
    "hemoptysis": int(hemoptysis),
    "head_laceration": int(head_laceration),
    "head_injury": int(head_injury),
    "epistaxis": int(epistaxis),
    "blurred_vision": int(blurred_vision)
}

# Submit button
if st.button("Predict Risk Level"):
    with st.spinner('Predicting...'):
        prediction = predict_risk_level(input_data)
    st.success('Prediction completed!')

    if "error" in prediction:
        st.error(f"Error: {prediction['error']}")
    else:
        st.subheader("Risk Level Prediction")
        st.write(f"Risk Level: {prediction['risk_level']}")
        st.write("Predicted Probabilities:")
        st.write(f"Critical: {prediction['predicted_probabilities']['critical']:.2f}")
        st.write(f"Urgent: {prediction['predicted_probabilities']['urgent']:.2f}")
        st.write(f"Non-Urgent: {prediction['predicted_probabilities']['non-urgent']:.2f}")
