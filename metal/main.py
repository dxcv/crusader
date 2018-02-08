# encoding: utf-8
import pandas as pd

import metal.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 铜产量
source_copper_prod = ColumnDataSource(data=dict(date=[], prod=[]))
def update_copper_prod():
    df = pd.read_excel(u'%s/铜产量.xlsx'%(const.DATA_DIR))
    source_copper_prod.data = {'date': df.index,
                               'prod':df[dic[u'铜产量']] / 100}

# LME铜三个月期货价格
source_copper_p = ColumnDataSource(data=dict(date=[], p=[]))
def update_copper_p():
    df = pd.read_excel(u'%s/LME铜三个月期货价格.xlsx'%(const.DATA_DIR))
    source_copper_p.data = {'date': df.index,
                            'p': df[dic[u'LME铜三个月期货价格']]}

# LME铜库存、上交所铜库存
source_copper_inv = ColumnDataSource(data=dict(date=[], lme=[], sh=[]))
def update_copper_inv():
    df = pd.read_excel(u'%s/LME铜库存.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/上交所铜库存.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_copper_inv.data = {'date': df.index,
                              'lme': df[dic[u'LME铜库存']],
                              'sh': df[dic[u'上交所铜库存']]}

# 铝产量
source_alum_prod = ColumnDataSource(data=dict(date=[], prod=[]))
def update_alum_prod():
    df = pd.read_excel(u'%s/铝产量.xlsx'%(const.DATA_DIR))
    source_alum_prod.data = {'date': df.index,
                               'prod':df[dic[u'铝产量']] / 100}

# LME铝三个月期货价格
source_alum_p = ColumnDataSource(data=dict(date=[], p=[]))
def update_alum_p():
    df = pd.read_excel(u'%s/LME铝三个月期货价格.xlsx'%(const.DATA_DIR))
    source_alum_p.data = {'date': df.index,
                            'p': df[dic[u'LME铝三个月期货价格']]}

# LME铝库存、上交所铝库存
source_alum_inv = ColumnDataSource(data=dict(date=[], lme=[], sh=[]))
def update_alum_inv():
    df = pd.read_excel(u'%s/LME铝库存.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/上交所铝库存.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_alum_inv.data = {'date': df.index,
                              'lme': df[dic[u'LME铝库存']],
                              'sh': df[dic[u'上交所铝库存']]}

# 铅产量
source_plum_prod = ColumnDataSource(data=dict(date=[], prod=[]))
def update_plum_prod():
    df = pd.read_excel(u'%s/铅产量.xlsx'%(const.DATA_DIR))
    source_plum_prod.data = {'date': df.index,
                               'prod':df[dic[u'铅产量']] / 100}

# LME铅三个月期货价格
source_plum_p = ColumnDataSource(data=dict(date=[], p=[]))
def update_plum_p():
    df = pd.read_excel(u'%s/LME铅三个月期货价格.xlsx'%(const.DATA_DIR))
    source_plum_p.data = {'date': df.index,
                            'p': df[dic[u'LME铅三个月期货价格']]}

# LME铅库存、上交所铅库存
source_plum_inv = ColumnDataSource(data=dict(date=[], lme=[], sh=[]))
def update_plum_inv():
    df = pd.read_excel(u'%s/LME铅库存.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/上交所铅库存.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_plum_inv.data = {'date': df.index,
                              'lme': df[dic[u'LME铅库存']],
                              'sh': df[dic[u'上交所铅库存']]}

# 锌产量
source_zinc_prod = ColumnDataSource(data=dict(date=[], prod=[]))
def update_zinc_prod():
    df = pd.read_excel(u'%s/锌产量.xlsx'%(const.DATA_DIR))
    source_zinc_prod.data = {'date': df.index,
                               'prod':df[dic[u'锌产量']] / 100}

# LME锌三个月期货价格
source_zinc_p = ColumnDataSource(data=dict(date=[], p=[]))
def update_zinc_p():
    df = pd.read_excel(u'%s/LME锌三个月期货价格.xlsx'%(const.DATA_DIR))
    source_zinc_p.data = {'date': df.index,
                            'p': df[dic[u'LME锌三个月期货价格']]}

# LME锌库存、上交所锌库存
source_zinc_inv = ColumnDataSource(data=dict(date=[], lme=[], sh=[]))
def update_zinc_inv():
    df = pd.read_excel(u'%s/LME锌库存.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/上交所锌库存.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_zinc_inv.data = {'date': df.index,
                              'lme': df[dic[u'LME锌库存']],
                              'sh': df[dic[u'上交所锌库存']]}

# 20-23%江西上饶铜精矿价格
source_copper_mine = ColumnDataSource(data=dict(date=[], p=[]))
def update_copper_mine():
    df = pd.read_excel(u'%s/20-23%%江西上饶铜精矿价格.xlsx'%(const.DATA_DIR))
    source_copper_mine.data = {'date': df.index, 'p': df[dic[u'20-23%江西上饶铜精矿价格']]}

# 国产现货氧化铝价格
source_alumina = ColumnDataSource(data=dict(date=[], p=[]))
def update_alumina():
    df = pd.read_excel(u'%s/国产现货氧化铝价格.xlsx'%(const.DATA_DIR))
    source_alumina.data = {'date': df.index, 'p': df[dic[u'国产现货氧化铝价格']]}

# 河南60%min铅精矿价格
source_plum_mine = ColumnDataSource(data=dict(date=[], p=[]))
def update_plum_mine():
    df = pd.read_excel(u'%s/河南60%%min铅精矿价格.xlsx'%(const.DATA_DIR))
    source_plum_mine.data = {'date': df.index, 'p': df[dic[u'河南60%min铅精矿价格']]}

# 河池50%锌精矿价格
source_zinc_mine = ColumnDataSource(data=dict(date=[], p=[]))
def update_zinc_mine():
    df = pd.read_excel(u'%s/河池50%%锌精矿价格.xlsx'%(const.DATA_DIR))
    source_zinc_mine.data = {'date': df.index, 'p': df[dic[u'河池50%锌精矿价格']]}

# 山西古交2#焦煤车板含税价
source_coal = ColumnDataSource(data=dict(date=[], p=[]))
def update_coal():
    df = pd.read_excel(u'%s/山西古交2#焦煤车板含税价.xlsx'%(const.DATA_DIR))
    source_coal.data = {'date': df.index, 'p': df[dic[u'山西古交2#焦煤车板含税价']]}

# BDI
source_bdi = ColumnDataSource(data=dict(date=[], bdi=[]))
def update_bdi():
    df = pd.read_excel(u'%s/BDI.xlsx'%(const.DATA_DIR))
    source_bdi.data = {'date': df.index, 'bdi': df[dic['BDI']]}

# OECD全球领先指数
source_oecd = ColumnDataSource(data=dict(date=[], index=[]))
def update_oecd():
    df = pd.read_excel(u'%s/OECD全球领先指数.xlsx'%(const.DATA_DIR))
    source_oecd.data = {'date': df.index, 'index': df[dic[u'OECD全球领先指数']]}

# 中国房地产新开工面积
source_estate = ColumnDataSource(data=dict(date=[], new=[]))
def update_estate():
    df = pd.read_excel(u'%s/中国房地产新开工面积.xlsx'%(const.DATA_DIR))
    source_estate.data = {'date': df.index, 'new': df[dic[u'中国房地产新开工面积']] / 100}

# 中国汽车产量
source_car = ColumnDataSource(data=dict(date=[], prod=[]))
def update_car():
    df = pd.read_excel(u'%s/中国汽车产量.xlsx'%(const.DATA_DIR))
    source_car.data = {'date': df.index, 'prod': df[dic[u'中国汽车产量']] / 100}

# 中国冰箱产量
source_ice = ColumnDataSource(data=dict(date=[], ice=[]))
def update_ice():
    df = pd.read_excel(u'%s/中国冰箱产量.xlsx'%(const.DATA_DIR))
    source_ice.data = {'date': df.index, 'ice': df[dic[u'中国冰箱产量']] / 100}

# 中国空调产量
source_air = ColumnDataSource(data=dict(date=[], air=[]))
def update_air():
    df = pd.read_excel(u'%s/中国空调产量.xlsx'%(const.DATA_DIR))
    source_air.data = {'date': df.index, 'air': df[dic[u'中国空调产量']] / 100}

def update_all():
    update_copper_prod()
    update_copper_p()
    update_copper_inv()
    update_alum_prod()
    update_alum_p()
    update_alum_inv()
    update_plum_prod()
    update_plum_p()
    update_plum_inv()
    update_zinc_prod()
    update_zinc_p()
    update_zinc_inv()
    update_copper_mine()
    update_alumina()
    update_plum_mine()
    update_zinc_mine()
    update_coal()
    update_bdi()
    update_oecd()
    update_estate()
    update_car()
    update_ice()
    update_air()

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

plot_copper_prod = get_plot(u'铜产量同比', pct=True)
plot_copper_prod.line('date', 'prod', source=source_copper_prod, line_width=2, legend=u'铜产量')

plot_copper_p = get_plot(u'LME铜三个月期货价格')
plot_copper_p.line('date', 'p', source=source_copper_p, line_width=2, legend=u'LME铜三个月期货价格')

plot_copper_inv = get_plot(u'LME铜库存')
plot_copper_inv.line('date', 'lme', source=source_copper_inv, line_width=2, legend=u'LME铜库存')
plot_copper_inv.line('date', 'sh', source=source_copper_inv, line_width=2, color='green', legend=u'上交所铜库存')

plot_alum_prod = get_plot(u'铝产量同比', pct=True)
plot_alum_prod.line('date', 'prod', source=source_alum_prod, line_width=2, legend=u'铝产量')

plot_alum_p = get_plot(u'LME铝三个月期货价格')
plot_alum_p.line('date', 'p', source=source_alum_p, line_width=2, legend=u'LME铝三个月期货价格')

plot_alum_inv = get_plot(u'LME铝库存')
plot_alum_inv.line('date', 'lme', source=source_alum_inv, line_width=2, legend=u'LME铝库存')
plot_alum_inv.line('date', 'sh', source=source_alum_inv, line_width=2, color='green', legend=u'上交所铝库存')

plot_plum_prod = get_plot(u'铅产量同比', pct=True)
plot_plum_prod.line('date', 'prod', source=source_plum_prod, line_width=2, legend=u'铅产量')

plot_plum_p = get_plot(u'LME铅三个月期货价格')
plot_plum_p.line('date', 'p', source=source_plum_p, line_width=2, legend=u'LME铅三个月期货价格')

plot_plum_inv = get_plot(u'LME铅库存')
plot_plum_inv.line('date', 'lme', source=source_plum_inv, line_width=2, legend=u'LME铅库存')
plot_plum_inv.line('date', 'sh', source=source_plum_inv, line_width=2, color='green', legend=u'上交所铅库存')

plot_zinc_prod = get_plot(u'锌产量同比', pct=True)
plot_zinc_prod.line('date', 'prod', source=source_zinc_prod, line_width=2, legend=u'锌产量')

plot_zinc_p = get_plot(u'LME锌三个月期货价格')
plot_zinc_p.line('date', 'p', source=source_zinc_p, line_width=2, legend=u'LME锌三个月期货价格')

plot_zinc_inv = get_plot(u'LME锌库存')
plot_zinc_inv.line('date', 'lme', source=source_zinc_inv, line_width=2, legend=u'LME锌库存')
plot_zinc_inv.line('date', 'sh', source=source_zinc_inv, line_width=2, color='green', legend=u'上交所锌库存')

plot_copper_mine = get_plot(u'20-23%江西上饶铜精矿价格')
plot_copper_mine.line('date', 'p', source=source_copper_mine, line_width=2, legend=u'20-23%江西上饶铜精矿价格')

plot_alumina = get_plot(u'国产现货氧化铝价格')
plot_alumina.line('date', 'p', source=source_alum_p, line_width=2, legend=u'国产现货氧化铝价格')

plot_plum_mine = get_plot(u'河南60%min铅精矿价格')
plot_plum_mine.line('date', 'p', source=source_plum_mine, line_width=2, legend=u'河南60%min铅精矿价格')

plot_zinc_mine = get_plot(u'河池50%锌精矿价格')
plot_zinc_mine.line('date', 'p', source=source_zinc_mine, line_width=2, legend=u'河池50%锌精矿价格')

plot_coal = get_plot(u'山西古交2#焦煤车板含税价')
plot_coal.line('date', 'p', source=source_coal, line_width=2, legend=u'山西古交2#焦煤车板含税价')

plot_bdi = get_plot(u'波罗的海干散货指数（BDI）')
plot_bdi.line('date', 'bdi', source=source_bdi, line_width=2, legend=u'BDI')

plot_oecd = get_plot(u'OECD全球领先指数')
plot_oecd.line('date', 'index', source=source_oecd, line_width=2, legend=u'OECD全球领先指数')

plot_estate = get_plot(u'中国房地产新开工面积同比', pct=True)
plot_estate.line('date', 'new', source=source_estate, line_width=2, legend=u'中国房地产新开工面积')

plot_car = get_plot(u'中国汽车产量同比', pct=True)
plot_car.line('date', 'prod', source=source_car, line_width=2, legend=u'中国汽车产量')

plot_ice = get_plot(u'中国冰箱产量', pct=True)
plot_ice.line('date', 'ice', source=source_ice, line_width=2, legend=u'中国冰箱产量')

plot_air = get_plot(u'中国空调产量', pct=True)
plot_air.line('date', 'air', source=source_air, line_width=2, legend=u'中国空调产量')

update_all()

curdoc().add_root(column(plot_copper_prod, plot_copper_p, plot_copper_inv,
                         plot_alum_prod, plot_alum_p, plot_alum_inv,
                         plot_plum_prod, plot_plum_p, plot_plum_inv,
                         plot_zinc_prod, plot_zinc_p, plot_zinc_inv,
                         plot_copper_mine, plot_alumina, plot_plum_mine, plot_zinc_mine, plot_coal, plot_bdi,
                         plot_oecd, plot_estate, plot_car, plot_ice, plot_air))
curdoc().title = u'有色金属中观数据库'
