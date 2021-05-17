import pandas as pd
import os

class Data:

    def create_df(self):
        """Saves a csv with all NEO asteroids and their charasteristics & another with accessible NEAs
        Raw data comes from
        - JPL database named neo_asteroids_jpl: https://ssd.jpl.nasa.gov/sbdb_query.cgi#x
        - Asterank complete database named asterank: https://github.com/typpo/asterank
        - CNEOS accessible asteroids database: https://cneos.jpl.nasa.gov/nhats/
        All files located in data/raw_data"""

        # Get paths
        rootdir = os.path.dirname(os.path.dirname(__file__))
        data_path = os.path.join(rootdir, "data")
        raw_data_path = os.path.join(data_path, "raw_data")

        # Get raw_data
        asterank_file = os.path.join(raw_data_path, 'asterank.csv')
        asterank = pd.read_csv(asterank_file)

        neo_jpl_file = os.path.join(raw_data_path, 'neo_asteroids_jpl.csv')
        neo_jpl = pd.read_csv(neo_jpl_file)

        cneos_file = os.path.join(raw_data_path, 'cneos_asteroids.csv')
        cneos = pd.read_csv(cneos_file)
        cneos = cneos.rename(columns={'Unnamed: 10':'id'})

        # Merge dataframes
        df_neo = asterank.merge(neo_jpl['id'], how='inner', on='id')
        df_acc = df_neo.merge(cneos, how='inner', on='id')

        # Save data
        neo_location = os.path.join(data_path,'neo_asteroids.csv')
        acc_location = os.path.join(data_path,'acc_asteroids.csv')


        df_neo.to_csv(neo_location)
        df_acc.to_csv(acc_location)

        return "csv file saved!"

    def get_neo_data(self):
        """Returns the neo asteroids DataFrame"""
        
        # Get path
        rootdir = os.path.dirname(__file__)
        df_path = os.path.join(rootdir, "data", "neo_asteroids.csv")
        
        # Read csv
        df = pd.read_csv(df_path)
        return df

    def get_acc_data(self):
        """Returns the accessible asteroids DataFrame"""
        
        # Get path
        rootdir = os.path.dirname(__file__)
        df_path = os.path.join(rootdir, "data", "acc_asteroids.csv")
        
        # Read csv
        df = pd.read_csv(df_path)
        return df
    

