import os

def main():
    bokeh_cmd = 'bokeh.exe serve'
    industry = ['agriculture', 'engineering', 'cars', 'transportation', 'estate', 'metal', 'coal', 'chemical', 'steel', 'bank',
                'cement']

    os.system('%s %s --host * --port 5008'%(bokeh_cmd, ' '.join(industry)))

if __name__ == '__main__':
    main()
