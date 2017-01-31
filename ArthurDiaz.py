myQs = {
          19:  {
               "problem" : ["Will this function return true or false?",
                             "def sleep_in(weekday, vacation): ",
                             "    if not weekday or vacation: ",
                                   "        return true ",
                                "    else: ",
                                   "        return false",
                             "----- ------ -----",
                             "sleep_in(Tuesday, false)"],
               "answer"  :  "false"
               },

           20:  {
               "problem" : ["What is the output?",
                              "def add_sum(number):",
                              "    if(number % 2 == 0):",
                              "        number = number + 69",
                              "    else:",
                              "        number = number - 13",
                              "    return number",
                              "----- ------ ------",
                              "print(add_sum(14))" ],
               "answer"  :  "83"
               },

           21:  {
               "problem"  :  ["What is the output?",
                                "def string(string):",
                                "    string.replace(\"r\",\"b\")",
                                "    newstr = string.replace(\"e\",\"u\")",
                                "    return newstr",
                                "------ ------ -------",
                                "string(\"redbens\")"],
               "answer"  :  "rudbuns"
               },

           22:  {
               "problem"  :  ["What is the output?",
                                "def string(string):",
                                "    string += \"me\"",
                                "    return string",
                                "------ ------ -------",
                                "string = \"\"",
                                "for x in range(0,4):",
                                "    string = string(string)",
                                "print(string)"],
               "answer"  :  "memememe"
               },

           23:  {
               "problem"  :  ["What is the output?",
                                  "def even_or_odd(num):",
                                  "    for x in range(0,5):",
                                  "        if(num % 2 == 0):",
                                  "            num = num + 3",
                                  "        else:",
                                  "            num = num + 2",
                                  "    if(num % 2 == 0):",
                                  "        print(\"even\")",
                                  "    else:",
                                  "        print(\"odd\")",
                                  "------ ------ -------",
                                  "even_or_odd(11)"],
               "answer"  :  "odd"
                 },
           }
