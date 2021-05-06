Generating Python code
Max. score: 100
You're given a string , you should generate a python code which its output is .
Your score for each test will be:

Notes:

 is the length of .
Your generated python code cannot use import. the code should use built-in python syntax(check this list).
You will get the wrong answer if your generated python code gets any exceptions or errors.
Your generated python code's output must be  plus an end of the line. (Refer to the example)
You can find tests here. Their order is not the same as a judge.
Your generated python code should terminate after at most seconds otherwise, you will get the wrong answer.
Input format

The first line contains an integer .
The second line contains a string with length ,  which contains 'a'-'z', '#', '.', and '0'-'9' characters.
Output format

Firstly, print the number of your generated python code's lines and then print each code's line.

Constraints


SAMPLE INPUT 
6
allall
SAMPLE OUTPUT 
1
print("all"*2)
Explanation
The python code's output is .

Time Limit:	7.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned when all the testcases pass.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
