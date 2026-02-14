"""
I.Zagorodnov and S.Tomin, 03.2018.
"""

import numpy as np

c = 299792458
Z0 = 3.767303134695850e02
a = 10  # in mm half gap
y0 = 9.5  # in mm POSITION of the charge CHANGE ONLY THIS PARAMETER
# now distance from the plate 500um = a-y0
L = 1  # in m
D = 20  # in mm
y = y0
x0 = D / 2
x = x0
sigma = 0.03  # in mm

Nm = 300
dir_out = ""

s = np.arange(0, 50 + 0.01, 0.01) * sigma


ns = len(s)

t = 0.25
p = 0.5
t2p = t / p
alpha = 1 - 0.465 * np.sqrt(t2p) - 0.07 * t2p
# s0r_fit=0.41*a**1.8*0.25^1.6/0.5^2.4;
s0r_bane = a * a * t / (2 * np.pi * alpha**2 * p**2)
s0r_igor = s0r_bane * np.pi / 4
s0 = 4 * s0r_igor


W = np.zeros(ns)

dWdx0 = np.zeros(ns)
dWdy0 = np.zeros(ns)
dWdx = np.zeros(ns)
dWdy = np.zeros(ns)
ddWdx0dx0 = np.zeros(ns)  # h11
ddWdy0dx0 = np.zeros(ns)  # h12=0
ddWdxdx0 = np.zeros(ns)
ddWdxdy0 = np.zeros(ns)  # h13 h23=0
ddWdydx0 = np.zeros(ns)
ddWdydy0 = np.zeros(ns)
ddWdydx = np.zeros(ns)  # %h14=0 h24 h34=0

Fz = np.zeros((Nm, ns))
Fyd = np.zeros((Nm, ns))
A = Z0 * c / (2 * a) * L
f = []
for i in np.arange(Nm):
    m = i + 1
    # f[i] = np.pi/D*m
    M = np.pi / D * m
    X = M * a
    dx = np.sin(M * x0) * np.sin(M * x)
    Wcc = (
        A
        * X
        / (np.cosh(X) * np.sinh(X))
        * np.exp(-((s / s0) ** 0.5) * (X / np.tanh(X)))
    )
    print(i, X)
    Wss = (
        A
        * X
        / (np.cosh(X) * np.sinh(X))
        * np.exp(-((s / s0) ** 0.5) * (X * np.tanh(X)))
    )

    Fz[i, :] = Wcc * np.cosh(M * y) * np.cosh(M * y0) + Wss * np.sinh(M * y) * np.sinh(
        M * y0
    )

    dW = Fz[i, :] * dx
    W = W + dW
    ddx0 = np.cos(M * x0) * np.sin(M * x)
    dWdx0 = dWdx0 + M * Fz[i, :] * ddx0
    ddy0 = Wcc * np.cosh(M * y) * np.sinh(M * y0) + Wss * np.sinh(M * y) * np.cosh(
        M * y0
    )
    dWdy0 = dWdy0 + M * ddy0 * dx
    ddx = np.sin(M * x0) * np.cos(M * x)
    dWdx = dWdx + M * Fz[i, :] * ddx
    ddy = Wcc * np.sinh(M * y) * np.cosh(M * y0) + Wss * np.cosh(M * y) * np.sinh(
        M * y0
    )
    dWdy = dWdy + M * ddy * dx
    Fyd[i, :] = M * ddy * dx
    ddWdx0dx0 = ddWdx0dx0 - M**2 * dW
    # Fyq[i, :] = M ** 2 * Fz[i,:]
    ddWdy0dx0 = ddWdy0dx0 + M**2 * (ddy0 * ddx0)
    ddWdxdx0 = ddWdxdx0 + M**2 * Fz[i, :] * np.cos(M * x0) * np.cos(M * x)
    ddWdxdy0 = ddWdxdy0 + M**2 * ddy0 * ddx
    ddWdydx0 = ddWdydx0 + M**2 * ddy * ddx0
    ddWdydy0 = (
        ddWdydy0
        + M**2
        * (
            Wcc * np.sinh(M * y) * np.sinh(M * y0)
            + Wss * np.cosh(M * y) * np.cosh(M * y0)
        )
        * dx
    )
    ddWdydx = ddWdydx + M**2 * ddy * ddx


# subplot(3,1,1)
# if Nm>1, mesh(s,f,Fz(:,:)); end;
# zlabel('W_z(k,s)[V/pC]');xlabel('s[mm]');ylabel('k[1/mm]');
# title(['offsets[mm]: y0=' num2str(y0*1e3) ' y=' num2str(y*1e3) ' x0=' num2str(x0*1e3)  ' x=' num2str(x*1e3)]);

W = W * 2 / D * 1e6
h00 = W
dWdx0 = dWdx0 * 2 / D * 1e9
h01 = dWdx0
dWdy0 = dWdy0 * 2 / D * 1e9
h02 = dWdy0
dWdx = dWdx * 2 / D * 1e9
h03 = dWdx
dWdy = dWdy * 2 / D * 1e9
h04 = dWdy
ddWdx0dx0 = ddWdx0dx0 * 2 / D * 1e12
h11 = ddWdx0dx0 * 0.5
ddWdy0dx0 = ddWdy0dx0 * 2 / D * 1e12
h12 = ddWdy0dx0 * 0.5
ddWdxdx0 = ddWdxdx0 * 2 / D * 1e12
h13 = ddWdxdx0 * 0.5
ddWdydx0 = ddWdydx0 * 2 / D * 1e12
h14 = ddWdydx0 * 0.5
ddWdxdy0 = ddWdxdy0 * 2 / D * 1e12
h23 = ddWdxdy0 * 0.5
ddWdydy0 = ddWdydy0 * 2 / D * 1e12
h24 = ddWdydy0 * 0.5
ddWdydx = ddWdydx * 2 / D * 1e12
h34 = ddWdydx * 0.5

h33 = h11

print(h00)


# subplot(3,1,2)
# plot(s,h00*1e-15);ylabel('W_z[MV/nC]');xlabel('s[mm]');xlim([0,0.1]);
# subplot(3,1,3)
##%Wd=-IntegrTr(s(2)-s(1),h04)*1e-3;
##%plot(s,Wd*1e-15);ylabel('Wd[MV/nC/m]');xlabel('s[mm]');xlim([0,0.1]);
##%Wq=-IntegrTr(s(2)-s(1),2*h33)*1e-6;
##%plot(s,Wq*1e-15);ylabel('Wq[MV/nC/m]');xlabel('s[mm]');xlim([0,0.1]);

"""
s=s*1e-3;
N=len(s);

out00=[N 0; 0 0; 0 0; [s;h00]'];
out02=[N 0; 0 0; 0 2; [s;h02]'];
out04=[N 0; 0 0; 0 4; [s;h04]'];
out11=[N 0; 0 0; 0 11;[s;h11]'];
out13=[N 0; 0 0; 0 13;[s;h13]'];
out24=[N 0; 0 0; 0 24;[s;h24]'];
out33=[N 0;0 0; 0 33;[s;h33]'];
      
out=[[7 0];out00;out02;out04;out11;out13;out24;out33];
save([dir_out 'wake_hor_1m_800um.txt'],'out','-ascii');
out11=[N 0; 0 0; 0 11; [s;-h11]'];
out33=[N 0; 0 0; 0 33; [s;-h33]'];
out01=[N 0; 0 0; 0 1; [s;h02]'];
out03=[N 0; 0 0; 0 3; [s;h04]'];
out13=[N 0; 0 0; 0 13; [s;h24]'];
out24=[N 0; 0 0; 0 24; [s;h13]'];


out=[[7 0];out00;out01;out03;out11;out13;out24;out33];
save([dir_out 'wake_vert_1m_800um.txt'],'out','-ascii');
"""
