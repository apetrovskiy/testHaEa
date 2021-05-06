The GCD function
Max. score: 100
You are given an integer  and there is a function . Here, GCD denotes the greatest common divisor. You are required to select an integer value  that is greater than or equal to 1. 

Your task is to determine the following:

The maximum possible value of  that you can get 
The minimum  for which maximum value will be achieved
Input format

The first line contains an integer  denoting the number of test cases.
Next  lines contain a single integer .
Output format

Print  lines. For each test case:

Print a single line containing two integers, the maximum value of  and the minimum value of  for which  is maximized.
Constraints



SAMPLE INPUT 
1
3
SAMPLE OUTPUT 
6 6
Explanation
N is 3 so F(3)=GCD(1,x)+GCD(2,x)+GCD(x,3)

If we choose x=6 we will get F(3)=GCD(1,6)+GCD(2,6)+GCD(3,6)=6.

There is no smaller value than X=6 for which F(3)=6. Also no other value of X we can get a greater value of F(3).

 

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned if any testcase passes.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
