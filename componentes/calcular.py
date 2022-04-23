# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:10:43 2020

__author__: Miguel Correia e Ana Beatriz Varela

This modules contains only one function (calcular_atrasos), this function
calculates the ratio, or the mean, of the data given to it.
"""

def calcular_atrasos(a_c,atrasos,mean=True,vals=None):
        """

        Parameters
        ----------
        a_c : String
            A string to determine wether it is an airline's delays
            we're taking to account or a airport's.
        atrasos : Pandas DataFrame
            A DataFrame that shows how many times an airline or airport
            had a delay, False being all the times it didn't and True
            being all the times it did have a delay.
        mean : boolean, default True
            Mean is a boolean to check wether we're doing the mean or
            the ration
        vals : Pandas DataFrame, default None
            A Pandas Dataframe that shows how many minutes a flight has
            been delayed per airport or airline. The default is None
            because you only need it to calculate the mean of deyals

        Returns
        -------
        delay : Pandas DataFrame
            A list with all of the delays, ordered by the
            order they came in.
        ratio : Pandas DataFrame
            A list with all of the ratios, ordered by the
            order they came in.

        Does
        -------
        Calculates the mean of delays or the ratio of delays by a
        company or airline and pre-organizes the DataFrame given.
        
        """
        if mean==True:
            delay=(vals/atrasos[1]).tolist()
            return delay 
        else:
            ratio=(atrasos[1]/atrasos["soma"]).tolist()
            return ratio

