#!/usr/bin/env python3
"""Original closed titanium band, projected and shaded into a portable SVG."""
from pathlib import Path
from math import sin,cos,pi,copysign,sqrt
N,M=128,32
ax,ay,az=.83,-.22,-.35

def rotate(p):
 x,y,z=p;y,z=y*cos(ax)-z*sin(ax),y*sin(ax)+z*cos(ax);x,z=x*cos(ay)+z*sin(ay),-x*sin(ay)+z*cos(ay)
 return x*cos(az)-y*sin(az),x*sin(az)+y*cos(az),z

def point(u,v):
 c,s=cos(v),sin(v);r=1+.155*copysign(abs(c)**.38,c)
 return rotate((r*cos(u),r*sin(u),.235*copysign(abs(s)**.38,s)))
pts=[point(i/N*2*pi,j/M*2*pi) for i in range(N) for j in range(M)]
faces=[]
for i in range(N):
 for j in range(M):
  ids=[i*M+j,((i+1)%N)*M+j,((i+1)%N)*M+(j+1)%M,i*M+(j+1)%M]
  a,b,c=[pts[k] for k in ids[:3]];v=[b[k]-a[k] for k in range(3)];w=[c[k]-a[k] for k in range(3)]
  n=[v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0]];l=sqrt(sum(x*x for x in n)) or 1;n=[x/l for x in n]
  # Broad environment light plus narrow softbox highlights on a closed band.
  diffuse=max(0,n[0]*-.4+n[1]*-.55+n[2]*.7)
  strip=max(0,n[0]*.2+n[1]*-.65+n[2]*.73)**22
  rim=max(0,n[0]*-.8+n[1]*.15+n[2]*.58)**12
  shade=.25+diffuse*.63+rim*.38
  col=[min(255,round(c*shade+strip*120)) for c in [185,190,183]]
  # Recessed optical windows on the inside surface, integrated into the mesh.
  if 11<=j<=14 and i in [15,16,17,42,43,44,69,70,71,96,97,98]:
   col=[38,48,40] if j in [11,14] else [77,132,92]
  p=[]
  for k in ids:
   x,y,z=pts[k];pers=3.8/(3.8-z);p.append((360+x*210*pers,282+y*210*pers))
  d='M'+'L'.join(f'{x:.2f},{y:.2f}' for x,y in p)+'Z'
  faces.append((sum(pts[k][2] for k in ids)/4,d,'#'+''.join(f'{c:02x}' for c in col)))
faces.sort()
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 600" role="img" aria-labelledby="title desc"><title id="title">Oura Ring 4 titanium form study</title><desc id="desc">Original three-dimensional illustration of a continuous silver titanium band with recessed optical windows.</desc><defs><radialGradient id="bg"><stop stop-color="#4a5442"/><stop offset="1" stop-color="#30372e"/></radialGradient><radialGradient id="shadow"><stop stop-color="#141a13" stop-opacity=".65"/><stop offset="1" stop-color="#141a13" stop-opacity="0"/></radialGradient></defs><rect width="720" height="600" rx="16" fill="url(#bg)"/><g stroke="#c5cfb7" opacity=".06"><path d="M0 150H720M0 300H720M0 450H720M180 0V600M360 0V600M540 0V600"/></g><ellipse cx="360" cy="480" rx="235" ry="42" fill="url(#shadow)"/>']
for _,d,c in faces:svg.append(f'<path d="{d}" fill="{c}" stroke="{c}" stroke-width=".55" stroke-linejoin="round"/>')
svg.append('<text x="36" y="555" fill="#f2e8d2" font-family="monospace" font-size="24" letter-spacing="1">TITANIUM / ORIGINAL 3D FORM STUDY</text></svg>')
path=Path(__file__).resolve().parents[1]/'dist/assets/ring-poster.svg';path.write_text(''.join(svg));print('Built continuous ring illustration:',path.stat().st_size,'bytes')
