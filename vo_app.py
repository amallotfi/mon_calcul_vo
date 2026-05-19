import streamlit as st
st.title("ComptaSmart : Calculateur de VO & TVA")
st.subheader("Convertissez vos montants TTC en HT avec précision")

montant_tcc=st.number_input("Veuillez enter le montant TTC: ", min_value=0.0)
taux_tva= st.number_input("enter le taux de TVA (%):", min_value=0.0, step=0.1, value=20.0)
if montant_tcc > 0 and taux_tva > 0: 
    VO_HT = montant_tcc/(1 + (taux_tva/100))
    montant_tva = montant_tcc - VO_HT
    st.success(f"la valeur d'origine est {VO_HT:.2f} DH HT")
    st.info(f"Le montant de la TVA est {montant_tva:.2f} DH")




    