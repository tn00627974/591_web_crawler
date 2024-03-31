import pandas as pd

# req = pd.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")

# df = req[0]
# print(df.head())


import pandas as pd

# 從網址讀取表格
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
dfs = pd.read_html(url)

# 查看讀取到的表格數量
print(len(dfs))  # 假設只有一個表格

# 將表格轉換為DataFrame
df = dfs[0]

# 顯示DataFrame的前幾行
print(df.head())
