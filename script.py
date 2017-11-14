# -*- coding: utf-8 -*-
#!/usr/bin/env python

import speechrecog as srecog

def callback():
	response = srecog.listen()
	print(response)

srecog.adjust_amb_noise()

#--------------------------------------------------------

import hotword_hold as hw
import sys

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)
model = sys.argv[1]

hw.detect(callback,model)
