from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_pelaaja_vs_tekoaly import KPSPelaajaVsTekoaly

from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

def kaksinpeli():
    return KPSPelaajaVsPelaaja()

def yksinpeli_tekoaly():
    return KPSPelaajaVsTekoaly(Tekoaly())

def yksinpeli_parannettu_tekoaly():
    return KPSPelaajaVsTekoaly(TekoalyParannettu())
