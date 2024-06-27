# Project Overview: Wind Data Visualization

## Objective:
The primary objective of this project is to visualize wind data to understand wind patterns and distributions. Wind data includes direction and speed, which are crucial for various applications, such as weather forecasting, aviation, maritime navigation, and renewable energy planning. By visualizing this data, we can gain insights into wind behavior, which can help in making informed decisions in these fields.

## Project Steps and Implementation:

1. **Data Loading:**
   - We started by loading the wind data from an Excel file (`Datos_Rosa_de_Vientos.xlsx`). This file contains information about wind speed and direction.
   - The `pandas` library is used to read the Excel file into a DataFrame for easy manipulation and analysis.

2. **Wind Speed Representation:**
   - We calculated the components of wind speed in the x and y directions using trigonometric functions. This helps in visualizing the wind vectors in a 2D plane.
   - The equations used are:
     - \( \text{velocidad\_x} = \text{VELOCIDAD} \times \sin(\text{DIRECCION} \times \pi / 180.0) \)
     - \( \text{velocidad\_y} = \text{VELOCIDAD} \times \cos(\text{DIRECCION} \times \pi / 180.0) \)
   - These components are added as new columns in the DataFrame.

3. **Scatter Plot of Wind Speed Components:**
   - A scatter plot is created to visualize the wind speed components in the x and y directions. This plot helps in understanding the distribution and intensity of wind vectors in different directions.

4. **Histogram of Wind Speed:**
   - A histogram of wind speed is plotted to show the frequency distribution of different wind speed values. This visualization helps in identifying the most common wind speeds and their variations.

5. **Windrose Plots:**
   - Several types of windrose plots are created to visualize the distribution of wind speed and direction:
     - **Bar Mode:** Shows wind speed distribution in bar format for different directions.
     - **Proportional Box Mode:** Displays wind speed distribution using proportional boxes for different directions.
     - **Filled Mode:** Uses filled contours to show wind speed distribution for different directions.
     - **Linear Mode:** Displays wind speed distribution using contour lines for different directions.
   - These plots are generated using the `WindroseAxes` class from the `windrose` library.

## Tools and Libraries Used:
- **pandas:** For data manipulation and analysis.
- **numpy:** For numerical operations and calculations.
- **matplotlib:** For creating various plots and visualizations.
- **windrose:** For generating windrose plots, a specialized type of plot for wind data visualization.
- **math:** For mathematical operations, especially trigonometric functions.

## Conclusion:
By implementing this project, we have successfully visualized wind data in multiple ways, providing a comprehensive view of wind speed and direction patterns. The different plots help in identifying prevalent wind directions, common wind speeds, and the overall behavior of wind in a specific area. These visualizations are valuable for various practical applications where understanding wind patterns is crucial.

## Example Output Plots:
1. **Scatter Plot of Wind Speed Components:**
   - Visualizes the wind vectors in a 2D plane.
2. **Histogram of Wind Speed:**
   - Shows the frequency distribution of wind speeds.
3. **Windrose Plots:**
   - **Bar Mode:** Displays wind speed distribution in a bar format.
   - **Proportional Box Mode:** Uses proportional boxes to show wind speed distribution.
   - **Filled Mode:** Shows wind speed distribution using filled contours.
   - **Linear Mode:** Displays wind speed distribution with contour lines.

These visualizations help in understanding the wind patterns and can be used for further analysis and decision-making in relevant fields.
