#!/bin/bash

if [ "$1" = "dev" ]; then
    gradio app.py --demo-name=page
else
    python app.py
fi
