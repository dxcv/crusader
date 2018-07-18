# encoding: utf-8
import pandas as pd

import coal.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 发电累计耗用原煤
source_elec = ColumnDataSource(data=dict(date=[], coal=[]))
def update_elec():
    df = pd.read_excel(u'%s/发电累计耗用原煤.xlsx'%(const.DATA_DIR))
    source_elec.data = {'date': df.index, 'coal': df[dic[u'发电累计耗用原煤']] / 100}

# 六大电厂日均耗煤量
source_elec_coal = ColumnDataSource(data=dict(date=[], coal=[]))
def update_elec_coal():
    df = pd.read_excel(u'%s/六大电厂日均耗煤量.xlsx'%(const.DATA_DIR))
    source_elec_coal.data = {'date': df.index, 'coal': df[dic[u'六大电厂日均耗煤量']]}

# 动力煤进出口数量
source_steam = ColumnDataSource(data=dict(date=[], inp=[], out=[]))
def update_steam():
    df = pd.read_excel(u'%s/动力煤进口数量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/动力煤出口数量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_steam.data = {'date': df.index,
                         'inp': df[dic[u'动力煤进口数量']].pct_change(12),
                         'out': df[dic[u'动力煤出口数量']].pct_change(12)}

# 炼焦煤进出口数量
source_cok = ColumnDataSource(data=dict(date=[], inp=[], out=[]))
def update_cok():
    df = pd.read_excel(u'%s/炼焦煤进口数量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/炼焦煤出口数量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_cok.data = {'date': df.index,
                       'inp': df[dic[u'炼焦煤进口数量']].pct_change(12),
                       'out': df[dic[u'炼焦煤出口数量']].pct_change(12)}

# 国内动力煤价格
source_stp = ColumnDataSource(data=dict(date=[], sx=[], qhd=[]))
def update_stp():
    df = pd.read_excel(u'%s/国内动力煤价格--山西6000大卡大同坑口含税价.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/国内动力煤价格--秦皇岛港6000大卡大同优混平仓价.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_stp.data = {'date': df.index,
                       'sx': df[dic[u'国内动力煤价格--山西6000大卡大同坑口含税价']],
                       'qhd': df[dic[u'国内动力煤价格--秦皇岛港6000大卡大同优混平仓价']]}

# 国内炼焦煤
source_cop = ColumnDataSource(data=dict(date=[], p=[]))
def update_cop():
    df = pd.read_excel(u'%s/国内炼焦煤价格--山西古交#2焦煤车板含税价.xlsx'%(const.DATA_DIR))
    source_cop.data = {'date': df.index, 'p': df[dic[u'国内炼焦煤价格--山西古交#2焦煤车板含税价']]}

# 国内无烟煤价格-
source_smk = ColumnDataSource(data=dict(date=[], p=[]))
def update_smk():
    df = pd.read_excel(u'%s/国内无烟煤价格--山西阳泉洗中块7000大卡坑口不含税价.xlsx'%(const.DATA_DIR))
    source_smk.data = {'date': df.index, 'p': df[dic[u'国内无烟煤价格--山西阳泉洗中块7000大卡坑口不含税价']]}

# 秦皇岛港煤炭库存
source_coalinv = ColumnDataSource(data=dict(date=[], inv=[]))
def update_coalinv():
    df = pd.read_excel(u'%s/秦皇岛港煤炭库存.xlsx'%(const.DATA_DIR))
    source_coalinv.data = {'date': df.index, 'inv': df[dic[u'秦皇岛港煤炭库存']]}

# 秦皇岛港煤炭调入量
source_coalin = ColumnDataSource(data=dict(date=[], inp=[]))
def update_coalin():
    df = pd.read_excel(u'%s/秦皇岛港煤炭调入量.xlsx'%(const.DATA_DIR))
    # print df[dic[u'秦皇岛港煤炭调入量']].rolling(window=5).mean()
    source_coalin.data = {'date': df.index, 'inp': df[dic[u'秦皇岛港煤炭调入量']].rolling(window=5).mean()}

# 直供电厂煤炭库存
source_elecinv = ColumnDataSource(data=dict(date=[], inv=[]))
def update_elecinv():
    df = pd.read_excel(u'%s/直供电厂煤炭库存.xlsx'%(const.DATA_DIR))
    source_elecinv.data = {'date': df.index, 'inv': df[dic[u'直供电厂煤炭库存']]}

# 六大电厂煤炭库存
source_e6inv = ColumnDataSource(data=dict(date=[], inv=[]))
def update_e6inv():
    df = pd.read_excel(u'%s/六大电厂煤炭库存.xlsx'%(const.DATA_DIR))
    source_e6inv.data = {'date': df.index, 'inv': df[dic[u'六大电厂煤炭库存']]}

# 火电生产量当月同比增速
source_fire = ColumnDataSource(data=dict(date=[], inc=[]))
def update_fire():
    df = pd.read_excel(u'%s/火电生产量当月同比增速.xlsx'%(const.DATA_DIR))
    source_fire.data = {'date': df.index, 'inc': df[dic[u'火电生产量当月同比增速']] / 100}

# 水泥产量增速
source_cement = ColumnDataSource(data=dict(date=[], inc=[]))
def update_cement():
    df = pd.read_excel(u'%s/水泥产量增速.xlsx'%(const.DATA_DIR))
    source_cement.data = {'date': df.index, 'inc': df[dic[u'水泥产量增速']] / 100}

# 生铁产量增速
source_iron = ColumnDataSource(data=dict(date=[], inc=[]))
def update_iron():
    df = pd.read_excel(u'%s/生铁产量增速.xlsx'%(const.DATA_DIR))
    source_iron.data = {'date': df.index, 'inc': df[dic[u'生铁产量增速']] / 100}

# 焦炭出口量增速
source_coke = ColumnDataSource(data=dict(date=[], inc=[]))
def update_coke():
    df = pd.read_excel(u'%s/焦炭出口量增速.xlsx'%(const.DATA_DIR))
    source_coke.data = {'date': df.index, 'inc': df[dic[u'焦炭出口量增速']] / 100}

# 合成氨产量增速
source_syn = ColumnDataSource(data=dict(date=[], inc=[]))
def update_syn():
    df = pd.read_excel(u'%s/合成氨产量增速.xlsx'%(const.DATA_DIR))
    source_syn.data = {'date': df.index, 'inc': df[dic[u'合成氨产量增速']] / 100}

# 布伦特原油现货价
source_brent = ColumnDataSource(data=dict(date=[], p=[]))
def update_brent():
    df = pd.read_excel(u'%s/布伦特原油现货价.xlsx'%(const.DATA_DIR))
    source_brent.data = {'date': df.index, 'p': df[dic[u'布伦特原油现货价']]}

def update_all():
    update_elec()
    update_steam()
    update_cok()
    update_stp()
    update_cop()
    update_smk()
    update_coalinv()
    update_coalin()
    update_elecinv()
    update_fire()
    update_cement()
    update_iron()
    update_coke()
    update_syn()
    update_brent()
    update_elec_coal()
    update_e6inv()

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

plot_elec = get_plot(u'发电累计耗用原煤增速（月）', pct=True)
plot_elec.line('date', 'coal', source=source_elec, line_width=2, legend=u'发电累计耗用原煤')

plot_steam = get_plot(u'动力煤进出口数量同比（月）', pct=True)
plot_steam.line('date', 'inp', source=source_steam, line_width=2, legend=u'动力煤进口数量')
plot_steam.line('date', 'out', source=source_steam, line_width=2, color='green', legend=u'动力煤出口数量')

plot_cok = get_plot(u'炼焦煤进出口数量同比（月）', pct=True)
plot_cok.line('date', 'inp', source=source_cok, line_width=2, legend=u'炼焦煤进口数量')
plot_cok.line('date', 'out', source=source_cok, line_width=2, color='green', legend=u'炼焦煤出口数量')

plot_stp = get_plot(u'国内动力煤价格（周）')
plot_stp.line('date', 'sx', source=source_stp, line_width=2, legend=u'国内动力煤价格--山西6000大卡大同坑口含税价')
plot_stp.line('date', 'qhd', source=source_stp, line_width=2, color='green', legend=u'国内动力煤价格--秦皇岛港6000大卡大同优混平仓价')

plot_cop = get_plot(u'国内炼焦煤价格（周）')
plot_cop.line('date', 'p', source=source_cop, line_width=2, legend=u'国内炼焦煤价格--山西古交#2焦煤车板含税价')

plot_smk = get_plot(u'国内无烟煤价格（周）')
plot_smk.line('date', 'p', source=source_smk, line_width=2, legend=u'国内无烟煤价格--山西阳泉洗中块7000大卡坑口不含税价')

plot_coalinv = get_plot(u'秦皇岛港煤炭库存（周）')
plot_coalinv.line('date', 'inv', source=source_coalinv, line_width=2, legend=u'秦皇岛港煤炭库存')

plot_coalin = get_plot(u'秦皇岛港煤炭调入量（日）')
plot_coalin.line('date', 'inp', source=source_coalin, line_width=2, legend=u'秦皇岛港煤炭调入量')

plot_elecinv = get_plot(u'直供电厂煤炭库存（月）')
plot_elecinv.line('date', 'inv', source=source_elecinv, line_width=2, legend=u'直供电厂煤炭库存')

plot_fire = get_plot(u'火电生产量当月同比增速（月）', pct=True)
plot_fire.line('date', 'inc', source=source_fire, line_width=2, legend=u'火电生产量当月同比增速')

plot_cement = get_plot(u'水泥产量增速（月）', pct=True)
plot_cement.line('date', 'inc', source=source_cement, line_width=2, legend=u'水泥产量增速')

plot_iron = get_plot(u'生铁产量增速（月）', pct=True)
plot_iron.line('date', 'inc', source=source_iron, line_width=2, legend=u'生铁产量增速')

plot_coke = get_plot(u'焦炭出口量增速（月）', pct=True)
plot_coke.line('date', 'inc', source=source_coke, line_width=2, legend=u'焦炭出口量增速')

plot_syn = get_plot(u'合成氨产量增速（季）', pct=True)
plot_syn.line('date', 'inc', source=source_syn, line_width=2, legend=u'合成氨产量增速')

plot_brent = get_plot(u'布伦特原油现货价（日）')
plot_brent.line('date', 'p', source=source_brent, line_width=2, legend=u'布伦特原油现货价')

plot_elec_coal = get_plot(u'六大电厂日均耗煤量（日）')
plot_elec_coal.line('date', 'coal', source=source_elec_coal, line_width=2, legend=u'六大电厂日均耗煤量')

plot_e6inv = get_plot(u'六大电厂煤炭库存（日）')
plot_e6inv.line('date', 'inv', source=source_e6inv, line_width=2, legend=u'六大电厂煤炭库存')

update_all()

curdoc().add_root(column(plot_elec, plot_elec_coal, plot_steam, plot_cok, plot_stp, plot_cop, plot_smk, plot_coalinv, plot_coalin,
                         plot_elecinv, plot_e6inv, plot_fire, plot_cement, plot_iron, plot_coke, plot_syn, plot_brent))
curdoc().title = u'煤炭中观数据库'
