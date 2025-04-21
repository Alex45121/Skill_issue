import pandas as pd
import matplotlib.pyplot as plt


# "Advertising.csv" containts the data set used in this exercise
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8, 8.7, 57.5, 200.0, 90.0, 120.0,234.0,321.5,123.4,1555.2,2134,21],
    'Radio': [37.8, 39.3, 45.9, 41.3, 10.8, 48.9, 32.8, 35.0, 40.0, 25.0,48.9, 32.8, 35.0, 40.0, 25.0,12.0],
    'Newspaper': [69.2, 45.1, 69.3, 58.5, 58.4, 75.0, 23.5, 50.0, 60.0, 30.0,48.9, 32.8, 35.0, 40.0, 25.0,12.0],
    'Sales': [22.1, 10.4, 9.3, 18.5, 12.9, 7.2, 11.8, 20.0, 15.0, 14.0,10.8, 48.9, 32.8, 35.0, 40.0, 25.0]
}

# Read the file "Advertising.csv" file using the pandas library
print(len(data["TV"]), len(data["Sales"]),len(data["Newspaper"]),len(data["Radio"]))
df = pd.DataFrame(data)
# Get a quick look of the data

df_new = df.head(7)
df_new_2 = df.head(len(df))
print(df_new)
# Use a scatter plot for plotting a graph of TV vs Sales


plt.scatter(df_new_2["TV"], df_new_2["Sales"], color = "red")
plt.xlabel("TV Budget")
plt.ylabel("Sales")
plt.title("TV Budget Impact on Sales")
plt.legend()
plt.grid(True)
plt.show()




