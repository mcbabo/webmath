# WEBMATH #

Online Math Calculator

Shoutout to [BobDotCom#4428](https://github.com/BobDotCom "Bob's Github") for his help

## Instructions ##

### Install: ###

```py
pip install web-math
```

### Run Programm: ###

```py
# import webmath and asyncio
import asyncio
from web_math import webmath

# make def
async def bread():
    output = await webmath.calculate("3+3*3-sqrt(pi)")
    print(output)

# run def
asyncio.run(bread())
```

### OUTPUT ###
```py
8.45509229818897
```


## Ride the space skyway home to 80s Miami ##
