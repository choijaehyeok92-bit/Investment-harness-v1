"""Resolve one canonical current assessment. Read-only, no quote refresh/trading."""
import argparse
from .core import read, dumps

def resolve(ticker):
    ticker=ticker.upper()
    registry=read(read('reviews/latest.json')['registry'])['companies']
    matches=[r for r in registry if ticker==r['ticker'] or ticker in r['aliases']]
    if len(matches)!=1:raise ValueError('Unknown or ambiguous ticker: '+ticker)
    latest=read(matches[0]['latest'])
    return read(latest['assessment'])

def main():
    p=argparse.ArgumentParser();p.add_argument('ticker',nargs='?');p.add_argument('--list',action='store_true');a=p.parse_args()
    if a.list:print(dumps(read(read('reviews/latest.json')['registry'])))
    elif a.ticker:print(dumps(resolve(a.ticker)))
    else:p.error('Provide ticker or --list')

if __name__=='__main__':main()
