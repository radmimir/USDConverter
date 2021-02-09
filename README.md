# USD converter
USD converter server application on SimpleHTTPServer

Quickstart 
----------
1. Clone project::
```
    git clone https://github.com/radmimir/USDConverter
    cd USDConverter
```
2. Run tests::
```
    python ./tests/test_USDConverter.py
```
Deployment with Docker
----------------------

You must have ``docker`` tool installed to work with material in this section.
Run in ``/`` section of project::
```
    docker build . && docker run 
```
Application will be available on ``localhost:8000`` in your browser.

Application requests

Manual testing responces
----------

1. Get usd course and result of conversation USD->RUB of currency(for example, 1000 rub to usd)::
```
   curl -X GET "http://localhost:8000/usd_rub/1000"
```

2. Get usd course and result of conversation RUB->USD of currency(for example, 1000 usd to rub)::
```
   curl -X GET "http://localhost:8000/rub_usd/1000"
```

TODO
----------

1. Add more unittests
2. Edit Readme.md
3. Convert SimpleHTTPServer to another
4. Add async
5. Add authentification
6. Some comments in code
