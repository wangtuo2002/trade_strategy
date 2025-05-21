import math

# Parameters
X = 1      # Purchase price (USD per share)
a = 0.25   # Price increase (25%)
Y = 20     # Expected profit (USD)
k = 2      # Minimum shares to hold

# Calculate minimum number of shares to buy n
n = math.ceil((Y / X + (1 + a) * (k + 1)) / a)

# Calculate corresponding number of shares to sell m
m = math.ceil((n + Y / X) / (1 + a))

# Calculate sell amount
sell_amount = m * X * (1 + a)

# Total purchase amount
buy_amount = n * X

# Shares held after selling
hold_amount = n - m

# Output parameters and results
print(f'Purchase price X = {X:.2f} USD/share')
print(f'Price increase a = {a:.2f} ({a*100:.2f}%)')
print(f'Expected profit Y = {Y:.2f} USD')
print(f'Minimum shares to hold k = {k} shares')
print('--------------------------')
print(f'Minimum shares to buy n = {n} shares')
print(f'Corresponding shares to sell m = {m} shares')
print(f'Total purchase amount = {buy_amount:.2f} USD')
print(f'Sell amount = {sell_amount:.2f} USD')
print(f'Shares held after selling = {hold_amount} shares')
print(f'Actual profit = {sell_amount - buy_amount:.2f} USD')

# Check conditions
cond1 = (sell_amount >= buy_amount + Y)  # Sell amount meets expected profit
cond2 = (hold_amount >= k)                # Hold shares meet minimum requirement
cond3 = (m < n)                          # Shares sold less than shares bought

if cond1 and cond2 and cond3:
    print('All conditions are met.')
else:
    print('Some conditions are not met:')
    if not cond1:
        print('- Sell amount is insufficient to achieve expected profit')
    if not cond2:
        print('- Not enough shares held after selling')
    if not cond3:
        print('- Shares sold are not less than shares bought')