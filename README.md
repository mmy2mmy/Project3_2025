 send_times = ["07:00", "10:00", "13:00", "16:00"] 3 for t in send_times:
 schedule.every().day.at(t).do(send_email)
 print(f"Scheduled email at {t} every day.") 67 # ===== Main Loop =====
 print("Plant Moisture Monitoring System is running...") 9
 try:
 while True:
 schedule.run_pending()
 time.sleep(1)
 except KeyboardInterrupt:
 print("Program manually terminated.")
