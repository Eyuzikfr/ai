% 5 Facts
male(john).
male(david).
female(mary).
female(susan).
parent(john, susan).
parent(mary, susan).
parent(john, david).
parent(mary, david).
parent(susan, lily).

% Rules
% 1. X is the father of Y if male and parent of Y
father(X, Y) :- male(X), parent(X, Y).

% 2. X is the mother of Y if X is female and parent of Y
mother(X, Y) :- female(X), parent(X, Y).

% 3. X is the child of Y if Y is parent of X
child(X, Y) :- parent(Y, X).

% 4. X and Y are siblings if they share at least one parent
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X\= Y.

% 5. X is the grandparent of Y if X is parent of Z and Z is parent of Y
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
