import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Provided data
step_counts = [6167, 3730, 2762, 8337, 5840, 5450, 9061, 6639, 7713, 5510, 7572, 9163, 7639, 7148, 6363, 8110, 13307, 11455, 3790, 9012, 5172, 9730, 8237, 9986, 6908, 5375, 9214, 7435, 5470, 6356, 6848]
dates = ['11-5-2024', '11-6-2024', '11-7-2024', '11-8-2024', '11-9-2024', '11-10-2024', '11-11-2024', '11-12-2024', '11-13-2024', 
         '11-14-2024', '11-15-2024', '11-16-2024', '11-17-2024', '11-18-2024', '11-19-2024', '11-20-2024', '11-21-2024', '11-22-2024', 
         '11-23-2024', '11-24-2024', '11-25-2024', '11-26-2024', '11-27-2024', '11-28-2024', '11-29-2024', '11-30-2024', '12-1-2024', '12-2-2024', '12-3-2024', '12-4-2024', '12-5-2024']

# Convert date strings to datetime objects for plotting
date_objs = [datetime.strptime(d, '%m-%d-%Y') for d in dates]

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(date_objs, step_counts, marker='o')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Step Count Challenge')
plt.title('Work Steps Challenge')
plt.grid(True)
plt.tight_layout()
plt.show()

print(len(step_counts))
print(len(dates))

