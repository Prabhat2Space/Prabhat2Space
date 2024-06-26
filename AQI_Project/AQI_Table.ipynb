import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table

# Define the data
data = {
    "Air Quality Index": ["0 to 50", "51 to 100", "101 to 150", "151 to 200", "201 to 300", "301 to 500"],
    "Category": ["GOOD", "MODERATE", "UNHEALTHY FOR SENSITIVE GROUPS", "UNHEALTHY", "VERY UNHEALTHY", "HAZARDOUS"],
    "Who needs to be concerned?": [
        "Air quality is satisfactory, and air pollution poses little or no risk.",
        "Some people who may be unusually sensitive to particle pollution.",
        "Sensitive groups include people with heart or lung disease, older adults, children and teenagers, minority populations, and outdoor workers.",
        "Everyone",
        "Everyone",
        "Everyone"
    ],
    "What should I do?": [
        "It’s a great day to be active outside.",
        "Unusually sensitive people: Consider making outdoor activities shorter and less intense. Watch for symptoms such as coughing or shortness of breath. These are signs to take it easier.\nEveryone else: It’s a good day to be active outside.",
        "Sensitive groups: Make outdoor activities shorter and less intense. It’s OK to be active outdoors, but take more breaks. Watch for symptoms such as coughing or shortness of breath.\nPeople with asthma: Follow your asthma action plan and keep quick relief medicine handy.\nPeople with heart disease: Symptoms such as palpitations, shortness of breath, or unusual fatigue may indicate a serious problem. If you have any of these, contact your health care provider.",
        "Sensitive groups: Avoid long or intense outdoor activities. Consider rescheduling or moving activities indoors.*\nEveryone else: Reduce long or intense activities. Take more breaks during outdoor activities.",
        "Sensitive groups: Avoid all physical activity outdoors. Reschedule to a time when air quality is better or move activities indoors.*\nEveryone else: Avoid long or intense activities. Consider rescheduling or moving activities indoors.*",
        "Everyone: Avoid all physical activity outdoors.\nSensitive groups: Remain indoors and keep activity levels low. Follow tips for keeping particle levels low indoors.*"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define colors for each category
colors = {
    "GOOD": "#00E400",          # Green
    "MODERATE": "#FFFF00",      # Yellow
    "UNHEALTHY FOR SENSITIVE GROUPS": "#FF7E00",  # Orange
    "UNHEALTHY": "#FF0000",     # Red
    "VERY UNHEALTHY": "#8F3F97", # Purple
    "HAZARDOUS": "#7E0023"      # Maroon
}

# Create a function to wrap text
def wrap_text(text, width):
    import textwrap
    return "\n".join(textwrap.wrap(text, width))

# Plot the table
fig, ax = plt.subplots(figsize=(22, 12))
ax.axis('off')
tbl = Table(ax, bbox=[0, 0, 1, 1])

# Add table header
tbl.auto_set_font_size(False)
tbl.set_fontsize(12)
header_height = 0.05
tbl.add_cell(0, 0, width=0.1, height=header_height, text="Air Quality Index", loc='center', facecolor="lightgrey")
tbl.add_cell(0, 1, width=0.15, height=header_height, text="Category", loc='center', facecolor="lightgrey")
tbl.add_cell(0, 2, width=0.35, height=header_height, text="Who needs to be concerned?", loc='center', facecolor="lightgrey")
tbl.add_cell(0, 3, width=0.4, height=header_height, text="What should I do?", loc='center', facecolor="lightgrey")

# Add table rows
for i in range(len(df)):
    category = df.iloc[i, 1]
    color = colors[category]
    row_height = max(0.1, 0.05 + len(wrap_text(df.iloc[i, 3], 50).split("\n")) * 0.02)

    tbl.add_cell(i + 1, 0, width=0.1, height=row_height, text=df.iloc[i, 0], loc='center', facecolor=color)
    tbl.add_cell(i + 1, 1, width=0.15, height=row_height, text=category, loc='center', facecolor=color)
    tbl.add_cell(i + 1, 2, width=0.35, height=row_height, text=wrap_text(df.iloc[i, 2], 40), loc='left', facecolor=color)
    tbl.add_cell(i + 1, 3, width=0.4, height=row_height, text=wrap_text(df.iloc[i, 3], 50), loc='left', facecolor=color)

ax.add_table(tbl)

plt.show()
