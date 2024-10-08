import pandas as pd
import streamlit as st
import plotly.express as px


# Display the logo
#st.image('C:\Users\Jibin Mathai\PycharmProjects\FirstProject\.venv', use_column_width=True)

# Your Streamlit app code follows
st.image(r'C:\Users\Jibin Mathai\PycharmProjects\FirstProject\.venv\logo.png', use_column_width=True)

# Center-align the title using HTML
st.markdown("<h1 style='text-align: center;'>Hardware BOM Comparison Tool</h1>", unsafe_allow_html=True)

#st.write("By Jibin ")


# Upload the Excel files
file1 = st.file_uploader("Upload the 1st BOM file", type=["xlsx"])
file2 = st.file_uploader("Upload the 2nd BOM file", type=["xlsx"])

if file1 and file2:
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Perform the comparison
    merged_df = df1.merge(df2, how="outer", indicator=True)
    df_added = merged_df[merged_df["_merge"] == "left_only"]
    df_removed = merged_df[merged_df["_merge"] == "right_only"]
    # df_changed = df1.merge(df2, how="inner", on=df1.columns.tolist())
    # df_changed = df_changed[df1.ne(df2).any(axis=1)]

    # Display the results
    st.write("## Comparison Results")
    st.write("### Changes Detected in the 1st File:")
    st.dataframe(df_added)
    st.write("### Changes Detected in the 2nd File:")
    st.dataframe(df_removed)
    # st.write("### Rows changed between files:")
    # st.dataframe(df_changed)

    # calculate counts for Visualization
    num_added = len(df_added)
    num_removed = len(df_removed)
    num_common = len(df1) - num_added  # Assuming common entries are those not added/removed

    # Create a data frame for visualization
    comparison_data = pd.DataFrame({
        'Category': ['1st File', '2nd File', 'Common'],
        'Count': [num_added, num_removed, num_common]
    })

    # Create a pie chart using Plotly
    fig = px.pie(comparison_data, names='Category', values='Count', title='BOM Comparison PIE Chart')

    # Display the pie chart
    st.plotly_chart(fig)

    # Optionally, you could also display a bar graph
    fig_bar = px.bar(comparison_data, x='Category', y='Count', title='BOM Comparison Summary')
    st.plotly_chart(fig_bar)

# Footer
st.write("---")  # Horizontal line (optional)
st.write("Developed by Jibin")

