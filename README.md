# DD2480-DECIDE

## Summary

This program is a part of a hypothetical anti-ballistic missile system and inteds to decide if the missile should be launched or not. 

## How to use

### Input Variables

NUMPOINTS - The number of planar data points.

POINTS - Array containing the coordinates of data points.

PARAMETERS - Struct holding parameters for LIC’s.

LCM - Logical Connector Matrix.

PUV - Preliminary Unlocking Vector.

### Output Variables

LAUNCH - Final launch / no launch decision encoded as ”YES”, ”NO” on the standard output.

CMV - Conditions Met Vector.

PUM - Preliminary Unlocking Matrix.

FUV - Final Unlocking Vector.

### Running the code

Run the program in the command line by 

`python DECIDE.py`

Run the tests of the program by 

`python -m unittest`

## Statement of Contributions

The program was written by the group members together, often in meetings involving all or most of the members. Several parts of the startup, such as the code and git structure, was done collectively. The LICs were mainly completed using pair programming and the finishing parts were divided among the members, see below. 

Ali: designed LIC 0-7 in collaboration with Klara, designed the logic and functions necessary to generate the PUM, documented tests. 

Axel: initialized repository and set up continuous integration, designed LIC 0-7 in collaboration with Linus, merged the functions together in DECIDE. 

Klara: created the initial issues, designed LIC 8-14 in collaboration with Ali, documented tests and created the README. 

Linus: created code skeleton, designed LIC 0-7 in collaboration with Axel, designed functions that generate CMV and FUV.

Maegan: missed most of the project due to illness and problems with communication, helped write test for DECIDE function. 

## Authors

Axel Lervik

Klara Alpsten

Linus Below Blomkvist

Maegan Chen Peralta
