:- dynamic(player/2).
:- dynamic(inGame/0).

:- include('map.pl').

start :-
    inGame,
    write('Kamu sudah berada dalam permainan'),!.
start :-
    write('Welcome to Harvest Star. Choose Your Job'),nl,
    write('1. Fisherman'),nl,
    write('2. Farmer'),nl,
    write('3. Rancher'),nl,
    asserta(inGame),
    write('>'),
    read(Job),   /*Belum ngapa-ngapain ini*/
    write('You Choose ..., Now Start ...').

map :-
    \+(inGame),
    write('Kamu belum memasuki Permainan, silahkan start terlebih dahulu'),!.
map :-
    BMin is 0, KMin is 0,
    /*kolomPeta(K),
    K1 is K+1,
    barisPeta(B),
    B1 is B+1,*/
    forall(between(BMin,16,I),(
        nl, forall(between(KMin,16,J),(
            printPeta(I,J)
        ))
    )), nl,
    write('Keterangan Simbol : '), nl,
    write('P : Player'),nl,
    write('M : Marketplace'),nl,
    write('R : Ranch'),nl,
    write('H : House'),nl,
    write('Q : Quest Place'),nl,
    write('o : Water'),nl,
    write('= : Digged Tile'),nl,
    !.
