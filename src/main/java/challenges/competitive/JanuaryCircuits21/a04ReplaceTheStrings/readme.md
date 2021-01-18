Replace the strings
Max. score: 100
You are given two strings  and  that consist of lower case Latin letters and both strings contain single '?'. You need to replace '?' with some lower case Latin letter in both strings not necessarily the same.

After that, you can apply the following operation on  any number of times:

Swap any two adjacent characters.
Your task is to determine if it is possible to make  equal to  if you replace '?' with a lower case Latin letter and apply the mentioned operation on  any number of times.

Input format

The first line contains the number of test cases .
The first line of each test case contains the length of string  that is equal to the length of .
The second line of each test case contains the string .
The third line of each test case contains the string .
Output format

For each test case, print a single line. If possible to make  equal to , then print 'YES' else 'NO' without quotes.

Constraints



The sum of lengths of string in all test cases does not exceed 500000.

Strings  and  contain exactly one '?' and lower case Latin letters.

SAMPLE INPUT 
3
4
abc?
abc?
4
aab?
a?aa
5
aaa?a
bbbb?
SAMPLE OUTPUT 
YES
YES
NO
Explanation
In first sample we can replace '?' in both strings with any character but it must be same.

In second sample we can make S="aaba" and T="abaa" and now we can swap second 'a' and only 'b' in S.

In third sample there is no way to do it.

Time Limit:	2.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned if any testcase passes.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
