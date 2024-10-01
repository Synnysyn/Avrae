###
# użycie komendy -> wybranie najwyższego z (survival/perception/investigation/nature) -> wylosowanie ryby i ustalenia DC -> jeżeli zdane, to ryba złapała się na haczyk
# test drugi -> wybranie najwyższego z (athletics/acrobatics/survival) -> rzut ryby vs rzut gracza -> sprawdzenie rezultatów
# jeżeli gracz wygrał, to ryba do torby, jeżeli ryba wygrała, to dalej na haczyku, jeżeli ryba wygrała znacząco to się zrywa i trzeba szukać na nowo
# całość w jednym chain, jeżeli skończy się liczba prób dziennie to ryba odpływa
###

!alias fisherman embed <drac2> 
#SETUP
using(A="604b2b28-b437-4779-9a3a-8d71fffa5c77")
ch=character()
prefix=f'-title "{ch.name} idzie na ryby!"'
suffix=f'-color {color} -footer "{ctx.prefix}{ctx.alias} | made by Synnysyn" -thumb {image}'
dc_l=15
dc_p="2d20kh1+2"
f_name="Okoń"
md=0
text=[]
#SZUKANIE RYBY
rd, cs = A.fishing_locate(ch)
text.append(f"Rozglądasz się za dobrym miejscem...\nDC {dc_l}\n{cs.capitalize()}: {rd.result}")
if rd.total >= dc_l:
    text.append(":green_circle: **Miejsce jest dobre, coś złapało się haczyka!**")
else:
    text.append(":x: **Spławik ani drgnie, musisz zmienić miejsce.**")
    jtext = "\n".join(text)
    return f'embed {prefix} -desc "{jtext}" {suffix}'
while True:
    dc_f=int(roll(dc_p))+md
    rd2, cs2 = A.fishing_pull(ch)
    text.append(f"\nSiłujesz się z rybą...\nDC {dc_f}\n{cs2.capitalize()}: {rd2.result}")
    if rd2.total >= dc_f:
        text.append(f":green_circle: **Wyławiasz coś z wody...**\n\n**{f_name}** ląduje prosto do twojej torby!")
        break
    elif (rd2.total + 10) >= dc_f:
        text.append(":orange_circle: **Ryba nie daje za wygraną!**")
        md+=5
    else:
        text.append(":x: **Ryba zerwała się z haczyka!**")
        jtext = "\n".join(text)
        return f'embed {prefix} -desc "{jtext}" {suffix}'

jtext = "\n".join(text)
return f'embed {prefix} -desc "{jtext}" {suffix}'
</drac2>

""" bag_name = 'Fish'
				bag = load_json(get('bags', []))
				for bag_cat in bag:
					if bag_name.lower() in bag_cat[0].lower():
						bag_name = bag_cat[0]
						bag_loot_count = bag_cat[1][deposit] if deposit in list(bag_cat[1].keys()) else 0
						bag_cat[1][deposit] = bag_cat[1][deposit] + harvest if bag_loot_count > 0 else harvest
						loot_added = True
						break
				if not loot_added:
					bag.append([bag_name, {deposit: harvest}])
				c.set_cvar('bags', dump_json(bag)) """