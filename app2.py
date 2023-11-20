import streamlit as st

def main():
    st.title("웹 대시보드")
    # print("웹 대시보드")
    st.text("웹 대시보드 개발하기")
    
    st.header("이 영역은 헤더 영역")

    st.subheader("이 영역은 서브 헤더 영역")

    st.write("안녕하세요")

    st.success("성공했을 때") # 배경 녹색

    st.warning("경고 메세지 보여줄 때") # 배경 황토색

    st.info("정보성 메세지 보여줄 때") # 배경 파란색

    st.error("문제가 발생했음을 보여주고 싶을 때") # 배경 빨간색
    
if __name__ == "__main__" :
    main()    