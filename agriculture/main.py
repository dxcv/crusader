# encoding: utf-8
import pandas as pd

import const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure
from bokeh.palettes import Spectral9

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 消费者物价指数（CPI）、CPI-食品、CPI-粮食、CPI-猪肉、CPI-鲜菜
source_cpi = ColumnDataSource(data=dict(date=[], cpi=[], food=[], grain=[], pork=[], vega=[]))
def update_cpi():
    print('update cpi')
    df = pd.read_excel(u'%s/消费者物价指数（CPI）.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/CPI-食品.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/CPI-粮食.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/CPI-猪肉.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/CPI-鲜菜.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_cpi.data = {'date': df.index,
                       'cpi': df[dic[u'消费者物价指数（CPI）']] / 100.,
                       'food': df[dic[u'CPI-食品']] / 100.,
                       'grain': df[dic[u'CPI-粮食']] / 100.,
                       'pork': df[dic[u'CPI-猪肉']] / 100.,
                       'vega': df[dic[u'CPI-鲜菜']] / 100.}

# 食用农产品价格指数
source_agri_price = ColumnDataSource(data=dict(date=[], index=[]))
def update_agri_price():
    print('update agri price')
    df = pd.read_excel(u'%s/食用农产品价格指数.xlsx'%(const.DATA_DIR))
    source_agri_price.data = {'date': df.index,
                              'index': df[dic[u'食用农产品价格指数']]}

# 食用农产品价格指数-粮食类周环比、食用农产品价格指数-蔬菜类周环比
source_agri_detail = ColumnDataSource(data=dict(date=[], food=[], vega=[]))
def update_agri_detail():
    print('update agri detail')
    df = pd.read_excel(u'%s/食用农产品价格指数-粮食类周环比.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/食用农产品价格指数-蔬菜类周环比.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_agri_detail.data = {'date': df.index,
                               'food': df[dic[u'食用农产品价格指数-粮食类周环比']] / 100.,
                               'vega': df[dic[u'食用农产品价格指数-蔬菜类周环比']] / 100.}
# 鲜猪肉批发价格
source_pork = ColumnDataSource(data=dict(date=[], pork=[]))
def update_pork():
    print('update pork')
    df = pd.read_excel(u'%s/鲜猪肉批发价格.xlsx'%(const.DATA_DIR))
    source_pork.data = {'date': df.index,
                        'pork': df[dic[u'鲜猪肉批发价格']]}

# 夏粮产量、秋粮产量、粮食产量
source_output = ColumnDataSource(data=dict(date=[], summer=[], autumn=[], total=[]))
def update_output():
    print('update output')
    df = pd.read_excel(u'%s/夏粮产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/秋粮产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/粮食产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_output.data = {'date': df.index,
                       'summer': df[dic[u'夏粮产量']],
                       'autumn': df[dic[u'秋粮产量']],
                       'total': df[dic[u'粮食产量']]}

# 粮食播种面积
source_seed = ColumnDataSource(data=dict(date=[], seed=[]))
def update_seed():
    print('update seed')
    df = pd.read_excel(u'%s/粮食播种面积.xlsx'%(const.DATA_DIR))
    source_seed.data = {'date': df.index,
                        'seed': df[dic[u'粮食播种面积']]}

# 生猪存栏数
source_pig = ColumnDataSource(data=dict(date=[], pig=[]))
def update_pig():
    print('update pig')
    df = pd.read_excel(u'%s/生猪存栏数.xlsx'%(const.DATA_DIR))
    source_pig.data = {'date': df.index,
                       'pig': df[dic[u'生猪存栏数']]}

# 能繁母猪存栏数
source_sow = ColumnDataSource(data=dict(date=[], sow=[]))
def update_sow():
    print('update sow')
    df = pd.read_excel(u'%s/能繁母猪存栏数.xlsx'%(const.DATA_DIR))
    source_sow.data = {'date': df.index,
                       'sow': df[dic[u'能繁母猪存栏数']]}

# CBOT玉米期货价格
source_cbot_corn = ColumnDataSource(data=dict(date=[], p=[]))
def update_cbot_corn():
    print('update cbot corn')
    df = pd.read_excel(u'%s/CBOT玉米期货价格.xlsx'%(const.DATA_DIR))
    source_cbot_corn.data = {'date': df.index,
                             'p': df[dic[u'CBOT玉米期货价格']]}

# 批发市场玉米均价
source_corn = ColumnDataSource(data=dict(date=[], p=[]))
def update_corn():
    print('update corn')
    df = pd.read_excel(u'%s/批发市场玉米均价.xlsx'%(const.DATA_DIR))
    source_corn.data = {'date': df.index,
                        'p': df[dic[u'批发市场玉米均价']]}

# 农产品批发价格200指数
source_agri200 = ColumnDataSource(data=dict(date=[], index=[]))
def update_agri200():
    print('update agri 200')
    df = pd.read_excel(u'%s/农产品批发价格200指数.xlsx'%(const.DATA_DIR))
    source_agri200.data = {'date': df.index,
                           'index': df[dic[u'农产品批发价格200指数']]}

def update_all():
    update_cpi()
    update_agri_price()
    update_agri_detail()
    update_output()
    update_pork()
    update_seed()
    update_pig()
    update_sow()
    update_cbot_corn()
    update_corn()
    update_agri200()

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

plot_cpi = get_plot(u'CPI', pct=True)
plot_cpi.line('date', 'cpi', source=source_cpi, line_width=2.5, color='red', legend=u'CPI')
plot_cpi.line('date', 'food', source=source_cpi, line_width=2, color='green', legend=u'CPI：食品')
plot_cpi.line('date', 'grain', source=source_cpi, line_width=2, color='blue', legend=u'CPI：粮食')
plot_cpi.line('date', 'pork', source=source_cpi, line_width=2, color='yellow', legend=u'CPI：猪肉')
plot_cpi.line('date', 'vega', source=source_cpi, line_width=2, color='gray', legend=u'CPI：鲜菜')

plot_agri_price = get_plot(u'食用农产品价格指数')
plot_agri_price.line('date', 'index', source=source_agri_price, line_width=2, legend=u'食用农产品价格指数')

plot_agri_detail = get_plot(u'食品农产品价格指数分项周环比', pct=True)
plot_agri_detail.line('date', 'food', source=source_agri_detail, line_width=2, legend=u'食用农产品价格指数：粮食类周环比')
plot_agri_detail.line('date', 'vega', source=source_agri_detail, line_width=2, color='green', legend=u'食用农产品价格指数：蔬菜类周环比')

plot_pork = get_plot(u'鲜猪肉批发价格')
plot_pork.line('date', 'pork', source=source_pork, line_width=2, legend=u'鲜猪肉批发价格')

plot_output = get_plot(u'粮食产量')
plot_output.line('date', 'summer', source=source_output, line_width=2, legend=u'夏粮产量')
plot_output.line('date', 'autumn', source=source_output, line_width=2, color='green', legend=u'秋粮产量')
plot_output.line('date', 'total', source=source_output, line_width=2, color='red', legend=u'粮食产量')

plot_seed = get_plot(u'粮食播种面积')
plot_seed.line('date', 'seed', source=source_seed, line_width=2, legend=u'粮食播种面积')

plot_pig = get_plot(u'生猪存栏数')
plot_pig.line('date', 'pig', source=source_pig, line_width=2, legend=u'生猪存栏数')

plot_sow = get_plot(u'能繁母猪存栏数')
plot_sow.line('date', 'sow', source=source_sow, line_width=2, legend=u'能繁母猪存栏数')

plot_cbot_corn = get_plot(u'CBOT玉米期货价格')
plot_cbot_corn.line('date', 'p', source=source_cbot_corn, line_width=2, legend=u'CBOT玉米期货价格')

plot_corn = get_plot(u'批发市场玉米均价')
plot_corn.line('date', 'p', source=source_corn, line_width=2, legend=u'批发市场玉米均价')

plot_agri200 = get_plot(u'农产品批发价格200指数')
plot_agri200.line('date', 'index', source=source_agri200, line_width=2, legend=u'农产品批发价格200指数')

update_all()

curdoc().add_root(column(plot_cpi, plot_agri_price, plot_agri_detail, plot_pork, plot_output,
                         plot_seed, plot_pig, plot_sow, plot_cbot_corn, plot_corn, plot_agri200))
curdoc().title = u'农林牧渔'
