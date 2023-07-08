import sys
input = sys.stdin.readline

S = input().rstrip()

stroke = {
    "fdsajkl;" : "in-out",
    "jkl;fdsa" : "in-out",
    "asdf;lkj" : "out-in",
    ";lkjasdf" : "out-in",
    "asdfjkl;" : "stairs",
    ";lkjfdsa" : "reverse"
}

if S not in stroke:
    print("molu")
else:
    print(stroke[S])