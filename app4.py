import streamlit as st
import pandas as pd

# 문자열.upper() -> 문자열 대문자로
# 문자열.lower() -> 문자열 소문자로

# button, checkbox = 클릭 시 True
# radio, selectbox, multiselect(list), slider = 클릭 시 해당 값 변수에 할당

def main():
    
    df = pd.read_csv("./data/iris.csv")
    name = "Mike"

    # 버튼 만드는 방법
    if st.button("데이터프레임 보기") : 
        st.dataframe(df)
 
    if st.button("대문자") : 
        st.subheader(name.upper()) 

    if st.button("소문자") :
        st.subheader(name.lower()) 

    # 라디오버튼 만드는 방법
    selected = st.radio("정렬을 선택하세요" , ["오름차순 정렬","내림차순 정렬"])
    
    # df의 petal_length 컬럼을 정렬하도록 한다.
    if selected == "오름차순 정렬" :
        st.dataframe(df.sort_values("petal_length"))
    elif selected == "내림차순 정렬" :
        st.dataframe(df.sort_values("petal_length", ascending=False))

    # 체크박스 만드는 방법    
    if st.checkbox("데이터프레임 보이기") : 
        st.dataframe(df)
    else : st.write("")       

    # 셀렉트박스 : 여러개 중에 한개를 선택할 때
    language = ["Python", "Java", "C", "PHP", "GO"]
    my_choice = st.selectbox("좋아하는 언어를 선택하세요.", language)

    if my_choice == language[0] or my_choice == language[3] or my_choice == language[-1]:
        st.text("배우기 쉽습니다.")
    elif my_choice == language[1] or my_choice == language[2] :
        st.text("배우기 어렵습니다")    

    # 멀티셀렉트 : 여러개를 동시에 선택 가능
    selected_list = st.multiselect("여러개 선택 가능", df.columns, placeholder="선택하세요") 
     
    if len(selected_list) != 0 : 
        st.dataframe(df[selected_list])
    else :
        st.text("")

    # 슬라이더(제목, 최소값, 최대값, 이동 간격(step), 시작값(value))
    age = st.slider("나이", 0, 100, 33)

    st.text(f"저의 나이는 {age}세 입니다.")

    st.slider("데이터", 50, 200, step=10)

    st.slider("나이2", 0, 100, value=33)

    st.slider("데이터", -0.5, 2.7, step=0.1)

    with st.expander("상세 내용 보기") :
        st.text("상세 내용 입니다~~")

if __name__ == "__main__" :
    main()    
