## 1. Case Study - Huda Beauty Product Composition
### Present a Hypothetical Breakdown of the Product's Key Ingredients

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data for the pie chart
ingredients = ['Coconut oil', 'Palm oil', 'Other oils/butters', 'Water', 'Other ingredients']
percentages = [25, 30, 20, 20, 10]

# Use seaborn color palette
colors = sns.color_palette("flare", n_colors=len(ingredients))

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(percentages, labels=ingredients, colors=colors, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title('Hypothetical Beauty Product Composition')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Display the chart
plt.show()

## 2. Proposed Solution - Optimizing Ingredient Composition
### Explain the Strategy of Reducing Levels of Expensive Ingredients
### Creating a bar chart to compare the original and optimized formulas.

# Data for original and optimized formulas
ingredients = ['Coconut oil', 'Palm oil', 'Other oils/butters', 'Water', 'Other ingredients']
original = [25, 30, 20, 20, 10]
optimised = [20, 25, 25, 25, 10]

# Set up the bar chart
x = np.arange(len(ingredients))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width/2, original, width, label='Original', color='#FF9FF3')
rects2 = ax.bar(x + width/2, optimised, width, label='Optimised', color='#9B72AA')

# Add labels and title
ax.set_ylabel('Percentage (%)')
ax.set_title('Comparison of Original and Optimised Product Formulas')
ax.set_xticks(x)
ax.set_xticklabels(ingredients, rotation=45, ha='right')
ax.legend()

# Add value labels on the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()

## 3. Calculate and Show the Impact on Product Cost
### Calculating the total cost per metric ton for both the original and optimized formulas using hypothetical prices.

# Hypothetical costs for other ingredients ($/mt)
other_oils_cost = 1000
water_cost = 100
other_ingredients_cost = 500

# Calculate total cost per metric ton
def calculate_total_cost(coconut_price, palm_price, formula):
    return (formula[0] * coconut_price +
            formula[1] * palm_price +
            formula[2] * other_oils_cost +
            formula[3] * water_cost +
            formula[4] * other_ingredients_cost) / 100

# Prices from the World Bank data
coconut_oil_price = 1075  # $/mt
palm_oil_price = 886  # $/mt

# Calculate costs for original and optimised formulas
original_cost = calculate_total_cost(coconut_oil_price, palm_oil_price, original)
optimized_cost = calculate_total_cost(coconut_oil_price, palm_oil_price, optimised)

print(f"Original formula cost: ${original_cost:.2f} per metric ton")
print(f"Optimized formula cost: ${optimized_cost:.2f} per metric ton")
print(f"Cost reduction: ${original_cost - optimized_cost:.2f} per metric ton")
print(f"Percentage savings: {((original_cost - optimized_cost) / original_cost * 100):.2f}%")

## 4. Visualize the Cost Impact
### Creating a bar chart to show the cost comparison between the original and optimized formulas.

# Data for cost comparison
formulas = ['Original 2023', 'Optimised 2023']
costs = [original_cost, optimized_cost]

plt.figure(figsize=(8, 6))
plt.bar(formulas, costs, color=['#FF9FF3', '#9B72AA'])
plt.title('Comparison of Original vs Optimised Formula Cost (2023)')
plt.ylabel('Cost ($/mt)')
for i, cost in enumerate(costs):
    plt.text(i, cost, f'${cost:.2f}', ha='center', va='bottom')
plt.show()
