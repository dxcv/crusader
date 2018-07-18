# encoding: utf-8
import pandas as pd

import estate.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 全国商品房销售面积、全国商品房销售额
source_sell = ColumnDataSource(data=dict(date=[], area=[], sell=[]))
def update_sell():
    df = pd.read_excel(u'%s/全国商品房销售面积.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/全国商品房销售额.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_sell.data = {'date': df.index,
                        'area': df[dic[u'全国商品房销售面积']] / 100,
                        'sell': df[dic[u'全国商品房销售额']] / 100}

# 一线城市商品房销售面积
source_city1 = ColumnDataSource(data=dict(date=[], bj=[], sh=[], sz=[], gz=[]))
def update_city1():
    df = pd.read_excel(u'%s/北京商品房销售面积.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/上海商品房销售面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/深圳商品房销售面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/广州商品房销售面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_city1.data = {'date': df.index,
                         'bj': df[dic[u'北京商品房销售面积']] / 100,
                         'sh': df[dic[u'上海商品房销售面积']] / 100,
                         'sz': df[dic[u'深圳商品房销售面积']] / 100,
                         'gz': df[dic[u'广州商品房销售面积']] / 100}

# 二线城市商品房销售面积
source_city2 = ColumnDataSource(data=dict(date=[], tj=[], nj=[], sz=[], cd=[], wh=[]))
def update_city2():
    df = pd.read_excel(u'%s/天津商品房销售面积.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/南京商品房销售面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/苏州商品房销售面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/成都商品房销售面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/武汉商品房销售面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_city2.data = {'date': df.index,
                         'tj': df[dic[u'天津商品房销售面积']] / 100,
                         'nj': df[dic[u'南京商品房销售面积']] / 100,
                         'sz': df[dic[u'苏州商品房销售面积']] / 100,
                         'cd': df[dic[u'成都商品房销售面积']] / 100,
                         'wh': df[dic[u'武汉商品房销售面积']] / 100}

# 全国七十个大中城市房屋销售价格指数
source_index = ColumnDataSource(data=dict(date=[], index=[]))
def update_index():
    df = pd.read_excel(u'%s/全国七十个大中城市房屋销售价格指数.xlsx'%(const.DATA_DIR))
    source_index.data = {'date': df.index, 'index': df[dic[u'全国七十个大中城市房屋销售价格指数']] / 10}

# 全国商品房销售均价
source_price = ColumnDataSource(data=dict(date=[], p=[]))
def update_price():
    df = pd.read_excel(u'%s/全国商品房销售均价.xlsx'%(const.DATA_DIR))
    source_price.data = {'date': df.index, 'p': df[dic[u'全国商品房销售均价']]}

# 房地产新开工、施工、竣工面积
source_house = ColumnDataSource(data=dict(date=[], new=[], done=[], build=[]))
def update_house():
    df = pd.read_excel(u'%s/房地产新开工面积.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/房地产施工面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/房地产竣工面积.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_house.data = {'date': df.index,
                         'new': df[dic[u'房地产新开工面积']] / 100,
                         'build': df[dic[u'房地产施工面积']] / 100,
                         'done': df[dic[u'房地产竣工面积']] / 100}

# 房地产投资总额、房地产开发投资资金来源
source_invest = ColumnDataSource(data=dict(date=[], inv=[], src=[]))
def update_invest():
    df = pd.read_excel(u'%s/房地产投资总额.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/房地产开发投资资金来源.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_invest.data = {'date': df.index,
                          'inv': df[dic[u'房地产投资总额']] / 100,
                          'src': df[dic[u'房地产开发投资资金来源']] / 100}

# 土地购置费
source_land = ColumnDataSource(data=dict(date=[], land=[]))
def update_land():
    df = pd.read_excel(u'%s/土地购置费.xlsx'%(const.DATA_DIR))
    source_land.data = {'date': df.index, 'land': df[dic[u'土地购置费']] / 100}

# M1、M2
source_money = ColumnDataSource(data=dict(date=[], m1=[], m2=[]))
def update_money():
    df = pd.read_excel(u'%s/M1.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/M2.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_money.data = {'date': df.index,
                         'm1': df[dic['M1']] / 100,
                         'm2': df[dic['M2']] / 100}

# 水泥产量
source_prod = ColumnDataSource(data=dict(date=[], cement=[], glass=[], air=[], ice=[]))
def update_prod():
    df = pd.read_excel(u'%s/水泥产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/平板玻璃产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/冰箱产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/空调产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_prod.data = {'date': df.index,
                        'cement': df[dic[u'水泥产量']] / 100,
                        'glass': df[dic[u'平板玻璃产量']] / 100,
                        'air': df[dic[u'冰箱产量']] / 100,
                        'ice': df[dic[u'空调产量']] / 100}

def update_all():
    update_sell()
    update_city1()
    update_city2()
    update_index()
    update_price()
    update_house()
    update_invest()
    update_land()
    update_money()
    update_prod()

def get_plot(title, pct=False):
    tools = "pan,wheel_zoom,box_select,reset"
    plot = figure(plot_height=500, plot_width=1200, tools=tools, x_axis_type='datetime')
    plot.title.text_font_size = "15pt"
    plot.title.text_font = "Microsoft YaHei"
    plot.yaxis.minor_tick_line_color = None
    plot.title.text = title
    if pct:
        plot.yaxis.formatter = NumeralTickFormatter(format='0.00%')
    else:
        plot.yaxis.formatter = NumeralTickFormatter(format='0.00')
    return plot

plot_sell = get_plot(u'全国商品房销售面积、销售额同比（月）', pct=True)
plot_sell.line('date', 'area', source=source_sell, line_width=2, legend=u'全国商品房销售面积')
plot_sell.line('date', 'sell', source=source_sell, line_width=2, color='green', legend=u'全国商品房销售额')

plot_city1 = get_plot(u'一线城市商品房销售面积同比（月）', pct=True)
plot_city1.line('date', 'bj', source=source_city1, line_width=2, legend=u'北京商品房销售面积')
plot_city1.line('date', 'sh', source=source_city1, line_width=2, color='green', legend=u'上海商品房销售面积')
plot_city1.line('date', 'sz', source=source_city1, line_width=2, color='red', legend=u'深圳商品房销售面积')
plot_city1.line('date', 'gz', source=source_city1, line_width=2, color='gray', legend=u'广州商品房销售面积')

plot_city2 = get_plot(u'二线城市商品房销售面积同比（月）', pct=True)
plot_city2.line('date', 'tj', source=source_city2, line_width=2, legend=u'天津商品房销售面积')
plot_city2.line('date', 'nj', source=source_city2, line_width=2, color='green', legend=u'南京商品房销售面积')
plot_city2.line('date', 'sz', source=source_city2, line_width=2, color='red', legend=u'苏州商品房销售面积')
plot_city2.line('date', 'cd', source=source_city2, line_width=2, color='gray', legend=u'成都商品房销售面积')
plot_city2.line('date', 'wh', source=source_city2, line_width=2, color='yellow', legend=u'武汉商品房销售面积')

plot_index = get_plot(u'全国七十个大中城市房屋销售价格指数同比：当月同比（月）', pct=True)
plot_index.line('date', 'index', source=source_index, line_width=2, legend=u'全国七十个大中城市房屋销售价格指数：当月同比')

plot_price = get_plot(u'全国商品房销售均价（月）')
plot_price.line('date', 'p', source=source_price, line_width=2, legend=u'全国商品房销售均价')

plot_house = get_plot(u'房地产新开工、施工、竣工面积同比（月）', pct=True)
plot_house.line('date', 'new', source=source_house, line_width=2, legend=u'房地产新开工面积')
plot_house.line('date', 'build', source=source_house, line_width=2, color='green', legend=u'房地产施工面积')
plot_house.line('date', 'done', source=source_house, line_width=2, color='red', legend=u'房地产竣工面积')

plot_invest = get_plot(u'房地产投资总额、房地产开发投资资金来源同比（月）', pct=True)
plot_invest.line('date', 'inv', source=source_invest, line_width=2, legend=u'房地产投资总额')
plot_invest.line('date', 'src', source=source_invest, line_width=2, color='green', legend=u'房地产开发投资资金来源')

plot_land = get_plot(u'土地购置费同比（月）', pct=True)
plot_land.line('date', 'land', source=source_land, line_width=2, legend=u'土地购置费')

plot_money = get_plot(u'M1、M2（月）', pct=True)
plot_money.line('date', 'm1', source=source_money, line_width=2, legend='M1')
plot_money.line('date', 'm2', source=source_money, line_width=2, color='green', legend=u'M2')

plot_prod = get_plot(u'水泥、平板玻璃、冰箱、空调产量同比（月）', pct=True)
plot_prod.line('date', 'cement', source=source_prod, line_width=2, legend=u'水泥产量')
plot_prod.line('date', 'glass', source=source_prod, line_width=2, color='green', legend=u'平板玻璃产量')
plot_prod.line('date', 'air', source=source_prod, line_width=2, color='red', legend=u'冰箱产量')
plot_prod.line('date', 'ice', source=source_prod, line_width=2, color='gray', legend=u'空调产量')

update_all()

curdoc().add_root(column(plot_sell, plot_city1, plot_city2, plot_index, plot_price, plot_house, plot_invest,
                         plot_land, plot_money, plot_prod))
curdoc().title = u'房地产中观数据库'
