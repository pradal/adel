""" Provides sample data for testing Adel without reference to file paths, nor needs to call package manager
"""

import os

datadir = os.path.dirname(__file__)

def leaves_db():
    import cPickle as Pickle
    import alinea.adel.fitting as fitting
    fn = datadir + '/data/leaves_simple.db'
    f = open(fn)
    leaves = Pickle.load(f)
    f.close()
    leaves,discard = fitting.fit_leaves(leaves, 9)
    return leaves
    
def devT():
    from alinea.adel.AdelR import devCsv
    
    axeT = datadir + '/data/axeTCa0N.csv'
    dimT = datadir + '/data/dimTCa0N.csv'
    phenT = datadir + '/data/phenTCa0N.csv'
    earT = datadir + '/data/earTCa0N.csv'
    ssisenT = datadir + '/data/ssi2sen.csv'
    
    return devCsv(axeT,dimT,phenT,earT,ssisenT)
    
def srdb():
    return datadir + '/data/SRSo.RData'
    
def xydb():
    return datadir + '/data/So99.RData'
    
def wheat_leaf_db():
    from alinea.adel.wheat.extract_wheat import extract_leaf_info
    import alinea.adel.fitting as fitting
    leaves= extract_leaf_info(xydb(),srdb())
    leaves,discard = fitting.fit_leaves(leaves, 9)
    return leaves

from alinea.adel.newmtg import mtg_factory, adel_metamer
from alinea.adel.mtg_interpreter import mtg_interpreter
from alinea.adel.stand.stand import regular

def adel_two_metamers(leaf_sectors = 1):
    """ create a very simple adel mtg """

    d = {'plant':[1,1],'axe_id':['MS','T1'],'ms_insertion':[0,1],'numphy':[1,1], 
         'Laz': [0,90], 'Ll' :[3,3], 'Lv' :[3,3] ,'Lr':[0,0], 'Lsen':[0,0], 'L_shape':[3,3], 'Lw_shape':[.3,.3], 'Linc':[0,0],
         'Einc':[0,45],'El':[1,1],'Ev':[1,1],'Esen':[0,0],'Ed': [0.1,0.1],'Gd': [0.1,0.1]}
    g=mtg_factory(d,adel_metamer,leaf_db=leaves_db(), leaf_sectors=leaf_sectors)
    g=mtg_interpreter(g)
    return g
    
def adel_two_metamers_stand(leaf_sectors = 1, inter_row=0.2, density = 150, convunit=100):
    """ create a very simple adel mtg """

    d = {'plant':[1,1],'axe_id':['MS','T1'],'ms_insertion':[0,1],'numphy':[1,1], 
         'Laz': [0,90], 'Ll' :[3,3], 'Lv' :[3,3] ,'Lr':[0,0], 'Lsen':[0,0], 'L_shape':[3,3], 'Lw_shape':[.3,.3], 'Linc':[0,0],
         'Einc':[0,45],'El':[1,1],'Ev':[1,1],'Esen':[0,0],'Ed': [0.1,0.1],'Gd': [0.1,0.1]}
    
    inter_plant = 1. / inter_row / density
    dx = inter_plant * convunit
    dy = inter_row * convunit
    positions, domain = regular(1, 1, dx, dy)
    xc = float(domain[1][0] + domain[0][0]) / 2
    yc = float(domain[1][1] + domain[0][1]) / 2
    positions = [(x - xc, y - yc, z) for x,y,z in positions]
    domain = ((domain[0][0] - xc,domain[0][1] - yc),(domain[1][0] - xc,domain[1][1] - yc))
    domain_area = abs(domain[1][0] - domain[0][0]) / convunit * abs(domain[1][1] - domain[0][1]) / convunit

    g=mtg_factory(d,adel_metamer,leaf_db=leaves_db(), leaf_sectors=leaf_sectors,stand=[(positions[0],0)])
    g=mtg_interpreter(g)
    
    
    return g, domain_area, domain, 1. / convunit
    
def adel_one_leaf(leaf_sectors=1):
    """ create a very simple adel mtg """
    d = {'plant':[1],'axe_id':['MS'],'ms_insertion':[0],'numphy':[1], 
         'Laz': [0], 'Ll' :[3], 'Lv' :[3] , 'Lr': [0], 'Lsen':[0], 'L_shape':[3], 'Lw_shape':[.3], 'Linc':[0],
         'Einc':[0],'El':[0],'Ev':[0],'Esen':[0],'Ed': [0.1],'Gd': [0.1]}
    g=mtg_factory(d,adel_metamer,leaf_db=leaves_db(),leaf_sectors=leaf_sectors)
    g=mtg_interpreter(g)
    return g

def adel_one_leaf_element():
    """ create a very simple adel mtg """
    d = {'plant':[1],'axe_id':['MS'],'ms_insertion':[0],'numphy':[1], 
         'Laz': [0], 'Ll' :[3], 'Lv' :[3] , 'Lr': [0], 'Lsen':[0], 'L_shape':[3], 'Lw_shape':[.3], 'Linc':[0],
         'Einc':[0],'El':[0],'Ev':[0],'Esen':[0],'Ed': [0.1],'Gd': [0.1]}
    g=mtg_factory(d,adel_metamer,leaf_db=leaves_db(), leaf_sectors=1)
    g=mtg_interpreter(g)
    g.remove_vertex(13)
    labels = g.property('label')
    labels[13] = 'Removed'
    return g
