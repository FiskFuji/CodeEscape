myQs = {
    11:  {
        "problem" : ["What is the output?",
                    " void main()",
                    "   {",
                    "   int x; ",
                    "   x = float(9 * 1.0 / 2);", 
                    "   cout << x;", 
                    "   }"],
        
        "answer" : "4.5"
        },
 
    12:  {
        "problem" : ["What is the output?",
                    "void main()",
                    "   {", 
                    "   float x = 5, y = 2; ",  
                    "   cout << x % y;", 
                    "   }"],
        "answer:" : "1"
        },
  
   13:  {
        "problem" : ["What is the output?",
                    "class Test",
                    "    {",
                    "     public:",
                    "     int x; ",
                    "     Test() { x = 6; }",
                    "     int getX() {return x;}",
                    "    };",
 
                    "void main()",
                    "{",
                    "   Test t;",
                    "   cout << t.getX();",
                    "}"],
        
        "answer"  : "6"
        },

    
    14 : {
        "problem" : ["What is the output",
                    "int main()",
                    "   {",
                    "   char * ptr;",
                    "   char Str[] = {\"abcdefg\"};",
                    "   ptr = Str;",
                    "   ptr += 5;",
                    "   cout << ptr;",
                    "   return 0;",
                    "   }"],
        
        "answer" :  "fg"
        },

    15: {
        "problem" : ["What is the output?",  
                    "int main()",
                    "   {",     
                    "   int x = 10, y = 20;", 
                    "   int *ptr = &x;",   
                    "   int &ref = y;",    
                    "   *ptr++;",   
                    "   ref++;",     
                    "   cout<< x + y;", 
                    "   return 0;", 
                    "   }"],
        
        "answer" : "31"
        },
   
    16: {
        "problem" : ["What is the output?",
                    "class Point",
                    "    {",
                    "    public:",
                    "     Point() { cout << \"constructor called\"; }",
                    "    };",
                    "void main()",
                    "    {",
                    "    Point *t1;",
                    "    t1 = new Point();",
                    "    }"],
        
        "answer" : "constructor called"
        },

    17: {
        "problem" : ["What is the output?",
                    "class X",
                    "{",
                    "public:",
                    "   int x;",
                    "X(int xx)",
                     "    {",
                     "    x = xx",
                     "    }",
                    "};",
                    "int main()",
                    "    {",
                    "    X a(10);",
                    "    cout << a.x",
                    "    return 0;",
                    "    }"],
        "answers" : "10"
        },

    18: {
        "problem" : ["What is the output?",  
                    "   void MyFunction(int a, int b = 40)",
                    "   {",     
                    "   cout<< a + b << endl; ",
                    "   }", 
                    "int main()",
                    "   {",     
                    "   MyFunction(20, 30);",     
                    "   return 0;",  
                    "   }"],
        "answer" : "50"
        }
    }



