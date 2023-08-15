# import ephem

# mars = ephem.Mars()
# mars.compute('2007/10/02 00:50:22')
# print (mars.ra, mars.dec)
# ephem.constellation(mars)

from skyfield.api import load

# planets = load('de421.bsp')
# earth, mars = planets['earth'], planets['mars']

# ts = load.timescale()
# t = ts.now()
# astrometric = earth.at(t).observe(mars)
# ra, dec, distance = astrometric.radec()

# print(ra)
# print(dec)
# print(distance)

from skyfield.api import Topos

planets = load('de421.bsp')
earth, mars = planets['earth'], planets['moon']
vilnius = earth + Topos('54.720915 N', '25.248981 W')
ts = load.timescale(builtin=True)
t = ts.now()
astrometric = vilnius.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)


# Calculate moon phase
# from skyfield.api import load

# ts = load.timescale()
# t = ts.utc(2019, 12, 9, 15, 36)

# eph = load('de421.bsp')
# sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

# e = earth.at(t)
# _, slon, _ = e.observe(sun).apparent().ecliptic_latlon()
# _, mlon, _ = e.observe(moon).apparent().ecliptic_latlon()
# phase = (mlon.degrees - slon.degrees) % 360.0

# print('{0:.1f}'.format(phase))