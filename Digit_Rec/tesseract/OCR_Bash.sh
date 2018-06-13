#!/bin/bash

echo "-----------------------"
echo "     VERSION:"
echo "-----------------------"
tesseract --version
echo "-----------------------"
tesseract example_05.png stdout
