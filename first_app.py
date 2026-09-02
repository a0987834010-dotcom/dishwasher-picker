import streamlit as st
import random
import time

# 設定網頁標題與圖示
st.set_page_config(page_title="今天誰中獎？", page_icon="😀")

st.title("溫馨家庭小遊戲：今天誰中獎？")
st.write("輸入大家的名字，讓系統為你選出今天的洗碗人員！")

# 1. 讓使用者輸入名字（以逗號分隔）
names_input = st.text_input("請輸入今天吃飯的人員（請用逗號隔開）:", "爸爸, 媽媽, 哥哥, 妹妹")

# 2. 抽籤按鈕 logic
if st.button("🎲 開始抽籤！", type="primary"):
    # 處理輸入字串，轉成 List 並去除多餘空白
    name_list = [name.strip() for name in names_input.split(",") if name.strip()]
    
    if name_list:
        # 隨機抽取一人
        chosen = random.choice(name_list)

        # 先顯示提示文字
        st.write('🤦‍♂️ **緊張的時刻來了! 中獎的是誰呢?**')

        #建立動態倒數
        countdown_place = st.empty()
        for i in [3, 2, 1]:
            countdown_place.header(f' **{i}**')
            time.sleep(1)

        #清空倒數數字
        countdown_place.empty()
        
        # 播放彩帶慶祝特效
        st.balloons()
        
        # 顯示結果
        st.success(f"🎉 恭喜 **{chosen}** 獲得今天洗碗的光榮任務！")
    else:
        st.warning(" 錯誤!!請至少輸入一個人的名字喔！")