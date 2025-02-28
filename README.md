# 串接使用 Gemini Api 達成辨識文字中的情緒含意

* Title : 串接使用 Gemini Api 達成辨識文字中的情緒含意
* Author : 林建宏 (Lin, Chien-Hung)
* 伺服器網址 : http://35.185.129.50:7890/emotion_detection.html

![image](./gemini.png)

## 題目 (topic)
開發一個網頁應用程式，允許使用者輸入文字內容，並即時顯示對該內容的情感分析結果（正面、負面或中性...等，名目您可以自己決定）。
服務使用Google Cloud Platforｍ雲端部建，不限制使用VM、容器、或無伺服器架構達成，但必須串接Gemini API的回訊功能。

此項實作包含程式介面、服務環境搭建，以及LLM模型服務串接。目的是檢驗您能否適任全端作業模式。
完成後請將服務上線並提供網站網址，並將原始碼放上Github，回信時請您簡單說明使用了哪幾項服務功能。

## 環境 (Requirements)
# 雲端伺服器(Cloud server)
* Google Cloud Platform (GCP) CPU:N2D 空間:100G 防火牆:建立防火牆規則，開啟port並設定TCP/UDP。
# 虛擬環境(Virtual Machine)
* Ubuntu 24.01 LTS x86/64
* Docker 2.5.0-cuda12.4-cudnn9-devel
* html
* Python 3.11.10

## (程式)資歷夾中具以下兩種檔案 ：
- **emotion_detection.html : 網頁程式介面，負責接收文字訊息，並回傳給Gemini Api 做情緒上的理解，最終回傳給使用者。
- **gemini.png : Gemini 網上的圖片。(來源 : https://blog.google/technology/ai/gemini-api-developers-cloud/)

## 操作流程：
1. 開啟terminal，進入具有HTML的資料夾，輸入以下指令：python3 -m http.server 6006 --bind 0.0.0.0。

2. 當使用者輸入文字並按下按鈕過後，系統將會回傳情緒預測回HTML。
