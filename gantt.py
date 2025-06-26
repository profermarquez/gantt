import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Planificación", Start='2025-06-01', Finish='2025-06-10'),
    dict(Task="Desarrollo", Start='2025-06-11', Finish='2025-07-01'),
    dict(Task="Pruebas", Start='2025-07-02', Finish='2025-07-15'),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Diagrama de Gantt")
fig.update_yaxes(categoryorder="total ascending")
fig.show()
