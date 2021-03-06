# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Tong Du
date: 2020/1/4 19:51
contact: dtshare@126.com
desc: 义乌小商品指数
http://www.ywindex.com/Home/Product/index/
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup


def index_yw(symbol="月景气指数"):
    """
    获取义乌小商品指数
    http://www.ywindex.com/Home/Product/index/
    :param symbol: 指数指标:["周价格指数", "月价格指数", "月景气指数"]
    :type symbol: str
    :return: 指数结果
    :rtype: pandas.DataFrame
    """
    name_num_dict = {
        "周价格指数": 1,
        "月价格指数": 3,
        "月景气指数": 5,
    }
    url = "http://www.ywindex.com/Home/Product/index/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    table_name = (
        soup.find_all(attrs={"class": "tablex"})[name_num_dict[symbol]]
        .get_text()
        .split("\n\n\n\n\n")[2]
        .split("\n")
    )
    table_content = (
        soup.find_all(attrs={"class": "tablex"})[name_num_dict[symbol]]
        .get_text()
        .split("\n\n\n\n\n")[3]
        .split("\n\n")
    )
    if symbol == "月景气指数":
        table_df = pd.DataFrame([item.split("\n") for item in table_content]).iloc[
            :, :5
        ]
        table_df.columns = table_name
        return table_df
    table_df = pd.DataFrame([item.split("\n") for item in table_content]).iloc[:, :6]
    table_df.columns = table_name
    return table_df


if __name__ == "__main__":
    index_yw_df = index_yw(symbol="月景气指数")
    print(index_yw_df)
