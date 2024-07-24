import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 파일 업로드
st.title("중학생 연령대 인구 비율")
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요:", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding='euc-kr')

    # 중학생 연령대 추출
    middle_school_ages = ['2024년06월_계_12세', '2024년06월_계_13세', '2024년06월_계_14세']

    # 고령 연령대 추출
    elderly_ages = ['2024년06월_계_65세', '2024년06월_계_66세', '2024년06월_계_67세', '2024년06월_계_68세', '2024년06월_계_69세', '2024년06월_계_70세', '2024년06월_계_71세', '2024년06월_계_72세', '2024년06월_계_73세', '2024년06월_계_74세', '2024년06월_계_75세', '2024년06월_계_76세', '2024년06월_계_77세', '2024년06월_계_78세', '2024년06월_계_79세', '2024년06월_계_80세', '2024년06월_계_81세', '2024년06월_계_82세', '2024년06월_계_83세', '2024년06월_계_84세', '2024년06월_계_85세', '2024년06월_계_86세', '2024년06월_계_87세', '2024년06월_계_88세', '2024년06월_계_89세', '2024년06월_계_90세', '2024년06월_계_91세', '2024년06월_계_92세', '2024년06월_계_93세', '2024년06월_계_94세', '2024년06월_계_95세', '2024년06월_계_96세', '2024년06월_계_97세', '2024년06월_계_98세', '2024년06월_계_99세']

    # 지역 선택
    selected_region = st.selectbox('지역을 선택하세요:', data['행정구역'].unique())

    # 선택한 지역의 데이터 추출
    region_data = data[data['행정구역'] == selected_region]

    # 중학생 연령대 인구수 합계
    middle_school_population = region_data[middle_school_ages].apply(lambda x: x.str.replace(',', '').astype(int)).sum(axis=1).values[0]

    # 고령 연령대 인구수 합계
    elderly_population = region_data[elderly_ages].apply(lambda x: x.str.replace(',', '').astype(int)).sum(axis=1).values[0]

    # 총 인구수
    total_population = int(region_data['2024년06월_계_총인구수'].str.replace(',', '').values[0])

    # 비율 계산
    middle_school_ratio = (middle_school_population / total_population) * 100
    elderly_ratio = (elderly_population / total_population) * 100
    other_ratio = 100 - middle_school_ratio - elderly_ratio

    # 원 그래프 생성
    labels = ['중학생 연령대', '고령 연령대', '기타 연령대']
    sizes = [middle_school_ratio, elderly_ratio, other_ratio]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    explode = (0.1, 0.1, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    ax1.axis('equal')

    # 그래프 출력
    st.pyplot(fig1)
