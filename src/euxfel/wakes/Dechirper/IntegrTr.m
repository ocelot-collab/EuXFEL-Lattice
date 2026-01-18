function y=IntegrTr(h,x)
n=length(x);	
y(1:n,1)=0;
for j=2:n,
	y(j)=y(j-1)+0.5*(x(j)+x(j-1));
end;
y=y*h;