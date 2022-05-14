import streamlit as st
import plotly.express as px
from draft_analyzer import values_for_graphs, draft_result_value_df, top_5_best_picks, top_5_worst_picks

# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
market_values = values_for_graphs
draft_ranks = draft_result_value_df
top_5_best_picks
top_5_worst_picks

# Row A
a1, a2, a3 = st.columns(3)
a1.draft_ranks
a2.top_5_best_picks
a3.top_5_worst_picks

# # Row B
# b1, b2, b3, b4 = st.columns(4)
# b1.metric("Temperature", "70 °F", "1.2 °F")
# b2.metric("Wind", "9 mph", "-8%")
# b3.metric("Humidity", "86%", "4%")
# b4.metric("Humidity", "86%", "4%")

# Row C

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Total Value')
    px.histogram(market_values, x="Manager", y="Sims Value", text_auto=True,
                 height=400)
with c2:
    st.markdown('### Value By Position')
    px.histogram(market_values, x="Manager", y="Sims Value", color='pos', barmode='group', text_auto=True,
                 height=400)


# fig = px.histogram(final_df, x="Manager", y="Sims Value", color='pos', barmode='group', text_auto=True,
#                    height=400, title='Value by Position')
# fig2 = px.histogram(final_df, x="Manager", y="Sims Value", text_auto=True,
#                     height=400, title='Total Value')
#
# fig3 = px.histogram(final_df, x='Manager', y='age', text_auto=True, title='Total Team Age')
#
# fig4 = px.histogram(final_df, x='Manager', y='weight', text_auto=True, title='Value by THICCness')
# fig5 = px.histogram(final_df, x='Manager', y='height', text_auto=True, title='Who drafts the short kings?')
# st.plotly_chart(fig2, use_container_width=True)
# st.plotly_chart(fig, use_container_width=True)
# st.plotly_chart(fig3, use_container_width=True)