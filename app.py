import streamlit as st
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("bachelo/Llama-2-7B-Chat-MultiTune")
    pipe = pipeline("text-generation", model="bachelo/Llama-2-7B-Chat-MultiTune", tokenizer=tokenizer, max_new_tokens=20, return_full_text=False)
    return pipe

pipe = load_model()
def call_model(prompt):
    result = pipe(prompt)
    answer = result[0]['generated_text']
    return answer
option = st.selectbox("Bạn có muốn nhập đoạn văn không?", ("Có", "Không"))


if option == "Có":
    
    text_input = st.text_area("Nhập đoạn văn: ")
    text_input = "Đoạn văn: " + text_input
    question_input = st.text_input("Nhập câu hỏi của bạn:")
    question_input = "Câu hỏi: " + question_input
    
    col1, col2 = st.columns(2)
    with col1:
        answer_a = st.text_input("Câu trả lời A:")
        answer_a = "A: " + answer_a
    with col2:
        answer_b = st.text_input("Câu trả lời B:")
        answer_b = "B: " + answer_b
        
    col3, col4 = st.columns(2)
    with col3:
        answer_c = st.text_input("Câu trả lời C:")
        answer_c = "C: " + answer_c
    with col4:
        answer_d = st.text_input("Câu trả lời D:")
        answer_d = "D: " + answer_d
    
    if st.button("Xác nhận"):
        if not text_input or not question_input or not answer_a or not answer_b or not answer_c or not answer_d:
            st.warning("Vui lòng điền đầy đủ tất cả các trường.")
        else:
            
            input = "<|im_start|>system Hãy đọc đoạn văn sau và trả lời câu hỏi bằng cách chọn 4 đáp án A, B, C, D <|im_end|> " + " <|im_start|>user "  + text_input + "\n"  + question_input + "\n"  + answer_a + "\n"  + answer_b + "\n"  + answer_c +  "\n"  + answer_d   + "<|im_end|> " + " <|im_start|>assistant "  
            st.success("Tất cả các trường đã được điền đầy đủ.")
            with st.spinner("Đang xử lý..."):
                output = call_model(input)
            st.write(output)
else:
    st.subheader("Layout 2: Không nhập đoạn văn")
    
    st.write("Bạn đã chọn không nhập đoạn văn.")
    st.write("Nội dung của Layout 2 sẽ hiển thị ở đây.")