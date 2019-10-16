import psana
import h5py
import numpy as np


def getBragg4cxi(fcxi):
    
    return posBragg

def points22d(experimentName, ):
    
    return 

def stack2image(stack=None,experimentName=None,runNumber=None,detInfo=None,eventInd=0):
    ds = psana.DataSource('exp='+str(experimentName)+':run='+str(runNumber)+':idx')
    run = ds.runs().next()
    times = run.times()
    env = ds.env()
    evt = run.event(times[0])
    det = psana.Detector(str(detInfo), env)
    evt = run.event(times[eventInd])
    image = det.image(evt,stack)
    return image

def image2stack(image=None,experimentName=None,runNumber=None,detInfo=None,eventInd=0):

    ds = psana.DataSource('exp='+str(experimentName)+':run='+str(runNumber)+':idx')
    run = ds.runs().next()
    times = run.times()
    env = ds.env()
    evt = run.event(times[0])
    det = psana.Detector(str(detInfo), env)

    evt = run.event(times[eventInd]) 

    stack = det.ndarray_from_image(par=evt, image=image, pix_scale_size_um=None, xy0_off_pix=None)
    return stack 


def display(image,clim=None):
    import matplotlib.pyplot as plt 
    plt.figure(figsize=(8,8))
    if clim is None:
        plt.imshow(image[:,::-1].T)
    plt.imshow(image[:,::-1].T, clim=clim)
    plt.tight_layout()
    plt.show()

