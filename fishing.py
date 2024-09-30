###
# użycie komendy -> wybranie najwyższego z (survival/perception/investigation/nature) -> wylosowanie ryby i ustalenia DC -> jeżeli zdane, to ryba złapała się na haczyk
# test drugi -> wybranie najwyższego z (athletics/acrobatics/survival) -> rzut ryby vs rzut gracza -> sprawdzenie rezultatów
# jeżeli gracz wygrał, to ryba do torby, jeżeli ryba wygrała, to dalej na haczyku, jeżeli ryba wygrała znacząco to się zrywa i trzeba szukać na nowo
# całość w jednym chain, jeżeli skończy się liczba prób dziennie to ryba odpływa
###

!test <drac2> 
ch = character()

def fishing_locate(ch):
    skills = {
        'survival': ch.skills.survival.value,
        'perception': ch.skills.perception.value,
        'investigation': ch.skills.investigation.value,
        'nature': ch.skills.nature.value
    }
    chosen_skill = [skill for skill, value in skills.items() if value == max(skills.values())][0]
    rolled = vroll(ch.skills[chosen_skill].d20())
    return rolled, chosen_skill

rolled, chosen_skill = fishing_locate(ch)

return f"{rolled.result} | {rolled.total} | {chosen_skill}" 
</drac2>

#!test <drac2> return f"{vroll(character().skills['acrobatics'].d20())}" </drac2>


h1=max(get_raw().skills.survival,get_raw().skills.survival,get('dexterityMod'),get('intelligenceMod'),get('strengthMod'),get('wisdomMod'))

_A='downtimePoints'
character().set_cvar_nx(_A,0)
points=int(downtimePoints)
gold=0
base_gp=int(AAA[0])
value=0
if base_gp >= 50:
    value = -(-base_gp // 500)
total=0
if points<value:text="doesn't have enough downtime.";description=f"You need at least {value} DT to complete this task. Current DT: ({points})";return
if character().coinpurse.get_coins()['gp']<base_gp:text="doesn't have enough GP.";description=f"You need at least {base_gp} GP to complete this task. \nCurrent GP: ({character().coinpurse.get_coins()['gp']})";return
points-=value
character().set_cvar(_A,points)
highest=max(get('charismaMod'),get('constitutionMod'),get('dexterityMod'),get('intelligenceMod'),get('strengthMod'),get('wisdomMod'))
expert=''
if len(AAA)==2:
    total+=int(AAA[1])
    if total==2:expert=' with expertise'
    if total==1:expert=' with proficiency'
c_roll=randint(1, 20)
total+=c_roll+highest
if total<=5:gold=.9
if 6<=total<=11:gold=.8
if 12<=total<=17:gold=.7
if 18<=total<=23:gold=.6
if 24<=total:gold=.5

wynik = int(base_gp * gold)
c_coins = character().coinpurse.modify_coins(gp=-1*wynik)
text = f'spends downtime ({value} DT) crafting an item{expert}, which costs:'
description=f'**{wynik } GP** (Rolled {c_roll}), now has {character().coinpurse.get_coins()["gp"]} GP'
