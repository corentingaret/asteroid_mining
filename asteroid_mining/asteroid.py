import math
from random import uniform
from utils import clean_spec

class Asteroids:
    
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

    
    
    def clean_accessible_database(self):
        
        
        df_neo['spec_B_clean'] = df_neo['spec_B'].apply(clean_spec)
        df_acc['spec_B_clean'] = df_acc['spec_B'].apply(clean_spec)

        spec_counts_neo = df_neo[['id', 'spec_B_clean']].groupby(['spec_B_clean']).count().reset_index()
        index_to_del = spec_counts_neo[ spec_counts_neo['spec_B_clean'] == 'nan'].index
        spec_counts_neo.drop(index_to_del , inplace=True)

        sum_spec_neo = spec_counts_neo['id'].sum()
        spec_counts_neo['per_spec'] = spec_counts_neo['id'].apply(lambda x: x / sum_spec_neo)
        spec_counts_neo['cum_perc_spec'] = spec_counts_neo['per_spec'].cumsum()
    

        def new_spec_acc(x):
            if x == 'nan':
                a = uniform(0,1)
                for i in range(spec_counts_neo.shape[0]):
                    if a > spec_counts_neo.loc[i, 'cum_perc_spec']:
                        continue
                    else:
                        new_spec = spec_counts_neo.loc[i, 'spec_B_clean']
                        break
                return new_spec
            else:
                return x
                
        df_acc['new_spec'] = df_acc['spec_B_clean'].apply(new_spec_acc)