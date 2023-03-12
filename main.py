
print('Hello, World!')

x = 5
print(x)

import ru_locals as ru

start_dst = 16637000000
voyage_spd = 38241
wave_spd = 299792458 * 2.24 # в милях/час

print(ru.days)
days = int(input())
dst_ml = start_dst + days * voyage_spd
dst_km = dst_ml * 1.6
dst_astro = 1.08 * 10**(-8)
wave_tm = dst_ml/wave_spd # часы
wave_ping = (days * 24 * 60) - wave_tm

print(ru.dst_ml, round(dst_ml))
print(ru.dst_km, round(dst_km))
print(ru.dst_astro, dst_astro)
print(ru.wave_ping, round(wave_ping))