# -*- coding: utf-8 -*-
"""
__author__: Miguel Correia e Ana Beatriz Varela
"""

import pandas as pd
import os
import plotter
import organizar
import calcular


class atrasos:
    
    """

    Does
    -------
    Has several functions that work together, but, overall, it gets
    the data from a CSV file about delays in airports and airlines
    and plots graphs taking that data to account.

    """
    def __init__(self,nome_companhias,nome_aeroportos,nome_estatisticas):
        """
        
        Parameters
        ----------
        nome_companhias : String
            Name of the CSV file that contains the ID's of the airlines
            matching their names.
        nome_aeroportos : String
            Name of the CSV file that contains the ID's of the airports
            matching their names.
        nome_estatisticas : String
            Name of the CSV file that contains every flight done by an
            airline in the month of February of the year of 2015, 
            having the data of how many minutes there were of a delay
            (if there wasn't a delay it's 0 minutes).

        Does
        -------
        Gives the file names to the whole class, using the names to read
        the data given to it.

        """
        self.nome_companhias=nome_companhias
        self.nome_aeroportos=nome_aeroportos
        self.nome_estatisticas=nome_estatisticas
    
    def atrasos(self):
        """
        Does
        -------
        Plots the graphs of: the mean of the delays per airline; the
        ratio of delays per airline; the mean of delays per airport;
        the ratio of delays per airport, of a specific month in an year.

        """
        tabela_nomes_companhias=pd.read_csv((os.getcwd()+"/ficheiros/"+self.nome_companhias))
        tabela_nomes_aeroportos=pd.read_csv((os.getcwd()+"/ficheiros/"+self.nome_aeroportos))
        tabela_estatisticas=pd.read_csv((os.getcwd()+"/ficheiros/"+self.nome_estatisticas))
        if len(tabela_estatisticas.YEAR.unique()) == 1 and len(tabela_estatisticas.MONTH.unique()) == 1:
            atrasos_c,atrasos_a,vals_c,vals_a=organizar.organizar_df(tabela_estatisticas)
            atrasos_comp = self.atrasos_medio_companhia(tabela_nomes_companhias,atrasos_c,vals_c)
            racio_comp = self.racios_atrasos_companhia(tabela_nomes_companhias,atrasos_c)
            atrasos_aero = self.atrasos_medio_aeroporto(tabela_nomes_aeroportos,atrasos_a,vals_a)
            racio_aero = self.racios_atrasos_aeroporto(tabela_nomes_aeroportos,atrasos_a)
            month=tabela_estatisticas.MONTH.unique()[0]
            year=tabela_estatisticas.YEAR.unique()[0]
            plotter.plotter(atrasos_comp,racio_comp, atrasos_aero, racio_aero,month,year)
        else:
            print("Insert values corresponding to only one month in a specific year please.")

        
    def atrasos_medio_companhia(self,tabela_nomes_companhias,atrasos_c,vals_c):
        """

        Parameters
        ----------
        tabela_nomes_companhias : Pandas DataFrame
            A DataFrame that specifies what the name of the airline or
            airport is taking to account its ID.
        atrasos_c : Pandas DataFrame
            A Pandas DataFrame that shows how many times airlines have
            delayed flight, and not delayed flights.
        vals_c : Pandas DataFrame, default None
            A Pandas Dataframe that shows how many minutes a flight has
            been delayed per airline.

        Returns
        -------
        delay_comp : Pandas Dataframe
            A DataFrame with the mean of the delays per airline.
            
        Does
        -------
        From the given DataFrames it organizes them to show the mean
        of delays per airline.

        """
        delay_list=calcular.calcular_atrasos("AIRLINE_ID",atrasos_c,vals=vals_c)
        delay_comp = organizar.trocar_id_por_nome(tabela_nomes_companhias, atrasos_c, delay_list,"comp",True)
        return delay_comp
    def racios_atrasos_companhia(self,tabela_nomes_companhias,atrasos_c):
        """

        Parameters
        ----------
        tabela_nomes_companhias : Pandas DataFrame
            A DataFrame that specifies what the name of the airline or
            airport is taking to account its ID.
        atrasos_c : Pandas DataFrame
            A Pandas DataFrame that shows how many times airlines have
            delayed flight, and not delayed flights.

        Returns
        -------
        ratio_comp : Pandas DataFrame
            A DataFrame with the ratio of delays per airline.
            
        Does
        -------
        From the given DataFrames it organizes them to show the ratio
        of delays per airline.

        """
        ratio_list=calcular.calcular_atrasos("AIRLINE_ID",atrasos_c,mean=False)
        ratio_comp = organizar.trocar_id_por_nome(tabela_nomes_companhias, atrasos_c, ratio_list,"comp",False)
        return ratio_comp
    def atrasos_medio_aeroporto(self,tabela_nomes_aeroportos,atrasos_a,vals_a):
        """

        Parameters
        ----------
        tabela_nomes_aeroportos : Pandas DataFrame
            A DataFrame that specifies what the name of the airport is
            taking to account its ID.
        atrasos_a : Pandas DataFrame
            A Pandas DataFrame that shows how many times airports have
            delayed flight, and not delayed flights.
        vals_a : Pandas DataFrame
            A Pandas DataFrame that shows how many minutes a flight
            has been delayed per airport.

        Returns
        -------
        delay_aero : Pandas DataFrame
            A DataFrame with the mean of delays per airport.
        
        Does
        -------
        From the given DataFrames it organizes them to show the mean
        of delays per airport.

        """
        delay_list=calcular.calcular_atrasos("DEST_AIRPORT_ID",atrasos_a,vals=vals_a)
        delay_aero = organizar.trocar_id_por_nome(tabela_nomes_aeroportos, atrasos_a, delay_list,"aero",True)
        return delay_aero
    def racios_atrasos_aeroporto(self,tabela_nomes_aeroportos,atrasos_a):
        """

        Parameters
        ----------
        tabela_nomes_aeroportos : Pandas DataFrame
            A DataFrame that specifies what the name of the airport is
            taking to account its ID.
        atrasos_a : Pandas DataFrame
            A Pandas DataFrame that shows how many times airports have
            delayed flight, and not delayed flights.


        Returns
        -------
        ratio_aero : Pandas DataFrame
            A DataFrame with the ratio of delays per airport.
            
        Does
        -------
        From the given DataFrames it organizes them to show the ratio
        of delays per airport.

        """
        ratio_list=calcular.calcular_atrasos("DEST_AIRPORT_ID",atrasos_a,mean=False)
        ratio_aero = organizar.trocar_id_por_nome(tabela_nomes_aeroportos, atrasos_a, ratio_list,"aero",False)
        return ratio_aero

if __name__=='__main__':
    atrasos("L_AIRLINE_ID.csv","L_AIRPORT_ID.csv","850566403_T_ONTIME.csv").atrasos()


