import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [10, 25, 15, 30, 20]
x = np.linspace(0, 10, 20)
y = np.sin(x)

print("=== Plotly: Bold X-Axis Tick Labels ===\n")

# Method 1: Basic bold tick labels
print("Method 1: Basic bold x-axis ticks")
fig1 = go.Figure()
fig1.add_trace(go.Bar(x=categories, y=values))

fig1.update_xaxes(
    tickfont=dict(
        size=12,
        weight='bold'  # Make tick labels bold
    ),
    tickangle=0
)

fig1.update_layout(
    title='Bold X-Axis Tick Labels (Basic)',
    width=600,
    height=400
)
fig1.show()

# Method 2: Bold with other styling
print("\nMethod 2: Bold with color and size")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=y, mode='lines+markers'))

fig2.update_xaxes(
    tickfont=dict(
        size=14,
        weight='bold',
        color='navy'  # Blue color
    ),
    tickangle=0
)

fig2.update_layout(
    title='Bold, Colored X-Axis Labels',
    width=700,
    height=450
)
fig2.show()

# Method 3: Bold labels at 45 degrees
print("\nMethod 3: Bold rotated labels")
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=categories * 3, y=values * 3))  # More categories

fig3.update_xaxes(
    tickmode='array',
    tickvals=categories * 3,
    ticktext=categories * 3,
    tickfont=dict(
        size=10,
        weight='bold',
        color='darkgreen'
    ),
    tickangle=45
)

fig3.update_layout(
    title='Bold Rotated Labels (45°)',
    width=900,
    height=500
)
fig3.show()

# Method 4: Plotly Express with bold ticks
print("\nMethod 4: Plotly Express bold ticks")
df = pd.DataFrame({
    'category': categories,
    'value': values
})

fig4 = px.bar(df, x='category', y='value', title='Express with Bold Ticks')

# Make x-axis tick labels bold
fig4.update_xaxes(
    tickfont=dict(
        size=13,
        weight='bold',
        color='purple'
    )
)

fig4.show()

# Method 5: Bold vs normal comparison
print("\nMethod 5: Bold vs normal comparison")
fig5 = go.Figure()

# Normal weight
fig5.add_trace(go.Bar(
    x=['Normal', 'Weight', 'Labels'],
    y=[15, 25, 20],
    name='Normal Weight',
    marker_color='lightblue'
))

# Bold weight
fig5.add_trace(go.Bar(
    x=['Bold', 'Weight', 'Labels'],
    y=[18, 28, 23],
    name='Bold Weight',
    marker_color='darkblue'
))

fig5.update_xaxes(
    tickfont=dict(size=12, weight='bold')
)

fig5.update_layout(
    title='Bold vs Normal Weight Comparison',
    barmode='group',
    width=700,
    height=450
)
fig5.show()

# Method 6: Bold with different font families
print("\nMethod 6: Bold with font families")
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x=x, y=np.cos(x), mode='lines'))

fig6.update_xaxes(
    tickfont=dict(
        size=11,
        weight='bold',
        family='Arial Black, sans-serif'  # Bold-friendly font
    ),
    tickangle=0
)

fig6.update_layout(
    title='Bold Labels with Font Family',
    width=600,
    height=400
)
fig6.show()

# Method 7: Multiple axes with bold styling
print("\nMethod 7: Multiple axes styling")
fig7 = go.Figure()

fig7.add_trace(go.Scatter(
    x=x,
    y=np.sin(x),
    mode='lines+markers',
    name='sin(x)',
    line=dict(color='blue')
))

fig7.add_trace(go.Scatter(
    x=x,
    y=np.cos(x),
    mode='lines+markers',
    name='cos(x)',
    line=dict(color='red')
))

# Style x-axis
fig7.update_xaxes(
    title_text='X Values (Bold Ticks)',
    tickfont=dict(
        size=12,
        weight='bold',
        color='black'
    ),
    tickangle=0
)

# Style y-axis
fig7.update_yaxes(
    title_text='Y Values',
    tickfont=dict(
        size=10,
        weight='normal',
        color='gray'
    )
)

fig7.update_layout(
    title='Multiple Axes with Bold X-Ticks',
    width=800,
    height=500
)
fig7.show()

# Method 8: Bold ticks in subplots
print("\nMethod 8: Subplots with bold ticks")
from plotly.subplots import make_subplots

fig8 = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Plot 1', 'Plot 2', 'Plot 3', 'Plot 4')
)

# Add traces
fig8.add_trace(go.Bar(x=categories, y=values), row=1, col=1)
fig8.add_trace(go.Scatter(x=x[:10], y=y[:10]), row=1, col=2)
fig8.add_trace(go.Bar(x=categories, y=[v*2 for v in values]), row=2, col=1)
fig8.add_trace(go.Scatter(x=x[10:], y=y[10:]), row=2, col=2)

# Make all subplot x-axes have bold ticks
for row in range(1, 3):
    for col in range(1, 3):
        fig8.update_xaxes(
            tickfont=dict(size=10, weight='bold'),
            row=row, col=col
        )

fig8.update_layout(
    title='Subplots with Bold X-Tick Labels',
    width=1000,
    height=800
)
fig8.show()

# Method 9: Conditional bold styling
print("\nMethod 9: Conditional bold styling")
fig9 = go.Figure()
fig9.add_trace(go.Bar(x=categories, y=values))

# You can make specific ticks bold by recreating the figure with custom styling
# For more control, use annotations or custom ticktext
annotations = []
for i, cat in enumerate(categories):
    annotations.append(
        dict(
            text=f'<b>{cat}</b>',  # Bold HTML text
            x=i,
            y=0,
            showarrow=False,
            font=dict(size=12),
            xanchor='center',
            yanchor='top'
        )
    )

fig9.update_xaxes(
    tickfont=dict(size=12, weight='bold'),
    showticklabels=False  # Hide default labels
)

fig9.update_layout(
    title='Bold Labels using Annotations',
    annotations=annotations,
    width=600,
    height=450
)
fig9.show()

print("\n=== Summary ===")
print("To make x-axis tick labels bold in Plotly:")
print("fig.update_xaxes(tickfont=dict(weight='bold'))")
print("\nAdditional styling options:")
print("- size: Font size (8-14)")
print("- color: Text color")
print("- family: Font family")
print("- weight: 'bold', 'normal', or numeric (100-900)")
print("\nFor subplots:")
print("fig.update_xaxes(tickfont=dict(weight='bold'), row=1, col=1)")
print("\nFor Plotly Express:")
print("fig.update_xaxes(tickfont=dict(weight='bold')) after creation")
