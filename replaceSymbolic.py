try:
    from json import load
except (Exception, OSError, RuntimeError, ImportError, ValueError, IOError, IndexError, OverflowError, TypeError, ArithmeticError) as ex:
        print(ex)# If some error or exception raised then print it to screen so that I can see. 
        #If I do not do it, then when an error occurs, the command line closes immmediately.

while True:
    try:
        print("#"*75)
        with open("replaceThose.json", "r", encoding="utf-8") as fil:
            replacedict = load(fil)
        myStr = input("Paste the symbolic expression. Press CTRL C to exit.\n--> ")
        myStr = myStr.replace("sym('", "").replace("')", "").replace("*", ".*").replace("/", "./").replace("^", ".^").replace("sym(1i)", "j") # make operations element-wise, and use j as imaginary unit 
        for key in replacedict:
            myStr = myStr.replace(key, replacedict[key])
        if "sym(" in myStr:
            strArr = myStr.split("sym(")

            for i, substring in enumerate(strArr):
                if i == 0: # pass the first index
                    continue
                index = substring.find(")") # returns the index of first match of '(' char, if there is no '(' the it returns -1
                if index == -1:
                    pass # if there is no '(' continue to this iteration. the keyword 'continue' skips this iteration, but 'pass' not.
                else:
                    substring = substring[:index] + substring[(index + 1):]
                    strArr[i] = substring
                    
            myStr = "".join(strArr)
        print("-"*50)
        print("Output: \n" + myStr)
    except KeyboardInterrupt:
        break
    except (Exception, OSError, RuntimeError, ImportError, ValueError, IOError, IndexError, OverflowError, TypeError, ArithmeticError) as ex:
        print(ex) # If some error or exception raised then print it to screen so that I can see. 
        #If I do not do it, then when an error occurs, the command line closes immmediately.
