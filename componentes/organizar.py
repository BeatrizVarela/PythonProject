# -*- coding: utf-8 -*-

"""
Created on Tue Dec 15 14:10:43 2020

__author__: Miguel Correia e Ana Beatriz Varela

This module contains two functions:
    -organizar_df, which takes care of organizing the DataFrames to only
    show the values needed for the ratios and averages.
    
    -trocar_id_por_nome, which takes care of switching the airline's and
    airport's id by their name. Not only that but it only shows the top
    10 airports/airlines for each value.
"""

import pandas as pd


def organizar_df(tabela_estatisticas):
        """

        Parameters
        ----------
        tabela_estatisticas : Pandas DataFrame
            A DataFrame with the values of each time a delay occured,
            specifying the airport it was headed and the airline.

        Returns
        -------
        atrasos_c : Pandas DataFrame
            A Pandas DataFrame that shows how many times airlines have
            delayed flight, and not delayed flights.
        atrasos_a : Pandas DataFrame
            A Pandas DataFrame that shows how many times airports have
            delayed flight, and not delayed flights.
        vals_c : Pandas DataFrame
            A Pandas DataFrame that shows how many minutes a flights has 
            been delayed per airline.
        vals_a : Pandas DataFrame
            A Pandas DataFrame that shows how many minutes a flight
            has been delayed per airport.

        Does
        -------
        Organizes the dataframes as needed by the other modules.
        
        """
        tabela_estatisticas=tabela_estatisticas.drop(columns="Unnamed: 5")
        tabela_s_na=(tabela_estatisticas.dropna())
        delays=((tabela_s_na.loc[:,"ARR_DELAY_NEW"])>0)
        #dataframes for the ratio of delays
        atrasos_c=pd.crosstab(tabela_s_na["AIRLINE_ID"],delays)
        atrasos_c["soma"]=atrasos_c.sum(axis=1)
        atrasos_a=pd.crosstab(tabela_s_na["DEST_AIRPORT_ID"],delays)
        atrasos_a["soma"]=atrasos_a.sum(axis=1)
        #dataframes for the mean of delays
        tabela_p_media_c = pd.crosstab(tabela_estatisticas["ARR_DELAY_NEW"],tabela_s_na["AIRLINE_ID"])
        vals_c=(tabela_p_media_c.mul(tabela_p_media_c.index, axis=0)).sum()
        tabela_p_media_a = pd.crosstab(tabela_estatisticas["ARR_DELAY_NEW"],tabela_s_na["DEST_AIRPORT_ID"])
        vals_a=(tabela_p_media_a.mul(tabela_p_media_a.index, axis=0)).sum()
        return atrasos_c,atrasos_a,vals_c,vals_a

def trocar_id_por_nome(tabela_nomes,atrasos,lista,tipo,mean=True):
        """

        Parameters
        ----------
        tabela_nomes : Pandas DataFrame
            A DataFrame that specifies what the name of the airline or
            airport is taking to account its ID.
        atrasos : Pandas DataFrame
            A DataFrame that shows how many times an airline or airport
            had a delay, False being all the times it didn't and True
            being all the times it did have a delay.
        lista : Pandas DataFrame
            A list with all of the delays or ratios, ordered by the
            order they came in.
        tipo : String
            A string that is required to check if you are ordering and
            switching the ID's of airports, or airlines.
        mean : boolean, optional
            Checks if the values you're giving are the Mean, being True
            or if the values you're giving are the Ratio, False. The 
            default is True.

        Returns
        -------
        new_df : Pandas DataFrame
            A DataFrame with the mean or ratio of the delays per 
            airline or airport.

        Does
        -------
        Makes a new organized DataFrame and switches the ID's by the
        name of each airport/airline
        """
        nomes=[]
        for i in tabela_nomes.index:
            if tabela_nomes["Code"][i] in list(atrasos.index):
                nomes.append(((tabela_nomes["Description"][i])))
        if mean==True:
            col="Minutos Atrasados"
            new_df=pd.DataFrame({col:lista},index=nomes)
            new_df.index = new_df.index.astype("U10")
            new_df.sort_values(col,ascending=False,inplace=True)
        else:
            col="Racio"
            new_df=pd.DataFrame({col:lista},index=nomes)
            new_df.index = new_df.index.astype("U10")
            new_df.sort_values(col,ascending=False,inplace=True)
        new_df=new_df.head(n=10)
        new_df.sort_values(col,ascending=True,inplace=True)
        return new_df

