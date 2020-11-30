# Snscrape-Dataframe-Builder (Version 0.1.0)
A dataframe builder extension for JustAnotherArchivist's [snscrape](https://github.com/JustAnotherArchivist/snscrape) API. Initially, the dataframe is exported just in CSV format, but will be avaliable in other formats (JSON for example). A keywords file reader was implemented to help extract several different keywords (avaliable to test in *test* folder).

## Getting Started
### Required Settings
- [Python 3.8.5+](https://www.python.org/download/releases/3.0/)
- [snscrape 0.3.5+](https://github.com/JustAnotherArchivist/snscrape)
- [Pandas 1.1.4+](https://pandas.pydata.org/)

### Installation
Just download the repository and use SnscrapeDFBuilder.py file

## How To Use
Inside folder containing SnscrapeDFBuilder.py and snscrape_crawler.py open terminal/cmd and call SnscrapeDFBuilder script

### Samples
> python SnscrapeDFBuilder.py -hashtag NewYork --since 2019-04-10 --until 2020-01-20
> python SnscrapeDFBuilder.py -list /tests/ex.txt -o /tests/res/output

## Arguments

### Obrigatory Arguments
- **-hashtag KEYWORD:** Get data by hashtag (Please do not use # in KEYWORD);
- **-user KEYWORD:** Get data by username (Please do not use @ in KEYWORD);
- **-keyword KEYWORD:** Get data by keyword;
- **-list FILE.txt:** Text file with all target keywords;

### Optional Argmuents
- **-o FILE:** Set file name where the results will be storage (default format: .csv)
- **--max-limit N:** Only return the first N results
- **--since DATETIME:** Only return results newer the DATETIME
- **--until DATETIME:** Only return results older the DATETIME
- **--help:** Show help message and exit
- **--version:** Show this script's version and exit
