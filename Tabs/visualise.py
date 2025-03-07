import warnings
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import tree
import streamlit as st
from web_functions import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualisasi Prediksi Batu Ginjal")

    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x, y)
        plt.figure(figsize=(10, 6))
        cm_display = ConfusionMatrixDisplay.from_estimator(model, x, y, display_labels=['Class 0', 'Class 1'], cmap=plt.cm.Blues, values_format='d')
        cm_display.plot()
        st.pyplot()

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nockd', 'ckd']
        )
        st.graphviz_chart(dot_data)