# WEBMATH #

Online Math Calculator

Shoutout to [BobDotCom#4428](https://github.com/BobDotCom "Bob's Github") for his help

[My Discord](https://discordapp.com/users/731128007388823592/ "Moritz⚜#6969")

[Bob's Discord](https://discordapp.com/users/690420846774321221/ "BobDotCom#4428")

## Instructions ##

### Install: ###

```py
pip install web-math
```

### Information: ###

```py
calculate() takes one required and one optional argument
calculate([TASK], [PRECISION])
TASK = str
PRECISION = int
```

### Run Program: ###

```py
# import webmath and asyncio
import asyncio
from web_math import webmath

# make def
async def bread():
    output = await webmath.calculate("3+3*3-sqrt(pi)", 4)
    print(output)

# run def
asyncio.run(bread())
```

### OUTPUT: ###
```py
# with 4 digit precision
10.23
# without digit precision
10.227546149094485
```

## Ride the space skyway home to 80s Miami ##
