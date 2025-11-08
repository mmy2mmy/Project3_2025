 # Callback when water is detected (button pressed)
 def on_water_detected():
 global water_needed
 water_needed = False
 # print("Water detected: Plant does NOT need watering.")
 # Callback when no water is detected (button released)
 def on_no_water():
 global water_needed
 water_needed = True
 # print("No water detected: Plant NEEDS watering.")

 # Attach sensor callbacks
 sensor.when_pressed = on_water_detected
 sensor.when_released = on_no_water

 # ===== Email Sending Function =====
 def send_email():
 now = datetime.now()
 status = "Plant NEEDS watering" if water_needed
 else "Plant does NOT need watering"
 timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

 body = f"""Plant Status Report

 Timestamp: {timestamp}
 Current Condition: {status}
 """

 msg = EmailMessage()
 msg.set_content(body)
 msg['From'] = FROM_EMAIL
 msg['To'] = TO_EMAIL
 msg['Subject'] = f"[Plant Daily] {status} - {now.strftime('%H:%M')}"

 server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 try:
 server.starttls()
 server.login(FROM_EMAIL, FROM_PASSWORD)
 server.send_message(msg)
 print(f"[{timestamp}] Email sent successfully: {status}")
 except Exception as e:
 print(f"[{timestamp}] Error during email send: {e}")
 finally:
 server.quit()
