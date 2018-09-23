import ads
import os
import datetime as dt
import pandas as pd


def query_counts(name, query, year, acknowledgements=False):
    if acknowledgements:
        query = 'ack:' + query
    modifiers = ' '.join(['year:%i'])
    full_query = ' '.join([query, modifiers])
    filter_query = ['database:astronomy',
                    'property:refereed']
    papers = ads.SearchQuery(q=full_query % year,
                             fq=filter_query)
    papers.execute()
    count = int(papers.response.numFound)
    total_papers = ads.SearchQuery(q=modifiers % year)
    total_papers.execute()
    total_count = int(total_papers.response.numFound)
    now = dt.datetime.now().timetuple()
    if year == now.tm_year:
        days_in_year = dt.date(year, 12, 31).timetuple().tm_yday
        count *= days_in_year / now.tm_yday
        total_count *= days_in_year / now.tm_yday
    return dict(name=name, query=query, year=year, count=count,
                total_count=total_count)


languages = {
             'IDL': ['IDL'],
             'Python': ['Python'],
             'Matlab': ['MATLAB', 'Matlab'],
             'Fortran': ['Fortran', 'FORTRAN'],
             'Java': ['Java'],
             'C': ['C programming language', 'C language', 'C code',
                   'C library', 'C module'],
             'R': ['R programming language', 'R language', 'R code',
                   'R library', 'R module'],
             'Mathematica': ['Mathematica'],
             'Julia': ['Julia'],
            }

filename = 'ADS_results.csv'

if not os.path.exists(filename):
    results = pd.DataFrame([query_counts(name, query, year)
                            for name, queries in languages.items()
                            for query in queries
                            for year in range(1995, 2018)])
    results.to_csv(filename, index=False)
