#!/usr/bin/env python
import database_utils
from time import sleep

while True:
    database_utils.prober()
    sleep(1)