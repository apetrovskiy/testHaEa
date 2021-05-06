A chessboard
Max. score: 100
In this version of chess, only two kings pieces are placed on the chessboard. Initially, the coordinates of the first king piece are generated , it is placed on the chessboard at the generated position. Now, the coordinates of the second king piece are generated , it is placed on the chessboard at the generated position.

These pieces can be moved in a sequential manner, that is, one by one, starting from the first piece. Both the kings want to win if they can not, at least draw.

Rules

The chessboard is a standard  board.
The kings can move from one cell to another if they have an edge or corner in common.
If the generated coordinates of the second king are exactly equal to the first, then the second king wins.
Both players play optimally.
The game is considered to be won by the first king piece if after it moves, then it can have the same coordinates as the second. The second king piece becomes the winner if after this piece is moved, then both kings have the same coordinates. The game is drawn if there is no possible ways for anyone to win if both the pieces are played optimally.
Input format

The first line contains  denoting the number of test cases.
The first line of each test case contains two space-separated integers denoting the row and column of the first king .
The second line of each test case contains two space-separated integers denoting the row and column of the second king .
Output format

Print  lines. For each test case:

In a single line, print 'FIRST' if the first king piece wins, print 'SECOND' if the second king piece wins, and print 'DRAW' if none of them wins.
Constraints



SAMPLE INPUT 
2
1 1
2 2
1 3
8 8
SAMPLE OUTPUT 
FIRST
DRAW
Explanation
In first case, first king can make an diagnol move and capture second king.

In second case if both play optimally no one can win.

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned if any testcase passes.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
