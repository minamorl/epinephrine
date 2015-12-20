# epinephrine
In-memory database

[![PyPI version](https://badge.fury.io/py/epinephrine.svg)](https://badge.fury.io/py/epinephrine)

[![Circle CI](https://circleci.com/gh/minamorl/epinephrine.svg?style=svg)](https://circleci.com/gh/minamorl/epinephrine)

## Installation
```
pip install epinephrine
```

Type `epinephrine` then press enter. Server will start up.

## Usage

Try `telnet localhost:9999`

All commands starts with `#`.

```
#INSERT:your data1
#INSERT:your data2
#RETRIVE:2:0
```


## Commands

### insert
INSERT:{text}

### retrive
RETRIVE:{line}:{page}
