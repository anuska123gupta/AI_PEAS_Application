import pandas as pd
import matplotlib.pyplot as plt

# PEAS data
data = {
    "S.No": [1, 2, 3, 4, 5, 6],
    "AI Application": [
        "Self-driving Car",
        "Email Spam Filter",
        "Chess Playing Program",
        "Google Search Engine",
        "Voice Assistant (e.g., Alexa)",
        "Robot Vacuum Cleaner"
    ],
    "Performance Measure": [
        "Safety, speed, obeying traffic rules, passenger comfort",
        "Accuracy of spam detection, low false positives/negatives",
        "Win/loss ratio, minimization of blunders",
        "Relevance of results, click-through rate, response time",
        "Accuracy of response, user satisfaction",
        "Cleanliness, area covered, battery efficiency"
    ],
    "Environment": [
        "Roads, traffic, pedestrians, weather",
        "Email inbox, incoming messages",
        "Chessboard, opponent moves",
        "Web content, user queries",
        "Indoor environment, user conversations",
        "Household rooms, furniture, floor types"
    ],
    "Actuators": [
        "Steering, accelerator, brakes, indicators",
        "Classifier (marks spam or not)",
        "Move generator (digital moves)",
        "Display of search results",
        "Speaker (voice), smart device control",
        "Wheels, suction motor, cleaning brushes"
    ],
    "Sensors": [
        "Cameras, GPS, lidar, radar, speedometer",
        "Email content, metadata, sender info",
        "Game state, opponent move input",
        "User query, browsing behavior",
        "Microphone, voice recognition",
        "Proximity sensors, bump sensors, dirt sensors"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plotting as a table using matplotlib
fig, ax = plt.subplots(figsize=(18, 6))  # width x height in inches
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='left', loc='center')

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.8)  # x, y scaling

# Save the image
plt.savefig("peas_table_image.png", bbox_inches='tight', dpi=300)
plt.show()
