import os

def main():
    industry = ['agriculture', 'engineering', 'cars', 'transportation', 'estate', 'metal', 'coal', 'chemical', 'steel', 'bank',
                'cement']
    for ind in industry:
        print('updating %s...'%(ind))
        os.system('python ./%s/%s/data.py'%(ind, ind))

if __name__ == '__main__':
    main()
