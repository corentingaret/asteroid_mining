import math
from random import uniform
from utils import clean_spec

class Asteroids:
    
    # Default attributes
    DEFAULT_RADIUS = .5  # km
    DEFAULT_MASS = 1.47e15  # kg
    DEFAULT_MOID = 2  # TODO get avg moid
    DEFAULT_DV = 12#6.5 #km/s
    DEFAULT_COMET_DV = 50  # km/s
    DEFAULT_ALBEDO = .15
    DEFAULT_DENSITY = 2 # g / cm^3


    # g/cm^3
    # https://en.wikipedia.org/wiki/Standard_asteroid_physical_characteristics#Density
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

    def __init__(self, df_neo, df_acc):
        self.df_neo = df_neo
        self.df_acc = df_acc

    def spec_distribution_neo(self):
        self.df_neo['spec_B_clean'] = self.df_neo['spec_B'].apply(clean_spec)

        spec_counts = self.df_neo[['id', 'spec_B_clean']].groupby(['spec_B_clean']).count().reset_index()
        
        # Drop NaNs
        index_to_del = spec_counts[ spec_counts['spec_B_clean'] == 'nan' ].index
        spec_counts.drop(index_to_del , inplace=True)

        # Get percentages
        sum_spec = spec_counts['id'].sum()
        spec_counts['perc_spec'] = spec_counts['id'].apply(lambda x: x / sum_spec)
        
        # Return what?
        return spec_counts[['spec_B_clean', 'perc_spec']]

    def apply_spec(self):

        self.df_acc['spec_B_clean'] = self.df_acc['spec_B'].apply(clean_spec)
        spec_counts = spec_distribution()

        # Create function that will enable to estimate spec classifications
        def new_spec_acc(x):
            
            if pd.isnull(x):
                a = uniform(0,1)
                for i in range(spec_counts.shape[0]):
                    if a > spec_counts.loc[i, 'cum_perc_spec']:
                        continue
                    else:
                        new_spec = spec_counts.loc[i, 'spec_B_clean']
                        break
                return new_spec
            
            else:
                return x
        
        # Apply it to spec
        self.df_acc['new_spec'] = self.df_acc['spec_B_clean'].apply(new_spec_acc)

        return df_acc





    
    # def closeness_weight(obj):
    #     if obj['spec'] == 'comet':
    #     return -1

    # emoid = DEFAULT_MOID if isinstance(obj['moid'], basestring) else obj['moid']

    # # penalize aphelion distance
    # aph = obj['ad']
    # if aph > 50:
    #     return -1
    # aph_score = 1/(1+math.exp(0.9*aph))

    # major_axis = obj['a']
    # ma_score = 1/(1+math.exp(0.45*major_axis))

    # ph = obj['q']
    # ph_score = 1/(1+math.exp(0.9*ph))

    # if 'dv' in obj:
    #     dv = obj['dv']
    # else:
    #     if obj['spec'] == 'comet':
    #     dv = DEFAULT_COMET_DV
    #     else:
    #     dv = DEFAULT_DV
    #     #return 0      # closeness shouldn't influence rank
    # dv_score = 1 + (1/(1+math.exp(1.3*dv-6)))

    # return pow(aph_score + ma_score + ph_score + 50*dv_score + 1, 2)

    # def price(obj):
    # """
    # Returns a tuple of $ price estimates for:
    #     0. Asteroid value per kg in raw materials.
    #     1. Asteroid $ saved per kg versus sending it up from Earth.
    # """
    # G = 6.67300e-20   # km^3 / kgs^2
    # if obj['spec'] == 'comet':
    #     return (-1, -1)

    # # estimate albedo
    # if isinstance(obj['albedo'], basestring):
    #     albedo = DEFAULT_ALBEDO
    # else:
    #     albedo = float(obj['albedo'])

    # # estimate diameter
    # if isinstance(obj['diameter'], basestring):
    #     if isinstance(obj['H'], basestring):
    #     # Can't estimate diameter :(
    #     diameter = DEFAULT_RADIUS * 2
    #     else:
    #     # Compute diameter in meters
    #     abs_magnitude = float(obj['H'])
    #     #diameter = 1329 * 10 ** (-abs_magnitude/5) * albedo ** (-1/2)
    #     diameter = 1329 / math.sqrt(albedo) * (10 ** (-0.2 * abs_magnitude))
    #     obj['est_diameter'] = diameter # keep as km

    # # mass in kg
    # exactmass = False
    # if isinstance(obj['GM'], basestring):
    #     diameter = obj['est_diameter'] if 'est_diameter' in obj else obj['diameter']
    #     if diameter:
    #     # Use diameter to estimate mass --> estimate price
    #     # Pick density based on spectral type
    #     general_spec_type = obj['spec'][0].upper()
    #     if general_spec_type in TYPE_DENSITY_MAP:
    #         assumed_density = TYPE_DENSITY_MAP[general_spec_type]
    #     else:
    #         assumed_density = DEFAULT_DENSITY

    #     # Compute mass form density and diameter
    #     # FIXME assuming a perfect sphere for now...
    #     assumed_vol = 4/3 * math.pi * ((diameter / 2) ** 3)
    #     # Volume: km^3
    #     # Density: g/cm^3
    #     mass = assumed_vol * assumed_density / 6 * 1e15
    #     else:
    #     mass = DEFAULT_MASS
    #     obj['inexact'] = True
    #     mass = mass + (random.random() - .5) * 1e14   # some random factor
    # else:
    #     exactmass = True
    #     mass = obj['GM'] / G

    #     if mass > 1e18:
    #     # if it's huge, penalize it because the surface will be covered in ejecta, etc.
    #     # and the goodies will be far beneath. Also, gravity well.
    #     mass = mass * 1e-6

    # stype = obj['spec']
    # value = estimate.valuePerKg(stype) * mass
    # saved = estimate.savedPerKg(stype) * mass
    # return (value, saved)