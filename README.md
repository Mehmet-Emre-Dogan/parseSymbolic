# replaceSymbolic
Converts MATLAB symbolic output to the form easy to use with MATLAB functions.
# Usage
Edit the replaceThose.json so that it become { "old": "new" }. Then copy your symbolic output from MATLAB and paste it to the command line. Hit enter: Done!
# Purpose
This is helpful when iterations are needed over the symbolic solution since numeric substitutions of symbolic expressions in loops take too much time. Using this code, you can quickly generate function templates, and array functions in MATLAB run way faster than numeric substitutions over symbolic expressions in loops.
