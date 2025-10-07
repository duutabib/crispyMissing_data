import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Sample data for demonstrations
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

print("=== Plotly Figure Size Examples ===\n")

# Method 1: Set size in layout (most common)
print("Method 1: Layout-based sizing")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines+markers'))
fig1.update_layout(
    title='Figure with Custom Size (800x600)',
    width=800,  # Width in pixels
    height=600,  # Height in pixels
    showlegend=True
)
fig1.show()

# Method 2: Set size when creating figure
print("\nMethod 2: Figure constructor sizing")
fig2 = go.Figure(layout=dict(
    width=1000,
    height=400,
    title='Wide Figure (1000x400)'
))
fig2.add_trace(go.Scatter(x=x, y=np.cos(x), mode='lines'))
fig2.show()

# Method 3: Using Plotly Express with size parameters
print("\nMethod 3: Plotly Express sizing")
df = pd.DataFrame({
    'x': x,
    'y': np.sin(x),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})
fig3 = px.scatter(df, x='x', y='y', color='category',
                 width=900, height=500,
                 title='Plotly Express with Custom Size')
fig3.show()

# Method 4: Responsive sizing with autosize
print("\nMethod 4: Responsive sizing")
fig4 = go.Figure()
fig4.add_trace(go.Bar(x=['A', 'B', 'C', 'D'], y=[10, 25, 15, 30]))
fig4.update_layout(
    title='Responsive Figure (autosize=False)',
    width=700,
    height=450,
    autosize=False  # Disable responsive behavior
)
fig4.show()

# Method 5: Template-based sizing
print("\nMethod 5: Template with size constraints")
fig5 = go.Figure()
fig5.add_trace(go.Heatmap(z=np.random.rand(10, 10)))
fig5.update_layout(
    title='Heatmap with Template Sizing',
    width=600,
    height=500,
    template='plotly_white'  # Clean template
)
fig5.show()

# Method 6: Subplot sizing
print("\nMethod 6: Subplots with custom sizing")
from plotly.subplots import make_subplots

fig6 = make_subplots(rows=2, cols=2,
                     subplot_titles=('Plot 1', 'Plot 2', 'Plot 3', 'Plot 4'),
                     specs=[[{'type': 'scatter'}, {'type': 'bar'}],
                           [{'type': 'surface'}, {'type': 'scatter3d'}]])

# Add traces to subplots
fig6.add_trace(go.Scatter(x=x[:50], y=y[:50]), row=1, col=1)
fig6.add_trace(go.Bar(x=['X', 'Y', 'Z'], y=[10, 20, 15]), row=1, col=2)
fig6.add_trace(go.Scatter3d(x=x[:20], y=y[:20], z=np.cos(x[:20])), row=2, col=2)

fig6.update_layout(
    title='Subplots with Custom Size (1200x800)',
    width=1200,
    height=800,
    showlegend=False
)
fig6.show()

# Method 7: Dynamic sizing based on data
print("\nMethod 7: Dynamic sizing")
data_length = len(x)
# Adjust size based on data length
dynamic_width = min(1200, max(600, data_length * 8))  # Scale width with data
dynamic_height = 500

fig7 = go.Figure()
fig7.add_trace(go.Scatter(x=x, y=y, mode='markers'))
fig7.update_layout(
    title=f'Dynamic Size Based on Data (width={dynamic_width})',
    width=dynamic_width,
    height=dynamic_height
)
fig7.show()

# Method 8: Saving figures with specific sizes
print("\nMethod 8: Saving with custom sizes")
fig8 = go.Figure()
fig8.add_trace(go.Scatter(x=x, y=np.sin(x), name='sin(x)'))
fig8.add_trace(go.Scatter(x=x, y=np.cos(x), name='cos(x)'))
fig8.update_layout(
    title='Figure for Saving',
    width=1000,
    height=600
)

# Save with specific size
fig8.write_html("custom_size_plot.html")
fig8.write_image("custom_size_plot.png", width=1000, height=600)

print("Figure saved as 'custom_size_plot.html' and 'custom_size_plot.png'")
print()

# Method 9: Responsive design with min/max constraints
print("\nMethod 9: Responsive with constraints")
fig9 = go.Figure()
fig9.add_trace(go.Box(y=y, name='Data'))
fig9.update_layout(
    title='Responsive Figure with Size Constraints',
    width=800,
    height=500,
    # For web deployment, you can set responsive behavior
    autosize=True  # Allow responsive resizing
)
fig9.show()

print("\n=== Size Comparison ===")
print("Small figure (400x300):")
fig_small = go.Figure()
fig_small.add_trace(go.Scatter(x=[1,2,3], y=[1,4,2]))
fig_small.update_layout(width=400, height=300, title='Small (400x300)')
fig_small.show()

print("\nLarge figure (1400x900):")
fig_large = go.Figure()
fig_large.add_trace(go.Scatter(x=[1,2,3,4,5], y=[1,4,2,5,3]))
fig_large.update_layout(width=1400, height=900, title='Large (1400x900)')
fig_large.show()

print("\nAll examples completed!")
print("\nKey Points:")
print("- Use 'width' and 'height' parameters in pixels")
print("- Set in layout: fig.update_layout(width=800, height=600)")
print("- Set in constructor: go.Figure(layout=dict(width=800, height=600))")
print("- Use with Plotly Express: px.scatter(..., width=800, height=600)")
print("- Combine with autosize=False for fixed dimensions")
print("- Save figures with write_image() to preserve exact dimensions")
