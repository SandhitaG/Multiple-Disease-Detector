import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🩺")

# Load models
diabetes_model = pickle.load(open('C:/Users/user/Desktop/New/sav_files/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/user/Desktop/New/sav_files/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/user/Desktop/New/sav_files/parkinsons_model.sav', 'rb'))
malaria_model = pickle.load(open('C:/Users/user/Desktop/New/sav_files/malaria_prediction_model.sav', 'rb'))
pox_model = pickle.load(open('C:/Users/user/Desktop/New/sav_files/pox_model.sav', 'rb'))
tb_model = pickle.load(open('C:/Users/user/Desktop/New/sav_files/TB_model.sav', 'rb'))

def display_legend(disease):
    """Display a legend for the given disease explaining the parameters."""
    if disease == 'Diabetes Prediction':
        st.subheader("Diabetes Prediction Parameters:")
        st.write("""
        - **Number of Pregnancies**: The number of times the individual has been pregnant.
        - **Glucose Level**: The blood glucose level measured in mg/dL.
        - **Blood Pressure**: The blood pressure value measured in mmHg.
        - **Skin Thickness**: The thickness of the skin at the triceps, measured in mm.
        - **Insulin Level**: The level of insulin in the blood measured in IU/mL.
        - **BMI**: Body Mass Index calculated using height and weight.
        - **Diabetes Pedigree Function**: A function that indicates the likelihood of diabetes based on family history.
        - **Age**: Age of the individual in years.
        """)

    elif disease == 'Heart Disease Prediction':
        st.subheader("Heart Disease Prediction Parameters:")
        st.write("""
        - **Age**: Age of the individual in years.
        - **Sex**: Gender of the individual (1 = male, 0 = female).
        - **Chest Pain Types**: Type of chest pain experienced (values range from 0 to 3).
        - **Resting Blood Pressure**: Blood pressure when at rest, measured in mmHg.
        - **Serum Cholesterol**: Cholesterol level in mg/dL.
        - **Fasting Blood Sugar**: Blood sugar level (1 = > 120 mg/dL, 0 = < 120 mg/dL).
        - **Resting Electrocardiographic Results**: Results from an electrocardiogram (values range from 0 to 2).
        - **Maximum Heart Rate Achieved**: The maximum heart rate achieved during exercise.
        - **Exercise Induced Angina**: Indicates if angina was induced by exercise (1 = yes, 0 = no).
        - **ST Depression**: ST depression induced by exercise, measured in mm.
        - **Slope of Peak Exercise ST Segment**: Slope of the ST segment during exercise.
        - **Major Vessels**: Number of major vessels colored by fluoroscopy (values range from 0 to 3).
        - **Thalassemia**: A blood disorder (values range from 0 to 3).
        """)

    elif disease == "Parkinsons Prediction":
        st.subheader("Parkinson's Prediction Parameters:")
        st.write("""
        - **MDVP:Fo**: Fundamental frequency (Hz).
        - **MDVP:Fhi**: Maximum fundamental frequency (Hz).
        - **MDVP:Flo**: Minimum fundamental frequency (Hz).
        - **MDVP:Jitter(%)**: Percent jitter (variability in frequency).
        - **MDVP:Jitter(Abs)**: Absolute jitter (msec).
        - **MDVP:RAP**: Relative Average Perturbation.
        - **MDVP:PPQ**: Pitch Perturbation Quotient.
        - **Jitter:DDP**: DDP (the difference in deviation of pitch).
        - **MDVP:Shimmer**: Amplitude variation (measure of loudness).
        - **MDVP:Shimmer(dB)**: Shimmer in decibels.
        - **Shimmer:APQ3**: Shimmer APQ3.
        - **Shimmer:APQ5**: Shimmer APQ5.
        - **MDVP:APQ**: Amplitude Perturbation Quotient.
        - **Shimmer:DDA**: DDA (the difference in deviation of amplitude).
        - **NHR**: Normalized Harmonics-to-Noise Ratio.
        - **HNR**: Harmonics-to-Noise Ratio.
        - **RPDE**: Recurrence Period Density Entropy.
        - **DFA**: Detrended Fluctuation Analysis.
        - **spread1**: Spread 1 parameter.
        - **spread2**: Spread 2 parameter.
        - **D2**: D2 (a measure of the vocal signal).
        - **PPE**: Pitch Period Entropy.
        """)

    elif disease == 'Malaria Prediction':
        st.subheader("Malaria Prediction Parameters:")
        st.write("""
        - **Fever**: Indicates if the individual has fever (1 = yes, 0 = no).
        - **Chills**: Indicates if the individual has chills (1 = yes, 0 = no).
        - **Headache**: Indicates if the individual has headache (1 = yes, 0 = no).
        - **Sweating**: Indicates if the individual has sweating (1 = yes, 0 = no).
        - **Nausea**: Indicates if the individual has nausea (1 = yes, 0 = no).
        - **Vomiting**: Indicates if the individual has vomiting (1 = yes, 0 = no).
        - **Fatigue**: Indicates if the individual feels fatigued (1 = yes, 0 = no).
        - **Recent Travel History**: Indicates if the individual has traveled recently (1 = yes, 0 = no).
        - **Anemia**: Indicates if the individual has anemia (1 = yes, 0 = no).
        """)

    elif disease == 'Chicken Pox Prediction':
        st.subheader("Chicken Pox Prediction Parameters:")
        st.write("""
        - **Fever**: Indicates if the individual has fever (1 = yes, 0 = no).
        - **Rash**: Indicates if the individual has rashes (1 = yes, 0 = no).
        - **Itching**: Indicates if the individual feels itching (1 = yes, 0 = no).
        - **Fatigue**: Indicates if the individual feels fatigued (1 = yes, 0 = no).
        - **Headache**: Indicates if the individual has headache (1 = yes, 0 = no).
        - **Loss of Appetite**: Indicates if the individual has loss of appetite (1 = yes, 0 = no).
        - **Recent Travel History**: Indicates if the individual has traveled recently (1 = yes, 0 = no).
        """)
    
    elif disease == 'Tuberculosis Prediction':
        st.subheader("Tuberculosis Prediction Parameters:")
        st.write("""
        - **Cough**: Indicates if the individual has cough (1 = yes, 0 = no).
        - **Fever**: Indicates if the individual has fever (1 = yes, 0 = no).
        - **Weight Loss**: Indicates if the individual has lost weight (1 = yes, 0 = no).
        - **Night Sweat**: Indicates if the individual sweats during night (1 = yes, 0 = no).
        - **Fatigue**: Indicates if the individual feels fatigued (1 = yes, 0 = no).
        - **Shortness of Breath**: Indicates if the individual suffers from shortness of breath (1 = yes, 0 = no).
        - **Contact History**: Indicates if the individual has had any contact with anyone(1 = yes, 0 = no).
        """)
        

# Now call display_legend function in each disease prediction section


# Define a utility function for displaying results with color coding
def display_result(message, is_positive):
    if is_positive:
        st.markdown(f"<div style='color: #d9534f; font-size:18px;'>🔴 {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color: #5cb85c; font-size:18px;'>🟢 {message}</div>", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction", "Malaria Prediction", "Chicken Pox Prediction","Tuberculosis Prediction"],
        icons=["activity", "heart", "person", "bug", "virus","info-circle"],
        menu_icon="hospital-fill",
        default_index=0
    )

# Main Content Area
st.title("Health Assistant 🩺")
st.write("Welcome to the Health Assistant! Select a disease from the sidebar to begin.")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    display_legend('Diabetes Prediction')
    st.header("Diabetes Prediction")
    st.write("**Predict the likelihood of diabetes based on health metrics.**")
    
    with st.form("diabetes_form"):
        col1, col2, col3 = st.columns(3)
        with col1: Pregnancies = st.number_input('Pregnancies', min_value=0, step=1)
        with col2: Glucose = st.number_input('Glucose Level', min_value=0)
        with col3: BloodPressure = st.number_input('Blood Pressure', min_value=0)
        with col1: SkinThickness = st.number_input('Skin Thickness', min_value=0)
        with col2: Insulin = st.number_input('Insulin Level', min_value=0)
        with col3: BMI = st.number_input('BMI', min_value=0.0)
        with col1: DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0)
        with col2: Age = st.number_input('Age', min_value=0, step=1)
        submit_button = st.form_submit_button("Get Diabetes Test Result")

    if submit_button:
        with st.spinner("Processing..."):
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            prediction = diabetes_model.predict([user_input])[0]
            if prediction == 1:
                display_result("The person is diabetic.", is_positive=True)
            else:
                display_result("The person is not diabetic.", is_positive=False)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    display_legend('Heart Disease Prediction')
    st.header("Heart Disease Prediction")
    st.write("**Enter health information to predict the likelihood of heart disease.**")
    
    with st.form("heart_form"):
        col1, col2, col3 = st.columns(3)
        with col1: age = st.number_input('Age', min_value=0, step=1)
        with col2: sex = st.selectbox('Sex', options=['Male', 'Female'])
        with col3: cp = st.number_input('Chest Pain Type', min_value=0, max_value=3)
        with col1: trestbps = st.number_input('Resting Blood Pressure', min_value=0)
        with col2: chol = st.number_input('Cholesterol Level', min_value=0)
        with col3: fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
        with col1: restecg = st.number_input('Resting ECG Results', min_value=0, max_value=2)
        with col2: thalach = st.number_input('Max Heart Rate Achieved', min_value=0)
        with col3: exang = st.selectbox('Exercise Induced Angina', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
        with col1: oldpeak = st.number_input('ST Depression', min_value=0.0)
        with col2: slope = st.number_input('Slope of ST Segment', min_value=0, max_value=2)
        with col3: ca = st.number_input('Major Vessels', min_value=0, max_value=4)
        with col1: thal = st.number_input('Thalassemia', min_value=0, max_value=3)
        submit_button = st.form_submit_button("Get Heart Disease Test Result")

    if submit_button:
        with st.spinner("Processing..."):
            user_input = [age, int(sex == 'Male'), cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            prediction = heart_disease_model.predict([user_input])[0]
            if prediction == 1:
                display_result("The person is likely to have heart disease.", is_positive=True)
            else:
                display_result("The person is unlikely to have heart disease.", is_positive=False)

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    display_legend("Parkinsons Prediction")
    st.header("Parkinson's Disease Prediction")
    st.write("*Enter symptoms to check for Parkinson's disease risk.*")
    
    with st.form("parkinsons_form"):
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: fo = st.text_input('MDVP:Fo(Hz)')
        with col2: fhi = st.text_input('MDVP:Fhi(Hz)')
        with col3: flo = st.text_input('MDVP:Flo(Hz)')
        with col4: Jitter_percent = st.text_input('MDVP:Jitter(%)')
        with col5: Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        with col1: RAP = st.text_input('MDVP:RAP')
        with col2: PPQ = st.text_input('MDVP:PPQ')
        with col3: DDP = st.text_input('Jitter:DDP')
        with col4: Shimmer = st.text_input('MDVP:Shimmer')
        with col5: Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        with col1: APQ3 = st.text_input('Shimmer:APQ3')
        with col2: APQ5 = st.text_input('Shimmer:APQ5')
        with col3: APQ = st.text_input('MDVP:APQ')
        with col4: DDA = st.text_input('Shimmer:DDA')
        with col5: NHR = st.text_input('NHR')
        with col1: HNR = st.text_input('HNR')
        with col2: RPDE = st.text_input('RPDE')
        with col3: DFA = st.text_input('DFA')
        with col4: spread1 = st.text_input('spread1')
        with col5: spread2 = st.text_input('spread2')
        with col1: D2 = st.text_input('D2')
        with col2: PPE = st.text_input('PPE')
        submit_button = st.form_submit_button("Get Parkinson's Test Result")

    if submit_button:
        with st.spinner("Processing..."):
            # Collect user inputs for prediction
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            
            # Perform prediction and handle possible errors
            try:
                prediction = parkinsons_model.predict([user_input])[0]
                if prediction == 1:
                    display_result("The person has Parkinson's disease.", is_positive=True)
                else:
                    display_result("The person does not have Parkinson's disease.", is_positive=False)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                
# Malaria Prediction Page
if selected == 'Malaria Prediction':
    display_legend('Malaria Prediction')
    st.header("Malaria Prediction")
    st.write("**Select symptoms to check for Malaria risk.**")

    with st.form("malaria_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1: Fever = st.selectbox('Fever', ['No', 'Yes'])
        with col2: Chills = st.selectbox('Chills', ['No', 'Yes'])
        with col3: Headache = st.selectbox('Headache', ['No', 'Yes'])
        with col1: Sweating = st.selectbox('Sweating', ['No', 'Yes'])
        with col2: Nausea = st.selectbox('Nausea', ['No', 'Yes'])
        with col3: Vomiting = st.selectbox('Vomiting', ['No', 'Yes'])
        with col1: Fatigue = st.selectbox('Fatigue', ['No', 'Yes'])
        with col2: Travel_History = st.selectbox('Recent Travel History', ['No', 'Yes'])
        with col3: Anemia = st.selectbox('Anemia', ['No', 'Yes'])
        
        submit_button = st.form_submit_button("Get Malaria Test Result")

    if submit_button:
        with st.spinner("Processing..."):
            # Convert 'Yes'/'No' to 1/0 for model input
            user_input = [1 if x == 'Yes' else 0 for x in 
                          [Fever, Chills, Headache, Sweating, Nausea, Vomiting, Fatigue, Travel_History, Anemia]]
            
            # Perform prediction and handle possible errors
            try:
                prediction = malaria_model.predict([user_input])[0]
                if prediction == 1:
                    display_result("The person has Malaria.", is_positive=True)
                else:
                    display_result("The person does not have Malaria.", is_positive=False)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Chicken Pox Prediction Page
if selected == 'Chicken Pox Prediction':
    display_legend('Chicken Pox Prediction')
    st.header("Chicken Pox Prediction")
    st.write("**Select symptoms to check for Chicken Pox risk.**")

    with st.form("chicken_pox_form"):
        col1, col2 = st.columns(2)
        
        with col1: Fever = st.selectbox('Fever', ['No', 'Yes'])
        with col2: Rash = st.selectbox('Rash', ['No', 'Yes'])
        with col1: Itching = st.selectbox('Itching', ['No', 'Yes'])
        with col2: Fatigue = st.selectbox('Fatigue', ['No', 'Yes'])
        with col1: Headache = st.selectbox('Headache', ['No', 'Yes'])
        with col2: Loss_of_Appetite = st.selectbox('Loss of Appetite', ['No', 'Yes'])
        with col1: Travel_History = st.selectbox('Recent Travel History', ['No', 'Yes'])
        
        submit_button = st.form_submit_button("Get Chicken Pox Test Result")

    if submit_button:
        with st.spinner("Processing..."):
            # Convert 'Yes'/'No' to 1/0 for model input
            user_input = [1 if x == 'Yes' else 0 for x in 
                          [Fever, Rash, Itching, Fatigue, Headache, Loss_of_Appetite, Travel_History]]
            
            # Perform prediction and handle possible errors
            try:
                prediction = pox_model.predict([user_input])[0]
                if prediction == 1:
                    display_result("The person has Chicken Pox.", is_positive=True)
                else:
                    display_result("The person does not have Chicken Pox.", is_positive=False)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Chicken Pox Prediction Page
if selected == 'Tuberculosis Prediction':
    display_legend('Tuberculosis Prediction')
    st.header("Tuberculosis Prediction")
    st.write("**Select symptoms to check for Tuberculosis risk.**")

    with st.form("tuberculosis_form"):
        col1, col2 = st.columns(2)
        
        with col1: Cough = st.selectbox('Cough', ['No', 'Yes'])
        with col2: Fever = st.selectbox('Fever', ['No', 'Yes'])
        with col1: Weight_Loss = st.selectbox('Weight Loss', ['No', 'Yes'])
        with col2: Night_Sweats = st.selectbox('Night Sweats', ['No', 'Yes'])
        with col1: Fatigue = st.selectbox('Fatigue', ['No', 'Yes'])
        with col2: Shortness_of_Breath = st.selectbox('Shortness of Breath', ['No', 'Yes'])
        with col1: Contact_History = st.selectbox('Contact History', ['No', 'Yes'])
        
        submit_button = st.form_submit_button("Get Tuberculosis Test Result")

    if submit_button:
        with st.spinner("Processing..."):
            # Convert 'Yes'/'No' to 1/0 for model input
            user_input = [1 if x == 'Yes' else 0 for x in 
                          [Cough, Fever,Weight_Loss, Night_Sweats, Fatigue, Shortness_of_Breath,Contact_History]]
            
            # Perform prediction and handle possible errors
            try:
                prediction = pox_model.predict([user_input])[0]
                if prediction == 1:
                    display_result("The person has Tuberculosis.", is_positive=True)
                else:
                    display_result("The person does not have Tuberculosis.", is_positive=False)
            except Exception as e:
                st.error(f"An error occurred: {e}")



