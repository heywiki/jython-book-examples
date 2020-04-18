import urllib.request as req

def fetch_url(url, fname):
    '''
    Save a url to a local file
    '''
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, mode='wb') as fout:
        fout.write(data)

def read_csv(fname):
    #import pdb; pdb.set_trace()
    with open(fname, encoding='utf8') as fin:
        rows = []
        for i, line in enumerate(fin):
            values = line.strip().split(',')
            if i == 0:
                headers = values
            else:
                for j, val in enumerate(values):
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                    values[j] = val
                rows.append(dict(zip(headers, values)))
    return rows

def filter(rows, state):
    res = []
    for row in rows:
        if row['state'] == state:
            res.append(row)
    return res

def sortby(rows, col_name):
    def get_col_name(row):
        return row[col_name]
    return sorted(rows, key=get_col_name)

def get_value(rows, col_name):
    res = []
    for row in rows:
        res.append(row[col_name])
    return res

def plot_state(state, csvname, plotname):
    res = covid.read_csv(csvname)
    state_res = covid.filter(res, state)
    state_res = covid.sortby(state_res, 'date')
    fix, ax = plt.subplots()
    ax.plot(covid.get_value(state_res, 'positive'))
    ax.plot(covid.get_value(state_res, 'death'))
    ax.plot(covid.get_value(state_res, 'hospitalized'))
    fig.savefig(plotname)
