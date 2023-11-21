import streamlit as st
import os
from PIL import Image
from datetime import datetime
import pandas as pd

# 이미지, csv 파일 업로드 하는 방법

# 디렉토리(폴더)명과 파일을 알려주면, 해당 디렉토리에 파일을 저장해 주는 함수
def save_uploaded_file(directory, file) :
    # 1. 위의 directory가 있는지 확인 후 없으면 새로 생성
    if not os.path.exists(directory) : 
        os.makedirs(directory)

    # 2. 디렉토리가 존재하니까, 파일을 이 디렉토리 안에 저장한다.
    with open(os.path.join(directory, file.name) , "wb") as f :
        f.write(file.getbuffer())

    # 3. 파일 저장 성공했으니까 화면에 보여준다    
    return st.success(f"{directory}에 {file.name}이 잘 저장됐습니다.")

def main() :
    st.title("파일 업로드 프로젝트")
    # st.sidebar = 왼쪽 사이드 바 사용
    choice = st.sidebar.selectbox("메뉴", ["Image","CSV"])

    if choice == "Image" :
        st.subheader("이미지 파일 업로드")

        # file_uploader(이름(제목) , type=파일타입)
        file = st.file_uploader("이미지파일을 업로드하세요", type=["jpg","jpeg","png"])
        
        # 파일이 업로드 되었을 때 
        if file is not None :
            # 파일명이 같으면 덮어쓰기 때문에 새로운 이름을 만든다.
            current_time = datetime.now()
            # isoformat() = 문자열로 바꿔줌
            file.name = current_time.isoformat().replace(":", "_").replace(".", "_") + ".jpg"

            save_uploaded_file("tmp", file)

            # 웹에 저장된 이미지파일 띄우기
            img = Image.open(file)
            st.image(img)

    elif choice == "CSV" :
        st.subheader("CSV 파일 업로드")

        file = st.file_uploader("CSV 파일 업로드", type=["csv"])
        
        # 파일이 업로드 되었을 때 
        if file is not None :

            # 파일명 유니크하게 만든다.
            current_time = datetime.now()
            
            file.name = current_time.isoformat().replace(":", "_").replace(".", "_") + ".csv"

            save_uploaded_file("csv", file)

            # csv 파일을 데이터프레임으로 읽어서 웹에 보여준다.
            df = pd.read_csv(file)
            st.dataframe(df)

if __name__ == "__main__" : main()