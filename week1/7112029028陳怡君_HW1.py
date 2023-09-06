# -*- coding: utf-8 -*-
"""
2023/9/6 HW1-BMI
author:7112029028-陳怡君
"""

#請求用戶輸入身高和體重
height = float(input("請輸入您的身高(公尺):"))
weight = float(input("請輸入您的體重(公斤):"))
#使用公式來計算BMI
BMI = weight / (height**2)

#顯示計算得到的BMI值
#BMI值會被格式化到兩位小數
print(f"您的BMI是:{BMI:.2f}")
