

class Parameters:

    spec_per_resources = {
    '?': {},
    'A': {},
    'B': {
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
        'iron': 10,
    },
    'C': {
        # from Keck report at http://www.kiss.caltech.edu/study/asteroid/asteroid_final_report.pdf
        'water': .2,
        'iron': .166,
        'nickel': .014,
        'cobalt': .002,

        # volatiles
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
    },
    'Ch': {
        # from Keck report at http://www.kiss.caltech.edu/study/asteroid/asteroid_final_report.pdf
        'water': .2,
        'iron': .166,
        'nickel': .014,
        'cobalt': .002,

        # volatiles
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
    },
    'Cg': {
        # from Keck report at http://www.kiss.caltech.edu/study/asteroid/asteroid_final_report.pdf
        'water': .2,
        'iron': .166,
        'nickel': .014,
        'cobalt': .002,

        # volatiles
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
    },
    'Cgh': {
        # from Keck report at http://www.kiss.caltech.edu/study/asteroid/asteroid_final_report.pdf
        'water': .2,
        'iron': .166,
        'nickel': .014,
        'cobalt': .002,

        # volatiles
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
    },
    'C': {
        # from Keck report at http://www.kiss.caltech.edu/study/asteroid/asteroid_final_report.pdf
        'water': .2,
        'iron': .166,
        'nickel': .014,
        'cobalt': .002,

        # volatiles
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
    },
    'Cb': {   # transition object between C and B
        # from Keck report at http://www.kiss.caltech.edu/study/asteroid/asteroid_final_report.pdf
        'water': .1,
        'iron': .083,
        'nickel': .007,
        'cobalt': .001,

        # volatiles
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
    },
    'D': {
        'water': 0.000023,
    },
    'E': {

    },
    'K': {  # cross between S and C
        # from Keck report at http://www.kiss.caltech.edu/study/asteroid/asteroid_final_report.pdf
        'water': .1,
        'iron': .083,
        'nickel': .007,
        'cobalt': .001,

        # volatiles
        'hydrogen': 0.235,
        'nitrogen': 0.001,
        'ammonia': 0.001,
    },
    'L': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
        'aluminum': 7
    },
    'Ld': {  # copied from S
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'M': {
        'iron': 88,
        'nickel': 10,
        'cobalt': 0.5,
    },
    'O': {
        'nickel-iron': 2.965,
        'platinum': 1.25,
    },
    'P': {  # correspond to CI, CM carbonaceous chondrites
        'water': 12.5,
    },
    'R': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'S': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    # Sa, Sq, Sr, Sk, and Sl all transition objects (assume half/half)
    'Sa': {
        'magnesium silicate': 5e-31,
        'iron silicate': 0,
    },
    'Sq': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'Sr': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'Sk': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'Sl': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'S(IV)': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'Q': {
        'nickel-iron': 13.315,
    },
    'R': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },
    'T': {
        'iron': 6,
    },
    'U': {

    },
    'V': {
        'magnesium silicate': 1e-30,
        'iron silicate': 0,
    },

    # TODO use density to decide what kind of X the object is?

    'X': {  # TODO these vals only apply to M-type within X
        'iron': 88,
        'nickel': 10,
        'cobalt': 0.5,
    },
    'Xe': {  # TODO these vals only apply to M-type within X
        'iron': 88,
        'nickel': 10,
        'cobalt': 0.5,
    },
    'Xc': {  # TODO these vals only apply to M-type within X
        'iron': 88,
        'nickel': 10,
        'cobalt': 0.5,
        'platinum': 0.005,
    },
    'Xk': {  # TODO these vals only apply to M-type within X
        'iron': 88,
        'nickel': 10,
        'cobalt': 0.5,
    },
    'comet': {
        # no estimates for now, because assumed mass, etc. would be off
    },
    }

    TYPE_DENSITY_MAP = {
    'C': 1.38,
    'D': 1.38,
    'P': 1.38,
    'T': 1.38,
    'B': 1.38,
    'G': 1.38,
    'F': 1.38,
    'S': 2.71,
    'K': 2.71,
    'Q': 2.71,
    'V': 2.71,
    'R': 2.71,
    'A': 2.71,
    'M': 5.32,
    }

    tholen_smasii_map = {'A':'A', 
                     'B':'B', 
                     'C':'C', 
                     'Ch':'C', 
                     'Cg':'C', 
                     'Cgh':'C', 
                     'Cb':'C', 
                     'D':'D', 
                     'E':'M', 
                     'K':'P', 
                     'L':'A', 
                     'Ld':'A', 
                     'M':'M', 
                     'O':'P', 
                     'P':'P', 
                     'R':'R', 
                     'S':'S', 
                     'Sa':'S', 
                     'Sq':'S', 
                     'Sr':'S', 
                     'Sk':'S', 
                     'Sl':'S', 
                     'S(IV)':'S', 
                     'Q':'Q', 
                     'T':'T', 
                     'U':'S', 
                     'V':'V', 
                     'X':'M', 
                     'Xe':'M', 
                     'Xc':'M', 
                     'Xk':'M'}