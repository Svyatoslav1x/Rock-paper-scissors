from colorama import init
from colorama import Fore, Back, Style

# Attachments section
label = """ __  __     ______     __  __     ______     ______     __  __     ______     __  __     __    
/\ \/ /    /\  __ \   /\ \/ /    /\  ___\   /\  ___\   /\ \/\ \   /\  == \   /\ \/\ \   /\ \   
\ \  _"-.  \ \  __ \  \ \  _"-.  \ \  __\   \ \ \__ \  \ \ \_\ \  \ \  __<   \ \ \_\ \  \ \ \  
 \ \_\ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ 
  \/_/\/_/   \/_/\/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/   \/_____/   \/_/ 
--The Rock-Paper-Scissors game--"""
paper = [[';$$$$$$$$$$$$$$$$$$$$$$$$$$$;'],
         [';X            $:;          ;X'],
         [';X      .x+  .  X.         ;X'],
         [';X      ;  X .  X   ; .;   ;X'],
         [';  :;:  +  ; .  X  .+ .;   ;X'],
         [';  X :: +  ; +  X  ;  :    ;X'],
         [';  X  ; ;. + .  X :; .+    ;X'],
         [';  ;  :;;  : .  X +  +     ;X'],
         [';  .X  +:: ; .  +:; ;:     ;X'],
         [';   ;.  +           x  .;;  X'],
         [';X   +              . +: ;  X'],
         [';X   ;:           x:;. ;:   X'],
         [';X   X          .     :.   ;X'],
         [';X   X         :     ::    ;X'],
         [';X    ;.             ;     ;X'],
         [';X     .+:.;++;;++++.      ;X'],
         [';$$$$$$$$$$$$$$$$$$$$$$$$$$$;']]
scissors = [[';$$$$$$$$$$$$$$$$$$$$$$$$$$$;'],
            [';X         .+.+:           X:'],
            [';X         ;   ;.  .+ .+   X:'],
            [';X         +   .;  ;   +.  X:'],
            [';X         +.   +  X   ;.  X:'],
            [';X          ;   + .+   x   X:'],
            [';X          ;:  ; ::   X   X:'],
            [';X      :;XX++  :;:    ;   X:'],
            [';   .;.;    :. .::.   .:   X:'],
            [';  ::  X  +:::      ::X.   X:'],
            [';  ;.   ;  +::..:;+    ;:  X:'],
            [';  .x;. .;:   ;:+       ;  X:'],
            [';   + .;+.;;++::;      .;  X:'],
            [';X  :.          ;.     x   X:'],
            [';X  .+               .+    X:'],
            [';X    .++:.;++;;+++++.     X:'],
            [';$$$$$$$$$$$$$$$$$$$$$$$$$$$;']]
rock = [[';$$$$$$$$$$$$$$$$$$$$$$$$$$$;'],
        [';X                         X:'],
        [';X                         X:'],
        [';X          :X;:X:xX+.     X:'],
        [';X      +: X.    X    X.   X:'],
        [';     :.   ;.    +Xx+ ..   X:'],
        [';  x   .    x+:.      ;;   X:'],
        ['; ;    $   .;           +:  :'],
        ['; ;     ;   .x:    :+    :; :'],
        [';  +    ::   :; +         + :'],
        [';  .x+ ;:.:  ;;+         ;: :'],
        [';X  X          :        ::  :'],
        [';X  ::                 ;:  X:'],
        [';X   ;.               ;.   X:'],
        [';X    .X   ;+:   .;xX+     X:'],
        [';X                         X:'],
        [';$$$$$$$$$$$$$$$$$$$$$$$$$$$;']]


def main():
    '''
    Основная функция программы.

    label -- название игры
    paper -- карточка с бумагой
    scissors -- карточка с ножницами
    rock -- карточка с камнем
    '''

    print(label)  # Приветствуем игрока
    while True:  # Основной цикл игры
        pass


if __name__ == "__main__":
    main()