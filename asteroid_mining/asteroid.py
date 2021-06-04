import math
import os
import random
import pandas as pd
import numpy as np

from utils import clean_spec
from asteroid_mining.parameters import Parameters
from asteroid_mining.utils import clean_diameter_acc, clean_spec
from asteroid_mining.data import Data

class Asteroids:

    def __init__(self):
        self.df_acc = None
        self.df_neo = None
        self.acc_resources = None
        self.resources_list = None
    
    def get_saved_df(self):
        """Instanciates two DataFrames if they have already been solved"""
        self.df_acc = Data().get_acc_data()
        self.df_neo = Data().get_neo_data()
        pass

    def get_df_from_scratch(self):
        """Creates df, saves them and instantiates them in the class"""
        Data().create_df()
        self.get_saved_df()
        pass
    
    def get_spec(self):
        """Gets the spec of each asteroid of the df by estimation"""
        
        self.df_neo['spec_B_clean'] = self.df_neo['spec_B'].apply(clean_spec)
        self.df_acc['spec_B_clean'] = self.df_acc['spec_B'].apply(clean_spec)

        spec_counts_neo = self.df_neo[['id', 'spec_B_clean']].groupby(['spec_B_clean']).count().reset_index()
        index_to_del = spec_counts_neo[ spec_counts_neo['spec_B_clean'] == 'nan'].index
        spec_counts_neo.drop(index_to_del , inplace=True)

        sum_spec_neo = spec_counts_neo['id'].sum()
        spec_counts_neo['per_spec'] = spec_counts_neo['id'].apply(lambda x: x / sum_spec_neo)
        spec_counts_neo['cum_perc_spec'] = spec_counts_neo['per_spec'].cumsum()
    

        def new_spec_acc(x):
            if x == 'nan':
                a = random.uniform(0,1)
                for i in range(spec_counts_neo.shape[0]):
                    if a > spec_counts_neo.loc[i, 'cum_perc_spec']:
                        continue
                    else:
                        new_spec = spec_counts_neo.loc[i, 'spec_B_clean']
                        break
                return new_spec
            else:
                return x
      
        self.df_acc['new_spec'] = self.df_acc['spec_B_clean'].apply(new_spec_acc)
        pass

    def compute_mass(self):
        """Computes the mass of each asteroid of the df"""

        # Estimate the % of resources for each asteroid according to its spec
        specs_param = Parameters().spec_per_resources
        self.acc_resources = self.df_acc[['id', 'new_spec']]
        
        for key in specs_param:
            for key1 in specs_param[key]:
                if key1 not in self.acc_resources.columns:
                    self.acc_resources[key1] = ''

        self.resources_list = list(self.acc_resources.columns)
        self.resources_list.remove('id')
        self.resources_list.remove('new_spec')

        for col in self.resources_list:
            for i, row in self.acc_resources.iterrows():
                if col in specs_param[row['new_spec']]:
                    self.acc_resources.at[i,col] = specs_param[row['new_spec']][col]

        # Get the diameter
        self.df_acc['diameter_clean'] = self.df_acc['Estimated Diameter (m)'].apply(clean_diameter_acc)

        # Get the volume
        self.df_acc['est_volume'] = 4/3 * math.pi * ((self.df_acc['diameter_clean'] / 2) ** 3)

        # Get the density
        def get_density(x):
            general_spec = Parameters().tholen_smasii_map[x]
            return Parameters().TYPE_DENSITY_MAP[general_spec]

        self.df_acc['est_density'] = self.df_acc['new_spec'].apply(get_density)

        # Get the mass
        self.df_acc['est_mass'] = ''

        for i, row in self.df_acc.iterrows():
            mass = row['est_volume'] * row['est_density'] / 6 * 1000
            
            # Add some random factor
            mass = mass + (random.random() - .5) * 1e6
            
            if mass > 1e11:
            # if it's huge, penalize it because the surface will be covered in ejecta, etc.
            # and the goodies will be far beneath. Also, gravity well.
                mass = mass * 1e-3
            
            self.df_acc.at[i,"est_mass"] = mass

        self.df_acc['est_mass'] = self.df_acc['est_mass'].astype('float64')
        pass

    def estimate_total_acc_resources(self):    
        # Estimate available resources for each asteroid in kg
        acc_total_resources = pd.merge(self.acc_resources, self.df_acc[['id', 'est_mass']], on='id', how='inner')

        for i in self.resources_list:
            acc_total_resources[i] = acc_total_resources[i].apply(lambda x: 0 if x == '' else x)
            acc_total_resources[f'{i}_kg'] = acc_total_resources[i] * acc_total_resources['est_mass']
        
        acc_total_resources = acc_total_resources.drop(columns=self.resources_list)

        # Get path
        rootdir = os.path.dirname(__file__)
        path_to_save = os.path.join(rootdir, 'data', 'acc_total_resources_test1.csv')
        
        acc_total_resources.to_csv(path_to_save)
        print('acc_total_resources csv saved!')
        pass


if __name__ == "__main__":
    
    asteroid = Asteroids()

    asteroid.get_saved_df()
    asteroid.get_spec()
    asteroid.compute_mass()
    asteroid.estimate_total_acc_resources()