#4. Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []
for tups in lst_tups:
    t_check.append(tups[2])
print(t_check)
#------------------------------------------------------------
#If you remember, the .items() dictionary method produces a sequence of tuples.
#Keeping this in mind, we have provided you a dictionary called pokemon.
#For every key value pair, append the key to the list p_names, and append the value to the list p_number.
#Do not use the .keys() or .values() methods.

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for tup in pokemon.items():
    p_names.append(tup[0])
    #p_names = p_names + [tup[1]]
    p_number.append(tup[1])
    #p_number = p_number + [tup[1]]
print(p_names)
print(p_number)


break
#------------------------------------------------------------
