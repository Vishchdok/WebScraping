import pandas as pd

symbol = 'WDC'
tgt_website = r'https://sg.finance.yahoo.com/quote/{}/key-statistics?p={}'.format(symbol,symbol)

def get_key_stats(tgt_website):

    # The web page is made up of several html tables. By calling the read_html function, all the tables are retrieved
    # in the dataframe format.
    # The next step is to append all the table and transpose it to give a clear, singular row of data.

    df_list = pd.read_html(tgt_website)
    result_df = df_list[0]

    for df in df_list[1:]:
        result_df = result_df.append(df)

    # The data is in column format.
    # Transpose the result to create a single row of data
    return result_df.set_index(0).T

# Save the result to csv format
result_df = get_key_stats(tgt_website)

# Pull stock symbols from nasdaq.com
weblink = 'https://www.nasdaq.com/screening/companies-by-name.aspx?letter=A&render=download'
sym_df = pd.read_csv(weblink)
stock_symbol_list = sym_df.Symbol.tolist()
#print(tgt_website)
print(stock_symbol_list)