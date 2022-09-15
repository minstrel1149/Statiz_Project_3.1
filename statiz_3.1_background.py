import sys
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from openpyxl.styles.fonts import Font
from openpyxl.styles.alignment import Alignment
from openpyxl.styles import PatternFill, colors
from pathlib import Path

class statiz:
    def __init__(self, year):
        statiz.record_site = {'타격기본':f'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=0&ys={year}&ye={year}&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=',
        '타격확장':f'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=0&ys={year}&ye={year}&se=0&te=&tm=&ty=0&qu=all&po=0&as=&ae=&hi=&un=&pl=&da=2&o1=WRCPLUS&o2=WAR_ALL&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=',
        '투수기본':f'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys={year}&ye={year}&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR&o2=OutCount&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=',
        '투수확장':f'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys={year}&ye={year}&se=0&te=&tm=&ty=0&qu=all&po=0&as=&ae=&hi=&un=&pl=&da=2&o1=FIP&o2=WAR&de=0&lr=0&tr=&cv=&ml=1&sn=30&si=&cn=',
        '투수구속':f'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys={year}&ye={year}&se=0&te=&tm=&ty=0&qu=all&po=0&as=&ae=&hi=&un=&pl=&da=14&o1=FVval&de=1&o2=WAR&lr=0&tr=&cv=&ml=1&sn=30&si=&cn='
        }
        statiz.kt_site = {'타격':f'http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys={year}&ye={year}&se=0&te=kt&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&lr=0&tr=&cv=&ml=1&sn=30&pa=0&si=&cn=',
        '투수':f'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys={year}&ye={year}&se=0&te=kt&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR&o2=OutCount&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn='}
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # @property를 통해 속성으로 바꿔주긴 하는데.. 하나의 메서드로 합칠 수는 없나?
    # 일단 다 만들어놓고 리팩토링을 생각해보자
    @property
    def hit_basic(self):
        self.driver.get(statiz.record_site['타격기본'])
        hit_basic_df_list = []
        while True:
            page = self.driver.page_source
            df = pd.read_html(page)[1]
            hit_basic_df_list.append(df)
            try:
                html = self.driver.find_element(By.TAG_NAME, 'html')
                next_link = self.driver.find_element(By.LINK_TEXT, '다음')
                html.send_keys(Keys.END)
                time.sleep(0.3)
                next_link.click()
                time.sleep(0.3)
            except:
                print('수집 종료')
                break
        hit_basic_df = pd.concat(hit_basic_df_list)
        return hit_basic_df
    
    @property
    def hit_expand(self):
        self.driver.get(statiz.record_site['타격확장'])
        hit_expand_df_list = []
        while True:
            page = self.driver.page_source
            df = pd.read_html(page)[1]
            hit_expand_df_list.append(df)
            try:
                html = self.driver.find_element(By.TAG_NAME, 'html')
                next_link = self.driver.find_element(By.LINK_TEXT, '다음')
                html.send_keys(Keys.END)
                time.sleep(0.3)
                next_link.click()
                time.sleep(0.3)
            except:
                print('수집 종료')
                break
        hit_expand_df = pd.concat(hit_expand_df_list)
        return hit_expand_df
    
    @property
    def pitch_basic(self):
        self.driver.get(statiz.record_site['타격기본'])
        pitch_basic_df_list = []
        while True:
            page = self.driver.page_source
            df = pd.read_html(page)[1]
            pitch_basic_df_list.append(df)
            try:
                html = self.driver.find_element(By.TAG_NAME, 'html')
                next_link = self.driver.find_element(By.LINK_TEXT, '다음')
                html.send_keys(Keys.END)
                time.sleep(0.3)
                next_link.click()
                time.sleep(0.3)
            except:
                print('수집 종료')
                break
        pitch_basic_df = pd.concat(pitch_basic_df_list)
        return pitch_basic_df
    
    @property
    def pitch_expand(self):
        self.driver.get(statiz.record_site['타격기본'])
        pitch_expand_df_list = []
        while True:
            page = self.driver.page_source
            df = pd.read_html(page)[1]
            pitch_expand_df_list.append(df)
            try:
                html = self.driver.find_element(By.TAG_NAME, 'html')
                next_link = self.driver.find_element(By.LINK_TEXT, '다음')
                html.send_keys(Keys.END)
                time.sleep(0.3)
                next_link.click()
                time.sleep(0.3)
            except:
                print('수집 종료')
                break
        pitch_expand_df = pd.concat(pitch_expand_df_list)
        return pitch_expand_df
    
    @property
    def pitch_speed(self):
        self.driver.get(statiz.record_site['타격기본'])
        pitch_speed_df_list = []
        while True:
            page = self.driver.page_source
            df = pd.read_html(page)[1]
            pitch_speed_df_list.append(df)
            try:
                html = self.driver.find_element(By.TAG_NAME, 'html')
                next_link = self.driver.find_element(By.LINK_TEXT, '다음')
                html.send_keys(Keys.END)
                time.sleep(0.3)
                next_link.click()
                time.sleep(0.3)
            except:
                print('수집 종료')
                break
        pitch_speed_df = pd.concat(pitch_speed_df_list)
        return pitch_speed_df
    
    def table_change(self, df):
        df = df.droplevel(0, axis=1)
        # pop() 메서드나 del[] 속성으로 제거해도 정렬에 있는 것이 중복으로 발생하므로, 굳이 제거하지 않고 진행
        return df
    
    def remove_records(self, df):
        df = df.query("이름 != '이름'")
        return df
    
    def numeric(self, df):
        for col in df.columns.tolist():
            df[col] = pd.to_numeric(df[col], errors='ignore')
        return df
    
    # 각 DataFrame 열, 행 등 전처리 진행 메서드 삽입

    



