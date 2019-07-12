#!/bin/bash
echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
gunicorn run:app -b 0.0.0.0:5000