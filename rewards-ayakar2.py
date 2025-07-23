'''
Serwus, sprawa będzie prostsza, bo będziemy procentami przeliczać wyłącznie XP, podrzucam wartości 100% (bazowe).

Pył - 700 XP
Iskra - 1300 XP
Rozbłysk - 2200 XP
Zenit - 2400 XP

Punktacja 1-12, gdzie 1 pkt = 10%, maksymalnie można uzyskać 120% nagrody

!wycena ranga punkty
!wycena zloto 8

Jakbys mogl udostepnic nam tez kod, to sobie potem zaktualizujemy nazwy rang ❤️
'''

!alias quest embed <drac2>
syntax=f'{ctx.prefix}{ctx.alias}'
_A='questTotal'
character().set_cvar_nx(_A,0)
AAA=&ARGS&
quest_total=int(questTotal)

if len(AAA)<2:text='sprawdza swój dziennik.';description=f"Misje ukończone: {quest_total}";return

rnk_input=lower(AAA[0])
suc_input=(AAA[1])
lvl_input=get('level')

current_xp=int(xp)+xp_reward
quest_total+=1
character().set_cvar(_A,quest_total)
character().set_cvar('xp','+'+str(current_xp))

if difficulty_input not in valid_rank:text='zapomniał co ma zrobić.';description=f"M: [lunar / solar / lost]";return
level_input=get('level')
max_xp,xp_reward,gold=calculate_experience_and_bonus(level_input,difficulty_input)
if difficulty_input=='lost':gold=0
current_xp=int(xp)+xp_reward
quest_total+=1
character().set_cvar('xp','+'+str(current_xp))
character().coinpurse.modify_coins(gp=gold)
character().set_cvar(_A,quest_total)
text=f"Completed another quest ({questTotal} total)"
description=f"Gained {xp_reward} XP and is missing {max_xp-current_xp} XP till next level.\nGuild payed him {gold} GP."
</drac2>
-color {{color}} 
-thumb {{image}}
-title "{{character().name}} {{text}}"
-desc "{{description}}"
-footer "{syntax} [ranga] [1-12] | Made by Synnysyn"