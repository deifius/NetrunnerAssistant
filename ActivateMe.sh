#!/bin/bash

mkdir -p allofthedecks
cd allofthedecks
unzip ../netrunnerdb.zip
cd ..
python deckpairset.ai.setawareness.py
rm -R allofthedecks
