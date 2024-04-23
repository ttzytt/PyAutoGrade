







def rotate_and_expand(point):
    x = point[0]
    y = point[1]
    new_x = 1.1 * y
    new_y = -1.1 * x
    return (new_x, new_y)





list_of_points = [(0.3, 0.1),
    (0.11000000000000001, -0.33),
    (-0.36300000000000004, -0.12100000000000002),
    (-0.13310000000000002, 0.3993000000000001),
    (0.4392300000000001, 0.14641000000000004),
    (0.16105100000000006, -0.48315300000000017),
    (-0.5314683000000002, -0.17715610000000007),
    (-0.1948717100000001, 0.5846151300000003),
    (0.6430766430000004, 0.2143588810000001),
    (0.23579476910000013, -0.7073843073000006),
    (-0.7781227380300006, -0.25937424601000014),
    (-0.28531167061100016, 0.8559350118330008),
    (0.9415285130163009, 0.3138428376721002),
    (0.3452271214393102, -1.035681364317931),
    (-1.1392495007497243, -0.37974983358324127),
    (-0.41772481694156544, 1.253174450824697),
    (1.3784918959071668, 0.45949729863572203),
    (0.5054470284992942, -1.5163410854978836),
    (-1.6679751940476721, -0.5559917313492238),
    (-0.6115909044841462, 1.8347727134524394),
    (2.0182499847976834, 0.6727499949325609),
    (0.740024994425817, -2.220074983277452),
    (-2.442082481605197, -0.8140274938683988),
    (-0.8954302432552388, 2.6862907297657173),
    (2.9549198027422894, 0.9849732675807628),
    (1.0834705943388392, -3.2504117830165185),
    (-3.5754529613181707, -1.1918176537727232),
    (-1.3109994191499956, 3.932998257449988),
    (4.326298083194987, 1.4420993610649953),
    (1.586309297171495, -4.758927891514486),
    (-5.234820680665935, -1.7449402268886445),
    (-1.919434249577509, 5.758302748732529),
    (6.334133023605783, 2.11137767453526),
    (2.3225154419887866, -6.967546325966362),
    (-7.664300958562999, -2.5547669861876656),
    (-2.8102436848064323, 8.430731054419299),
    (9.27380415986123, 3.0912680532870755),
    (3.4003948586157833, -10.201184575847353),
    (-11.22130303343209, -3.740434344477362),
    (-4.114477778925099, 12.3434333367753),
    (13.577776670452831, 4.525925556817609),
    (4.97851811249937, -14.935554337498115),
    (-16.429109771247926, -5.476369923749307),
    (-6.024006916124239, 18.072020748372722),
    (19.879222823209997, 6.626407607736663),
    (7.28904836851033, -21.867145105530998),
    (-24.0538596160841, -8.017953205361364),
    (-8.8197485258975, 26.459245577692514),
    (29.105170135461766, 9.701723378487252),
    (10.671895716335978, -32.015687149007945),
    (-35.21725586390874, -11.739085287969576)]



print(list_of_points)



points = [(0.3, 0.1)]
for _ in range(49):
    points.append(rotate_and_expand(points[-1]))
print(points)
