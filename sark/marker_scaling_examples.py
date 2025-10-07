import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data for demonstration
np.random.seed(42)
x = np.random.randn(50)
y = np.random.randn(50)
sizes = np.random.randint(10, 1000, 50)  # Random sizes for demonstration
categories = np.random.choice(['A', 'B', 'C'], 50)

print("=== Marker Scaling Examples ===\n")

# Method 1: Basic scatter with size scaling
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Marker Scaling Proportional to Values', fontsize=16)

# Original data scatter
scatter = ax1.scatter(x, y, s=sizes, alpha=0.6, c=sizes, cmap='viridis')
ax1.set_title('Method 1: Basic Size Scaling')
ax1.set_xlabel('X values')
ax1.set_ylabel('Y values')
plt.colorbar(scatter, ax=ax1, label='Size values')

# Method 2: Normalized sizes for better control
normalized_sizes = (sizes - sizes.min()) / (sizes.max() - sizes.min()) * 300 + 50
ax2.scatter(x, y, s=normalized_sizes, alpha=0.6, c=sizes, cmap='plasma')
ax2.set_title('Method 2: Normalized Sizes (50-350 range)')
ax2.set_xlabel('X values')
ax2.set_ylabel('Y values')
plt.colorbar(scatter, ax=ax2, label='Original size values')

# Method 3: Logarithmic scaling for wide value ranges
log_sizes = np.log(sizes) * 20 + 50  # Log scaling with offset
ax3.scatter(x, y, s=log_sizes, alpha=0.6, c=sizes, cmap='inferno')
ax3.set_title('Method 3: Logarithmic Scaling')
ax3.set_xlabel('X values')
ax3.set_ylabel('Y values')
plt.colorbar(scatter, ax=ax3, label='Size values')

# Method 4: Square root scaling (often looks more natural)
sqrt_sizes = np.sqrt(sizes) * 5 + 20
ax4.scatter(x, y, s=sqrt_sizes, alpha=0.6, c=sizes, cmap='cividis')
ax4.set_title('Method 4: Square Root Scaling')
ax4.set_xlabel('X values')
ax4.set_ylabel('Y values')
plt.colorbar(scatter, ax=ax4, label='Size values')

plt.tight_layout()
plt.show()

# Method 5: Custom scaling function
def scale_markers(values, min_size=20, max_size=500, scaling='linear'):
    """Scale marker sizes based on values with different scaling methods."""
    if scaling == 'linear':
        return (values - values.min()) / (values.max() - values.min()) * (max_size - min_size) + min_size
    elif scaling == 'log':
        # Add small constant to avoid log(0) issues
        log_vals = np.log(values - values.min() + 1)
        return log_vals / log_vals.max() * (max_size - min_size) + min_size
    elif scaling == 'sqrt':
        sqrt_vals = np.sqrt(values - values.min())
        return sqrt_vals / sqrt_vals.max() * (max_size - min_size) + min_size
    elif scaling == 'square':
        square_vals = (values - values.min()) ** 2
        return square_vals / square_vals.max() * (max_size - min_size) + min_size

# Demonstrate custom scaling function
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Custom Scaling Function Examples', fontsize=16)

# Linear scaling
linear_sizes = scale_markers(sizes, scaling='linear')
axes[0,0].scatter(x, y, s=linear_sizes, alpha=0.6)
axes[0,0].set_title('Linear Scaling')

# Log scaling
log_sizes = scale_markers(sizes, scaling='log')
axes[0,1].scatter(x, y, s=log_sizes, alpha=0.6)
axes[0,1].set_title('Logarithmic Scaling')

# Square root scaling
sqrt_sizes = scale_markers(sizes, scaling='sqrt')
axes[1,0].scatter(x, y, s=sqrt_sizes, alpha=0.6)
axes[1,0].set_title('Square Root Scaling')

# Square scaling (emphasizes larger values)
square_sizes = scale_markers(sizes, scaling='square')
axes[1,1].scatter(x, y, s=square_sizes, alpha=0.6)
axes[1,1].set_title('Square Scaling (emphasizes large values)')

plt.tight_layout()
plt.show()

# Method 6: Bubble chart with categorical data
fig, ax = plt.subplots(figsize=(12, 8))

# Create sample data for bubble chart
companies = ['Apple', 'Google', 'Microsoft', 'Amazon', 'Tesla', 'Meta', 'Netflix', 'Spotify']
revenue = [394.3, 282.8, 211.9, 513.9, 81.5, 134.9, 31.6, 11.5]  # Billions
profit = [99.8, 76.0, 77.1, 30.4, 12.6, 39.4, 5.1, -0.3]  # Billions
market_cap = [3000, 1800, 2500, 1700, 800, 900, 200, 45]  # Billions

# Scale sizes by market cap
bubble_sizes = (np.array(market_cap) - min(market_cap)) / (max(market_cap) - min(market_cap)) * 1000 + 100

scatter = ax.scatter(revenue, profit, s=bubble_sizes, alpha=0.7, c=market_cap, cmap='RdYlBu')

# Add labels for each company
for i, company in enumerate(companies):
    ax.annotate(company, (revenue[i], profit[i]), xytext=(5, 5),
                textcoords='offset points', fontsize=9)

ax.set_xlabel('Revenue (Billions USD)')
ax.set_ylabel('Profit (Billions USD)')
ax.set_title('Company Performance Bubble Chart\n(Bubble size = Market Cap)')
ax.grid(True, alpha=0.3)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Market Cap (Billions USD)')

plt.tight_layout()
plt.show()

# Method 7: Handling edge cases (zeros, negatives)
print("\n=== Handling Edge Cases ===")

# Data with zeros and potential negative values
edge_case_sizes = np.array([0, 1, 10, 100, 1000, -5, -50])
edge_case_x = np.arange(len(edge_case_sizes))
edge_case_y = np.random.randn(len(edge_case_sizes))

# Method to handle edge cases
def robust_scale_markers(values, min_size=20, max_size=500):
    """Robust scaling that handles zeros and negative values."""
    # Handle negative values by taking absolute value
    abs_values = np.abs(values)

    # Handle zeros by adding small constant
    abs_values = np.where(abs_values == 0, 0.1, abs_values)

    # Use log scaling for better distribution
    log_scaled = np.log(abs_values)
    normalized = (log_scaled - log_scaled.min()) / (log_scaled.max() - log_scaled.min())

    return normalized * (max_size - min_size) + min_size

robust_sizes = robust_scale_markers(edge_case_sizes)

plt.figure(figsize=(10, 6))
plt.scatter(edge_case_x, edge_case_y, s=robust_sizes, alpha=0.7)
plt.title('Robust Scaling with Edge Cases')
plt.xlabel('Index')
plt.ylabel('Y values')

# Add text labels showing original values
for i, (size, orig_val) in enumerate(zip(robust_sizes, edge_case_sizes)):
    plt.annotate(f'{orig_val}', (edge_case_x[i], edge_case_y[i]),
                 xytext=(0, 10), textcoords='offset points', ha='center')

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("All marker scaling examples completed!")
print("Key takeaways:")
print("- Linear scaling: Good for evenly distributed values")
print("- Log scaling: Good for wide value ranges")
print("- Square root scaling: Often looks most natural to the eye")
print("- Always handle edge cases (zeros, negatives)")
print("- Normalize sizes to a reasonable range (50-500 works well)")
