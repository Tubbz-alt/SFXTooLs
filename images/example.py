from imagestack import *

fcxi = "/reg/d/psdm/cxi/cxitut13/scratch/zhensu/psocake/r0010/cxitut13_0010.cxi"

ch2stkx,ch2stky,ch2stkz = mapcheetch2stack(experimentName="cxitut13",detInfo="DscCsPad")
xraw,yraw = getBragg4pcxi(fcxi,pidx=None,eventInd=233) 

peaks = np.zeros((len(xraw),3))
peaks[:,0] = ch2stkx[xraw,yraw]
peaks[:,1] = ch2stky[xraw,yraw]
peaks[:,2] = ch2stkz[xraw,yraw]

#################################



iX = np.load('./gpuIndexing/cxitut13_iX.npy')
iY = np.load('./gpuIndexing/cxitut13_iY.npy')

cx = 877 # self.parent.cx
cy = 864 # self.parent.cy

photonEnergy = 8.06 # keV
D = 0.158 # m
pixSize = 110e-6 # m
wavelength = 12.407002 / float(photonEnergy) * 1e-10  # m

cenX = iX[np.array(peaks[:, 0], dtype=np.int64),
          np.array(peaks[:, 1], dtype=np.int64),
          np.array(peaks[:, 2], dtype=np.int64)]  # pixels
cenY = iY[np.array(peaks[:, 0], dtype=np.int64),
          np.array(peaks[:, 1], dtype=np.int64),
          np.array(peaks[:, 2], dtype=np.int64)]  # pixels

#strongInd = np.where(cenX > 500) and np.where(cenX < 1100) and np.where(cenY > 500) and np.where(cenY < 1100)
#cenX = cenX[strongInd]
#cenY = cenY[strongInd]

Xd = (cenX - cx) * pixSize # m
Yd = (cenY - cy) * pixSize # m
r = np.sqrt(Xd**2 + Yd**2 + D**2) # m
s = np.array([D/r-1, Xd/r, Yd/r]) / (wavelength) # m^-1