import pandas as pd
from pandas import DataFrame

XLS = pd.ExcelFile('Book1.xls')
LOGIN_SHEET = pd.read_excel(XLS, 'Login')
SITE_SHEET = pd.read_excel(XLS, 'Site')
PROGRAM_SHEET = pd.read_excel(XLS, 'Program', dtype=str)
TLOG_SHEET = pd.read_excel(XLS, 'T-Log')
class ExcelValueGetter:
    df = None

    def __init__(self, df: DataFrame) -> None:
        self.df = df

    def get_total_rows(self) -> int:
        return self.df.count().values[0]

    def get_value_wrt_col_row(self, colName, rowNo) -> str:
        return self.df[colName].iloc[rowNo]

    def get_first_value_wrt_col(self, colName):
        return self.df[colName].iloc[0]    