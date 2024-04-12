# Python: How to center the Title in Plotly 

import plotly.express as px

df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_length",
    y="sepal_width",
    color="species",
    title="Example title here"
)

fig.update_layout(title_text='Example title', title_x=0.5)

fig.show()
