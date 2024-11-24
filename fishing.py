!alias fisherman embed <drac2> 
using(A="604b2b28-b437-4779-9a3a-8d71fffa5c77")
ch, fs = character(), randchoice(list(load_yaml(get_gvar("622ff7e6-467e-4ac8-9c56-a192193b5275")).values()))
suffix = f'-color {color} -footer "{ctx.prefix}{ctx.alias} | made by Synnysyn" -thumb {image}'
dc_l, dc_p, f_name, md, text = fs.find_dc, fs.contest, fs.name, 0, []

ch.set_cvar_nx("fishingTime", 0)
ch.set_cvar_nx("fishingUS", 0)
usage_today = int(ch.get_cvar("fishingUS", 0))
curr_time = (time() - 1711332000) // 86400
last_time = float(ch.get_cvar("fishingTime", 0))

if curr_time > last_time: 
    usage_today = 0
ch.set_cvar("fishingTime", curr_time)

if usage_today >= 5: 
    return f'embed -title "{ch.name} zamierzał iść na ryby... [{usage_today}/5]" -desc "Nie przemęczaj się, spróbuj jutro!" {suffix}'

ch.set_cvar("fishingUS", usage_today+1)
prefix = f'-title "{ch.name} idzie na ryby! [{usage_today+1}/5]"'

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

"""

!alias fisherman embed <drac2> 
M='\n'
L='fishingUS'
K='fishingTime'
using(A='604b2b28-b437-4779-9a3a-8d71fffa5c77')
B,G=character(),randchoice(list(load_yaml(get_gvar('622ff7e6-467e-4ac8-9c56-a192193b5275')).values()))
F=f'-color {color} -footer "{ctx.prefix}{ctx.alias} | made by Synnysyn" -thumb {image}'
N,S,O,P,C=G.find_dc,G.contest,G.name,0,[]
B.set_cvar_nx(K,0)
B.set_cvar_nx(L,0)
D=int(B.get_cvar(L,0))
Q=(time()-1711332000)//86400
T=float(B.get_cvar(K,0))
if Q>T:D=0
B.set_cvar(K,Q)
if D>=5:return f'embed -title "{B.name} zamierzał iść na ryby... [{D}/5]" -desc "Nie przemęczaj się, spróbuj jutro!" {F}'
B.set_cvar(L,D+1)
H=f'-title "{B.name} idzie na ryby! [{D+1}/5]"'
R,U=A.fishing_locate(B)
C.append(f"Rozglądasz się za dobrym miejscem...\nDC {N}\n{U.capitalize()}: {R.result}")
if R.total>=N:C.append(':green_circle: **Miejsce jest dobre, coś złapało się haczyka!**')
else:C.append(':x: **Spławik ani drgnie, musisz zmienić miejsce.**');E=M.join(C);return f'embed {H} -desc "{E}" {F}'
while True:
	I=int(roll(S))+P;J,V=A.fishing_pull(B);C.append(f"\nSiłujesz się z rybą...\nDC {I}\n{V.capitalize()}: {J.result}")
	if J.total>=I:A.storage(O,B);C.append(f":green_circle: **Wyławiasz coś z wody...**\n\n**{O}** ląduje prosto do twojej torby!");break
	elif J.total+10>=I:C.append(':orange_circle: **Ryba nie daje za wygraną!**');P+=5
	else:C.append(':x: **Ryba zerwała się z haczyka!**');E=M.join(C);return f'embed {H} -desc "{E}" {F}'
E=M.join(C)
return f'embed {H} -desc "{E}" {F}'
</drac2>

"""