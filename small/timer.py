import time

countdown_time = 10 # Seconds
while countdown_time:
  mins, secs = divmod(t, 60)
  timer = '{:02d}:{:02d}'.format(mins, secs)
  print("Commence Countdown..." + str(timer), end="\r")
  time.sleep(1)
  countdown_time -= 1
