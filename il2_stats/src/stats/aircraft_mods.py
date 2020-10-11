import functools

from django.utils.translation import pgettext_lazy


@functools.lru_cache(maxsize=1024)
def get_aircraft_mods(aircraft, id_list):
    mods = []
    for id in id_list:
        try:
            mod = aircraft_mods[aircraft][id]
            mods.append(mod)
        except KeyError:
            pass
    return mods


aircraft_mods = {
    'a-20b': {
        1: pgettext_lazy('aircraft_mod', '20 x FAB-100M bombs'),
        2: pgettext_lazy('aircraft_mod', '4 x FAB-250tsk bombs'),
        3: pgettext_lazy('aircraft_mod', 'Bendix MN-26'),
    },
    'albatros d.va': {
        1: pgettext_lazy('aircraft_mod', 'Collimator Day'),
        2: pgettext_lazy('aircraft_mod', 'Collimator Night'),
        3: pgettext_lazy('aircraft_mod', 'Gunsight'),
        4: pgettext_lazy('aircraft_mod', 'Anemometer, Altimeter, Clock'),
        5: pgettext_lazy('aircraft_mod', 'Inclinometer'),
        6: pgettext_lazy('aircraft_mod', 'Bullet Counters'),
        7: pgettext_lazy('aircraft_mod', 'Thermometer'),
        8: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        9: pgettext_lazy('aircraft_mod', 'Lewis Overwing'),
    },
    'bf 109 e-7': {
        1: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        2: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        3: pgettext_lazy('aircraft_mod', 'Armoured Wind Screen'),
        4: pgettext_lazy('aircraft_mod', 'Removed Headrest'),
        5: pgettext_lazy('aircraft_mod', 'Additional armour plates'),
    },
    'bf 109 f-2': {
        1: pgettext_lazy('aircraft_mod', '20mm MG 151/20 gun'),
        2: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        4: pgettext_lazy('aircraft_mod', 'Armoured Wind Screen'),
        5: pgettext_lazy('aircraft_mod', 'Removed Headrest'),
    },
    'bf 109 f-4': {
        1: pgettext_lazy('aircraft_mod', '2 x 15mm MG 151/15 gun pods'),
        2: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        4: pgettext_lazy('aircraft_mod', 'Armoured Wind Screen'),
        5: pgettext_lazy('aircraft_mod', 'Removed Headrest'),
        6: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
    },
    'bf 109 g-14': {
        1: pgettext_lazy('aircraft_mod', '30mm MK 108 gun'),
        2: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
        3: pgettext_lazy('aircraft_mod', '4 x SD 70 bombs'),
        4: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        5: pgettext_lazy('aircraft_mod', '21 cm BR'),
        6: pgettext_lazy('aircraft_mod', 'FuG-16ZY'),
    },
    'bf 109 g-2': {
        1: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
        2: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        4: pgettext_lazy('aircraft_mod', 'Armoured Glass Head Rest'),
        5: pgettext_lazy('aircraft_mod', 'Removed Headrest'),
    },
    'bf 109 g-4': {
        1: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
        2: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        4: pgettext_lazy('aircraft_mod', 'Armoured Glass Head Rest'),
        5: pgettext_lazy('aircraft_mod', 'Removed Headrest'),
    },
    'bf 109 g-6': {
        1: pgettext_lazy('aircraft_mod', '30mm MK 108 gun'),
        2: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
        3: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        4: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        5: pgettext_lazy('aircraft_mod', 'Armoured Glass Head Rest'),
        6: pgettext_lazy('aircraft_mod', 'Removed Headrest'),
        7: pgettext_lazy('aircraft_mod', 'Peilrahmen PR 16'),
    },
    'bf 109 k-4': {
        1: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
        2: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 500 bomb'),
        4: pgettext_lazy('aircraft_mod', 'DB 605 DC engine'),
    },
    'bf 110 e-2': {
        1: pgettext_lazy('aircraft_mod', 'Armoured Windscreen and pilot\'s Headrest'),
        2: pgettext_lazy('aircraft_mod', 'Additional armour plates'),
        3: pgettext_lazy('aircraft_mod', '12 x SC 50 bombs'),
        4: pgettext_lazy('aircraft_mod', '2 x SC 500 bomb'),
        5: pgettext_lazy('aircraft_mod', 'SC 1000 heavy bomb'),
    },
    'bf 110 g-2': {
        1: pgettext_lazy('aircraft_mod', 'Removed Headrest'),
        2: pgettext_lazy('aircraft_mod', '12 x SC 50 bombs'),
        3: pgettext_lazy('aircraft_mod', '2 x SC 500 bomb'),
        4: pgettext_lazy('aircraft_mod', 'SC 1000 heavy bomb'),
        5: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pod'),
        6: pgettext_lazy('aircraft_mod', '37mm 3.7cm BK gun pod'),
    },
    'bristol f2b (f.ii)': {
        1: pgettext_lazy('aircraft_mod', 'Twin Lewis Overwing'),
        2: pgettext_lazy('aircraft_mod', 'Twin Lewis MG turret'),
        3: pgettext_lazy('aircraft_mod', 'Aldis'),
        4: pgettext_lazy('aircraft_mod', 'Fuel Gauge'),
        5: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        6: pgettext_lazy('aircraft_mod', 'Cooper / H.E.R.L. bombs'),
        7: pgettext_lazy('aircraft_mod', 'Camera'),
        8: pgettext_lazy('aircraft_mod', 'Radio'),
    },
    'bristol f2b (f.iii)': {
        1: pgettext_lazy('aircraft_mod', 'Twin Lewis Overwing'),
        2: pgettext_lazy('aircraft_mod', 'Twin Lewis MG turret'),
        3: pgettext_lazy('aircraft_mod', 'Aldis'),
        4: pgettext_lazy('aircraft_mod', 'Fuel Gauge'),
        5: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        6: pgettext_lazy('aircraft_mod', 'Cooper / H.E.R.L. bombs'),
        7: pgettext_lazy('aircraft_mod', 'Camera'),
        8: pgettext_lazy('aircraft_mod', 'Radio'),
    },
    'fokker d.vii': {
        1: pgettext_lazy('aircraft_mod', 'Collimator Day'),
        2: pgettext_lazy('aircraft_mod', 'Collimator Night'),
        3: pgettext_lazy('aircraft_mod', 'Gunsight'),
        4: pgettext_lazy('aircraft_mod', 'Anemometer'),
        5: pgettext_lazy('aircraft_mod', 'High Altimeter'),
        6: pgettext_lazy('aircraft_mod', 'Bullet counters'),
        7: pgettext_lazy('aircraft_mod', 'Thermometer'),
        8: pgettext_lazy('aircraft_mod', 'Cockpit light'),
    },
    'fokker d.viif': {
        1: pgettext_lazy('aircraft_mod', 'Collimator Day'),
        2: pgettext_lazy('aircraft_mod', 'Collimator Night'),
        3: pgettext_lazy('aircraft_mod', 'Gunsight'),
        4: pgettext_lazy('aircraft_mod', 'Anemometer'),
        5: pgettext_lazy('aircraft_mod', 'High Altimeter'),
        6: pgettext_lazy('aircraft_mod', 'Thermometer'),
        7: pgettext_lazy('aircraft_mod', 'Cockpit light'),
    },
    'fokker dr.i': {
        1: pgettext_lazy('aircraft_mod', 'Collimator Day'),
        2: pgettext_lazy('aircraft_mod', 'Collimator Night'),
        3: pgettext_lazy('aircraft_mod', 'Gunsight'),
        4: pgettext_lazy('aircraft_mod', 'Inclinometer'),
        5: pgettext_lazy('aircraft_mod', 'Bullet Counters'),
        6: pgettext_lazy('aircraft_mod', 'Cockpit light'),
    },
    'fw 190 a-3': {
        1: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        2: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 500 bomb'),
        4: pgettext_lazy('aircraft_mod', '2 x 20mm MG FF/M (120 rounds)'),
        5: pgettext_lazy('aircraft_mod', '2 x 20mm MG FF/M (180 rounds)'),
    },
    'fw 190 a-5': {
        1: pgettext_lazy('aircraft_mod', '4 x SC 50 bombs'),
        2: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 500 bomb'),
        4: pgettext_lazy('aircraft_mod', '2 x 20mm MG FF/M (180 rounds)'),
        5: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
        6: pgettext_lazy('aircraft_mod', 'U17 strike modification'),
    },
    'fw 190 a-8': {
        1: pgettext_lazy('aircraft_mod', '30mm MK 108 guns'),
        2: pgettext_lazy('aircraft_mod', 'ETC 501 Central Bombholder'),
        3: pgettext_lazy('aircraft_mod', '21 cm BR'),
        4: pgettext_lazy('aircraft_mod', 'Sturmjäger'),
        5: pgettext_lazy('aircraft_mod', 'Fw 190 F-8 / G-8'),
        6: pgettext_lazy('aircraft_mod', 'Removal of MG 131'),
    },
    'fw 190 d-9': {
        1: pgettext_lazy('aircraft_mod', '4 x SD 70 bombs'),
        2: pgettext_lazy('aircraft_mod', '1 x SC 250 bomb'),
        3: pgettext_lazy('aircraft_mod', '1 x SC 500 bomb'),
        4: pgettext_lazy('aircraft_mod', '21 cm BR'),
        5: pgettext_lazy('aircraft_mod', '26 x R4M rockets'),
        6: pgettext_lazy('aircraft_mod', 'Gyro Gunsight'),
        7: pgettext_lazy('aircraft_mod', 'Bubble Canopy'),
    },
    'halberstadt cl.ii': {
        1: pgettext_lazy('aircraft_mod', 'Twin Spandau MG'),
        2: pgettext_lazy('aircraft_mod', 'Twin Parabellum MG Turret'),
        3: pgettext_lazy('aircraft_mod', '20mm Becker Turret'),
        4: pgettext_lazy('aircraft_mod', 'Aldis (Trophy)'),
        5: pgettext_lazy('aircraft_mod', 'Additional Gauges'),
        6: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        7: pgettext_lazy('aircraft_mod', 'P.u.W. Bombs'),
        8: pgettext_lazy('aircraft_mod', 'Camera'),
        9: pgettext_lazy('aircraft_mod', 'Radio'),
    },
    'halberstadt cl.ii 200hp': {
        1: pgettext_lazy('aircraft_mod', 'Twin Spandau MG'),
        2: pgettext_lazy('aircraft_mod', 'Twin Parabellum MG Turret'),
        3: pgettext_lazy('aircraft_mod', '20mm Becker Turret'),
        4: pgettext_lazy('aircraft_mod', 'Aldis (Trophy)'),
        5: pgettext_lazy('aircraft_mod', 'Additional Gauges'),
        6: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        7: pgettext_lazy('aircraft_mod', 'P.u.W. Bombs'),
        8: pgettext_lazy('aircraft_mod', 'Camera'),
        9: pgettext_lazy('aircraft_mod', 'Radio'),
    },
    'he 111 h-16': {
        1: pgettext_lazy('aircraft_mod', '2 x SC 1000 heavy bombs'),
        2: pgettext_lazy('aircraft_mod', '2 x SC 1800 heavy bombs'),
        3: pgettext_lazy('aircraft_mod', 'SC 2500 heavy bomb'),
    },
    'he 111 h-6': {
        1: pgettext_lazy('aircraft_mod', 'Belly 20mm gun turret'),
        2: pgettext_lazy('aircraft_mod', 'Nose 20mm gun turret'),
        3: pgettext_lazy('aircraft_mod', '2 x SC 1000 heavy bombs'),
        4: pgettext_lazy('aircraft_mod', '2 x SC 1800 heavy bombs'),
        5: pgettext_lazy('aircraft_mod', 'SC 2500 heavy bomb'),
    },
    'hs 129 b-2': {
        1: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun'),
        2: pgettext_lazy('aircraft_mod', '4 x 7.92mm MG 17 gun pod'),
        3: pgettext_lazy('aircraft_mod', '30mm MK 101'),
        4: pgettext_lazy('aircraft_mod', '30mm MK 103'),
        5: pgettext_lazy('aircraft_mod', 'Peilrahmen PR 16'),
        6: pgettext_lazy('aircraft_mod', 'Mirror'),
    },
    'i-16 type 24': {
        1: pgettext_lazy('aircraft_mod', '4 x ROS-82 rockets'),
        2: pgettext_lazy('aircraft_mod', '6 x ROS-82 rockets'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-50sv / FAB-100M bombs'),
        4: pgettext_lazy('aircraft_mod', 'One-piece Windscreen'),
        5: pgettext_lazy('aircraft_mod', '2 x 20mm ShVAK (180 rounds)'),
    },
    'il-2 mod.1941': {
        1: pgettext_lazy('aircraft_mod', '2 x 23mm VYa-23 gun'),
        2: pgettext_lazy('aircraft_mod', '6 x FAB-50sv / FAB-100M bombs'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-250sv bombs'),
        4: pgettext_lazy('aircraft_mod', '8 x RBS-82 rockets'),
        5: pgettext_lazy('aircraft_mod', '8 x ROFS-132 rockets'),
    },
    'il-2 mod.1942': {
        1: pgettext_lazy('aircraft_mod', '2 x 23mm VYa-23 gun'),
        2: pgettext_lazy('aircraft_mod', '2 x 37mm Sh-37 gun'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-250sv bombs'),
        4: pgettext_lazy('aircraft_mod', '8 x RBS-82 / ROFS-132 rockets'),
        5: pgettext_lazy('aircraft_mod', 'Rear turret'),
    },
    'il-2 mod.1943': {
        1: pgettext_lazy('aircraft_mod', '2 x 23mm VYa-23 gun'),
        2: pgettext_lazy('aircraft_mod', '2 x 37mm NS-37gun'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-250sv bombs'),
        4: pgettext_lazy('aircraft_mod', '4 x RBS-82 / ROFS-132 rockets'),
        5: pgettext_lazy('aircraft_mod', '192(240) x PTAB-2.5-1.5 bomblets'),
    },
    'ju 52 3mg4e': {
        1: pgettext_lazy('aircraft_mod', '2300 kg of cargo'),
        2: pgettext_lazy('aircraft_mod', '10 x MAB 250 containers'),
        3: pgettext_lazy('aircraft_mod', '12 paratroopers'),
        4: pgettext_lazy('aircraft_mod', 'Rear turret'),
    },
    'ju 87 d-3': {
        1: pgettext_lazy('aircraft_mod', 'Siren'),
        2: pgettext_lazy('aircraft_mod', 'SC 1800 heavy bomb'),
        3: pgettext_lazy('aircraft_mod', 'Additional armour plates'),
        4: pgettext_lazy('aircraft_mod', 'Machine gun pods'),
        5: pgettext_lazy('aircraft_mod', '2 x 37mm 3.7cm BK gun pods'),
    },
    'ju 88 a-4': {
        1: pgettext_lazy('aircraft_mod', '6 x SC 250 bombs'),
        2: pgettext_lazy('aircraft_mod', '4 x SC 500 bombs'),
        3: pgettext_lazy('aircraft_mod', '2 x SC 1000 heavy bombs'),
        4: pgettext_lazy('aircraft_mod', 'SC 1800 heavy bomb'),
        5: pgettext_lazy('aircraft_mod', '44 x SC 50 bombs'),
    },
    'la-5fn ser.2': {
        1: pgettext_lazy('aircraft_mod', '2 x FAB-50sv bombs'),
        2: pgettext_lazy('aircraft_mod', '2 x FAB-100M bombs'),
        3: pgettext_lazy('aircraft_mod', 'Landing light'),
        4: pgettext_lazy('aircraft_mod', 'RPK-10'),
        5: pgettext_lazy('aircraft_mod', 'Mirror'),
        6: pgettext_lazy('aircraft_mod', 'Special Guns Ammo Load'),
    },
    'la-5 ser.8': {
        1: pgettext_lazy('aircraft_mod', '2 x FAB-50sv bombs'),
        2: pgettext_lazy('aircraft_mod', '2 x FAB-100M bombs'),
        3: pgettext_lazy('aircraft_mod', 'RPK-10'),
        4: pgettext_lazy('aircraft_mod', 'Flat Windscreen'),
        5: pgettext_lazy('aircraft_mod', 'Special Guns Ammo Load'),
        6: pgettext_lazy('aircraft_mod', 'M-82F engine'),
    },
    'lagg-3 ser.29': {
        1: pgettext_lazy('aircraft_mod', '23mm VYa-23 gun'),
        2: pgettext_lazy('aircraft_mod', '37mm Sh-37 gun'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-50sv bombs'),
        4: pgettext_lazy('aircraft_mod', '2 x FAB-100M bombs'),
        5: pgettext_lazy('aircraft_mod', '6 x ROS-82 rockets'),
    },
    'mc.202 ser.viii': {
        1: pgettext_lazy('aircraft_mod', 'Armoured Wind Screen'),
        2: pgettext_lazy('aircraft_mod', '2 x 50-T bombs'),
        3: pgettext_lazy('aircraft_mod', '2 x 100-T bombs'),
        4: pgettext_lazy('aircraft_mod', '2 x 7.7mm machineguns'),
        5: pgettext_lazy('aircraft_mod', '2 x 20mm MG 151/20 gun pods'),
    },
    'me 262 a': {
        1: pgettext_lazy('aircraft_mod', 'Gyro Gunsight'),
        2: pgettext_lazy('aircraft_mod', '24 x R4M rockets'),
        3: pgettext_lazy('aircraft_mod', 'Armoured Headrest'),
        4: pgettext_lazy('aircraft_mod', 'Back Armor'),
        5: pgettext_lazy('aircraft_mod', 'Removed Front Armor'),
        6: pgettext_lazy('aircraft_mod', 'Removed Inner Cannons'),
        7: pgettext_lazy('aircraft_mod', 'Bomb load'),
        8: pgettext_lazy('aircraft_mod', 'Fuel regulating valve'),
    },
    'mig-3 ser.24': {
        1: pgettext_lazy('aircraft_mod', '6 x ROS-82 rockets'),
        2: pgettext_lazy('aircraft_mod', '2 x FAB-50sv / FAB-100M bombs'),
        3: pgettext_lazy('aircraft_mod', '2 x 12.7 mm BK machinegun pods'),
        4: pgettext_lazy('aircraft_mod', '2 x BS 12.7 mm (700 rounds)'),
        5: pgettext_lazy('aircraft_mod', '2 x 20mm ShVAK (300 rounds)'),
    },
    'p-38j-25': {
        1: pgettext_lazy('aircraft_mod', 'Additional ANM2 .50 cal MG ammo'),
        2: pgettext_lazy('aircraft_mod', 'General purpose bombs'),
        3: pgettext_lazy('aircraft_mod', 'Additional bomb racks'),
        4: pgettext_lazy('aircraft_mod', 'M8 rockets'),
        5: pgettext_lazy('aircraft_mod', 'Bendix MN-26'),
    },
    'p-39l-1': {
        1: pgettext_lazy('aircraft_mod', 'FAB-100M bomb'),
        2: pgettext_lazy('aircraft_mod', 'FAB-250tsk bomb'),
        3: pgettext_lazy('aircraft_mod', 'Additional ANM2 .30 cal MG ammo'),
        4: pgettext_lazy('aircraft_mod', 'Removal of ANM2 .30'),
        5: pgettext_lazy('aircraft_mod', 'Special 37mm Gun Ammo Load'),
        6: pgettext_lazy('aircraft_mod', 'Bendix MN-26'),
    },
    'p-40e-1': {
        1: pgettext_lazy('aircraft_mod', '4 x ANM2 .50 cal machine guns'),
        2: pgettext_lazy('aircraft_mod', 'Additional ANM2 .50 cal MG ammo'),
        3: pgettext_lazy('aircraft_mod', '4 x ROS-82 rockets'),
        4: pgettext_lazy('aircraft_mod', 'FAB-250sv bomb'),
        5: pgettext_lazy('aircraft_mod', 'FAB-500M bomb'),
        6: pgettext_lazy('aircraft_mod', 'Mirror'),
    },
    'p-47d-28': {
        1: pgettext_lazy('aircraft_mod', '6 x ANM2 .50 cal machine guns'),
        2: pgettext_lazy('aircraft_mod', '4 x ANM2 .50 cal machine guns'),
        3: pgettext_lazy('aircraft_mod', 'Additional ANM2 .50 cal MG ammo'),
        4: pgettext_lazy('aircraft_mod', 'Ground attack modification'),
        5: pgettext_lazy('aircraft_mod', 'Gyro Gunsight'),
        6: pgettext_lazy('aircraft_mod', 'Bendix MN-26'),
        7: pgettext_lazy('aircraft_mod', 'Mirror'),
    },
    'p-51d-15': {
        1: pgettext_lazy('aircraft_mod', '4 x ANM2 .50 cal machine guns'),
        2: pgettext_lazy('aircraft_mod', 'Additional ANM2 .50 cal MG ammo'),
        3: pgettext_lazy('aircraft_mod', '2 x M64 bombs'),
        4: pgettext_lazy('aircraft_mod', '2 x M65 bombs'),
        5: pgettext_lazy('aircraft_mod', 'M8 rockets'),
        6: pgettext_lazy('aircraft_mod', 'Gyro Gunsight'),
        7: pgettext_lazy('aircraft_mod', '150 grade fuel'),
        8: pgettext_lazy('aircraft_mod', 'Bendix MN-26'),
        9: pgettext_lazy('aircraft_mod', 'Mirror'),
    },
    'pe-2 ser.35': {
        1: pgettext_lazy('aircraft_mod', '10 x FAB-100M bombs'),
        2: pgettext_lazy('aircraft_mod', '4 x FAB-250sv bombs'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-500M bombs'),
        4: pgettext_lazy('aircraft_mod', '10 x ROS-132 rockets'),
        5: pgettext_lazy('aircraft_mod', 'RPK-2'),
    },
    'pe-2 ser.87': {
        1: pgettext_lazy('aircraft_mod', '10 x FAB-100M bombs'),
        2: pgettext_lazy('aircraft_mod', '4 x FAB-250sv bombs'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-500M bombs'),
        4: pgettext_lazy('aircraft_mod', '10 x ROS-132 rockets'),
        5: pgettext_lazy('aircraft_mod', 'Blister turret'),
    },
    'pfalz d.iiia': {
        1: pgettext_lazy('aircraft_mod', 'Collimator Day'),
        2: pgettext_lazy('aircraft_mod', 'Collimator Night'),
        3: pgettext_lazy('aircraft_mod', 'Gunsight'),
        4: pgettext_lazy('aircraft_mod', 'Anemometer'),
        5: pgettext_lazy('aircraft_mod', 'High Altimeter'),
        6: pgettext_lazy('aircraft_mod', 'Inclinometer'),
        7: pgettext_lazy('aircraft_mod', 'Bullet Counters'),
        8: pgettext_lazy('aircraft_mod', 'Thermometer'),
        9: pgettext_lazy('aircraft_mod', 'Cockpit light'),
    },
    's.e.5a': {
        1: pgettext_lazy('aircraft_mod', 'Aldis'),
        2: pgettext_lazy('aircraft_mod', 'Fuel Gauge'),
        3: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        4: pgettext_lazy('aircraft_mod', 'Cooper bombs'),
    },
    'sopwith camel': {
        1: pgettext_lazy('aircraft_mod', 'Aldis'),
        2: pgettext_lazy('aircraft_mod', 'Enlarged window'),
        3: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        4: pgettext_lazy('aircraft_mod', 'Cooper bombs'),
    },
    'sopwith dolphin': {
        1: pgettext_lazy('aircraft_mod', 'Twin Lewis Overwing'),
        2: pgettext_lazy('aircraft_mod', 'Twin Lewis lower-wing'),
        3: pgettext_lazy('aircraft_mod', 'Aldis'),
        4: pgettext_lazy('aircraft_mod', 'Thermometer'),
        5: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        6: pgettext_lazy('aircraft_mod', 'Cooper bombs'),
    },
    'spad 13.c1': {
        1: pgettext_lazy('aircraft_mod', 'Balloon guns'),
        2: pgettext_lazy('aircraft_mod', 'Aldis'),
        3: pgettext_lazy('aircraft_mod', 'Le-Chretien'),
        4: pgettext_lazy('aircraft_mod', 'Cockpit light'),
        5: pgettext_lazy('aircraft_mod', 'Cooper bombs'),
        6: pgettext_lazy('aircraft_mod', 'Camera'),
    },
    'spitfire mk.ixe': {
        1: pgettext_lazy('aircraft_mod', '500 lb G.P. bomb'),
        2: pgettext_lazy('aircraft_mod', '2 x 250 lb G.P. bombs'),
        3: pgettext_lazy('aircraft_mod', '2 х RP-3 HE / AP rockets'),
        4: pgettext_lazy('aircraft_mod', 'Gyro Gunsight'),
        5: pgettext_lazy('aircraft_mod', 'Mirror'),
        6: pgettext_lazy('aircraft_mod', 'Clipped Wing'),
        7: pgettext_lazy('aircraft_mod', 'Merlin 70 engine'),
        8: pgettext_lazy('aircraft_mod', '150 grade fuel'),
    },
    'spitfire mk.vb': {
        1: pgettext_lazy('aircraft_mod', 'Merlin 45 engine'),
        2: pgettext_lazy('aircraft_mod', 'Mirror'),
    },
    'tempest mk.v ser.2': {
        1: pgettext_lazy('aircraft_mod', '2 x 500 lb M.C. bombs'),
        2: pgettext_lazy('aircraft_mod', '2 x 1000 lb M.C. bomb'),
        3: pgettext_lazy('aircraft_mod', 'Sabre IIA engine with +11 lb boost'),
    },
    'u-2vs': {
        1: pgettext_lazy('aircraft_mod', 'Rear turret'),
        2: pgettext_lazy('aircraft_mod', 'Bow MG'),
        3: pgettext_lazy('aircraft_mod', 'Bomb load'),
        4: pgettext_lazy('aircraft_mod', 'Navigation lights'),
        5: pgettext_lazy('aircraft_mod', 'Landing light'),
        6: pgettext_lazy('aircraft_mod', 'Horizon indicator'),
        7: pgettext_lazy('aircraft_mod', 'Radio transmitter'),
        8: pgettext_lazy('aircraft_mod', 'Rockets'),
    },
    'yak-1b ser.127': {
        1: pgettext_lazy('aircraft_mod', '2 x FAB-50sv bombs'),
        2: pgettext_lazy('aircraft_mod', '2 x FAB-100M bombs'),
        3: pgettext_lazy('aircraft_mod', 'Landing light'),
        4: pgettext_lazy('aircraft_mod', 'RPK-10'),
        5: pgettext_lazy('aircraft_mod', 'Mirror'),
    },
    'yak-1 ser.69': {
        1: pgettext_lazy('aircraft_mod', '2 x ROS-82 rockets'),
        2: pgettext_lazy('aircraft_mod', '6 x ROS-82 rockets'),
        3: pgettext_lazy('aircraft_mod', '2 x FAB-50sv bombs'),
        4: pgettext_lazy('aircraft_mod', '2 x FAB-100M bombs'),
        5: pgettext_lazy('aircraft_mod', 'RPK-10'),
    },
    'yak-7b ser.36': {
        1: pgettext_lazy('aircraft_mod', '2 x FAB-50sv bombs'),
        2: pgettext_lazy('aircraft_mod', '2 x FAB-100M bombs'),
        3: pgettext_lazy('aircraft_mod', 'RPK-10'),
        4: pgettext_lazy('aircraft_mod', 'Landing light'),
    },
    'yak-9 ser.1': {
        1: pgettext_lazy('aircraft_mod', 'RPK-10'),
        2: pgettext_lazy('aircraft_mod', 'Landing light'),
        3: pgettext_lazy('aircraft_mod', 'Mirror'),
        4: pgettext_lazy('aircraft_mod', 'Reflector Gunsight'),
    },
    'yak-9t ser.1': {
        1: pgettext_lazy('aircraft_mod', 'RPK-10'),
        2: pgettext_lazy('aircraft_mod', 'Landing light'),
        3: pgettext_lazy('aircraft_mod', 'Mirror'),
        4: pgettext_lazy('aircraft_mod', 'Reflector Gunsight'),
        5: pgettext_lazy('aircraft_mod', 'Ammo counter'),
    },
}
