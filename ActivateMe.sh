#!/bin/bash

mkdir -p allofthedecks
cd allofthedecks
unzip ../netrunnerdb.zip
cd ..
python deckpairset.py
rm -R allofthedecks
