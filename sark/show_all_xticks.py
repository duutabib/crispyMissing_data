import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create sample data that would typically cause tick label issues
categories = [f'Category_{i}' for i in range(20)]  # 20 categories
values = np.random.randint(10, 100, 20)
x_positions = np.arange(len(categories))

print("=== Display All X Tick Labels ===\n")

# Method 1: Basic approach with rotation
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Methods to Display All X Tick Labels', fontsize=16)

# Method 1: Simple rotation
ax1.bar(x_positions, values)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(categories, rotation=45, ha='right')
ax1.set_title('Method 1: Basic Rotation (45°)')
ax1.tick_params(axis='x', labelsize=9)

# Method 2: Vertical labels
ax2.bar(x_positions, values, color='orange')
ax2.set_xticks(x_positions)
ax2.set_xticklabels(categories, rotation=90, ha='center')
ax2.set_title('Method 2: Vertical Labels (90°)')
ax2.tick_params(axis='x', labelsize=8)

# Method 3: Wider figure with smaller rotation
fig3, ax3_wide = plt.subplots(figsize=(16, 6))
ax3_wide.bar(x_positions, values, color='green')
ax3_wide.set_xticks(x_positions)
ax3_wide.set_xticklabels(categories, rotation=30, ha='right')
ax3_wide.set_title('Method 3: Wider Figure (30° rotation)')
ax3_wide.tick_params(axis='x', labelsize=10)

# Method 4: Multiple lines for long labels
fig4, ax4_multi = plt.subplots(figsize=(14, 8))
long_categories = [f'Very_Long_Category_Name_{i}_With_More_Text' for i in range(15)]
long_values = np.random.randint(20, 80, 15)
long_positions = np.arange(len(long_categories))

ax4_multi.bar(long_positions, long_values, color='red')
ax4_multi.set_xticks(long_positions)

# Multi-line labels using '\n'
wrapped_labels = [f'Very Long\nCategory\nName {i}' for i in range(15)]
ax4_multi.set_xticklabels(wrapped_labels, rotation=0, ha='center', va='top')
ax4_multi.set_title('Method 4: Multi-line Labels')
ax4_multi.tick_params(axis='x', labelsize=8)

plt.tight_layout()
plt.show()

# Method 5: Using minor ticks and grid
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(x_positions, values, 'o-', markersize=6, linewidth=2)

# Show all x ticks
ax.set_xticks(x_positions)
ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=9)

# Add minor ticks
ax.minorticks_on()
ax.grid(True, which='major', linestyle='-', alpha=0.7)
ax.grid(True, which='minor', linestyle=':', alpha=0.4)

ax.set_title('Method 5: With Grid and Minor Ticks')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
plt.tight_layout()
plt.show()

# Method 6: Subplot approach for many categories
fig, axes = plt.subplots(3, 1, figsize=(16, 15))

# Split categories into groups
group_size = 7
for i, ax in enumerate(axes):
    start_idx = i * group_size
    end_idx = min((i + 1) * group_size, len(categories))

    subset_categories = categories[start_idx:end_idx]
    subset_values = values[start_idx:end_idx]
    subset_positions = np.arange(len(subset_categories))

    ax.bar(subset_positions, subset_values)
    ax.set_xticks(subset_positions)
    ax.set_xticklabels(subset_categories, rotation=45, ha='right', fontsize=10)
    ax.set_title(f'Method 6: Subplot Group {i+1} (Categories {start_idx+1}-{end_idx})')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Method 7: Dynamic label sizing based on count
def smart_label_display(categories, max_labels_per_line=8, rotation=45):
    """Automatically adjust figure size and label display based on category count."""
    n_categories = len(categories)

    if n_categories <= max_labels_per_line:
        fig_width = 10
        rotation_angle = 0
        fontsize = 12
    elif n_categories <= 15:
        fig_width = 12
        rotation_angle = 45
        fontsize = 10
    else:
        fig_width = 16
        rotation_angle = 45
        fontsize = 8

    fig, ax = plt.subplots(figsize=(fig_width, 6))
    positions = np.arange(n_categories)

    ax.bar(positions, values[:n_categories])
    ax.set_xticks(positions)
    ax.set_xticklabels(categories, rotation=rotation_angle, ha='right', fontsize=fontsize)
    ax.set_title(f'Smart Display: {n_categories} Categories')
    ax.grid(True, alpha=0.3)

    return fig, ax

# Demonstrate smart labeling
print("\nMethod 7: Smart labeling examples")

# Small number of categories
fig_small, ax_small = smart_label_display(['A', 'B', 'C', 'D', 'E'])
plt.show()

# Medium number of categories
fig_med, ax_med = smart_label_display([f'Cat_{i}' for i in range(12)])
plt.show()

# Large number of categories
fig_large, ax_large = smart_label_display([f'Category_{i}' for i in range(25)])
plt.show()

# Method 8: Pandas plotting with all labels
print("\nMethod 8: Pandas DataFrame plotting")
df = pd.DataFrame({
    'category': categories,
    'value': values
})

fig, ax = plt.subplots(figsize=(16, 6))
df.set_index('category').plot(kind='bar', ax=ax, rot=45)
ax.set_title('Pandas Bar Plot with All Labels')
ax.tick_params(axis='x', labelsize=8)
plt.tight_layout()
plt.show()

# Method 9: Custom formatter for long labels
fig, ax = plt.subplots(figsize=(14, 8))

# Create very long category names
long_cats = [f'This_is_a_very_long_category_name_that_might_cause_display_issues_{i}' for i in range(10)]
long_vals = np.random.randint(30, 90, 10)

ax.bar(range(len(long_cats)), long_vals)

# Custom tick formatter to show full labels
ax.set_xticks(range(len(long_cats)))
ax.set_xticklabels(long_cats, rotation=45, ha='right', fontsize=7,
                  wrap=True)  # wrap=True helps with very long labels

ax.set_title('Method 9: Very Long Labels with Wrapping')
plt.tight_layout()
plt.show()

print("\n=== Summary ===")
print("Key methods to display all x tick labels:")
print("1. Set custom ticks: ax.set_xticks(positions)")
print("2. Set custom labels: ax.set_xticklabels(categories, rotation=45)")
print("3. Rotate labels: rotation=45 or rotation=90")
print("4. Adjust figure size: figsize=(width, height)")
print("5. Reduce font size: labelsize=8 or smaller")
print("6. Use multi-line labels: '\\n' in label strings")
print("7. Add grid for better readability")
print("8. Consider subplots for many categories")
print("9. Use smart/dynamic sizing based on data length")
