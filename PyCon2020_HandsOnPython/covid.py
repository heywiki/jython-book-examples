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
    with open(fname, encoding='utf8') as fin:
        rows = []
        for line in fin:
            values = line.strip().split(',')
            if len(rows) == 0:
                headers = values
            else:
                rows.append(dict(zip(headers, values)))
    return rows
