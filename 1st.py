import pandas as pd
import streamlit as st

# Display the logo
#st.image('C:\Users\Jibin Mathai\PycharmProjects\FirstProject\.venv', use_column_width=True)

# Your Streamlit app code follows
st.image(r'C:\Users\Jibin Mathai\PycharmProjects\FirstProject\.venv\logo.png', use_column_width=True)

# Center-align the title using HTML
st.markdown("<h1 style='text-align: center;'>Hardware BOM Comparison Tool</h1>", unsafe_allow_html=True)

#st.write("By Jibin ")


# Upload the Excel files
file1 = st.file_uploader("Upload the first BOM file", type=["xlsx"])
file2 = st.file_uploader("Upload the second BOM file", type=["xlsx"])

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
    st.write("### Rows added in the second file:")
    st.dataframe(df_added)
    st.write("### Rows removed from the first file:")
    st.dataframe(df_removed)
    # st.write("### Rows changed between files:")
    # st.dataframe(df_changed)
