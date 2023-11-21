import streamlit as st

def main():

    # 텍스트를 입력 받는 방법

    # text_input(이름(제목), max_charts=글자 수 제한, placeholder=예시, type=password(비밀번호))
    # text_area() 
    name = st.text_input("이름을 입력하세요!") # 엔터 시 변수에 값 할당
    st.subheader(f"제 이름은 {name}입니다.")

    st.text_input("이름 입력", max_chars=5, placeholder="홍길동") 

    text = st.text_area("메세지를 입력하세요") 
    st.text(text)

    # 숫자 입력 받는 방법
    # number_input(이름(제목), 최소값, 최대값, step=간격) 
    birth_year = st.number_input("출생년도를 입력하세요.", 1900, 2023)
    st.text(f"제 출생년도는 {birth_year} 입니다.")

    st.number_input("실수를 입력하세요.", -2.0, 100.0, step=0.3)

    # strftime() -> 형식 포맷 함수
    # %Y = 년도(year) , %m = 월(month) , %d = 일(day) , %A = 요일  
    # %H = 시간(hour) , %M = 분(minute)

    # 날짜 입력 받는 방법
    # date_input(이름(제목)) -> date 타입
    my_date = st.date_input("약속 날짜 입력")
    st.text(my_date) # date 타입
    st.text(my_date.strftime("%Y년 %m월 %d일 %A입니다."))

    # 시간 입력 받는 방법
    # time_input(이름(제목)) -> time 타입
    my_time = st.time_input("약속 시간 선택") 
    st.text(my_time.strftime("%H:%M 에 약속 시간을 잡았습니다."))
    
    # 비밀번호 입력 받는 방법
    password = st.text_input("비밀번호 입력", type="password")
    # print(password)

    # 색깔 입력
    # color_picker(이름(제목))
    color = st.color_picker("색을 선택하세요")
    st.text(color)

if __name__ == "__main__" : main()