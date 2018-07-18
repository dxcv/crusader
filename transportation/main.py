# encoding: utf-8
import pandas as pd

import transportation.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 沿海主要港口集装箱吞吐量
source_thruput = ColumnDataSource(data=dict(date=[], tot=[], dl=[], tj=[], qd=[], nb=[], sh=[], sz=[]))
def update_thruput():
    print('update thruput')
    df = pd.read_excel(u'%s/沿海主要港口集装箱吞吐量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/大连港口集装箱吞吐量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/天津港口集装箱吞吐量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/青岛港口集装箱吞吐量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/上海港口集装箱吞吐量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/宁波舟山港口集装箱吞吐量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/深圳港口集装箱吞吐量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_thruput.data = {'date': df.index,
                           'tot': df[dic[u'沿海主要港口集装箱吞吐量']] / 100,
                           'dl': df[dic[u'大连港口集装箱吞吐量']] / 100,
                           'tj': df[dic[u'天津港口集装箱吞吐量']] / 100,
                           'qd': df[dic[u'青岛港口集装箱吞吐量']] / 100,
                           'sh': df[dic[u'上海港口集装箱吞吐量']] / 100,
                           'nb': df[dic[u'宁波舟山港口集装箱吞吐量']] / 100,
                           'sz': df[dic[u'深圳港口集装箱吞吐量']] / 100}

# 民航旅客周转量
source_pas = ColumnDataSource(data=dict(date=[], turn=[]))
def update_pas():
    print('update pas')
    df = pd.read_excel(u'%s/民航旅客周转量.xlsx'%(const.DATA_DIR))
    source_pas.data = {'date': df.index, 'turn': df[dic[u'民航旅客周转量']] / 100}

# 民航客座率
source_seat = ColumnDataSource(data=dict(date=[], seat=[]))
def update_seat():
    print('update seat')
    df = pd.read_excel(u'%s/民航客座率.xlsx'%(const.DATA_DIR))
    source_seat.data = {'date': df.index, 'seat': df[dic[u'民航客座率']] / 100}

# 主要港口铁矿石库存
source_iron = ColumnDataSource(data=dict(date=[], inv=[]))
def update_iron():
    print('update iron')
    df = pd.read_excel(u'%s/主要港口铁矿石库存.xlsx'%(const.DATA_DIR))
    source_iron.data = {'date': df.index, 'inv': df[dic[u'主要港口铁矿石库存']]}

# 公路货运量
source_road = ColumnDataSource(data=dict(date=[], load=[]))
def update_road():
    print('update road')
    df = pd.read_excel(u'%s/公路货运量.xlsx'%(const.DATA_DIR))
    source_road.data = {'date': df.index, 'load': df[dic[u'公路货运量']] / 100}

# 出口同比增长
source_out = ColumnDataSource(data=dict(date=[], out=[]))
def update_out():
    print('update out')
    df = pd.read_excel(u'%s/出口同比增长.xlsx'%(const.DATA_DIR))
    source_out.data = {'date': df.index, 'out': df[dic[u'出口同比增长']] / 100}

# 工业增加值同比增长
source_ind = ColumnDataSource(data=dict(date=[], ind=[]))
def update_ind():
    print('update ind')
    df = pd.read_excel(u'%s/工业增加值同比增长.xlsx'%(const.DATA_DIR))
    source_ind.data = {'date': df.index, 'ind': df[dic[u'工业增加值同比增长']] / 100}

# 生铁产量
source_iron2 = ColumnDataSource(data=dict(date=[], prod=[]))
def update_iron2():
    print('update iron2')
    df = pd.read_excel(u'%s/生铁产量.xlsx'%(const.DATA_DIR))
    source_iron2.data = {'date': df.index, 'prod': df[dic[u'生铁产量']] / 100}

# 上海出口集装箱运价指数
source_con = ColumnDataSource(data=dict(date=[], index=[]))
def update_con():
    print('update con')
    df = pd.read_excel(u'%s/上海出口集装箱运价指数.xlsx'%(const.DATA_DIR))
    source_con.data = {'date': df.index, 'index':df[dic[u'上海出口集装箱运价指数']]}

# BDI
source_bdi = ColumnDataSource(data=dict(date=[], bdi=[]))
def update_bdi():
    df = pd.read_excel(u'%s/BDI.xlsx'%(const.DATA_DIR))
    source_bdi.data = {'date': df.index, 'bdi': df[dic['BDI']]}

# 国内航线综合票价指数
source_ticket = ColumnDataSource(data=dict(date=[], t=[]))
def update_ticket():
    df = pd.read_excel(u'%s/国内航线综合票价指数.xlsx'%(const.DATA_DIR))
    source_ticket.data = {'date': df.index, 't': df[dic[u'国内航线综合票价指数']]}

# 中国出口集装箱运价指数（CCFI）
source_ccfi = ColumnDataSource(data=dict(date=[], index=[]))
def update_ccfi():
    df = pd.read_excel(u'%s/中国出口集装箱运价指数（CCFI）.xlsx'%(const.DATA_DIR))
    source_ccfi.data = {'date': df.index, 'index': df[dic[u'中国出口集装箱运价指数（CCFI）']]}

def update_all():
    update_thruput()
    update_pas()
    update_iron()
    update_out()
    update_ind()
    update_seat()
    update_road()
    update_iron2()
    update_con()
    update_bdi()
    update_ticket()
    update_ccfi()

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

plot_thruput = get_plot(u'沿海主要港口集装箱吞吐量同比（月）', pct=True)
plot_thruput.line('date', 'tot', source=source_thruput, line_width=2.5, color='red', legend=u'沿海主要港口集装箱吞吐量')
plot_thruput.line('date', 'dl', source=source_thruput, line_width=2, legend=u'大连港口集装箱吞吐量')
plot_thruput.line('date', 'tj', source=source_thruput, line_width=2, color='green', legend=u'天津港口集装箱吞吐量')
plot_thruput.line('date', 'qd', source=source_thruput, line_width=2, color='blue', legend=u'青岛港口集装箱吞吐量')
plot_thruput.line('date', 'sh', source=source_thruput, line_width=2, color='yellow', legend=u'上海港口集装箱吞吐量')
plot_thruput.line('date', 'nb', source=source_thruput, line_width=2, color='orange', legend=u'宁波舟山港口集装箱吞吐量')
plot_thruput.line('date', 'sz', source=source_thruput, line_width=2, color='gray', legend=u'深圳港口集装箱吞吐量')

plot_pas = get_plot(u'民航旅客周转量同比（月）', pct=True)
plot_pas.line('date', 'turn', source=source_pas, line_width=2, legend=u'民航旅客周转量')

plot_iron = get_plot(u'主要港口铁矿石库存（周）')
plot_iron.line('date', 'inv', source=source_iron, line_width=2, legend=u'主要港口铁矿石库存')

plot_out = get_plot(u'出口同比增长（月）', pct=True)
plot_out.line('date', 'out', source=source_out, line_width=2, legend=u'出口同比增长')

plot_ind = get_plot(u'工业增加值同比增长（月）', pct=True)
plot_ind.line('date', 'ind', source=source_ind, line_width=2, legend=u'工业增加值同比增长')

plot_iron2 = get_plot(u'生铁产量（月）', pct=True)
plot_iron2.line('date', 'prod', source=source_iron2, line_width=2, legend=u'生铁产量')

plot_seat = get_plot(u'民航客座率同比（月）', pct=True)
plot_seat.line('date', 'seat', source=source_seat, line_width=2, legend=u'民航客座率')

plot_road = get_plot(u'公路货运量同比（月）', pct=True)
plot_road.line('date', 'load', source=source_road, line_width=2, legend=u'公路货运量')

plot_con = get_plot(u'上海出口集装箱运价指数（周）')
plot_con.line('date', 'index', source=source_con, line_width=2, legend=u'上海出口集装箱运价指数')

plot_bdi = get_plot(u'波罗的海干散货指数（BDI）（日）')
plot_bdi.line('date', 'bdi', source=source_bdi, line_width=2, legend=u'BDI')

plot_ticket = get_plot(u'国内航线综合票价指数（月）')
plot_ticket.line('date', 't', source=source_ticket, line_width=2, legend=u'国内航线综合票价指数')

plot_ccfi = get_plot(u'中国出口集装箱运价指数（CCFI）（周）')
plot_ccfi.line('date', 'index', source=source_ccfi, line_width=2, legend=u'中国出口集装箱运价指数（CCFI）')

update_all()

curdoc().add_root(column(plot_thruput, plot_pas, plot_seat, plot_iron, plot_out, plot_ind, plot_iron2, plot_road,
                         plot_con, plot_bdi, plot_ticket, plot_ccfi))
curdoc().title = u'交通运输中观数据库'
