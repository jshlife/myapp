streamlit run main.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = '202406_202406_연령별인구현황_월간.csv'
data = pd.read_csv(file_path, encoding='cp949')

# Preprocess data
# Remove commas and convert numerical columns to integers
for col in data.columns[1:]:
    data[col] = data[col].str.replace(',', '').astype(int)

# Streamlit app
st.title('지역별 중학생 인구 비율')

# Select box for choosing a region
regions = data['행정구역'].unique()
selected_region = st.selectbox('지역을 선택하세요:', regions)

# Filter data for the selected region
region_data = data[data['행정구역'] == selected_region]

# Calculate total population and middle school population (13-15 years)
total_population = region_data.iloc[0, 1]
middle_school_population = region_data.iloc[0, 15] + region_data.iloc[0, 16] + region_data.iloc[0, 17]

# Calculate percentages
middle_school_percentage = (middle_school_population / total_population) * 100
other_population_percentage = 100 - middle_school_percentage

# Pie chart
labels = '중학생 인구', '기타 인구'
sizes = [middle_school_percentage, other_population_percentage]
colors = ['#ff9999', '#66b3ff']
explode = (0.1, 0)  # explode 1st slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
