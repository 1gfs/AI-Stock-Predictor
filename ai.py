import numpy as np
import matplotlib.pyplot as plt
import random

print("\n" + "=" * 50)
print("STOCK TREND PREDICTOR")
print("=" * 50)

print("\nFirst, let's create some sample stock data...")
stock_prices = [100]
for day in range(29):
    daily_change = random.uniform(-2.5, 2.5)
    new_price = stock_prices[-1] + daily_change
    stock_prices.append(round(new_price, 2))

print(f"Created 30 days of stock prices")
print(f"Prices start at ${stock_prices[0]} and end at ${stock_prices[-1]}")

def predict_next_price(prices, look_back=3):
    forecasts = []
    
    for start_day in range(len(prices) - look_back):
        recent_prices = prices[start_day:start_day + look_back]
        average_price = sum(recent_prices) / look_back
        forecasts.append(round(average_price, 2))
    
    return forecasts

print("\nMaking predictions...")
print("-" * 30)

short_term_forecast = predict_next_price(stock_prices, 3)
long_term_forecast = predict_next_price(stock_prices, 5)

print(f"3-day forecasts ready: {len(short_term_forecast)} predictions")
print(f"5-day forecasts ready: {len(long_term_forecast)} predictions")

print("\nLet's see how accurate we were...")
differences_3day = []
for i in range(len(short_term_forecast)):
    actual = stock_prices[i + 3]
    predicted = short_term_forecast[i]
    difference = abs(actual - predicted)
    differences_3day.append(difference)

avg_difference_3day = sum(differences_3day) / len(differences_3day)
accuracy_3day = 100 * (1 - (avg_difference_3day / np.mean(stock_prices)))

differences_5day = []
for i in range(len(long_term_forecast)):
    actual = stock_prices[i + 5]
    predicted = long_term_forecast[i]
    difference = abs(actual - predicted)
    differences_5day.append(difference)

avg_difference_5day = sum(differences_5day) / len(differences_5day)
accuracy_5day = 100 * (1 - (avg_difference_5day / np.mean(stock_prices)))

print(f"\nResults:")
print(f"3-day forecast: ${avg_difference_3day:.2f} average error")
print(f"3-day forecast: {accuracy_3day:.1f}% accuracy")
print(f"5-day forecast: ${avg_difference_5day:.2f} average error")
print(f"5-day forecast: {accuracy_5day:.1f}% accuracy")

print("\nCreating chart...")

plt.figure(figsize=(12, 6))

days = list(range(1, len(stock_prices) + 1))
plt.plot(days, stock_prices, 'b-', linewidth=2, marker='o', markersize=5, label='Actual Price')

prediction_days_3day = list(range(4, len(stock_prices) + 1))
plt.plot(prediction_days_3day, short_term_forecast, 'r--', linewidth=2, marker='s', markersize=5, label='3-Day Forecast')

prediction_days_5day = list(range(6, len(stock_prices) + 1))
plt.plot(prediction_days_5day, long_term_forecast, 'g-.', linewidth=2, marker='^', markersize=5, label='5-Day Forecast')

plt.title('Stock Price Forecasts', fontsize=14, fontweight='bold')
plt.xlabel('Trading Day', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(range(1, len(stock_prices) + 1, 2))

plt.tight_layout()
plt.savefig('stock_forecast_chart.png')
print("Chart saved as 'stock_forecast_chart.png'")

plt.show()

print("\n" + "=" * 50)
print("FORECAST SUMMARY")
print("=" * 50)
print(f"{'Day':<6} {'Actual':<10} {'3-Day':<12} {'5-Day':<12}")
print("-" * 50)

for day in range(len(stock_prices)):
    actual = stock_prices[day]
    
    if day >= 3:
        forecast_3day = short_term_forecast[day - 3]
    else:
        forecast_3day = "--"
    
    if day >= 5:
        forecast_5day = long_term_forecast[day - 5]
    else:
        forecast_5day = "--"
    
    print(f"{day+1:<6} ${actual:<9.2f} ${str(forecast_3day):<11} ${str(forecast_5day):<11}")

print("\n" + "=" * 50)
print("TRY IT WITH YOUR OWN NUMBERS")
print("=" * 50)

print("\nWant to try your own prices?")
print("Example: 100 102 105 103 107 110 108 112 115 113")

user_input = input("\nEnter your prices (space separated) or press Enter to exit: ")

if user_input.strip():
    try:
        user_prices = [float(price) for price in user_input.split()]
        print(f"\nUsing your {len(user_prices)} prices...")
        
        user_window = int(input("How many days to average? (3 or 5): "))
        
        user_forecast = predict_next_price(user_prices, user_window)
        
        print(f"\nYour forecasts:")
        for i in range(len(user_forecast)):
            print(f"Day {i+user_window+1}: Predicted ${user_forecast[i]:.2f}")
        
        if len(user_prices) > user_window:
            actual = user_prices[user_window]
            predicted = user_forecast[0]
            print(f"\nFirst forecast was: ${predicted:.2f}")
            print(f"Actual was: ${actual:.2f}")
            print(f"Difference: ${abs(actual - predicted):.2f}")
    
    except:
        print("Oops! Please enter numbers like: 100 102 105 103")

print("\n" + "=" * 50)
print("HOW THIS WORKS")
print("=" * 50)
print("""
This predictor uses a simple idea:
1. Look at the last few days of prices
2. Calculate their average
3. Use that average as tomorrow's prediction

Why this matters:
• Simple but widely used in real trading
• Shows how machines can spot trends
• Foundation for more advanced AI models
""")

print("\nDone! Check your folder for the chart image.")