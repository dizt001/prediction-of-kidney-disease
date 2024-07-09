import streamlit as st

from web_functions import predict

def app(df, x, y):

    st.title("Halaman Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input ('Input Nilai Blood Pressure')
    with col1:
        sg = st.text_input ('Input Nilai Specific Grafity')
    with col1:
        al = st.text_input ('Input Nilai Albumin')
    with col1:
        su = st.text_input ('Input Nilai Sugar')
    with col1:
        rbc = st.text_input ('Input Nilai Red Blood Cells')
    with col1:
        pc = st.text_input ('Input Nilai Pus Cell')
    with col1:
        pcc = st.text_input ('Input Nilai  Pus Cell Clumps')
    with col1:
        ba = st.text_input ('Input Nilai Bacteria')
    with col2:
        bgr = st.text_input ('Input Nilai Blood Glucose Random')
    with col2:
        bu = st.text_input ('Input Nilai Blood Urea')
    with col2:
        sc = st.text_input ('Input Nilai Serum Creatinine')
    with col2:
        sod = st.text_input ('Input Nilai Sodium')
    with col2:
        pot = st.text_input ('Input Nilai Pottasium')
    with col2:
        hemo = st.text_input ('Input Nilai Hemoglobin')
    with col2:
        pcv = st.text_input ('Input Nilai Packed Cell Volume')
    with col2:
        wc = st.text_input ('Input Nilai White Blood Cell Count')
    with col3:
        rc = st.text_input ('Input Nilai Red Blood Cell Count')
    with col3:
        htn = st.text_input ('Input Nilai Hypertension')
    with col3:
        dm = st.text_input ('Input Nilai Diabetes Melitus')
    with col3:
        cad = st.text_input ('Input Nilai Coronary Artery Disease')
    with col3:
        appet = st.text_input ('Input Nilai Appetite')
    with col3:
        pe = st.text_input ('Input Nilai Pedal Edema')
    with col3:
        ane = st.text_input ('Input Nilai Anemia')

    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]

    #tombol prediksi 
    if st.button("Prediksi"):
        predicttion, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses...")

        if (predicttion == 1):
            st.warning("Orang tersebut rentan terkena penyakit ginjal")
        else:
            st.success("Orang tersebut relatif aman dari penyakit ginjal")

        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")


