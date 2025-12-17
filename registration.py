import streamlit as st
import sqlite3
import pandas as pd
conn=sqlite3.connect("users.db",check_same_thread=False)
cursor=conn.cursor()
#create table
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    name text PRIMARY KEY,password text)""")
conn.commit()
st.title("Registration Form")
menu=["REGISTER","LOGIN","VIEW"]
choice=st.sidebar.selectbox("MENU",menu)
if choice=="REGISTER":
    name=st.text_input("USERNAME")
    password=st.text_input("PASSWORD",type="password")
    if st.button("REGISTER"):
        cursor.execute("""INSERT INTO users(name,password)
        VALUES(?,?)""",(name,password))
        conn.commit()
        st.success("REGISTERED SUCCESSFULLY")
        st.ballons()
if choice=="VIEW":
    data=cursor.execute("SELECT * FROM users")
    st.dataframe(data)
if choice=="LOGIN":
    name=st.text_input("USERNAME")
    password=st.text_input("PASSWORD",type="password")
    if st.button("LOGIN"):
        cursor.execute("""SELECT*FROM users WHERE name=? AND password=?""",(name,password))
        result=cursor.fetchone()
        if result:
                       st.success("VALID USER")
        else:
            st.success("INVALID USER")
                       
                               
                
        
    

