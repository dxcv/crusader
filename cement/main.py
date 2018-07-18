# encoding: utf-8
import pandas as pd

import cement.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 水泥价格指数
source_price = ColumnDataSource(data=dict(date=[], tot=[], east=[], north=[], south=[]))
def update_price():
    df = pd.read_excel(u'%s/水泥价格指数（全国）.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/水泥价格指数（华北）.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/水泥价格指数（华东）.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/水泥价格指数（中南）.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    source_price.data = {'date': df.index,
                         'tot': df[dic[u'水泥价格指数（全国）']],
                         'north': df[dic[u'水泥价格指数（华北）']],
                         'east': df[dic[u'水泥价格指数（华东）']],
                         'south': df[dic[u'水泥价格指数（中南）']]}

def update_all():
    update_price()

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

plot_price = get_plot(u'水泥价格指数（周）')
plot_price.line('date', 'tot', source=source_price, line_width=2, legend=u'水泥价格指数（全国）')
plot_price.line('date', 'north', source=source_price, line_width=2, color='green', legend=u'水泥价格指数（华北）')
plot_price.line('date', 'east', source=source_price, line_width=2, color='red', legend=u'水泥价格指数（华东）')
plot_price.line('date', 'south', source=source_price, line_width=2, color='gray', legend=u'水泥价格指数（中南）')

update_all()

curdoc().add_root(plot_price)
curdoc().title = u'水泥中观数据库'
