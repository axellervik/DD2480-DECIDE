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

Run the code in the command line by 

`python DECIDE.py`

Run the tests of the program by 

`python -m unittest`

## Statement of Contributions

The program was written by the group members together, often in meetings involving all the members. Several parts of the startup, such as the code and git structure, was done collectively by all members together. The LICs were mainly completed using pair programming, Linus and Axel did LIC0-7 and Klara and Ali did LIC8-14. The finishing parts were divided among the members. 

## Authors

Klara Alpsten