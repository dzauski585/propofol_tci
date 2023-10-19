#James formula for lean body weight in kg
def lbm_calc(g, w, h): 
    if g == 'm':
        lbm = 1.1 * w - 128 * (w / h)**2
    elif g == 'f':
        lbm = 1.07 * w - 148 * (w / h)**2
    return round(lbm)