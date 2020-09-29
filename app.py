#!/usr/bin/env python3

from aws_cdk import core

from demo2.demo2_stack import Demo2Stack


app = core.App()
Demo2Stack(app, "demo2")

app.synth()
