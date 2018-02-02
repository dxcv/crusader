# encoding: utf-8
import pandas as pd

import engineering.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 工程机械主营业务收入
source_income = ColumnDataSource(data=dict(date=[], income=[]))
def update_income():
    print('update income')
    df = pd.read_excel(u'%s/工程机械主营业务收入.xlsx'%(const.DATA_DIR))
    source_income.data = {'date': df.index, 'income': df[dic[u'工程机械主营业务收入']]}

# 挖掘机销量
source_excavator = ColumnDataSource(data=dict(date=[], vol=[]))
def update_excavator():
    print('update excavator')
    df = pd.read_excel(u'%s/挖掘机销量.xlsx'%(const.DATA_DIR))
    source_excavator.data = {'date': df.index, 'vol': df[dic[u'挖掘机销量']].pct_change(12)}

# 推土机销量、出口量
source_dozer = ColumnDataSource(data=dict(date=[], vol=[], out=[]))
def update_dozer():
    print('update dozer')
    df = pd.read_excel(u'%s/推土机销量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/推土机出口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_dozer.data = {'date': df.index,
                         'vol': df[dic[u'推土机销量']].pct_change(12),
                         'out': df[dic[u'推土机出口量']].pct_change(12)}

# 20mm普板平均价
source_ban = ColumnDataSource(data=dict(date=[], p=[]))
def update_ban():
    print('update ban')
    df = pd.read_excel(u'%s/20mm普板平均价.xlsx'%(const.DATA_DIR))
    source_ban.data = {'date': df.index, 'p': df[dic[u'20mm普板平均价']]}

# 装载机销量
source_load = ColumnDataSource(data=dict(date=[], vol=[]))
def update_load():
    print('update load')
    df = pd.read_excel(u'%s/装载机销量.xlsx'%(const.DATA_DIR))
    source_load.data = {'date': df.index, 'vol': df[dic[u'装载机销量']].pct_change(12)}

# 履带式起重机销量
source_crane = ColumnDataSource(data=dict(date=[], vol=[]))
def update_crane():
    print('update crane')
    df = pd.read_excel(u'%s/履带式起重机销量.xlsx'%(const.DATA_DIR))
    source_crane.data = {'date': df.index, 'vol': df[dic[u'履带式起重机销量']].pct_change(12)}

# 城镇固定资产投资增速、房地产新开工施工面积增速、基础设施建设投资增速
source_invest = ColumnDataSource(data=dict(date=[], city=[], house=[], base=[]))
def update_invest():
    print('update invest')
    df = pd.read_excel(u'%s/城镇固定资产投资增速.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/房地产新开工施工面积增速.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/基础设施建设投资增速.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_invest.data = {'date': df.index,
                          'city': df[dic[u'城镇固定资产投资增速']] / 100,
                          'house': df[dic[u'房地产新开工施工面积增速']] / 100,
                          'base': df[dic[u'基础设施建设投资增速']] / 100}

# 出口总额同比增速
source_out = ColumnDataSource(data=dict(date=[], inc=[]))
def update_output():
    print('update out')
    df = pd.read_excel(u'%s/出口总额同比增速.xlsx'%(const.DATA_DIR))
    source_out.data = {'date': df.index, 'inc': df[dic[u'出口总额同比增速']] / 100}

# CRB指数
source_crb = ColumnDataSource(data=dict(date=[], crb=[]))
def update_crb():
    print('update crb')
    df = pd.read_excel(u'%s/CRB指数.xlsx'%(const.DATA_DIR))
    source_crb.data = {'date': df.index, 'crb': df[dic[u'CRB指数']]}

def update_all():
    update_income()
    update_excavator()
    update_dozer()
    update_ban()
    update_load()
    update_crane()
    update_invest()
    update_output()
    update_crb()

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

plot_income = get_plot(u'工程机械主营业务收入')
plot_income.line('date', 'income', source=source_income, line_width=2, legend=u'工程机械主营业务收入')

plot_excavator = get_plot(u'挖掘机销量同比增速', pct=True)
plot_excavator.line('date', 'vol', source=source_excavator, line_width=2, legend=u'挖掘机销量同比增速')

plot_dozer = get_plot(u'推土机销量、出口量同比增速', pct=True)
plot_dozer.line('date', 'vol', source=source_dozer, line_width=2, legend=u'推土机销量同比增速')
plot_dozer.line('date', 'out', source=source_dozer, line_width=2, color='green', legend=u'推土机出口量同比增速')

plot_ban = get_plot(u'20mm普板平均价')
plot_ban.line('date', 'p', source=source_ban, line_width=2, legend=u'20mm普板平均价')

plot_load = get_plot(u'装载机销量', pct=True)
plot_load.line('date', 'vol', source=source_load, line_width=2, legend=u'装载机销量')

plot_crane = get_plot(u'履带式起重机销量', pct=True)
plot_crane.line('date', 'vol', source=source_crane, line_width=2, legend=u'履带式起重机销量')

plot_invest = get_plot(u'固定资产投资、房地产新开工面积、基础设施投资增速', pct=True)
plot_invest.line('date', 'city', source=source_invest, line_width=2, legend=u'固定资产投资增速')
plot_invest.line('date', 'house', source=source_invest, line_width=2, color='green', legend=u'房地产新开工面积增速')
plot_invest.line('date', 'base', source=source_invest, line_width=2, color='red', legend=u'基础设施投资增速')

plot_output = get_plot(u'出口总额同比增速', pct=True)
plot_output.line('date', 'inc', source=source_out, line_width=2, legend=u'出口总额同比增速')

plot_crb = get_plot(u'CRB指数')
plot_crb.line('date', 'crb', source=source_crb, line_width=2, legend=u'CRB指数')

update_all()

curdoc().add_root(column(plot_income, plot_excavator, plot_dozer, plot_ban, plot_load, plot_crane, plot_invest,
                         plot_crb))
curdoc().title = u'工程机械中观数据库'
