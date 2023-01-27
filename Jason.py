import json
dwarf_planets = '''{
    "Ceres": {"Mean distance from the Sun, AU": 2.766, "Mean radius, :E": 0.0742, "Orbital period, years": 4.599, "Moons": 0},
    "Haumea": {"Mean distance from the Sun, AU": 43.335, "Mean radius, :E": 0.13, "Orbital period, years": 283.8, "Moons": 2},
    "Makemake": {"Mean distance from the Sun, AU": 45.792, "Mean radius, :E": 0.11, "Orbital period, years": 306.2, "Moons": 1},
    "Eris": {"Mean distance from the Sun, AU": 67.668, "Mean radius, :E": 0.18, "Orbital period, years": 559, "Moons": 1},
    "Orcus": {"Mean distance from the Sun, AU": 67.668, "Mean radius, :E": 0.0720, "Orbital period, years": 559, "Moons": 1},
    "Salacia": {"Mean distance from the Sun, AU": 67.668, "Mean radius, :E": 0.0664, "Orbital period, years": 559, "Moons": 1},
    "Quaoar": {"Mean distance from the Sun, AU": 67.668, "Mean radius, :E": 0.0870, "Orbital period, years": 559, "Moons": 1},
    "Gonggong": {"Mean distance from the Sun, AU": 67.668, "Mean radius, :E": 0.0982, "Orbital period, years": 559, "Moons": 1},
    "Sedna": {"Mean distance from the Sun, AU": 67.668, "Mean radius, :E": 0.0780, "Orbital period, years": 559, "Moons": 0}
}'''

satellites = '''{
    "Moon": {"Mean radius, :E": 0.272},
    "Io": {"Mean radius, :E": 0.285},
    "Europa": {"Mean radius, :E": 0.246},
    "Ganymede": {"Mean radius, :E": 0.413},
    "Callisto": {"Mean radius, :E": 0.378},
    "Mimas": {"Mean radius, :E": 0.031},
    "Enceladus": {"Mean radius, :E": 0.04},
    "Tethys": {"Mean radius, :E": 0.084},
    "Dione": {"Mean radius, :E": 0.088},
    "Rhea": {"Mean radius, :E": 0.12},
    "Titan": {"Mean radius, :E": 0.404},
    "Iapetus": {"Mean radius, :E": 0.115},
    "Miranda": {"Mean radius, :E": 0.037},
    "Ariel": {"Mean radius, :E": 0.091},
    "Umbriel": {"Mean radius, :E": 0.092},
    "Titania": {"Mean radius, :E": 0.124},
    "Oberon": {"Mean radius, :E": 0.119},
    "Triton": {"Mean radius, :E": 0.212},
    "Charon": {"Mean radius, :E": 0.095}
}'''

planets = {
    "Mercury": {"Mean distance from the Sun, AU": 0.38709893,
                "Equatorial radius, :E": 0.3825,
                "Orbital period, days": 87.969,
                "Moons": 0},
    "Venus":   {"Mean distance from the Sun, AU": 0.72333199,
                "Equatorial radius, :E": 0.9488,
                "Orbital period, days": 224.701,
                "Moons": 0},
    "Earth":   {"Mean distance from the Sun, AU": 1.00000011,
                "Equatorial radius, :E": 1,
                "Orbital period, days": 365.256363,
                "Moons": 1},
    "Mars":    {"Mean distance from the Sun, AU": 1.52366231,
                "Equatorial radius, :E": 0.53260,
                "Orbital period, days": 686.971,
                "Moons": 2},
    "Jupiter": {"Mean distance from the Sun, AU": 5.20336301,
                "Equatorial radius, :E": 11.209,
                "Orbital period, days": 4332.59,
                "Moons": 79},
    "Saturn":  {"Mean distance from the Sun, AU": 9.53707032,
                "Equatorial radius, :E": 9.449,
                "Orbital period, days": 10759.22,
                "Moons": 82},
    "Uranus":  {"Mean distance from the Sun, AU": 19.19126393,
                "Equatorial radius, :E": 4.007,
                "Orbital period, days": 30688.5,
                "Moons": 27},
    "Neptune": {"Mean distance from the Sun, AU": 30.06896348,
                "Equatorial radius, :E": 3.883,
                "Orbital period, days": 60182,
                "Moons": 14},
    "Pluto":   {"Mean distance from the Sun, AU": 39.482,
                "Mean radius, :E": 0.186,
                "Orbital period, years": 247.9,
                "Moons": 5}
}

with open('galaxies.json','r') as file:
    data=json.load(file)
data['galaxies']['milky_way']['solar_system']['planets']=planets
dwarf_planets=json.loads(dwarf_planets)
satellites=json.loads(satellites)
data['galaxies']['milky_way']['solar_system']['dwarf_planets']=dwarf_planets
data['galaxies']['milky_way']['solar_system']['satellites']=satellites
j_data=json.dumps(data, indent=5)
print(j_data)
with open('galaxies2.json','w') as file:
    json.dump(data,file,indent=4)
with open('galaxies2.json','r') as file:
    data=json.load(file)
plt=data['galaxies']['milky_way']['solar_system']['planets']['Pluto']
del(data['galaxies']['milky_way']['solar_system']['planets']['Pluto'])
data['galaxies']['milky_way']['solar_system']['dwarf_planets']['Pluto']=plt
with open('galaxies3.json','w') as file:
    json.dump(data,file,indent=4)