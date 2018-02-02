# encoding: utf-8
import pandas as pd

import cars.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 乘用车销量、乘用车产量
source_cars = ColumnDataSource(data=dict(date=[], sell=[], prod=[]))
def update_cars():
    print('update cars')
    df = pd.read_excel(u'%s/乘用车销量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/乘用车产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_cars.data = {'date': df.index,
                        'sell': df[dic[u'乘用车销量']] / 100,
                        'prod': df[dic[u'乘用车产量']] / 100}

# 轿车销量、产量、出口
source_auto = ColumnDataSource(data=dict(date=[], sell=[], prod=[], out=[]))
def update_auto():
    print('update auto')
    df = pd.read_excel(u'%s/轿车销量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/轿车产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/轿车出口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_auto.data = {'date': df.index,
                        'sell': df[dic[u'轿车销量']] / 100,
                        'prod': df[dic[u'轿车产量']] / 100,
                        'out': df[dic[u'轿车出口量']] / 100}

# 载货车产量
source_van = ColumnDataSource(data=dict(date=[], prod=[]))
def update_van():
    print('update van')
    df = pd.read_excel(u'%s/载货车产量.xlsx'%(const.DATA_DIR))
    source_van.data = {'date': df.index, 'prod': df[dic[u'载货车产量']].pct_change()}

# M1、M2
source_money = ColumnDataSource(data=dict(date=[], m1=[], m2=[]))
def update_money():
    print('update money')
    df = pd.read_excel(u'%s/M1.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/M2.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_money.data = {'date': df.index,
                         'm1': df[dic['M1']] / 100,
                         'm2': df[dic['M2']] / 100}

# 城镇固定资产投资增速、房地产新开工施工面积增速
source_invest = ColumnDataSource(data=dict(date=[], city=[], house=[]))
def update_invest():
    print('update invest')
    df = pd.read_excel(u'%s/城镇固定资产投资增速.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/房地产新开工施工面积增速.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_invest.data = {'date': df.index,
                          'city': df[dic[u'城镇固定资产投资增速']] / 100,
                          'house': df[dic[u'房地产新开工施工面积增速']] / 100}

# 原煤产量、煤进口量
source_coal = ColumnDataSource(data=dict(date=[], prod=[], inp=[]))
def update_coal():
    print('update coal')
    df = pd.read_excel(u'%s/原煤产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/煤进口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_coal.data = {'date': df.index,
                        'prod': df[dic[u'原煤产量']] / 100,
                        'inp': df[dic[u'煤进口量']] / 100}

# 铁矿石原矿量产量、铁矿砂及其精矿进口量
source_iron = ColumnDataSource(data=dict(date=[], prod=[], inp=[]))
def update_iron():
    print('update iron')
    df = pd.read_excel(u'%s/铁矿石原矿量产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/铁矿砂及其精矿进口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_iron.data = {'date': df.index,
                        'prod': df[dic[u'铁矿石原矿量产量']] / 100,
                        'inp': df[dic[u'铁矿砂及其精矿进口量']].pct_change(12)}

# 铜材产量、铜材进口量
source_copper = ColumnDataSource(data=dict(date=[], prod=[], inp=[]))
def update_copper():
    print('update copper')
    df = pd.read_excel(u'%s/铜材产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/铜材进口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_copper.data = {'date': df.index,
                          'prod': df[dic[u'铜材产量']].pct_change(12),
                          'inp': df[dic[u'铜材进口量']] / 100}

# 粗钢产量、钢材出口量
source_steel = ColumnDataSource(data=dict(date=[], prod=[], out=[]))
def update_steel():
    print('update steel')
    df = pd.read_excel(u'%s/粗钢产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/钢材出口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_steel.data = {'date': df.index,
                         'prod': df[dic[u'粗钢产量']] / 100,
                         'out': df[dic[u'钢材出口量']] / 100}

# 丁苯橡胶价格
source_rubber = ColumnDataSource(data=dict(date=[], p=[]))
def update_rubber():
    print('update rubber')
    df = pd.read_excel(u'%s/丁苯橡胶价格.xlsx'%(const.DATA_DIR))
    source_rubber.data = {'date': df.index, 'p': df[dic[u'丁苯橡胶价格']]}

# 平板玻璃价格指数
source_glass = ColumnDataSource(data=dict(date=[], p=[]))
def update_glass():
    print('update glass')
    df = pd.read_excel(u'%s/平板玻璃价格指数.xlsx'%(const.DATA_DIR))
    source_glass.data = {'date': df.index, 'p': df[dic[u'平板玻璃价格指数']]}

# 公路货运量、公路货运周转量
source_road = ColumnDataSource(data=dict(date=[], vol=[], turn=[]))
def update_road():
    print('update road')
    df = pd.read_excel(u'%s/公路货运量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/公路货运周转量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_road.data = {'date': df.index,
                        'vol': df[dic[u'公路货运量']] / 100,
                        'turn': df[dic[u'公路货运周转量']] / 100}

# BDI
source_bdi = ColumnDataSource(data=dict(date=[], bdi=[]))
def update_bdi():
    print('update bdi')
    df = pd.read_excel(u'%s/BDI.xlsx'%(const.DATA_DIR))
    source_bdi.data = {'date': df.index, 'bdi': df[dic['BDI']]}

def update_all():
    update_cars()
    update_auto()
    update_van()
    update_money()
    update_invest()
    update_coal()
    update_iron()
    update_copper()
    update_steel()
    update_rubber()
    update_glass()
    update_road()
    update_bdi()

def get_plot(title, pct=False):
    tools = "pan,wheel_zoom,box_select,reset"
    plot = figure(plot_height=400, plot_width=1000, tools=tools, x_axis_type='datetime')
    plot.title.text_font_size = "15pt"
    plot.title.text_font = "Microsoft YaHei"
    plot.yaxis.minor_tick_line_color = None
    plot.title.text = title
    if pct:
        plot.yaxis.formatter = NumeralTickFormatter(format='0.00%')
    else:
        plot.yaxis.formatter = NumeralTickFormatter(format='0.00')
    return plot

plot_cars = get_plot(u'乘用车销量、产量同比', pct=True)
plot_cars.line('date', 'sell', source=source_cars, line_width=2, legend=u'乘用车销量同比')
plot_cars.line('date', 'prod', source=source_cars, line_width=2, color='green', legend=u'乘用车产量同比')

plot_auto = get_plot(u'轿车销量、产量同比', pct=True)
plot_auto.line('date', 'sell', source=source_auto, line_width=2, legend=u'轿车销量同比')
plot_auto.line('date', 'prod', source=source_auto, line_width=2, color='green', legend=u'轿车产量同比')
plot_auto.line('date', 'out', source=source_auto, line_width=2, color='red', legend=u'轿车出口量同比')

plot_van = get_plot(u'载货车产量同比', pct=True)
plot_van.line('date', 'prod', source=source_van, line_width=2, legend=u'载货车产量')

plot_money = get_plot(u'M1、M2', pct=True)
plot_money.line('date', 'm1', source=source_money, line_width=2, legend='M1')
plot_money.line('date', 'm2', source=source_money, line_width=2, color='green', legend=u'M2')

plot_invest = get_plot(u'固定资产投资、房地产新开工面积', pct=True)
plot_invest.line('date', 'city', source=source_invest, line_width=2, legend=u'固定资产投资增速')
plot_invest.line('date', 'house', source=source_invest, line_width=2, color='green', legend=u'房地产新开工面积增速')

plot_coal = get_plot(u'原煤产量、煤进口量同比', pct=True)
plot_coal.line('date', 'prod', source=source_coal, line_width=2, legend=u'原煤产量同比')
plot_coal.line('date', 'inp', source=source_coal, line_width=2, color='green', legend=u'煤进口量同比')

plot_iron = get_plot(u'铁矿石原矿量产量、铁矿砂及其精矿进口量同比', pct=True)
plot_iron.line('date', 'prod', source=source_iron, line_width=2, legend=u'铁矿石原矿量产量同比')
plot_iron.line('date', 'inp', source=source_iron, line_width=2, color='green', legend=u'铁矿砂及其精矿进口量同比')

plot_copper = get_plot(u'铜材产量、铜材进口量同比', pct=True)
plot_copper.line('date', 'prod', source=source_copper, line_width=2, legend=u'铜材产量同比')
plot_copper.line('date', 'inp', source=source_copper, line_width=2, color='green', legend=u'铜材进口量同比')

plot_steel = get_plot(u'粗钢产量、钢材出口量同比', pct=True)
plot_steel.line('date', 'prod', source=source_steel, line_width=2, legend=u'粗钢产量同比')
plot_steel.line('date', 'out', source=source_steel, line_width=2, color='green', legend=u'钢材出口量同比')

plot_rubber = get_plot(u'丁苯橡胶价格')
plot_rubber.line('date', 'p', source=source_rubber, line_width=2, legend=u'丁苯橡胶价格')

plot_glass = get_plot(u'平板玻璃价格指数')
plot_glass.line('date', 'p', source=source_glass, line_width=2, legend=u'平板玻璃价格指数')

plot_road = get_plot(u'公路货运量、公路货运周转量同比', pct=True)
plot_road.line('date', 'vol', source=source_road, line_width=2, legend=u'公路货运量同比')
plot_road.line('date', 'turn', source=source_road, line_width=2, color='green', legend=u'公路货运周转量同比')

plot_bdi = get_plot(u'波罗的海干散货指数（BDI）')
plot_bdi.line('date', 'bdi', source=source_bdi, line_width=2, legend=u'BDI')

update_all()

curdoc().add_root(column(plot_cars, plot_auto, plot_van, plot_money, plot_invest, plot_coal, plot_iron,
                         plot_copper, plot_steel, plot_rubber, plot_glass, plot_road, plot_bdi))
curdoc().title = u'乘用车中观数据库'
