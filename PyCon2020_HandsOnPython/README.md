Tutorial: Matt Harrison - Hands-on Beginning Python

https://www.youtube.com/watch?v=fuJcSNUMrW0&feature=youtu.be

From https://us.pycon.org/2020/online/, 2020-04-15

Crash course similar to Jython book but with less text:
https://github.com/mattharrison/Tiny-Python-3.8-Notebook

I am using Atom with platform-ide-termina and git bash on Windows:

== TS: 0
Virtual Environments, Editors

python -m venv env
source env/Scripts/activate

deactivate

REPL (read, evaluate, print, loop)
python -m idlelib.idle &     -> starts the editor, REPL
python -i                    -> REPL on bash (Ctrl-Z to exit)

Editors:
Emacs, PyCharm, VSCode (i use Atom,Vi)

== TS 17:57
REPL, download csv from url

https://github.com/COVID19Tracking/covid-tracking-data

REPL:
>>> url='https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'
>>> import urllib.request as req
>>> req
>>> fin = req.urlopen(url)
>>> data = fin.read()
>>> len(data)
>>> # orange -keywords,syntax
>>> # purple - builtin

>>> type(data)
<class 'bytes'>
>>> data[0:100] # slice
b'date,state,positive,negative,pending,hospitalizedCurrently,hospitalizedCumulative,inIcuCurrently,inI'
>>> fout = open('covid.csv', mode='wb')
>>> fout.write(data)
295154
>>> fout.close()


== TS 27:43   
Functions, dir(), help(), context (with ... as :)

Alt+P to get back previous lines in REPL

when you have a colon at the end of the line:
    ident with 4 spaces

see covid.py
-> run command
dir()

>>> url='https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'
>>> fname='covid.csv'
>>> fetch_url(url, fname)

docstrings triple quotes
>>> help(fetch_url)

context:

instead of:

fout = open(fname, mode='wb')
fout.write(data)
fout.close()

write

with open(fname, mode='wb') as fout:
    fout.write()
#upon unindent file is closed (otherwise when function is done)


== TS 35:49
unicode streams, type(), len(), dunder, REPL help

Python 3 Features: Unicode Streams natively

fin = open('covid.csv', encoding='utf8')
lines = []
#empty list literal

When you open a file in text mode you can loop over lines
for line in fin:

>>> for line in fin:
	lines.append(line)
>>> len(lines)
>>> lines[0]  #first line
>>> lines[-1]  #last line
>>> type(line[0])

dir(lines)
# dunder - double underscore
# protocols that Python responds to
'__contains___'
'name' in lines

help(lines.append)
help() -> help mode (keywords, topics, etc)
enter -> exits


== TS 43:04
string processing

>>> help(lines[1])
>>> help(lines[1].split)
>>> lines[1].split(',')
>>> 'matt\n\t'.strip()
>>> lines[1].strip().split(',')

#Dictionary maps keys to values
>>> d = {}
>>> d['cat'] = 'furry feline'
>>> d['dog'] = 'cozy canine'
>>> d
{'cat': 'furry feline', 'dog': 'cozy canine'}
>>> d['cat']
'furry feline'

Example from https://github.com/mattharrison/Tiny-Python-3.8-Notebook/blob/master/python38.rst

If you have two parallel arrays the following also works:

>>> names = ['Paul', 'John']
>>> insts = ['Bass', 'Guitar']
>>> instruments = dict(zip(names, insts))


>>> zip(lines[0].strip().split(','), lines[1].strip().split(','))
<zip object at 0x0000025555539E80>
>>> list(zip(lines[0].strip().split(','), lines[1].strip().split(',')))
[('date', '20200415'), ('state', 'AK'), ('positive', '293'), ('negative', '8371'), ('pending', ''), ('hospitalizedCurrently', ''), ('hospitalizedCumulative', '34'), ('inIcuCurrently', ''), ('inIcuCumulative', ''), ('onVentilatorCurrently', ''), ('onVentilatorCumulative', ''), ('recovered', '106'), ('hash', '673f84f2ad0944b787570c22a3fa5081f0dee21a'), ('dateChecked', '2020-04-15T20:00:00Z'), ('death', '9'), ('hospitalized', '34'), ('total', '8664'), ('totalTestResults', '8664'), ('posNeg', '8664'), ('fips', '02'), ('deathIncrease', '0'), ('hospitalizedIncrease', '2'), ('negativeIncrease', '308'), ('positiveIncrease', '8'), ('totalTestResultsIncrease', '316')]

>>> dict(zip(lines[0].strip().split(','), lines[1].strip().split(',')))
{'date': '20200415', 'state': 'AK', 'positive': '293', 'negative': '8371', 'pending': '', 'hospitalizedCurrently': '', 'hospitalizedCumulative': '34', 'inIcuCurrently': '', 'inIcuCumulative': '', 'onVentilatorCurrently': '', 'onVentilatorCumulative': '', 'recovered': '106', 'hash': '673f84f2ad0944b787570c22a3fa5081f0dee21a', 'dateChecked': '2020-04-15T20:00:00Z', 'death': '9', 'hospitalized': '34', 'total': '8664', 'totalTestResults': '8664', 'posNeg': '8664', 'fips': '02', 'deathIncrease': '0', 'hospitalizedIncrease': '2', 'negativeIncrease': '308', 'positiveIncrease': '8', 'totalTestResultsIncrease': '316'}

Matt notes that with build in csv module or https://pandas.pydata.org/ this would be easier, but he wants to show data structures

Deomonstration of code, see covid.py:


def read_csv(fname):
    with open(fname, encoding='utf8') as fin:
        rows = []
        for line in fin:
            values = line.strip().split(',')
            if len(rows) == 0:  # if not rows:
                headers = values
            else:
                rows.append(dict(zip(headers, values)))
    return rows


Detecting length of list
>>> bool([])
False
>>> bool([1,3])
True
>>> bool(len([]) == 0)
True

if not rows


== TS 55:55
debugging

>>> import covid           # i do this because i am not usint the REPL editor, but atom
>>> dir()
>>> covid.read_csv('covid.csv')

rubberduck debugging -> explaining to someone else
print debugging -> using print(statements)
