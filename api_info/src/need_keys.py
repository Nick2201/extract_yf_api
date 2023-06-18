from pathlib import Path
import json
docs = (Path(Path.cwd()/'api_info'/"docs"))
finviz = Path(docs/"finviz_filters.json")


with open(finviz,"r") as _file:
    data = (json.load(_file))
    _keys = list(data.keys())
    # print(
    #     len(data.keys()),
    #     data.keys(),
    #     )
    descriptive = _keys[0:16]
    funamental = _keys[16:30]
    # print(descriptive)

descriptive = ("""Exchange
    Any
    Index
    Any
    Sector
    Any
    Industry
    Any
    Country
    Any
    Market Cap.
    Any
    Dividend Yield
    Any
    Float Short
    Any
    Analyst Recom.
    Any
    Option/Short
    Any
    Earnings Date
    Any
    Average Volume
    Any
    Relative Volume
    Any
    Current Volume
    Any
    Price
    Any
    Target Price
    Any
    IPO Date
    Any
    Shares Outstanding
    Any
    Float
    Any""")
fundamental = ("""P/E
    Any
    Forward P/E
    Any
    PEG
    Any
    P/S
    Any
    P/B
    Any
    Price/Cash
    Any
    Price/Free Cash Flow
    Any
    EPS growth
    this year
    Any
    EPS growth
    next year
    Any
    EPS growth
    past 5 years
    Any
    EPS growth
    next 5 years
    Any
    Sales growth
    past 5 years
    Any
    EPS growth
    qtr over qtr
    Any
    Sales growth
    qtr over qtr
    Any
    Return on Assets
    Any
    Return on Equity
    Any
    Return on Investment
    Any
    Current Ratio
    Any
    Quick Ratio
    Any
    LT Debt/Equity
    Any
    Debt/Equity
    Any
    Gross Margin
    Any
    Operating Margin
    Any
    Net Profit Margin
    Any
    Payout Ratio
    Any
    Insider
    Ownership
    Any
    Insider
    Transactions
    Any
    Institutional
    Ownership
    Any
    Institutional
    Transactions
    Any""")
technical = ('''Performance
    Any
    Performance 2
    Any
    Volatility
    Any
    RSI (14)
    Any
    Gap
    Any
    20-Day Simple Moving Average
    Any
    50-Day Simple Moving Average
    Any
    200-Day Simple Moving Average
    Any
    Change
    Any
    Change from Open
    Any
    20-Day High/Low
    Any
    50-Day High/Low
    Any
    52-Week High/Low
    Any
    Pattern
    Any
    Candlestick
    Any
    Beta
    Any
    Average True Range
    Any
    After-Hours Close
    Any
    After-Hours Change
    Any''')
def elements(_text):

    [print(element.strip()) for element in _text.split("\n")[0::2]]


elements(descriptive)
elements(fundamental)
elements(technical)

# print((descriptive.split("\n")[0::2]))
# print((fundamental.strip().split("\n")[0::2]))
# print((technical.strip().split("\n")[0::2]))
