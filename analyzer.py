from storage import load_last

def combine_data(local, web, wl=0.5, ww=0.5):
    if local and web:
        t = local[0]*wl + web[0]*ww
        h = local[1]*wl + web[1]*ww
        p = local[2]*wl + web[2]*ww
        return round(t,2), round(h,2), round(p,2)

    return local or web


def get_current():
    d = load_last(1)
    return d[0] if d else None


def pressure_trend():
    d = load_last(12)
    if len(d) < 6:
        return "Недостаточно данных."

    dp = d[-1][3] - d[0][3]

    if dp > 1: return "📈 Давление растёт — погода улучшается"
    if dp < -1: return "📉 Давление падает — возможна непогода"
    return "➡ Давление стабильно"
