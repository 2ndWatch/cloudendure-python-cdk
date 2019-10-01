#!/usr/bin/env python3

from aws_cdk import core

from cloudendure.cloudendure_stack import MyStack


app = core.App()
MyStack(app, "cloudendure-cdk", env={"region": "us-east-1"})

app.synth()
