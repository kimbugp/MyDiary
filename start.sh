#!/bin/bash
echo "<<<<<<<<<<<<<<<<<<<< update database >>>>>>>>>>>>>>>>>>>>>>>>"
flask migrate && flask seed
sleep 2

echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
gunicorn run:app -b 0.0.0.0:5000