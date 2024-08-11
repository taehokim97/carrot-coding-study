# 가상환경 생성 및 실행
# $ python -m venv .venv
# $ .venv/Scripts/activate
# (.venv) $ pip install streamlit pandas numpy pillow


import streamlit as st

# 1. 제목 및 텍스트 표시

st.title("나의 첫 Streamlit 앱")  # 앱의 제목 설정
st.header("텍스트 표시")  # 헤더 설정

st.write("안녕하세요! Streamlit을 사용하여 웹 앱을 만들고 있습니다.")  # 일반 텍스트 표시
st.markdown("**Markdown**도 지원합니다. *이탤릭체*, **굵은 글씨**, `코드 블록` 등을 사용할 수 있습니다.")  # Markdown 형식 텍스트 표시
st.latex(r"\int_0^\infty x^2 dx")  # LaTeX 수식 표시

# 2. 입력 위젯

st.header("입력 위젯")

name = st.text_input("이름을 입력하세요:")  # 텍스트 입력 위젯
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120, value=30)  # 숫자 입력 위젯
favorite_color = st.color_picker("좋아하는 색을 선택하세요:")  # 색상 선택 위젯
is_student = st.checkbox("학생입니까?")  # 체크박스 위젯
gender = st.radio("성별을 선택하세요:", ("남성", "여성"))  # 라디오 버튼 위젯
selected_fruits = st.multiselect("좋아하는 과일을 선택하세요:", ["사과", "바나나", "오렌지"])  # 멀티 선택 위젯
uploaded_file = st.file_uploader("파일을 업로드하세요:")  # 파일 업로드 위젯

# 3. 출력 및 시각화

st.header("출력 및 시각화")

if st.button("입력 정보 확인"):  # 버튼 클릭 시 정보 출력
    st.write("입력하신 정보:")
    st.write(f"이름: {name}")
    st.write(f"나이: {age}")
    st.write(f"좋아하는 색: {favorite_color}")
    st.write(f"학생 여부: {is_student}")
    st.write(f"성별: {gender}")
    st.write(f"좋아하는 과일: {', '.join(selected_fruits)}")
    if uploaded_file is not None:
        st.write(f"업로드한 파일: {uploaded_file.name}")

import pandas as pd
import numpy as np

# 데이터프레임 생성 및 표시
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['col1', 'col2', 'col3'])
st.write(df)  # 데이터프레임 표시

# 차트 그리기
st.line_chart(df)  # 선 차트
st.bar_chart(df)  # 막대 차트

# 이미지 표시
from PIL import Image
image = Image.open('sample_image.jpg')
st.image(image, caption='샘플 이미지')
