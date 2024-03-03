
import streamlit as st

def get_medication(disease):
    medications = {
        'Fever': ['Paracetamol', 'Dolo-650mg', 'Zerodol Sp', 'Ibuprofen', 'Diclofenac'],
        'Cold': ['Monteleucast (Montina-L)', 'Cetrizine', 'ALTRIZ-M', 'ASTADIN', 'Coriminic (for common cold)'],
        'Fever+cold': ['Cheston cold', 'Peacemol-D', 'ECICLO-SP', 'Crocin C&F max'],
        'Vomitings': ['Ondansetron (Periset MD)', 'Vomikind-Fast Strip', 'Pantagra-40', 'Esmog-DSR'],
        'Stomach Pain': ['Drotin-40mg', 'Buscogast', 'Cyclopam', 'Lupispas Plus 20 mg/500 mg'],
        'Bowel Sickness': ['Andial', 'Zenflox-OZ', 'Dulcoflex 5mg'],
        'Headache': ['Combiflam', 'Zerodol-P', 'Diclofenac']
    }
    return medications.get(disease, [])

st.image("PillPal.jpeg", width = 700)

st.latex(r"{\Large Your\ Personalised\ Medicine\ Recommender}")

disease_col, severity_col = st.columns(2)
disease = disease_col.selectbox('Choose your Disease', ('Fever', 'Cold', 'Fever+cold', 'Vomitings', 'Stomach pain', 'Motion sickness', 'Headache'))
severity = severity_col.selectbox('Choose Disease Severity', ('Very high', 'High', 'Mild', 'Low'))

age = st.slider("Choose your Age", min_value=18, max_value=60, value=20)
if age > 45:
    st.success("Hmm. An Old user :thinking_face:")
elif age > 28:
    st.success("Hmm. A Middle-aged user :thinking_face:")
elif age > 18:
    st.success("Hmm. A young user :thinking_face:")

sex, other_d = st.columns(2)
sex1 = sex.selectbox('Sex', ('Female', 'Male', 'Others'))
spec_dis = ("Sugar", 'BP', 'High Cholestrol', 'Skin Disease', 'Allergies', 'No diseases')
other_dis = other_d.selectbox('Any Other Diseases you have', spec_dis)
if other_dis in spec_dis[:-1]:
    with other_d:
        st.info(" :x: Do not use these medicines without Doctor's consultation :stethoscope:")
elif other_dis == 'No diseases':
    with other_d:
        st.success(":blossom: Great, stay fit stay healthy :blossom:")

suffer = st.number_input("How many days are you suffering from ?", min_value=0, max_value=5, value=1)
if suffer > 1:
    st.warning("Consult a doctor immediately!!")

agree = st.checkbox("Agree to the terms and conditions")
if agree:
    st.error(":warning: Disclaimer: The medication recommendations provided by this tool should not replace professional medical advice. Consult a healthcare professional before making any decisions regarding medication. Use of this tool implies acceptance of these terms and conditions.")
    sub = st.button("Submit")
else:
    sub = False

if sub:
    medications = get_medication(disease)
    st.info(f"Choose a medicine after consulting a doctor,\nRecommended medication(s) for, {disease}:")
    for medication in medications:
        st.write(f"- {medication}")
    st.success(":handshake: I hope you recover soon :hugging_face:")
    st.info(":star: Stay joyful and let go of your worries in this world. Your happiness and positivity have the power to heal your illness by 90%. 	:i_love_you_hand_sign: ")

st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

st.write("Made with :heart: by **Shandilya**")
