import streamlit as st


if "foods" not in st.session_state:
    st.session_state["foods"] = []





with st.form('survay_form',clear_on_submit=True):
    name = st.text_input("이름을 입력하세요")
    food = st.text_input("좋아하는 음식을 입력하세요")
    sport=st.text_input('좋아하는 운동을 입력하세요.')

    if st.form_submit_button("추가"):
        if name and food:
            st.session_state["foods"].append(f"{name} - {food} - {sport}")
        else:
            st.warning("이름과 음식을 모두 입력하세요!")


st.write("지금까지 입력된 목록:")
for item in st.session_state["foods"]:
    st.write(item)
