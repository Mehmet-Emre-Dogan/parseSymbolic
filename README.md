# replaceSymbolic
Converts MATLAB symbolic output to the form easy to use with MATLAB functions.
# Usage
Edit the replaceThose.json so that it become { "old": "new" }. Then copy your symbolic output from MATLAB and paste to the commant line. Hit enter: Done!
# Purpose
This is pretty helpful when iterations are needed over the symbolic solution since numeric substitutions of symbolic expressions in loops takes too much time. Using this code, you can generate function templates easily, and needless to say, array functions in MATLAB runs way more fast compared to numeric substitutions over symbolic expressions in loops.
