import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Sample data for demonstrations
categories = [f'Category_{i}' for i in range(20)]
values = np.random.randint(10, 100, 20)
x_positions = list(range(len(categories)))

print("=== Plotly: Display All X Tick Labels ===\n")

# Method 1: Basic approach with ticktext and tickvals
print("Method 1: Basic ticktext and tickvals")
fig1 = go.Figure()
fig1.add_trace(go.Bar(x=categories, y=values, name='Values'))

# Set all tick labels explicitly
fig1.update_xaxes(
    tickmode='array',
    tickvals=categories,  # All category positions
    ticktext=categories,  # All category labels
    tickangle=45  # Rotate labels
)
fig1.update_layout(
    title='All X Labels (45° rotation)',
    width=1000,
    height=500
)
fig1.show()

# Method 2: Vertical labels (90° rotation)
print("\nMethod 2: Vertical labels")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=categories, y=values, mode='lines+markers'))

fig2.update_xaxes(
    tickmode='array',
    tickvals=categories,
    ticktext=categories,
    tickangle=90  # Vertical labels
)
fig2.update_layout(
    title='Vertical Labels (90°)',
    width=800,
    height=600
)
fig2.show()

# Method 3: Plotly Express with custom tick formatting
print("\nMethod 3: Plotly Express")
df = pd.DataFrame({
    'categories': categories,
    'values': values
})

fig3 = px.bar(df, x='categories', y='values',
             title='Plotly Express with All Labels')

# Update x-axis to show all labels
fig3.update_xaxes(
    tickmode='array',
    tickvals=categories,
    ticktext=categories,
    tickangle=45
)
fig3.update_layout(width=1100, height=500)
fig3.show()

# Method 4: Handling very long labels
print("\nMethod 4: Long labels with wrapping")
long_categories = [f'This_is_a_very_long_category_name_that_might_cause_display_issues_number_{i}' for i in range(12)]

fig4 = go.Figure()
fig4.add_trace(go.Bar(x=long_categories, y=np.random.randint(20, 80, 12)))

fig4.update_xaxes(
    tickmode='array',
    tickvals=long_categories,
    ticktext=long_categories,
    tickangle=45,
    tickfont=dict(size=8)  # Smaller font for long labels
)
fig4.update_layout(
    title='Long Labels with Small Font',
    width=1200,
    height=600,
    margin=dict(b=150)  # Extra bottom margin for rotated labels
)
fig4.show()

# Method 5: Multi-line labels using <br> tags
print("\nMethod 5: Multi-line labels")
multiline_categories = ['Line 1<br>Line 2', 'Category A<br>Sub A', 'Category B<br>Sub B'] * 6

fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=multiline_categories, y=np.random.randn(18), mode='markers'))

fig5.update_xaxes(
    tickmode='array',
    tickvals=multiline_categories,
    ticktext=multiline_categories,
    tickangle=0  # No rotation for multi-line
)
fig5.update_layout(
    title='Multi-line Labels',
    width=1000,
    height=500
)
fig5.show()

# Method 6: Subplots for many categories
print("\nMethod 6: Subplots approach")
from plotly.subplots import make_subplots

# Split categories into groups for subplots
group_size = 8
n_groups = (len(categories) + group_size - 1) // group_size

fig6 = make_subplots(
    rows=n_groups, cols=1,
    subplot_titles=[f'Categories {i*group_size+1}-{(i+1)*group_size}' for i in range(n_groups)],
    vertical_spacing=0.1
)

for i in range(n_groups):
    start_idx = i * group_size
    end_idx = min((i + 1) * group_size, len(categories))

    subset_categories = categories[start_idx:end_idx]
    subset_values = values[start_idx:end_idx]

    fig6.add_trace(
        go.Bar(x=subset_categories, y=subset_values, showlegend=False),
        row=i+1, col=1
    )

    fig6.update_xaxes(
        tickmode='array',
        tickvals=subset_categories,
        ticktext=subset_categories,
        tickangle=45,
        row=i+1, col=1
    )

fig6.update_layout(
    title='Subplots for Many Categories',
    width=1000,
    height=300 * n_groups,
    showlegend=False
)
fig6.show()

# Method 7: Dynamic sizing based on category count
print("\nMethod 7: Dynamic sizing")
def create_plotly_plot(categories, values):
    n_cats = len(categories)

    # Dynamic width based on category count
    if n_cats <= 10:
        width = 600
        tickangle = 0
        fontsize = 12
    elif n_cats <= 20:
        width = 900
        tickangle = 45
        fontsize = 10
    else:
        width = 1200
        tickangle = 45
        fontsize = 8

    fig = go.Figure()
    fig.add_trace(go.Bar(x=categories, y=values))

    fig.update_xaxes(
        tickmode='array',
        tickvals=categories,
        ticktext=categories,
        tickangle=tickangle,
        tickfont=dict(size=fontsize)
    )

    fig.update_layout(
        title=f'Dynamic Plot: {n_cats} Categories',
        width=width,
        height=500
    )

    return fig

# Demonstrate dynamic sizing
small_cats = categories[:8]
small_fig = create_plotly_plot(small_cats, values[:8])
small_fig.show()

medium_cats = categories[:15]
medium_fig = create_plotly_plot(medium_cats, values[:15])
medium_fig.show()

large_cats = categories
large_fig = create_plotly_plot(large_cats, values)
large_fig.show()

# Method 8: Heatmap with all labels
print("\nMethod 8: Heatmap with categorical axes")
matrix_data = np.random.rand(10, 20)

fig8 = go.Figure(data=go.Heatmap(
    z=matrix_data,
    x=categories[:20],  # Use first 20 categories
    y=[f'Row_{i}' for i in range(10)],
    colorscale='Viridis'
))

fig8.update_xaxes(
    tickmode='array',
    tickvals=categories[:20],
    ticktext=categories[:20],
    tickangle=45
)

fig8.update_layout(
    title='Heatmap with All Category Labels',
    width=1200,
    height=600
)
fig8.show()

# Method 9: Time series with all date labels
print("\nMethod 9: Time series data")
dates = pd.date_range('2023-01-01', periods=30, freq='D')
time_values = np.cumsum(np.random.randn(30)) + 100

fig9 = go.Figure()
fig9.add_trace(go.Scatter(x=dates, y=time_values, mode='lines+markers'))

# For time series, Plotly automatically handles most labels well
# But you can force specific formatting if needed
fig9.update_xaxes(
    tickformat='%m-%d',  # Custom date format
    tickangle=45,
    dtick='D'  # Daily ticks
)

fig9.update_layout(
    title='Time Series with All Date Labels',
    width=1000,
    height=500
)
fig9.show()

print("\n=== Summary for Plotly ===")
print("Key methods to display all x tick labels in Plotly:")
print("1. Use tickmode='array' with tickvals and ticktext")
print("2. Set tickangle for rotation (45, 90 degrees)")
print("3. Adjust tickfont size for many labels")
print("4. Increase figure width for more categories")
print("5. Use subplots for very many categories")
print("6. Consider dynamic sizing based on data length")
print("7. Add extra margin for rotated labels")
print("8. Use smaller font sizes (8-10) for many labels")
