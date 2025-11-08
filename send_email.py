# Program: Plant Moisture Sensor with Email Notification
 # Author: Xuanru Guo
 # Student Number: W20109677
 # Date: 23/4/2025
 # Description: send daily email reports using GPIO moisture sensor input
 # Course & Year: Project Semester 3
 import smtplib
 from email.message import EmailMessage
 from gpiozero import Button
 from datetime import datetime
 import schedule
 import time

 # ===== Email Configuration =====
 FROM_EMAIL = "1241428411@qq.com"
 FROM_PASSWORD = "mmy712833" # QQ Mail app password
 TO_EMAIL = "1021145277@qq.com"
 SMTP_SERVER = "smtp.qq.com"
 SMTP_PORT = 587

 # ===== Moisture Sensor Configuration =====
 MOISTURE_PIN = 17
 sensor = Button(MOISTURE_PIN, pull_up=True, bounce_time=0.2)

 # ===== Water Status (updated in real-time) =====
 # True = Dry (no water detected): watering needed
 # False = Wet (water detected): no watering needed
 water_needed = not sensor.is_pressed # Initial status on startup
