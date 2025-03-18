import streamlit as st
import math

def hitungTotal(price):
    service_charge = total_price * 5 / 100
    st.write(f"Service Charge: {service_charge}")

    ppn = (total_price + service_charge) * 10 /100
    st.write(f"PPN: {ppn}")

    total_final = total_price + service_charge + ppn
    st.write(f"Total harga: {total_final}")

st.title("Bukber Element 2025")
st.write("## Tools hitung harga makanan & minuman")

total_price = st.number_input("Masukkan total makanan & minuman (Harga Dasar)", 10000)

button = st.button("Hitung Total")

if button:
    service_charge = total_price * 5 / 100
    st.write(f"Service Charge: {service_charge:,}")

    ppn = (total_price + service_charge) * 10 /100
    st.write(f"PPN: {ppn:,}")

    total_final = total_price + service_charge + ppn
    st.write(f"Total harga: {total_final:,}")

    pembulatan = math.ceil(total_final / 5000) * 5000
    st.write(f"Yang harus ditransfer: **{pembulatan:,}**")

