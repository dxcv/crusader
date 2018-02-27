# encoding: utf-8
import pandas as pd
import numpy as np

import chemical.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 乙烯、聚乙烯产量
source_eth = ColumnDataSource(data=dict(date=[], eth=[], pol=[]))
def update_eth():
    df = pd.read_excel(u'%s/乙烯产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/聚乙烯产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_eth.data = {'date': df.index,
                       'eth': df[dic[u'乙烯产量']] / 100,
                       'pol': df[dic[u'聚乙烯产量']] / 100}

# 纯碱产量
source_soda = ColumnDataSource(data=dict(date=[], prod=[]))
def update_soda():
    df = pd.read_excel(u'%s/纯碱产量.xlsx'%(const.DATA_DIR))
    source_soda.data = {'date': df.index, 'prod': df[dic[u'纯碱产量']] / 100}

# 尿素产量、出口量
source_car = ColumnDataSource(data=dict(date=[], prod=[], out=[]))
def update_car():
    df = pd.read_excel(u'%s/尿素产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/尿素出口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df[df <= 200]
    df = df.fillna(method='ffill')
    source_car.data = {'date': df.index,
                       'prod': df[dic[u'尿素产量']] / 100,
                       'out':df[dic[u'尿素出口量']] / 100}

# 钾肥产量、出口量
source_pot = ColumnDataSource(data=dict(date=[], prod=[], out=[]))
def update_pot():
    df = pd.read_excel(u'%s/钾肥产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/钾肥出口量.xlsx'%(const.DATA_DIR))
    tdf = tdf.pct_change(12) * 100
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df[df <= 200]
    df = df.fillna(method='ffill')
    source_pot.data = {'date': df.index,
                       'prod': df[dic[u'钾肥产量']] / 100,
                       'out': df[dic[u'钾肥出口量']] / 100}

# 涤纶产量
source_ter = ColumnDataSource(data=dict(date=[], prod=[]))
def update_ter():
    df = pd.read_excel(u'%s/涤纶产量.xlsx'%(const.DATA_DIR))
    source_ter.data = {'date': df.index, 'prod': df[dic[u'涤纶产量']] / 100}

# 东南亚乙烯、LDPE价格
source_ep = ColumnDataSource(data=dict(date=[], p=[], ldpe=[]))
def update_ep():
    df = pd.read_excel(u'%s/东南亚乙烯价格.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/东南亚LDPE价格.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    df = df[df.diff() != 0].dropna()
    source_ep.data = {'date': df.index,
                      'p': df[dic[u'东南亚乙烯价格']],
                      'ldpe': df[dic[u'东南亚LDPE价格']]}

# 轻质纯碱价格
source_lsoda = ColumnDataSource(data=dict(date=[], p=[]))
def update_lsoda():
    df = pd.read_excel(u'%s/轻质纯碱价格.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_lsoda.data = {'date': df.index, 'p': df[dic[u'轻质纯碱价格']]}

# 国内尿素出厂价
source_dcar = ColumnDataSource(data=dict(date=[], p=[]))
def update_dcar():
    df = pd.read_excel(u'%s/国内尿素出厂价.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_dcar.data = {'date': df.index, 'p': df[dic[u'国内尿素出厂价']]}

# 盐湖钾肥出厂价
source_potp = ColumnDataSource(data=dict(date=[], p=[]))
def update_potp():
    df = pd.read_excel(u'%s/盐湖钾肥出厂价.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_potp.data = {'date': df.index, 'p': df[dic[u'盐湖钾肥出厂价']]}

# 氯化钾温哥华FOB
source_chpot = ColumnDataSource(data=dict(date=[], p=[]))
def update_chpot():
    df = pd.read_excel(u'%s/氯化钾温哥华FOB.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_chpot.data = {'date': df.index, 'p': df[dic[u'氯化钾温哥华FOB']]}

# 涤纶短纤价格
source_ster = ColumnDataSource(data=dict(date=[], p=[]))
def update_ster():
    df = pd.read_excel(u'%s/涤纶短纤价格.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_ster.data = {'date': df.index, 'p': df[dic[u'涤纶短纤价格']]}

# 新加坡石脑油价格
source_nap = ColumnDataSource(data=dict(date=[], p=[]))
def update_nap():
    df = pd.read_excel(u'%s/新加坡石脑油价格.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_nap.data = {'date': df.index, 'p': df[dic[u'新加坡石脑油价格']]}

# PTA价格
source_pta = ColumnDataSource(data=dict(date=[], p=[]))
def update_pta():
    df = pd.read_excel(u'%s/PTA价格.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_pta.data = {'date': df.index, 'p': df[dic[u'PTA价格']]}

# MEG价格
source_meg = ColumnDataSource(data=dict(date=[], p=[]))
def update_meg():
    df = pd.read_excel(u'%s/MEG价格.xlsx'%(const.DATA_DIR))
    df = df[df.diff() != 0].dropna()
    source_meg.data = {'date': df.index, 'p': df[dic[u'MEG价格']]}

# OECD工业生产指数
source_oecd = ColumnDataSource(data=dict(date=[], index=[]))
def update_oecd():
    df = pd.read_excel(u'%s/OECD工业生产指数.xlsx'%(const.DATA_DIR))
    source_oecd.data = {'date': df.index, 'index': df[dic[u'OECD工业生产指数']]}

# 平板玻璃产量
source_glass = ColumnDataSource(data=dict(date=[], prod=[]))
def update_glass():
    df = pd.read_excel(u'%s/平板玻璃产量.xlsx'%(const.DATA_DIR))
    source_glass.data = {'date': df.index, 'prod': df[dic[u'平板玻璃产量']] / 100}

# 汽车产量
source_auto = ColumnDataSource(data=dict(date=[], prod=[]))
def update_auto():
    df = pd.read_excel(u'%s/汽车产量.xlsx'%(const.DATA_DIR))
    source_auto.data = {'date': df.index, 'prod': df[dic[u'汽车产量']] / 100}

# 房地产新开工面积、房地产投资开发增速
source_est = ColumnDataSource(data=dict(date=[], new=[], inc=[]))
def update_est():
    df = pd.read_excel(u'%s/房地产新开工面积.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/房地产投资开发增速.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_est.data = {'date': df.index,
                       'new': df[dic[u'房地产新开工面积']] / 100,
                       'inc': df[dic[u'房地产投资开发增速']] / 100}

# 国际玉米期货价格
source_corn = ColumnDataSource(data=dict(date=[], p=[]))
def update_corn():
    df = pd.read_excel(u'%s/国际玉米期货价格.xlsx'%(const.DATA_DIR))
    source_corn.data = {'date': df.index, 'p': df[dic[u'国际玉米期货价格']]}

# 纺织品出口量
source_spin = ColumnDataSource(data=dict(date=[], out=[]))
def update_spin():
    df = pd.read_excel(u'%s/纺织品出口量.xlsx'%(const.DATA_DIR))
    source_spin.data = {'date': df.index, 'out': df[dic[u'纺织品出口量']] / 100}

# 秦皇岛港6000大卡大同优混平仓价
source_coal = ColumnDataSource(data=dict(date=[], p=[]))
def update_coal():
    df = pd.read_excel(u'%s/秦皇岛港6000大卡大同优混平仓价.xlsx'%(const.DATA_DIR))
    source_coal.data = {'date': df.index, 'p': df[dic[u'秦皇岛港6000大卡大同优混平仓价']]}

def update_all():
    update_eth()
    update_soda()
    update_car()
    update_pot()
    update_ter()
    update_ep()
    update_lsoda()
    update_dcar()
    update_potp()
    update_chpot()
    update_ster()
    update_nap()
    update_pta()
    update_meg()
    update_oecd()
    update_glass()
    update_auto()
    update_est()
    update_corn()
    update_spin()
    update_coal()

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

plot_eth = get_plot(u'乙烯、聚乙烯产量同比', pct=True)
plot_eth.line('date', 'eth', source=source_eth, line_width=2, legend=u'乙烯产量')
plot_eth.line('date', 'pol', source=source_eth, line_width=2, color='green', legend=u'聚乙烯产量')

plot_soda = get_plot(u'纯碱产量', pct=True)
plot_soda.line('date', 'prod', source=source_soda, line_width=2, legend=u'纯碱产量')

plot_car = get_plot(u'尿素产量、出口量同比', pct=True)
plot_car.line('date', 'prod', source=source_car, line_width=2, legend=u'尿素产量')
plot_car.line('date', 'out', source=source_car, line_width=2, color='green', legend=u'尿素出口量')

plot_pot = get_plot(u'钾肥产量、出口量同比', pct=True)
plot_pot.line('date', 'prod', source=source_pot, line_width=2, legend=u'钾肥产量')
plot_pot.line('date', 'out', source=source_pot, line_width=2, color='green', legend=u'钾肥出口量')

plot_ter = get_plot(u'涤纶产量', pct=True)
plot_ter.line('date', 'prod', source=source_ter, line_width=2, legend=u'涤纶产量')

plot_ep = get_plot(u'东南亚乙烯、LDPE价格')
plot_ep.line('date', 'p', source=source_ep, line_width=2, legend=u'东南亚乙烯价格')
plot_ep.line('date', 'ldpe', source=source_ep, line_width=2, color='green', legend=u'东南亚LDPE价格')

plot_lsoda = get_plot(u'轻质纯碱价格')
plot_lsoda.line('date', 'p', source=source_lsoda, line_width=2, legend=u'轻质纯碱价格')

plot_dcar = get_plot(u'国内尿素出厂价')
plot_dcar.line('date', 'p', source=source_dcar, line_width=2, legend=u'国内尿素出厂价')

plot_potp = get_plot(u'盐湖钾肥出厂价')
plot_potp.line('date', 'p', source=source_potp, line_width=2, legend=u'盐湖钾肥出厂价')

plot_chpot = get_plot(u'氯化钾温哥华FOB')
plot_chpot.line('date', 'p', source=source_chpot, line_width=2, legend=u'氯化钾温哥华FOB')

plot_ster = get_plot(u'涤纶短纤价格')
plot_ster.line('date', 'p', source=source_ster, line_width=2, legend=u'涤纶短纤价格')

plot_nap = get_plot(u'新加坡石脑油价格')
plot_nap.line('date', 'p', source=source_nap, line_width=2, legend=u'新加坡石脑油价格')

plot_pta = get_plot(u'PTA价格')
plot_pta.line('date', 'p', source=source_pta, line_width=2, legend=u'PTA价格')

plot_meg = get_plot(u'MEG价格')
plot_meg.line('date', 'p', source=source_meg, line_width=2, legend=u'MEG价格')

plot_oecd = get_plot(u'OECD工业生产指数')
plot_oecd.line('date', 'index', source=source_oecd, line_width=2, legend=u'OECD工业生产指数')

plot_glass = get_plot(u'平板玻璃产量同比', pct=True)
plot_glass.line('date', 'prod', source=source_glass, line_width=2, legend=u'平板玻璃产量')

plot_auto = get_plot(u'汽车产量同比', pct=True)
plot_auto.line('date', 'prod', source=source_auto, line_width=2, legend=u'汽车产量')

plot_est = get_plot(u'房地产新开工面积、房地产投资开发增速同比', pct=True)
plot_est.line('date', 'new', source=source_est, line_width=2, legend=u'房地产新开工面积')
plot_est.line('date', 'inc', source=source_est, line_width=2, color='green', legend=u'房地产投资开发增速')

plot_corn = get_plot(u'国际玉米期货价格')
plot_corn.line('date', 'p', source=source_corn, line_width=2, legend=u'国际玉米期货价格')

plot_spin = get_plot(u'纺织品出口量同比', pct=True)
plot_spin.line('date', 'out', source=source_spin, line_width=2, legend=u'纺织品出口量')

plot_coal = get_plot(u'秦皇岛港6000大卡大同优混平仓价')
plot_coal.line('date', 'p', source=source_coal, line_width=2, legend=u'秦皇岛港6000大卡大同优混平仓价')

update_all()

curdoc().add_root(column(plot_eth, plot_soda, plot_car, plot_pot, plot_ter, plot_ep, plot_lsoda, plot_dcar,
                         plot_potp, plot_chpot, plot_ster, plot_nap, plot_pta, plot_meg, plot_oecd,
                         plot_glass, plot_auto, plot_est, plot_corn, plot_spin, plot_coal))
curdoc().title = u'化工中观数据库'
