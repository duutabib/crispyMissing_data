import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Sample data
x = np.linspace(0, 10, 50)
y = np.sin(x) + np.random.normal(0, 0.1, 50)
categories = ['Category A', 'Category B', 'Category C', 'Category D']

print("=== Plotly Font Size Control in update_layout ===\n")

# Method 1: Basic font size control
print("Method 1: Basic font sizing")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Data'))

fig1.update_layout(
    title=dict(
        text='Custom Title Font Size',
        font=dict(size=24)  # Title font size
    ),
    xaxis=dict(
        title=dict(text='X Axis Label', font=dict(size=16)),
        tickfont=dict(size=12)  # X tick labels
    ),
    yaxis=dict(
        title=dict(text='Y Axis Label', font=dict(size=16)),
        tickfont=dict(size=12)  # Y tick labels
    ),
    legend=dict(font=dict(size=14)),  # Legend font size
    width=800,
    height=600
)
fig1.show()

# Method 2: Complete font family and style control
print("\nMethod 2: Font family and styling")
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=categories, y=[10, 25, 15, 30], name='Values'))

fig2.update_layout(
    title=dict(
        text='Styled Title with Font Family',
        font=dict(
            size=20,
            family='Arial, sans-serif',
            color='navy'
        )
    ),
    xaxis=dict(
        title=dict(
            text='Categories',
            font=dict(size=14, family='Times New Roman, serif')
        ),
        tickfont=dict(size=11, color='darkgreen')
    ),
    yaxis=dict(
        title=dict(
            text='Values',
            font=dict(size=14, family='Times New Roman, serif')
        ),
        tickfont=dict(size=11, color='darkred')
    ),
    legend=dict(
        font=dict(size=12, family='Courier New, monospace')
    ),
    font=dict(size=12)  # Global font size for any unstyled text
)
fig2.show()

# Method 3: Plotly Express with font control
print("\nMethod 3: Plotly Express font sizing")
df = pd.DataFrame({
    'x': x,
    'y': y,
    'category': np.random.choice(['Group A', 'Group B'], 50)
})

fig3 = px.scatter(df, x='x', y='y', color='category',
                 title='Express Plot with Custom Fonts')

# Update fonts after creation
fig3.update_layout(
    title=dict(font=dict(size=22, color='purple')),
    xaxis=dict(
        title=dict(font=dict(size=15)),
        tickfont=dict(size=10)
    ),
    yaxis=dict(
        title=dict(font=dict(size=15)),
        tickfont=dict(size=10)
    ),
    legend=dict(font=dict(size=13))
)
fig3.show()

# Method 4: Multiple subplots with individual font control
print("\nMethod 4: Subplots with individual font sizing")
from plotly.subplots import make_subplots

fig4 = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Plot 1', 'Plot 2', 'Plot 3', 'Plot 4')
)

# Add traces
fig4.add_trace(go.Scatter(x=x[:25], y=y[:25]), row=1, col=1)
fig4.add_trace(go.Bar(x=categories, y=[20, 30, 25, 35]), row=1, col=2)
fig4.add_trace(go.Scatter(x=x[25:], y=y[25:]), row=2, col=1)
fig4.add_trace(go.Bar(x=categories, y=[15, 35, 20, 40]), row=2, col=2)

# Individual subplot font control
fig4.update_xaxes(tickfont=dict(size=9), row=1, col=1)
fig4.update_yaxes(tickfont=dict(size=9), row=1, col=1)

fig4.update_xaxes(tickfont=dict(size=10), row=1, col=2)
fig4.update_yaxes(tickfont=dict(size=10), row=1, col=2)

fig4.update_xaxes(tickfont=dict(size=8), row=2, col=1)
fig4.update_yaxes(tickfont=dict(size=8), row=2, col=1)

fig4.update_xaxes(tickfont=dict(size=11), row=2, col=2)
fig4.update_yaxes(tickfont=dict(size=11), row=2, col=2)

fig4.update_layout(
    title=dict(text='Subplots with Individual Font Sizes', font=dict(size=18)),
    width=1000,
    height=800
)
fig4.show()

# Method 5: Font size comparison
print("\nMethod 5: Font size comparison")
fig_sizes = []

font_sizes = [8, 12, 16, 20]
for size in font_sizes:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 2], mode='markers+lines'))

    fig.update_layout(
        title=dict(text=f'Font Size {size}', font=dict(size=size)),
        xaxis=dict(
            title=dict(text='X Axis', font=dict(size=size-2)),
            tickfont=dict(size=size-4)
        ),
        yaxis=dict(
            title=dict(text='Y Axis', font=dict(size=size-2)),
            tickfont=dict(size=size-4)
        ),
        width=400,
        height=300
    )
    fig_sizes.append(fig)

# This would show 4 separate figures with different font sizes
for i, fig in enumerate(fig_sizes):
    print(f"\nShowing figure {i+1} with font size {font_sizes[i]}")
    fig.show()

# Method 6: Responsive font sizing
print("\nMethod 6: Responsive font sizing")
fig6 = go.Figure()
fig6.add_trace(go.Heatmap(
    z=np.random.rand(8, 12),
    x=[f'Col_{i}' for i in range(12)],
    y=[f'Row_{i}' for i in range(8)]
))

# Responsive font sizing based on data dimensions
n_cols = 12
n_rows = 8

# Adjust font sizes based on data size
title_font = max(14, min(24, 300 // max(n_cols, n_rows)))
axis_font = max(10, min(16, 200 // max(n_cols, n_rows)))
tick_font = max(8, min(12, 150 // max(n_cols, n_rows)))

fig6.update_layout(
    title=dict(text=f'Heatmap {n_rows}x{n_cols}', font=dict(size=title_font)),
    xaxis=dict(
        tickfont=dict(size=tick_font),
        tickangle=45 if n_cols > 8 else 0
    ),
    yaxis=dict(tickfont=dict(size=tick_font)),
    width=800,
    height=600
)
fig6.show()

# Method 7: Complete font styling example
print("\nMethod 7: Complete font styling")
fig7 = go.Figure()
fig7.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='lines+markers',
    name='Sine Wave',
    line=dict(width=3),
    marker=dict(size=6)
))

# Comprehensive font styling
fig7.update_layout(
    title=dict(
        text='Comprehensive Font Styling Example',
        font=dict(
            size=20,
            family='Arial Black, sans-serif',
            color='darkblue'
        ),
        x=0.5,  # Center the title
        xanchor='center'
    ),
    xaxis=dict(
        title=dict(
            text='Time (seconds)',
            font=dict(size=14, family='Times, serif', color='darkgreen')
        ),
        tickfont=dict(size=11, color='black'),
        tickangle=0
    ),
    yaxis=dict(
        title=dict(
            text='Amplitude',
            font=dict(size=14, family='Times, serif', color='darkred')
        ),
        tickfont=dict(size=11, color='black')
    ),
    legend=dict(
        title=dict(text='Legend', font=dict(size=13, weight='bold')),
        font=dict(size=12, family='Arial, sans-serif')
    ),
    annotations=[
        dict(
            text='Custom Annotation',
            x=5, y=0,
            font=dict(size=12, color='purple'),
            showarrow=True,
            arrowhead=2
        )
    ],
    width=900,
    height=600
)
fig7.show()

# Method 8: Saving with custom font sizes
print("\nMethod 8: Saving plots with custom fonts")
fig8 = go.Figure()
fig8.add_trace(go.Bar(x=categories, y=[30, 45, 25, 40]))

fig8.update_layout(
    title=dict(text='Plot for Saving', font=dict(size=18)),
    xaxis=dict(tickfont=dict(size=12)),
    yaxis=dict(tickfont=dict(size=12)),
    width=800,
    height=500
)

# Save as HTML (preserves fonts)
fig8.write_html("custom_fonts_plot.html")

# Save as image (static fonts)
fig8.write_image("custom_fonts_plot.png", width=800, height=500)

print("Figures saved with custom font sizes")

print("\n=== Font Size Summary ===")
print("Title fonts: 16-24px (larger for emphasis)")
print("Axis label fonts: 12-16px (readable)")
print("Tick label fonts: 8-12px (smaller for many labels)")
print("Legend fonts: 10-14px (clear but not dominant)")
print("Annotation fonts: 10-12px (contextual)")
print("\nGeneral tips:")
print("- Use consistent font families across plots")
print("- Consider readability vs space constraints")
print("- Test on target display sizes")
print("- Use relative sizing for responsive design")
