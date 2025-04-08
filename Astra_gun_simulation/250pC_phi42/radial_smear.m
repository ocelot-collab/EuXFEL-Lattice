name_in='cath.ini';
name_out='cath_smear.ini';
P=load(name_in);
r=sqrt(P(:,1).^2+P(:,2).^2);
figure(1); subplot(2,1,1); hist(r,100);

x_smear=0.10; % particles to be smeared
r_max=max(r); r_smear=r_max*sqrt(1-x_smear);
L_smear=r>r_smear;
rs=r;
fun=@(x) 2*r_max-r_smear-sqrt(4*(r_max-x)*(r_max-r_smear));
rs(L_smear)=fun(r(L_smear));

%subplot(2,1,2); hist(rs,200);

P(L_smear,1)=P(L_smear,1).*rs(L_smear)./r(L_smear);
P(L_smear,2)=P(L_smear,2).*rs(L_smear)./r(L_smear);
rs=sqrt(P(:,1).^2+P(:,2).^2);
subplot(2,1,2); hist(rs,200);

disp(['writing ' name_out])
save(name_out,'P','-ascii','-double');
disp('finished')