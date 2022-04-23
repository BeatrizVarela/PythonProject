# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:15:17 2020

__author__: Miguel Correia e Ana Beatriz Varela

This module contains only one function (plotter), that function plots 4 graphs
within one plot, all of them corresponding to the same year and month, one 
graph contains the mean of delays per company , another contains the ratio
of delays per company, another contains the mean of delays per destined airport
and the last one contains the ratio of delays per destined airport.
"""


import matplotlib.pyplot as plt

def plotter(atrasos_comp,racio_comp,atrasos_aero,racio_aero,month,year):
        """
        Parameters
        ----------
        atrasos_comp : Pandas Dataframe
            A DataFrame with the mean of the delays per airline.
        racio_comp : Pandas DataFrame
            A DataFrame with the ratio of delays per airline.
        atrasos_aero : Pandas Dataframe
            A DataFrame with the mean of the delays per airport.
        racio_aero : Pandas DataFrame
            A DataFrame with the ratio of delays per airport.
        month : Int
            An intiger with the month of the data we're plotting.
        year : Int
            An intiger with the year of the data we're plotting

        Returns
        -------
        A plot with four plotted graphs, each representing the mean, or
        ratio, of delays of an airline, or company.

        """
        month_str={1:'janeiro',2:'fevereiro',3:'março',4:'abril',5:'maio',
                   6:'junho',7:'julho',8:'agosto',9:'setembro',10:'outubro',
                   11:'novembro',12:'dezembro'}
        plt.subplots(2, 2, figsize=(8, 5), tight_layout=True)
        Params={'xtick.labelsize':9,'xtick.top':True,
                'xtick.direction':'in','ytick.right':True,
                'ytick.direction':'in','ytick.labelright':False}
        for i in Params:
            plt.rcParams[i]
        plt.subplot(2,2,1)
        comps=atrasos_comp.index.tolist()
        atrasos=atrasos_comp["Minutos Atrasados"].tolist()
        plt.bar(comps,atrasos,edgecolor="black",color="pink")
        plt.title("Atraso médio por companhia (top 10)",fontsize=9)
        plt.xticks([0,1,2,3,4,5,6,7,8,9], comps, rotation=30)
        plt.yticks([0,20,40,60],[0,20,40,60])
        plt.subplot(2,2,2)
        comps_rat=racio_comp.index.tolist()
        racio_c=racio_comp["Racio"].tolist()
        plt.bar(comps_rat,racio_c,edgecolor="black",color="pink")
        plt.title("Voos atrasados por companhia (top 10)",fontsize=9)
        plt.xticks([0,1,2,3,4,5,6,7,8,9], comps_rat, rotation=30)
        plt.subplot(2,2,3)
        aero=atrasos_aero.index.tolist()
        atraso_a=atrasos_aero["Minutos Atrasados"].tolist()
        plt.bar(aero,atraso_a,edgecolor="black",color="pink")
        plt.xticks([0,1,2,3,4,5,6,7,8,9], aero, rotation=30)
        plt.subplot(2,2,4)
        aero_rat=racio_aero.index.tolist()
        racio_a=racio_aero["Racio"].tolist()
        plt.bar(aero_rat,racio_a,edgecolor="black",color="pink")
        plt.title("Voos atrasados por aeroporto (top 10)",fontsize=9)
        plt.xticks([0,1,2,3,4,5,6,7,8,9], aero_rat, rotation=30)
        plt.suptitle("Atrasos à chegada na aviação comercial ("+month_str[month]+" de "+str(year)+")",fontsize=8)
        plt.show()
        