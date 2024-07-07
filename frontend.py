import streamlit as st
import time
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained(rf"google/mt5-small")
model = AutoModelForSeq2SeqLM.from_pretrained(rf"student_best")
if "messages" not in st.session_state:
    st.session_state.messages=[]
if "model" not in st.session_state:
    st.session_state.model=model
if "tokenizer" not in st.session_state:
    st.session_state.tokenizer=tokenizer

def generate_summary(prompt):
    prompt="summarize: "+prompt
    inputs = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)
    sumary=tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sumary
def load_data():
    time.sleep(3)
st.title("HINDI TEXT SUMMARIZER 📝✨\n")
st.subheader("Knowledge Distillation")
col1,col2=st.columns([0.2,0.8])
with col2:
    st.image("image.png",width=200)
with st.chat_message("ai"):
    st.write("🗣️ : नमस्ते, मैं हिंदी में पाठ का संक्षेपण करने में विशेषज्ञ हूं।")
for m in st.session_state.messages:
    role=m["role"]
    msj=m["msj"]
    with st.chat_message(role):
        st.write(msj)


prompt = st.chat_input("Write a Hindi text to summarize: 🙏🏼")
if prompt:
    dic2={"role":"user","msj":prompt}
    st.session_state.messages.append(dic2)
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("ai"):
        sum1=generate_summary(prompt)
        with st.spinner("कृपया प्रतीक्षा करें.."):
            # Call the function to load data
            data_loaded = load_data()
        st.write(f'''🗣️ निम्नलिखित टेक्स्ट का संक्षिप्तिकरण निम्नलिखित है:" {sum1}"''')
        t=f"🗣️ निम्नलिखित टेक्स्ट का संक्षिप्तिकरण निम्नलिखित है: {sum1}"
        dic={"role":"ai","msj":t}
        st.session_state.messages.append(dic)



