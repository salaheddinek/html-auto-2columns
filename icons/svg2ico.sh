#!/bin/bash
convert -density 256x256 -background transparent $1 -define icon:auto-resize -colors 256 $1.ico 
