:- dynamic(barisPeta/1).
:- dynamic(kolomPeta/1).
:- dynamic(player/2).
house(2,2).
marketplace(7,9).
quest(13,10).
ranch(4,8).

map_size :-
    asserta(barisPeta(15)),asserta(kolomPeta(15)),
    asserta(player(3,2)).

batasAtas(B,_) :- B=:=0.
batasKiri(_,K) :- K=:=0.
batasBawah(B,_):-
    Z is B-1,
    barisPeta(Z),!.
batasKanan(_,K):-
    Z is K-1,
    kolomPeta(Z),!.

printPeta(B,K) :-
    batasBawah(B,K),
    batasKanan(B,K),
    write('#'),nl,!.
printPeta(B,K) :-
    batasKanan(B,K),
    write('#'),nl,!.
printPeta(B,K) :-
    batasAtas(B,K), 
    write('#'),!.
printPeta(B,K) :-
    batasKiri(B,K),
    write('#'),!.
printPeta(B,K) :-
    batasBawah(B,K),
    write('#'),!.

printPeta(B,K) :- player(B,K), write('P'),!.
printPeta(B,K) :- house(B,K),!, write('H'),!.
printPeta(B,K) :- marketplace(B,K),!, write('M'),!.
printPeta(B,K) :- quest(B,K),!, write('Q'),!.
printPeta(B,K) :- ranch(B,K),!, write('R'),!.
printPeta(_,_) :- write('-'),!.
