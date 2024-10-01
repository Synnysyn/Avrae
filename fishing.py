!alias fisherman embed <drac2> 
#SETUP
using(A="604b2b28-b437-4779-9a3a-8d71fffa5c77")
ch, fs = character(), randchoice(list(load_yaml(get_gvar("622ff7e6-467e-4ac8-9c56-a192193b5275")).values()))
prefix, suffix = f'-title "{ch.name} idzie na ryby!"', f'-color {color} -footer "{ctx.prefix}{ctx.alias} | made by Synnysyn" -thumb {image}'
dc_l, dc_p, f_name, md, text = fs.find_dc, fs.contest, fs.name, 0, []

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
        A.storage(f_name,ch)
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