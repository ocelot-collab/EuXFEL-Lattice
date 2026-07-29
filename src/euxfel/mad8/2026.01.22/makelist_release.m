function [list] = makelist_release

%!mad8 < xfel_run.txm

%load rooms
%[~,~,txt] = xlsread('N:\wdecking\My Documents\XFEL\lattice\XFELSVN\branches\version7\Rooms.xlsx');
[~,~,txt] = xlsread('Rooms.xlsx');
rooms.NAME = txt(:,1);
rooms.Zmin = txt(:,2);
rooms.Zmax = txt(:,3);
rooms.BRANCH = txt(:,4);
rooms.PBRANCH = txt(:,5);

files = {'T4D','T5D','TLD','G1D','I1D','B1D','B2D','T6','T7','T8','T9','T10'}; %,'T8E'}; %,'T20'};

% files = {'T4D', 'T5D','T8','T8E'}; %,'T20'};


longlist = struct('SECTION',[],'SUBSECTION',[],'CADRoom',[],'NAME1',[],'NAME2',[],'GROUP',[],'CLASS',[],'TYPE',[],...
    'L',[],'KXL',[],'TILT',[],'E1',[],'E2',[],...
    'S',[],'X',[],'Y',[],'Z',[],'ST',[],'THETA',[],'PHI',[],'CHI',[],...
    'XPD',[],'YPD',[],'ZPD',[],'THETAPD',[],'PHIPD',[],'CHIPD',[],...
    'ENERGY',[],'BETX',[],'ALFX',[],'MUX',[],'BETY',[],'ALFY',[],'MUY',[],'DX',[],'DPX',[],'DY',[],'DPY',[],...
    'XAP',[],'YAP',[]);

% read files
for ifile = 1 : length(files)
    listname=['list_' files{ifile}];
    longlistfile = ['LONGLIST_' files{ifile} '.dat'];
    magnetfile = ['TWISS_' files{ifile}]
    layoutfile = ['SURVEY_' files{ifile}];
    
    % create structure
    list = struct('SECTION',[],'SUBSECTION',[],'CADRoom',[],'NAME1',[],'NAME2',[],'GROUP',[],'CLASS',[],'TYPE',[],...
        'L',[],'KXL',[],'TILT',[],'E1',[],'E2',[],...
        'S',[],'X',[],'Y',[],'Z',[],'ST',[],'THETA',[],'PHI',[],'CHI',[],...
        'XPD',[],'YPD',[],'ZPD',[],'THETAPD',[],'PHIPD',[],'CHIPD',[],...
        'ENERGY',[],'BETX',[],'ALFX',[],'MUX',[],'BETY',[],'ALFY',[],'MUY',[],'DX',[],'DPX',[],'DY',[],'DPY',[],...
        'XAP',[],'YAP',[]);
    
    ds =0;
    xaper=0.035;
    yaper=0.035;
    newsub = 0;
    icav = 0;
    icirch = 0;
    icircv = 0;
    
    magnets = read_survey_raw(magnetfile);
    layout  = read_survey_raw(layoutfile);
    
    % remove first line of input
    layout = layout(2:end);
    magnets= magnets(2:end);
    % remove rot elements if any
    layout = layout(strncmp('ROT',{layout.NAME},3)==0);
    
    switch files{ifile}
        case 'T6'
            newstart = find(strncmp('STSEC.T6.T6',{layout.NAME},11));
            layout = layout(newstart:end);
            magnets= magnets(newstart:end);
        case 'T7'
            newstart = find(strncmp('STSEC.T7.T7',{layout.NAME},11));
            layout = layout(newstart:end);
            magnets= magnets(newstart:end);
        case 'T8'
            newstart = find(strncmp('STSEC.T8.T8',{layout.NAME},11));
            layout = layout(newstart:end);
            magnets= magnets(newstart:end);
        case 'T9'
            newstart = find(strncmp('STSEC.T9.T9',{layout.NAME},11));
            layout = layout(newstart:end);
            magnets= magnets(newstart:end);
        case 'T10'
            newstart = find(strncmp('STSEC.T10.T10',{layout.NAME},13));
            layout = layout(newstart:end);
            magnets= magnets(newstart:end);
    end
    
    
    %    istart = nameparser('NAME',start{ifile},layout);
    %    layout = layout(istart:end);
    %    istart = nameparser('NAME',start{ifile},magnets);
    %    magnets = magnets(istart:end);
    
    
    for i = 1:length(layout)
        if strcmp('DRIF',layout(i).KEYWORD) & strncmp(layout(i).NAME, 'DU',2)
            layout(i).KEYWORD = 'DUMP';
        elseif strcmp('MARK',layout(i).KEYWORD) & strncmp(layout(i).NAME, 'DU',2)
            layout(i).KEYWORD = 'DUMP';
        elseif strcmp('MARK',layout(i).KEYWORD) & strfind(layout(i).NAME, 'U40S')
            layout(i).KEYWORD = 'UNDULATOR';
        elseif strcmp('MARK',layout(i).KEYWORD) & strfind(layout(i).NAME, 'U68S')
            layout(i).KEYWORD = 'UNDULATOR';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'U40')
            layout(i).KEYWORD = 'UNDULATOR';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'U68')
            layout(i).KEYWORD = 'UNDULATOR';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'UE90')
            layout(i).KEYWORD = 'UNDULATOR';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'U74')
            layout(i).KEYWORD = 'UNDULATOR';    
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'SCU')
            layout(i).KEYWORD = 'UNDULATOR';
        elseif strcmp('MARK',layout(i).KEYWORD) & strfind(layout(i).NAME, 'U00')
            layout(i).KEYWORD = 'UNDPLACEH';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'BPS')
            layout(i).KEYWORD = 'PHASESHIFTER';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'ABSP')
            layout(i).KEYWORD = 'ABSORBER';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME, 'ABSP4')
            layout(i).KEYWORD = 'ABSORBER';
        elseif strcmp('MATR',layout(i).KEYWORD)
            %                 [strfind(layout(i).NAME, 'SA1_M') strfind(layout(i).NAME, 'SA2_M') ...
            %                  strfind(layout(i).NAME, 'SA3_M') strfind(layout(i).NAME, 'U40S')]
            layout(i).KEYWORD = 'UNDULATOR';
            layout(i).L = magnets(i).S-magnets(i-1).S;
            %         elseif strcmp('MATR',layout(i).KEYWORD) & ...
            %                 [strfind(layout(i).NAME, 'EX') strfind(layout(i).NAME, 'EN')]
            %             layout(i).KEYWORD = 'COUPLER';
        elseif strcmp('DRIF',layout(i).KEYWORD) & ...
                [strfind(layout(i).NAME,'CFBI') strfind(layout(i).NAME,'CTBI')  ...
                strfind(layout(i).NAME,'CTB') strfind(layout(i).NAME,'CFB') ...
                strfind(layout(i).NAME,'CSC')]
            layout(i).KEYWORD = 'CRYO';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strncmp(layout(i).NAME,'V',1)
            layout(i).KEYWORD = 'VAC';
        elseif strcmp('MARK',layout(i).KEYWORD) & ...
             [strfind(layout(i).NAME,'VCCHIRP') strfind(layout(i).NAME,'VV0')]
            layout(i).KEYWORD = 'VAC';
        elseif strcmp('MARK',layout(i).KEYWORD) & strncmp(layout(i).NAME,'VCST',4)
            layout(i).KEYWORD = 'VACSTEP';
        elseif strcmp('MARK',layout(i).KEYWORD) & ...
                [strfind(layout(i).NAME,'BAM') strfind(layout(i).NAME,'DCM')  ...
                strfind(layout(i).NAME,'OTR') strfind(layout(i).NAME,'SCRN') ...
                strfind(layout(i).NAME,'SRM') strfind(layout(i).NAME,'CHR') ...
                strfind(layout(i).NAME,'PYR') strfind(layout(i).NAME,'EOD') ...
                strfind(layout(i).NAME,'CRD') strfind(layout(i).NAME,'WIR') ...
                strfind(layout(i).NAME,'FCUP') strfind(layout(i).NAME,'SCRW') ...
                strfind(layout(i).NAME,'BHM')  strfind(layout(i).NAME,'BCM') ...
                strfind(layout(i).NAME,'SPEC')]
            layout(i).KEYWORD = 'INSTR';    
        elseif strcmp('MARK',layout(i).KEYWORD) & ...
                [strfind(layout(i).NAME,'TOR')]
            layout(i).KEYWORD = 'CM';
        elseif strcmp('MARK',layout(i).KEYWORD) & ...
                [strfind(layout(i).NAME,'MONO') strfind(layout(i).NAME,'RRM') ...
                strfind(layout(i).NAME,'PDIO') strfind(layout(i).NAME,'MIRR') ...
                strfind(layout(i).NAME,'ODL')]
            layout(i).KEYWORD = 'PHOTON';
            %        elseif strcmp('MARK',layout(i).KEYWORD) & strncmp(layout(i).NAME,'BPM',3)
            %            layout(i).KEYWORD = 'MONI';
            %elseif strcmp('RBEN',layout(i).KEYWORD) & strfind(layout(i).NAME,'BY')
            %    layout(i).KEYWORD = 'SEPTUM';
        elseif strcmp('KICK',layout(i).KEYWORD) & strfind(layout(i).NAME,'SWEEP')
            layout(i).KEYWORD = 'SWEEPER';
        elseif strcmp('DRIF',layout(i).KEYWORD) & strfind(layout(i).NAME,'BSEC') %#ok<*AND2>
            layout(i).KEYWORD = 'BSEC';
        end
    end
    
    % remove couplerkic elements
    %     inocoupler = find(strcmp('COUPLER',{layout.KEYWORD})==0);
    %     layout = layout(inocoupler);
    %     magnets = magnets(inocoupler);
    
    % reduce size of magnet structure to corresponding layout structure
    % magnets = magnets(min(nameparser('NAME',layout(1).NAME,magnets)):max(nameparser('NAME',layout(end).NAME,magnets)));
    
    % find half magnets (ending with H.) and combine to single magnet
    ihalfs = [];
    for i = 1:length(layout);
        if(strfind(layout(i).NAME,'H.') ...
                & isempty(strfind(layout(i).NAME,'QH.')) ...
                & isempty(strfind(layout(i).NAME,'MATCH.')) ...
                & isempty(strfind(layout(i).NAME,'BPMH.')) ...
                & isempty(strfind(layout(i).NAME,'KIH.')))
            ihalfs = [ihalfs i];
            layout(i).NAME =strrep(layout(i).NAME,'H.','.');
            layout(i).L   = 2* layout(i).L;
            layout(i).KXL = 2* layout(i).KXL;
        end
    end
    index = zeros(length(magnets),1);
    index(ihalfs(1:2:end)) = 1;
    magnets = magnets(find(~index));
    layout = layout(find(~index));
    
    %combine layout and magnets into list
    leng = length(magnets);
    
    [list(1:leng).NAME1] = deal(layout.NAME);
    [list(1:leng).NAME2] = deal(layout.NAME);
    [list(1:leng).CLASS] = deal(layout.KEYWORD);
    [list(1:leng).L] = deal(layout.L);
    [list(1:leng).KXL] = deal(layout.KXL);
    [list(1:leng).TILT] = deal(layout.TILT);
    [list(1:leng).E1] = deal(layout.E1);
    [list(1:leng).E2] = deal(layout.E2);
    [list(1:leng).S] = deal(magnets.S);
    [list(1:leng).X] = deal(layout.X);
    [list(1:leng).Y] = deal(layout.Y);
    [list(1:leng).Z] = deal(layout.Z);
    [list(1:leng).THETA] = deal(layout.PHI);   % exchange theta and phi
    [list(1:leng).PHI] = deal(layout.THETA);
    [list(1:leng).CHI] = deal(layout.CHI);
    [list(1:leng).ENERGY] = deal(layout.ENERGY);
    [list(1:leng).BETX] = deal(magnets.BETX);
    [list(1:leng).ALFX] = deal(magnets.ALFX);
    [list(1:leng).MUX] = deal(magnets.MUX);
    [list(1:leng).BETY] = deal(magnets.BETY);
    [list(1:leng).ALFY] = deal(magnets.ALFY);
    [list(1:leng).MUY] = deal(magnets.MUY);
    [list(1:leng).DX] = deal(magnets.DX);
    [list(1:leng).DPX] = deal(magnets.DPX);
    [list(1:leng).DY] = deal(magnets.DY);
    [list(1:leng).DPY] = deal(magnets.DPY);
    
    % create element midpositions
    
    bend = strcmp('RBEN',{list.CLASS});
    bend = bend + strcmp('SBEN',{list.CLASS});
    bendindex = find(bend);
    [index] = find([list(bendindex).KXL] ~= 0);
    bendindex = bendindex(index);
    %    kslindex = find(strcmp('KS',{list.TYPE})+strcmp('KL',{list.TYPE}));
    kslindex = find(strcmp('KSPOS',{list.TYPE})+strcmp('KSNEG',{list.TYPE})...
             +strcmp('KL',{list.TYPE}) +strcmp('KMX',{list.TYPE})+strcmp('KNY',{list.TYPE}));
    bendindex = bendindex(ismember(bendindex,kslindex)==0);
    
    for i = 1:length(bendindex)
        j = bendindex(i) + 4*(i-1);
        list = [list(1:j-1) list(j-1) list(j) list(j) list(j) list(j:end)];
        alpha = list(j+1).KXL;
        la = list(j+1).L;
        tilt = list(j+1).TILT;
        rho = la/alpha;
        [pos_mid pos_arc pos_straight pos_sekant angnew] = bendmidtrans([list(j).X;list(j).Y;list(j).Z],...
            [list(j).PHI;list(j).THETA;list(j).CHI],...
            rho,alpha,tilt,list(j+1).E1,list(j+1).E2);
        
        
        %Bending Magnet Mid Position
        list(j+1).X = pos_mid(1);
        list(j+1).Y = pos_mid(2);
        list(j+1).Z = pos_mid(3);
        list(j+1).PHI=angnew(1);
        list(j+1).THETA = angnew(2);
        list(j+1).CHI = angnew(3);
        list(j+1).S = list(j).S+la/2;
        
        if (strcmp(list(j+1).CLASS,'SBEN'))
            if list(j+1).KXL == 0
                list(j+1).L = list(j+1).L;
            elseif list(j+1).E1 ~= list(j+1).E2
                list(j+1).L = round(1e4*list(j+1).L.*sin(list(j+1).KXL)/list(j+1).KXL)/1e4;
            else
                list(j+1).L = round(1e4*2*list(j+1).L.*sin(list(j+1).KXL/2)./(list(j+1).KXL))/1e4;
                %                             list(j+1).L = round(1e4*list(j+1).L.*sin(list(j+1).KXL)./(list(j+1).KXL))/1e4;
            end
            if list(j+1).E2 == list(j+1).KXL
                list(j+1).PHI=list(j).PHI;
                list(j+1).THETA = list(j).THETA;
            elseif list(j+1).E1 == list(j+1).KXL
                list(j+1).PHI=list(j+2).PHI;
                list(j+1).THETA = list(j+2).THETA;
            end
        end
        
        % create bending magnet name
        newname2 = ['M' list(j+1).NAME1];
        % namepos = floor(list(j+1).Z);
        % newname1 =  [list(j+1).TYPE '.' num2str(namepos) '.' list(j+1).SECTION];
        newname1 = ['M' list(j+1).NAME1];
        
        %Bending Magnet Entrance
        list(j).CLASS = 'BENDIN';
        list(j).L = 0;
        list(j).KXL = deal(0);
        list(j).TILT = deal(0);
        list(j).NAME1 = newname1;
        list(j).NAME2 = newname2;
        
        %Bending Magnet Straight Position
        list(j+2).CLASS = 'BENDSTR';
        list(j+2).L = 0;
        list(j+2).KXL = 0;
        list(j+2).TILT = 0;
        list(j+2).E1 = 0;
        list(j+2).E2 = 0;
        list(j+2).KXL = alpha;
        list(j+2).TILT = tilt;
        list(j+2).E1 = alpha*cos(tilt);
        list(j+2).E2 = alpha*sin(tilt);
        list(j+2).X = pos_straight(1);
        list(j+2).Y = pos_straight(2);
        list(j+2).Z = pos_straight(3);
        list(j+2).S = list(j).S+la/2;
        list(j+2).L = rho*tan(alpha/2);
        list(j+2).NAME1 = newname1;
        list(j+2).NAME2 = newname2;
        
        %Bending Magnet Arc Position
        list(j+3).CLASS = 'BENDARC';
        list(j+3).L = 0;
        list(j+3).KXL = 0;
        list(j+3).TILT = 0;
        list(j+3).E1 = 0;
        list(j+3).E2 = 0;
        list(j+3).X = pos_arc(1);
        list(j+3).Y = pos_arc(2);
        list(j+3).Z = pos_arc(3);
        list(j+3).PHI=angnew(1);
        list(j+3).THETA = angnew(2);
        list(j+3).CHI = angnew(3);
        list(j+3).S = list(j).S+la/2;
        list(j+3).NAME1 = newname1;
        list(j+3).NAME2 = newname2;
        
        %Bending Magnet Exit
        list(j+4).CLASS = 'BENDOUT';
        list(j+4).L = 0;
        list(j+4).KXL = 0;
        list(j+4).TILT = 0;
        list(j+4).E1 = 0;
        list(j+4).E2 = 0;
        list(j+4).NAME1 = newname1;
        list(j+4).NAME2 = newname2;
    end
    
    % remove unwanted drifts and markers
    drif = strcmp('DRIF',{list.CLASS});
    list = list(~drif);
    drif = strcmp('SROT',{list.CLASS});
    list = list(~drif);
    drif = strcmp('YROT',{list.CLASS});
    list = list(~drif);
    
    %
    % correct marker positions for modules
    
    miac = find(strncmp('MIAC',{list.NAME1},4));
    for i = 1:length(miac)
        j = miac(i);
        if (strfind(list(j).NAME2,'AH1')) % shift for 3.9 GHz Module = middle of 2nd cavity (as defined by PP 28.06.11)
            s=-0.3550;
        else
            s=+0.59142;                  % shift for standard XFEL module
        end
        x=0;
        y=0;
        [x, y, z] = rotation3d(list(j).PHI,list(j).THETA,list(j).CHI,x,y,s);
        list(j).X = list(j).X+x;
        list(j).Y = list(j).Y+y;
        list(j).Z = list(j).Z+z;
        list(j).S = list(j).S+s;
    end
    
    
    % correct element positions in undulator
    for i = 1:length(list)
        if contains(list(i).NAME1,'CUX') 
            deltas = 2.5;
        elseif contains(list(i).NAME1,'CUS') 
            deltas = 1.3;
        elseif strfind (list(i).NAME1,'CMVQA')
            deltas = -0.1137/2;
        elseif strfind (list(i).NAME1,'MVUE90')
            deltas = -1.98/2;
        elseif strfind (list(i).NAME1,'CAX')
            deltas = +0.0125;
        elseif strfind (list(i).NAME1,'CAY')
            deltas=-0.0125;
        elseif strfind (list(i).NAME1,'CBX')
            deltas = +0.0125;
        elseif strfind (list(i).NAME1,'CBY')
            deltas=-0.0125;
        else
            deltas=0;
        end
        [x, y, z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,0,0,deltas);
        list(i).X = list(i).X+x;
        list(i).Y = list(i).Y+y;
        list(i).Z = list(i).Z+z;
        list(i).S = list(i).S+deltas;
    end
    
    
    
    % Shift first Solenoid to correct position before cathode (-0.102 m)
    sola = find(strncmp('SOLA',{list.NAME2},4));
    if ~isempty(sola)
        list(sola).Z = list(sola).Z-0.102;
        list(sola).S = list(sola).S-0.102;
    end
    
    nonmark = find([list.L]);
    for i = 1:length(nonmark)
        j = nonmark(i);
        switch list(j).CLASS
            case {'SBEN','RBEN'}
                if list(j).KXL == 0
                    x=0;
                    y=0;
                    z=- list(j).L/2;
                    [x, y, z] = rotation3d(list(j).PHI,list(j).THETA,list(j).CHI,x,y,z);
                    list(j).X = list(j).X+x;
                    list(j).Y = list(j).Y+y;
                    list(j).Z = list(j).Z+z;
                    list(j).S = list(j).S-list(j).L/2;
                end
            case {'BENDSTR'}
            otherwise
                %       if ~strcmp(list(j).CLASS,'SBEN') &  ~strcmp(list(j).CLASS,'RBEN') & ~strcmp(list(j).CLASS,'BENDSTR') % all non bend elemets
                x=0;
                y=0;
                z=- list(j).L/2;
                [x, y, z] = rotation3d(list(j).PHI,list(j).THETA,list(j).CHI,x,y,z);
                list(j).X = list(j).X+x;
                list(j).Y = list(j).Y+y;
                list(j).Z = list(j).Z+z;
                list(j).S = list(j).S-list(j).L/2;
        end
    end
    
    %create Name1 and Name2
    
    for i = 1:length(list)
        
        list(i).NAME1=deblank(list(i).NAME1);
        list(i).NAME2=deblank(list(i).NAME2);
        
        inddum = strfind(list(i).NAME2,'.');
        
        if isempty(inddum)
            [list(i).TYPE] = deblank(list(i).NAME2);
            [list(i).SECTION] = '_';
            [list(i).SUBSECTION] = '_';
        else
            [list(i).TYPE] = deblank(list(i).NAME2(1:min(inddum)-1));
            [list(i).SECTION] = deblank(list(i).NAME2(max(inddum)+1:end));
            [list(i).SUBSECTION] = [list(i).SECTION];
        end
        
        switch list(i).CLASS
            case {'RBEN','SBEN','HKIC','VKIC','KICK','QUAD','SEXT','OCTU','SEPTUM','SWEEP','SOLE'}
                if [strfind(list(i).TYPE,'KS') strfind(list(i).TYPE,'KL') ...
                        strfind(list(i).TYPE,'KAY') strfind(list(i).TYPE,'KDC') ...
                        strfind(list(i).TYPE,'KBY') strfind(list(i).TYPE,'KBX') ...
                        strfind(list(i).TYPE,'KDY') strfind(list(i).TYPE,'KDX') ...
                        strfind(list(i).TYPE,'KAX')]
                    list(i).GROUP = 'FASTKICK';
                elseif [strfind(list(i).TYPE,'KIX') strfind(list(i).TYPE,'KIY')]
                    list(i).GROUP = 'RAMPKICK';
                elseif [strfind(list(i).TYPE,'KJX') strfind(list(i).TYPE,'KJY')]
                    list(i).GROUP = 'RAMPKICK';
                elseif [strfind(list(i).TYPE,'KMX') strfind(list(i).TYPE,'KNY')]
                    list(i).GROUP = 'RAMPKICK';
                elseif [strfind(list(i).TYPE,'KFBX') strfind(list(i).TYPE,'KFBY')]
                    list(i).GROUP = 'FBKICK';
                elseif strfind(list(i).TYPE,'CMV')
                    list(i).GROUP = 'MOVER';
                elseif strfind(list(i).TYPE,'BSEC')
                    list(i).GROUP = 'PMAGNET';
                elseif strfind(list(i).TYPE,'QP')
                    list(i).GROUP = 'PMAGNET';    
                else
                    list(i).GROUP = 'MAGNET';
                    % if magnet, reduce NAME2 to circuit NAME
                    if length(inddum)==3
                        list(i).NAME2=[deblank(list(i).NAME2(1:inddum(2))) deblank(list(i).NAME2(max(inddum)+1:end))];
                    end
                end
            case  {'BENDIN','BENDOUT','BENDSTR','BENDARC'}
                list(i).GROUP = 'MARK';
                list(i).TYPE = 'BENDMARK';
            case {'LCAV'}
                list(i).GROUP = 'CAVITY';
            case {'MONI','INSTR','CM'}
                list(i).GROUP = 'DIAG';
            case{'MARK','SROT','YROT'}
                list(i).GROUP = 'MARK';
            case{'CRYO'}
                list(i).GROUP = 'CRYO';
            case{'ECOL','VAC','ABSORBER','VACSTEP','VV0','VCCHIRP'}
                list(i).GROUP = 'VACUUM';
            case{'UNDULATOR','PHASESHIFTER','UNDPLACEH'}
                list(i).GROUP = 'UNDU';
            case{'DUMP'}
                list(i).GROUP = 'DUMP';
            case{'PHOTON'}
                list(i).GROUP = 'PHOTON';
            otherwise
                list(i).GROUP = 'unknown';
        end
        
        switch list(i).CLASS
            case {'BENDIN'}
                ds = ds;
                ibendin = i;
            case {'SBEN'}
                straightlength=list(i+1).L;
                ds = (list(ibendin).ST-list(ibendin).S)-(list(i).S-list(ibendin).S)+straightlength;
            case {'BENDARC'}
                ds = - list(i).S;
            case {'BENDSTR'}
                straightlength=list(i).L;
                ds = (list(ibendin).ST-list(ibendin).S)-(list(i).S-list(ibendin).S)+straightlength;
                list(i).L = 0;
            case {'BENDOUT'}
                ds = -list(i).S + straightlength;
            otherwise
                ds = ds;
        end
        list(i).ST = list(i).S + ds;
        
        
        %         if length(inddum)==3
        %             list(i).NAME2=[deblank(list(i).NAME2(1:inddum(2))) deblank(list(i).NAME2(max(inddum)+1:end))];
        %         end
        
        if strfind(list(i).NAME2, 'STSUB')
            newsub = 1;
            subsection = deblank(list(i).NAME2(min(inddum)+1:max(inddum)-1));
        elseif  strfind(list(i).NAME2, 'ENSUB')
            newsub = -1;
        end
        if newsub == 1
            [list(i).SUBSECTION] = subsection;
        elseif newsub ==  -1
            [list(i).SUBSECTION] = subsection;
            newsub = 0;
        end
        
        
        if (strncmp(list(i).SECTION,'SA',2) & (strncmp(list(i).TYPE,'CA',2))) % || strncmp(list(i).TYPE,'CB',2)))
            namepos = round(list(i).Z);
        else
            namepos = floor(list(i).Z);
        end
        list(i).NAME1 =  [list(i).TYPE '.' num2str(namepos) '.' list(i).SECTION];
        
        if strfind(list(i).NAME2, 'STAC')
            circ1 = deblank(list(i).NAME2(inddum(1)+1:inddum(3)-1));
            circ2 = deblank(list(i).NAME2(inddum(1)+1:inddum(2)-1));
        end
        
        switch list(i).TYPE
            case {'C','C3'}
                icav = icav+1;
                [list(i).NAME1] = [list(i).TYPE '.' circ1 '.' num2str(icav) '.' list(i).SECTION];
                [list(i).NAME2] = [list(i).TYPE '.' circ2 '.' list(i).SECTION];
                icav = mod(icav,8);
            case {'Q','CX','CY','BPMC','BPMR'}
                [list(i).NAME2] = [list(i).TYPE '.' circ1 '.' list(i).SECTION];
        end
        
        if strfind(list(i).NAME2, 'STSEC')
            icirch = 0;
            icircv = 0;
            icirchCM = 0;
            icircvCM = 0;
        end
        inddum = strfind(list(i).NAME2,'.');
        if length(inddum) == 1
            switch list(i).GROUP
                case {'MAGNET'}
                    switch list(i).CLASS
                        case {'HKIC'}
                            if strfind(list(i).NAME2, 'CMX.T2')
                                icirchCM = icirchCM+1;
                                list(i).NAME2 = [list(i).TYPE '.' num2str(icirchCM) '.' list(i).SECTION];
                            else
                                icirch = icirch+1;
                                list(i).NAME2 = [list(i).TYPE '.' num2str(icirch) '.' list(i).SECTION];
                            end
                        case {'VKIC'}
                            if strfind(list(i).NAME2, 'CMY.T2')
                                icircvCM = icircvCM+1;
                                list(i).NAME2 = [list(i).TYPE '.' num2str(icircvCM) '.' list(i).SECTION];
                            else
                                icircv = icircv+1;
                                list(i).NAME2 = [list(i).TYPE '.' num2str(icircv) '.' list(i).SECTION];
                            end
                    end
            end
        end
        
        
        switch list(i).TYPE
            case {'VCST35T78'} ;xaper=0.078; yaper=0.078;
            case {'VCST78T30'} ;xaper=0.030; yaper=0.030;
            case {'VCST30T78'} ;xaper=0.078; yaper=0.078;
            case {'VCST78T40'} ;xaper=0.04; yaper=0.040;
            case {'VCST40T78'} ;xaper=0.078; yaper=0.078;
            case {'VCST40T35'} ;xaper=0.035; yaper=0.035;
            case {'VCST35T40'} ;xaper=0.040; yaper=0.040;
            case {'VCST40T98'} ;xaper=0.098; yaper=0.098;
            case {'VCST40T93Y'} ;xaper=0.040; yaper=0.093;
            case {'VCST93YT40'} ;xaper=0.040; yaper=0.040;
            case {'VCST40T93X'} ;xaper=0.093; yaper=0.040;
            case {'VCST93XT40'} ;xaper=0.040; yaper=0.040;
            case {'VCST40T98Y'} ;xaper=0.040; yaper=0.098;
            case {'VCST98YT98'} ;xaper=0.098; yaper=0.098;
            case {'VCST98T98Y'} ;xaper=0.040; yaper=0.098;
            case {'VCST98T40'} ;xaper=0.040; yaper=0.040;
            case {'VCST98T200'} ;xaper=0.2; yaper=0.2;
            case {'VCST40T10'} ;xaper=0.015; yaper=0.0088;
            case {'VCST40T60'} ;xaper=0.06; yaper=0.06;
            case {'VCST10T40'} ;xaper=0.04; yaper=0.04;
            case {'VCST40T30'} ;xaper=0.03; yaper=0.03;
            case {'VCST30T40'} ;xaper=0.04; yaper=0.04;
            case {'QA'}; xaper = 0.015; yaper = 0.0088;
            case {'BPS'}; xaper = 0.015; yaper = 0.0088;
            case {'VCST40T400Y'}; xaper = 0.04; yaper = 0.04;
            case {'VCST400Y'}; xaper = 0.04; yaper = 0.4;
            case {'VCST400YT40'}; xaper = 0.04; yaper = 0.04;
            case {'VCST40Y'}; xaper = 0.04; yaper = 0.04;
            case {'VCST10T22'}; xaper = 0.022; yaper = 0.022;
            case {'VCST22T40'}; xaper = 0.04; yaper = 0.04;  
            case {'VCST40T18'}; xaper = 0.018; yaper = 0.018;
            case {'VCST18T40'}; xaper = 0.04; yaper = 0.04; 
        end
        list(i).XAP = xaper;
        list(i).YAP = yaper;
        switch list(i).TYPE
            case {'COLM'}; list(i).XAP = 0.006; list(i).YAP = 0.006;
            case {'COLM4'}; list(i).XAP = 0.004; list(i).YAP = 0.004;
            case {'COLS'}; list(i).XAP = 0.02; list(i).YAP = 0.02;
            case {'BPME'}; list(i).XAP = 0.01; list(i).YAP = 0.01;
            case {'ABSP'}; list(i).XAP = 0.009; list(i).YAP = 0.008;
            case {'ABSP4'}; list(i).XAP = 0.004; list(i).YAP = 0.004;
            case {'ABSP6'}; list(i).XAP = 0.006; list(i).YAP = 0.006;
            case {'QA'}; list(i).XAP = 0.01; list(i).YAP = 0.01;
            case {'CMVQA'}; list(i).XAP = 0.01; list(i).YAP = 0.01;
        end
        
        
        if list(i).Z >= 1994.4920
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
        else
            list(i).XPD=0;
            list(i).YPD=0;
            list(i).ZPD=0;
            list(i).THETAPD=0;
            list(i).PHIPD=0;
            list(i).CHIPD=0;
        end
        
        % check for CADrooms
        if list(i).Z <=2160.296 || list(i).Z>= 3333.31
 %           for j = nameparser('BRANCH','ALL',rooms)
            for j = find(strcmp('ALL', rooms.BRANCH))'
                if list(i).Z > rooms.Zmin{j} && list(i).Z <= rooms.Zmax{j}
                    list(i).CADRoom = rooms.NAME{j};
                end
            end
        else
            list(i).CADRoom = '_';
            switch list(i).SECTION
                case {'T6','T7','T8','T9','T10'}
%                    for j = nameparser('PBRANCH',list(i).SECTION,rooms)
                    for j = find(strcmp(list(i).SECTION, rooms.PBRANCH))'
                        if list(i).Z > rooms.Zmin{j} && list(i).Z <= rooms.Zmax{j}
                            list(i).CADRoom = rooms.NAME{j};
                        end
                    end
                otherwise
                    if list(i).X > 0
  %                      for j = nameparser('BRANCH','TD1',rooms)
                        for j = find(strcmp('TD1', rooms.BRANCH))'
                            if list(i).Z > rooms.Zmin{j} && list(i).Z <= rooms.Zmax{j}
                                list(i).CADRoom = rooms.NAME{j};
                            end
                        end
                    elseif list(i).X <=0
 %                       for j = nameparser('BRANCH','TD2',rooms)
                        for j = find(strcmp('TD2', rooms.BRANCH))'
                            if list(i).Z > rooms.Zmin{j} && list(i).Z <= rooms.Zmax{j}
                                list(i).CADRoom = rooms.NAME{j};
                            end
                        end
                    end
            end
        end
        
    end
    
    
    
    %  Find Doublets
    Appendix = {'I';'II';'III';'IV';'V';'VI'};
    [~,b,~] = unique({list.NAME1},'stable');
    dup = find(ismember([1:length(list)],b)==0);
    [~,b,~] = unique({list(dup).NAME1},'stable');
    dup = dup(b);
    dup = dup(strcmp('BENDMARK',{list(dup).TYPE})==0);
    dup = dup(strcmp('MATR',{list(dup).TYPE})==0);
    for i = 1:length(dup)
%        dummy = nameparser('NAME1',list(dup(i)).NAME1,list);
        dummy = find(strcmp(list(dup(i)).NAME1,{list.NAME1}));
        [b,~,~] = unique({list(dummy).NAME2});
        [b,~,~] = unique({list(dummy).CLASS});
        if length(b) < length(dummy) && abs(list(dummy(1)).S-list(dummy(2)).S)<1e-3
            %      list(iben  disp(['Doublette:' {list(dummy).NAME1}]);
        else
            for j = 1:length(dummy)
                index = findstr(list(dummy(j)).NAME1,'.');
                newname = [list(dummy(j)).NAME1(1:index(end)-1) Appendix{mod(j-1,6)+1} list(dummy(j)).NAME1(index(end):end)];
                %               newname = [list(dummy(j)).NAME1(1:index(end)-1) '_' num2str(j) list(dummy(j)).NAME1(index(end):end)];
                list(dummy(j)).NAME1 = newname;
            end
        end
    end
    
    % Treat bend magnet markers
    
    iname = find(strncmp('BENDIN',{list(1:end).CLASS},6));
    for i = 1:length(iname)
        inddum = strfind(list(iname(i)+1).NAME1,'.');
        inddum = inddum(end)-1;
        list(iname(i)).NAME1 = ['M' list(iname(i)+1).NAME1(1:inddum) 'a.' list(iname(i)+1).SECTION];
        list(iname(i)+2).NAME1 = ['M' list(iname(i)+1).NAME1(1:inddum) 'b.' list(iname(i)+1).SECTION];
        list(iname(i)+3).NAME1 = ['M' list(iname(i)+1).NAME1(1:inddum) 'c.' list(iname(i)+1).SECTION];
        list(iname(i)+4).NAME1 = ['M' list(iname(i)+1).NAME1(1:inddum) 'd.' list(iname(i)+1).SECTION];
    end
    
    
    
    
    sectnames = {'SA1','SA2','SA3'};
    for isectnames = 1:length(sectnames)
        isect =  find(strcmp(sectnames{isectnames},{list.SECTION}));
        icell = 0;
        for i = 2:length(isect)-1
            
            if strcmp('STUCELL',list(isect(i)).TYPE)==1
                icell = icell+1;
            end
            %icell = floor((list(isect(i)).S-(list(isect(1)).S+0.3))/6.1)+1;
            if strncmp('QA',list(isect(i)).TYPE,2)== 1 || ...
                    strncmp('BS',list(isect(i)).TYPE,2)== 1 || strncmp('CBS',list(isect(i)).TYPE,3)== 1 || ...
                    strncmp('BSL',list(isect(i)).TYPE,3)== 1 || strncmp('CBSL',list(isect(i)).TYPE,4)== 1
            else
                list(isect(i)).NAME2=[list(isect(i)).TYPE '.CELL' num2str(icell) '.' list(isect(i)).SECTION];
            end
        end
    end
    
    
    
    % Special treatment for some elements
    
    % Change type of laser heater undulator to U74
    if ~isempty(find(strcmp('UNDU.49.I1',{list(1:end).NAME1}), 1))
        list(strcmp('UNDU.49.I1',{list(1:end).NAME1})).TYPE='U74';
    end
    
    if ~isempty(find(strcmp('CBP',{list(1:end).TYPE}), 1))
        icbp = find(strcmp('CBP',{list(1:end).TYPE}), 1);
        ibp  = find(strcmp('BP',{list(1:end).TYPE}), 1);
        for i = 1:length(icbp)
            for ii = 1:length(ibp)
                if abs(list(icbp(i)).S-list(ibp(ii)).S) < 0.3
                    list(icbp(i)).NAME1 = strcat('C',list(ibp(ii)).NAME1);
                end
            end
        end
    end
    
    % Change name of some kickers
    if ~isempty(find(strncmp('KAX.54.I1',{list(1:end).NAME1},11), 1))
        list(strncmp('KAX.54.I1',{list(1:end).NAME1},11)).NAME1='KAX.55.I1';
    end
    if ~isempty(find(strncmp('KJX.53.I1',{list(1:end).NAME1},11), 1))
        list(strncmp('KJX.53.I1',{list(1:end).NAME1},11)).NAME1='KJX.54.I1';
        end
    if ~isempty(find(strncmp('KJY.58.I1',{list(1:end).NAME1},11), 1))
        list(strncmp('KJY.58.I1',{list(1:end).NAME1},11)).NAME1='KJY.57.I1';
    end
    if ~isempty(find(strncmp('KAX.54I.I1',{list(1:end).NAME1},10), 1))
        list(strncmp('KAX.54I.I1',{list(1:end).NAME1},10)).NAME1='KAX.54.I1';
    end
    if ~isempty(find(strncmp('KAX.54II.I1',{list(1:end).NAME1},11), 1))
        list(strncmp('KAX.54II.I1',{list(1:end).NAME1},11)).NAME1='KAX.55.I1';
    end
    if ~isempty(find(strncmp('KAX.225I.B1',{list(1:end).NAME1},11), 1))
        list(strncmp('KAX.225I.B1',{list(1:end).NAME1},11)).NAME1='KAX.225.B1';
    end
    if ~isempty(find(strncmp('KAX.225II.B1',{list(1:end).NAME1},12), 1))
        list(strncmp('KAX.225II.B1',{list(1:end).NAME1},12)).NAME1='KAX.226.B1';
    end
    if ~isempty(find(strncmp('KDY.445I.B2',{list(1:end).NAME1},11), 1))
        list(strncmp('KDY.445I.B2',{list(1:end).NAME1},11)).NAME1='KDY.445.B2';
    end
    if ~isempty(find(strncmp('KDY.445II.B2',{list(1:end).NAME1},12), 1))
        list(strncmp('KDY.445II.B2',{list(1:end).NAME1},12)).NAME1='KDY.446.B2';
    end
    
    % Change group of some kickers
    if ~isempty(find(strncmp('KL.1938.TL',{list(1:end).NAME1},10), 1))
        list(strncmp('KL.1938.TL',{list(1:end).NAME1},10)).GROUP='RAMPKICK';
    end
    if ~isempty(find(strncmp('KL.1965.TL',{list(1:end).NAME1},10), 1))
        list(strncmp('KL.1965.TL',{list(1:end).NAME1},10)).GROUP='RAMPKICK';
    end
    if ~isempty(find(strncmp('KL.2005.TL',{list(1:end).NAME1},10), 1))
        list(strncmp('KL.2005.TL',{list(1:end).NAME1},10)).GROUP='RAMPKICK';
    end
    
    % change secdtion of two CBB correctors
    if ~isempty(find(strcmp('CBB.5.I1D',{list(1:end).NAME2}), 1))
        list(strcmp('CBB.5.I1D',{list(1:end).NAME2})).SECTION='I1';
    end
    if ~isempty(find(strcmp('CBB.1.B1D',{list(1:end).NAME2}), 1))
        list(strcmp('CBB.1.B1D',{list(1:end).NAME2})).SECTION='B1';
    end
    
    % change NAME2 of all 2nd sweep magnets to xxxx.1.yy to connect to one
    % circuit
    iname = find(strncmp('SWEEP.2',{list(1:end).NAME2},7));
    if iname ~= 0
        for i = 1:length(iname)
            list(iname).NAME2=['SWEEP.1.' list(iname(i)).SECTION];
        end
    end
    clear('iname');

    % change NAME2 of QE.24.T5 and QE.14.T5 to connect to QF.4.T5 and
    % QF.14.T5

    iname = find(strncmp('QLN.23.I1',{list(1:end).NAME1},9));
    if iname ~= 0
        list(iname).NAME2='GunC1-C4' ;
    end
    clear('iname');
    iname = find(strncmp('QLS.23.I1',{list(1:end).NAME1},9));
    if iname ~= 0
        list(iname).NAME2='GunC8&GunC6&GunC7&GunC5' ;
    end
    clear('iname');
    iname = find(strncmp('CLX.23.I1',{list(1:end).NAME1},9));
    if iname ~= 0
        list(iname).NAME2='GunC7&GunC5' ;
    end
    clear('iname');
    iname = find(strncmp('CLY.23.I1',{list(1:end).NAME1},9));
    if iname ~= 0
        list(iname).NAME2='GunC8&GunC6' ;
    end
    clear('iname');

    
    % change NAME2 of Gun 'multipol
    % QF.14.T5

    iname = find(strncmp('QE.24.T5',{list(1:end).NAME2},8));
    if iname ~= 0
        for i = 1:length(iname)
            list(iname).NAME2='QF.4.T5' ;
        end
    end
    iname = find(strncmp('QE.14.T5',{list(1:end).NAME2},8));
    if iname ~= 0
        for i = 1:length(iname)
            list(iname).NAME2='QF.14.T5' ;
        end
    end


    % change KFB0 TYPE to DRIFT
    iname = find(strncmp('KFB0',{list(1:end).NAME2},4));
    if iname ~=0
        for i = 1:length(iname)
            list(iname(i)).GROUP = 'VACUUM';
            list(iname(i)).CLASS = 'PLACEH';
            list(iname(i)).TYPE = 'DRIFT';
        end
    end
    
    % Adjust name of diagnostic elements and marjers in gun section
    if ~isempty(find(strncmp('G1D',{list(1:end).SUBSECTION},3), 1))
        if ~isempty(find(strncmp('FCUP.24II.I1',{list(1:end).NAME1},12), 1))
            list(strncmp('FCUP.24II.I1',{list(1:end).NAME1},12)).NAME1='FCUP.25II.I1';
        end
        if ~isempty(find(strncmp('FCUP.25.I1',{list(1:end).NAME1},10), 1))
            list(strncmp('FCUP.25.I1',{list(1:end).NAME1},10)).NAME1='FCUP.25III.I1';
        end
        if ~isempty(find(strncmp('BPMG.25.I1',{list(1:end).NAME1},10), 1))
            list(strncmp('BPMG.25.I1',{list(1:end).NAME1},10)).NAME1='BPMG.25II.I1';
        end
        if ~isempty(find(strncmp('SCRN.24II.I1',{list(1:end).NAME1},12), 1))
            list(strncmp('SCRN.24II.I1',{list(1:end).NAME1},10)).NAME1='SCRN.25II.I1';
        end
    end
    if ~isempty(find(strncmp('G1',{list(1:end).SUBSECTION},2), 1))
        if ~isempty(find(strncmp('FCUP.24I.I1',{list(1:end).NAME1},11), 1))
            list(strncmp('FCUP.24I.I1',{list(1:end).NAME1},11)).NAME1='FCUP.24.I1';
        end
        if ~isempty(find(strncmp('SCRN.24I.I1',{list(1:end).NAME1},11), 1))
            list(strncmp('SCRN.24I.I1',{list(1:end).NAME1},11)).NAME1='SCRN.24.I1';
        end
    end
    if ~isempty(find(strncmp('I1M',{list(1:end).SUBSECTION},3), 1))
        if ~isempty(find(strncmp('FCUP.25.I1',{list(1:end).NAME1},10), 1))
            list(strncmp('FCUP.25.I1',{list(1:end).NAME1},10)).NAME1='FCUP.25I.I1';
        end
        if ~isempty(find(strncmp('SCRN.25.I1',{list(1:end).NAME1},10), 1))
            list(strncmp('SCRN.25.I1',{list(1:end).NAME1},10)).NAME1='SCRN.25I.I1';
        end
        if ~isempty(find(strncmp('BPMG.25.I1',{list(1:end).NAME1},10), 1))
            list(strncmp('BPMG.25.I1',{list(1:end).NAME1},10)).NAME1='BPMG.25I.I1';
        end
    end
    iname = find(strncmp('STSUB.G1D.I1',{list(1:end).NAME2},12));
    if iname~= 0
        namepos = floor(list(iname).Z);
        list(iname).NAME1 =  [list(iname).TYPE '.' num2str(namepos) 'II.' list(iname).SECTION];
    end
    iname = find(strncmp('STSUB.I1M.I1',{list(1:end).NAME2},12));
    if iname~= 0
        namepos = floor(list(iname).Z);
        list(iname).NAME1 =  [list(iname).TYPE '.' num2str(namepos) 'I.' list(iname).SECTION];
    end
    
    % Change Position of BB chicane magnets
    
    if length([list(strncmp('BB.1.I1',{list(1:end).NAME2},7)).Y]) == 4
        [list(strncmp('BB.1.I1',{list(1:end).NAME2},7)).Y]= deal(-0.150,-0.200,-0.200,-0.150);
    end
    if length([list(strcmp('BB.1.B1',{list(1:end).NAME2})).Y]) == 4
        [list(strcmp('BB.1.B1',{list(1:end).NAME2})).Y]= deal(-0.150,-0.450,-0.450,-0.150);
    end
    if length([list(strncmp('BB.1.B1D',{list(1:end).NAME2},8)).Y]) == 1
        [list(strncmp('BB.1.B1D',{list(1:end).NAME2},8)).Y]= deal(-0.150);
    end
    if length([list(strncmp('BB.1.B2',{list(1:end).NAME2},7)).Y]) == 4
        [list(strncmp('BB.1.B2',{list(1:end).NAME2},7)).Y]= deal(-0.150,-0.375,-0.375,-0.150);
    end
    
    
    % Change Position of chicane magnets in SA2
    iSA2 = find(strcmp('SA2',  {list(1:end).SECTION})); 
    
    iBS = [find(strcmp('CBS',{list(iSA2).TYPE})) find(strcmp('MCBS',{list(iSA2).TYPE}))];
    iBS = iSA2(iBS);
    for ii = 1:length(iBS)
        if ~isempty(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,-0.0075,0,-0.0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
            namepos = floor(list(i).Z + z);
            if namepos == 2250; namepos = 2249; end
            list(i).NAME1 =  [list(i).TYPE '.' num2str(namepos) '.' list(i).SECTION];
        end
    end
    
    
    iBS = [find(strcmp('BS',{list(iSA2).TYPE})) find(strcmp('BPMH',{list(iSA2).TYPE}))];
    iBS = iSA2(iBS);
    if ~isempty(iBS)
        for ii = 1:length(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,-0.0075,0,0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
        end
    end
    
    
    % Change Position of chicane magnets in SA1
    iSA1 = find(strcmp('SA1',  {list(1:end).SECTION})); 
    
    iBS = [find(strcmp('CBS',{list(iSA1).TYPE})) find(strcmp('MCBS',{list(iSA1).TYPE}))];
    iBS = iSA1(iBS);
    for ii = 1:length(iBS)
        if ~isempty(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,+0.0075,0,-0.0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
            namepos = floor(list(i).Z + z);
            if namepos == 2433; namepos = 2432; end
            if namepos == 2436; namepos = 2435; end
            list(i).NAME1 =  [list(i).TYPE '.' num2str(namepos) '.' list(i).SECTION];
        end
    end
    
    iBS = [find(strcmp('BS',{list(iSA1).TYPE}))];
    iBS = iSA1(iBS);
    if ~isempty(iBS)
        for ii = 1:length(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,+0.0075,0,0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
        end
    end
    
    % Change Position of chicane magnets in SA3
    iSA3 = find(strcmp('SA3',  {list(1:end).SECTION})); 
    
    iBS = [find(strcmp('CBSL',{list(iSA3).TYPE})) find(strcmp('MCBSL',{list(iSA3).TYPE}))];
    iBS = iSA3(iBS);
    for ii = 1:length(iBS)
        if ~isempty(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,+0.025,0,-0.0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
            namepos = floor(list(i).Z + z);
            if namepos == 2878; namepos = 2877; end
            if namepos == 2879; namepos = 2878; end
            list(i).NAME1 =  [list(i).TYPE '.' num2str(namepos) '.' list(i).SECTION];
        end
    end
    
    iBS = [find(strcmp('BSL',{list(iSA3).TYPE}))];
    iBS = iSA3(iBS);
    if ~isempty(iBS)
        for ii = 1:length(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,+0.025,0,0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
            namepos = floor(list(i).Z + z);
            %if namepos == 2875; namepos = 2876; end
            list(i).NAME1 =  [list(i).TYPE '.' num2str(namepos) '.' list(i).SECTION];
        end
    end
    
    
    % Change Position of ASPECT chicane magnets in T2 and T4
    iT24 = [find(strcmp('T2',  {list(1:end).SECTION})) find(strcmp('T4',  {list(1:end).SECTION}))]; 
    
    iBS = [find(strcmp('CBT',{list(iT24).TYPE})) find(strcmp('MCBT',{list(iT24).TYPE}))];
    iBS = iT24(iBS);
    for ii = 1:length(iBS)
        if ~isempty(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,+0.025,0,-0.0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
            namepos = floor(list(i).Z + z);
            if namepos == 2879; namepos = 2878; end
            list(i).NAME1 =  [list(i).TYPE '.' num2str(namepos) '.' list(i).SECTION];
        end
    end
    
    iBS = [find(strcmp('BT',{list(iT24).TYPE}))];
    iBS = iT24(iBS);
    if ~isempty(iBS)
        for ii = 1:length(iBS)
            i = iBS(ii);
            [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,+0.025,0,0);
            list(i).X = list(i).X+x;
            list(i).Y = list(i).Y+y;
            list(i).Z = list(i).Z+z;
            list(i).S = list(i).S;
            [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
                LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
            namepos = floor(list(i).Z + z);
            if namepos == 2875; namepos = 2876; end
            list(i).NAME1 =  [list(i).TYPE '.' num2str(namepos) '.' list(i).SECTION];
        end
    end
    
    % Phaseshifters after chicanes belong to the previous cell
    
    iBS = find(strcmp('BPS.CELL33.SA1',{list(1:end).NAME2}));
    if ~isempty(iBS); list(iBS).NAME2 = 'BPS.CELL32.SA1';  end
    
    iBS = find(strcmp('BPS.CELL17.SA1',{list(1:end).NAME2}));
    if ~isempty(iBS); list(iBS).NAME2 = 'BPS.CELL16.SA1';  end
    
    if isempty(find(strcmp('BPS.CELL8.SA2',{list(1:end).NAME2})));
        iBS = find(strcmp('BPS.CELL9.SA2',{list(1:end).NAME2}));
        if ~isempty(iBS); list(iBS).NAME2 = 'BPS.CELL8.SA2';  end
    end
    if isempty(find(strcmp('BPS.CELL17.SA2',{list(1:end).NAME2})));
        iBS = find(strcmp('BPS.CELL18.SA2',{list(1:end).NAME2}));
        if ~isempty(iBS); list(iBS).NAME2 = 'BPS.CELL17.SA2'; end
    end
    
    if isempty(find(strcmp('BPS.CELL10.SA2',{list(1:end).NAME2})));
        iBS = find(strcmp('BPS.CELL11.SA2',{list(1:end).NAME2}));    % for 25
        if ~isempty(iBS); list(iBS).NAME2 = 'BPS.CELL10.SA2';  end
    end
    if isempty(find(strcmp('BPS.CELL19.SA2',{list(1:end).NAME2})));
        iBS = find(strcmp('BPS.CELL20.SA2',{list(1:end).NAME2}));   % for 25
        if ~isempty(iBS); list(iBS).NAME2 = 'BPS.CELL19.SA2'; end
    end
    
    iBS = find(strcmp('BPS.CELL13.SA3',{list(1:end).NAME2}));
    if ~isempty(iBS); list(iBS).NAME2 = 'BPS.CELL12.SA3'; end
    
    
    % rename bpms in L0
    iname = find(strncmp('BPMC.38.I1',{list(1:end).NAME1},10));
    if iname~= 0
        list(iname).NAME1 = 'BPMC.38I.I1';
    end
    iname = find(strncmp('BPMR.38.I1',{list(1:end).NAME1},10));
    if iname~= 0
        list(iname).NAME1 = 'BPMR.38II.I1';
    end
    
    % rename correctors in TL
    
    iname = find(strcmp('CHX.1964.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='CHX.1965.TL';
    end
    
    iname = find(strcmp('CHY.1997.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CHY.11.TL';
    end
    iname = find(strcmp('CHY.2004.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CHY.12.TL';
    end
    iname = find(strcmp('CFY.2010.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CFY.7.TL';
    end
    iname = find(strcmp('CHX.2012.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CHX.8.TL';
    end
    iname = find(strcmp('CHY.2012.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CHY.13.TL';
    end
    iname = find(strcmp('CNX.2021.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CNX.2.TL';
    end
    iname = find(strcmp('CNY.2021.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CNY.3.TL';
    end
    iname = find(strcmp('CFX.2042.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CFX.1.TL';
    end
    iname = find(strcmp('CHX.2054.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CHX.9.TL';
    end
    iname = find(strcmp('CHY.2054.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME2='CHY.14.TL';
    end
    
    % rename BAMs in TL
    
    iname = find(strcmp('BAM.1931I.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='BAM.1931.TL';
    end
    iname = find(strcmp('BAM.1931II.TL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='BAM.1932.TL';
    end
    
    % rename some sextupoles (MATLAB rounding bug ?)
    iname = find(strcmp('SA.1690.CL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='SA.1691.CL';
    end
    iname = find(strcmp('SA.1699.CL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='SA.1700.CL';
    end
    iname = find(strcmp('SA.1735.CL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='SA.1736.CL';
    end
    iname = find(strcmp('SA.1807.CL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='SA.1808.CL';
    end
    iname = find(strcmp('SA.1843.CL',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='SA.1844.CL';
    end
    iname = find(strcmp('SA.2015.TLD',{list(1:end).NAME1}));
    if iname~=0
        list(iname).NAME1='SA.2016.TLD';
    end
    
    % find last BE in T4 section and move by 15 mm in bend direction
    iT4 = find(strcmp('T4',{list(1:end).SECTION}));
    if iT4 ~= 0
        iBE = find(strcmp('BE',{list(iT4).TYPE}));
        i = iT4(iBE(2));
        [x y z] = rotation3d(list(i).PHI,list(i).THETA,list(i).CHI,-0.015,0,0);
        list(i).X = list(i).X+x;
        list(i).Y = list(i).Y+y;
        list(i).Z = list(i).Z+z;
        list(i).S = list(i).S+z;
        [list(i).XPD,list(i).YPD,list(i).ZPD,list(i).THETAPD,list(i).PHIPD,list(i).CHIPD] = ...
            LAtoPD(list(i).THETA,list(i).PHI,list(i).CHI,list(i).X,list(i).Y,list(i).Z);
    end
    
    % in case of HELP remove all with KXL == 0
    b1 = find(strncmp('HELP',{list(1:end).TYPE},2));
    b2 = find([list(b1).KXL] == 0);
    b1 = b1(b2);
    b = ones(size(list));
    b(b1)=0;
    list = list(find(b));
    
    
    % in case of BZ use coordinates of listing in TL and remove from TL
    ibz0name = find(strcmp('BZ.0.TL',{list(1:end).NAME2}));
    if length(ibz0name)==8
        bztl = list(ibz0name);
    end
    b = ones(size(list));
    b(ibz0name)=0;
    list = list(find(b));
    
    ibzt1name = [find(strcmp('BZ.1.T1',{list(1:end).NAME2})) find(strcmp('BZ.2.T1',{list(1:end).NAME2}))];
        for i = 1:length(ibzt1name)
            offset = 4;
            list(ibzt1name(i)).S = bztl(i+offset).S;
            list(ibzt1name(i)).X = bztl(i+offset).X;
            list(ibzt1name(i)).Y = bztl(i+offset).Y;
            list(ibzt1name(i)).Z = bztl(i+offset).Z;
            list(ibzt1name(i)).THETA = bztl(i+offset).THETA;
            list(ibzt1name(i)).PHI = bztl(i+offset).PHI;
            list(ibzt1name(i)).CHI = bztl(i+offset).CHI;
        end

    ibztldname = [find(strcmp('BZ.1.TLD',{list(1:end).NAME2})) find(strcmp('BZ.2.TLD',{list(1:end).NAME2}))];
        for i = 1:length(ibztldname)
            offset = 0;
            list(ibztldname(i)).S = bztl(i+offset).S;
            list(ibztldname(i)).X = bztl(i+offset).X;
            list(ibztldname(i)).Y = bztl(i+offset).Y;
            list(ibztldname(i)).Z = bztl(i+offset).Z;
            list(ibztldname(i)).THETA = bztl(i+offset).THETA;
            list(ibztldname(i)).PHI = bztl(i+offset).PHI;
            list(ibztldname(i)).CHI = bztl(i+offset).CHI;
        end
    %    end
    % Name BPMF and BPMI correctly after their mid position
    iBPMFI    = [find(strcmp('BPMF',{list(1:end).TYPE})) find(strcmp('BPMI',{list(1:end).TYPE}))];
    iMIDBPMFI = [find(strcmp('MIDBPMF',{list(1:end).TYPE})) find(strcmp('MIDBPMI',{list(1:end).TYPE}))];
    for i = 1:length(iBPMFI)
        list(iBPMFI(i)).NAME1 =  [list(iBPMFI(i)).TYPE '.' num2str(floor(list(iMIDBPMFI(i)).Z)) '.' list(iBPMFI(i)).SECTION];
    end
    
    % Name KSPOS and KSNEG according to mid marker
    iKSpos = [find(strcmp('KSPOS',{list(1:end).TYPE}))];
    iKSneg = [find(strcmp('KSNEG',{list(1:end).TYPE}))];
    iKS = [find(strcmp('KS',{list(1:end).TYPE}))];
    for i = 1:length(iKS)
        list(iKSpos(i)).NAME1 =  [list(iKSpos(i)).TYPE '.' num2str(floor(list(iKS(i)).Z)) '.' list(iKSpos(i)).SECTION];
        list(iKSneg(i)).NAME1 =  [list(iKSneg(i)).TYPE '.' num2str(floor(list(iKS(i)).Z)) '.' list(iKSneg(i)).SECTION];
    end
    
    % Name all Kickers NAME1 = NAME2
    iKickers = [find(strcmp('FASTKICK',{list(1:end).GROUP})) ...
                find(strcmp('RAMPKICK',{list(1:end).GROUP})) ...
                find(strcmp('FBKICK',{list(1:end).GROUP}))];
    for i = 1:length(iKickers)
        list(iKickers(i)).NAME2 = list(iKickers(i)).NAME1;
    end
    
    % Remove special elements that are needed to describe the south branch geometry
    list = list(strncmp('MQF',{list(1:end).NAME2},3)==0);
    list = list(strncmp('MYQ',{list(1:end).NAME2},3)==0);
    list = list(strncmp('MXQ',{list(1:end).NAME2},3)==0);
    list = list(strncmp('YQK',{list(1:end).NAME2},3)==0);
    list = list(strncmp('XQK',{list(1:end).NAME2},3)==0);
    
    fid = fopen(longlistfile,'w');
    
    % print header
    fprintf(fid,['%8s %8s %10s %20s %20s %10s %10s %10s ', ...
        '%10s %16s %12s %12s %12s ',...
        '%12s %12s %12s %12s %12s %12s %12s %12s ',...
        '%12s %12s %12s %12s %12s %12s ',...
        '%12s %12s %12s %12s %12s %12s %12s %12s %12s %12s %12s ', ...
        '%12s %12s \n'], ...
        'SECTION','SUBSECTION','CADRoom','NAME1','NAME2','GROUP','CLASS','TYPE',...
        'LENGTH','STRENGTH','E1/LAG','E2/FREQ','TILT',...
        'S','ST','X','Y','Z','THETA','PHI','CHI',...
        'XPD','YPD','ZPD','THETAPD','PHIPD','CHIPD',...
        'ENERGY','BETX','ALFX','MUX','BETY','ALFY','MUY','DX','DPX','DY','DPY',...
        'XAPER','YAPER');
    fprintf(fid,['%8s %8s %10s %20s %20s %10s %10s %10s ', ...
        '%10s %12s %12s %12s %12s ',...
        '%12s %12s %12s %12s %12s %12s %12s %12s ',...
        '%12s %12s %12s %12s %12s %12s ',...
        '%12s %12s %12s %12s %12s %12s %12s %12s %12s %12s %12s ', ...
        '%12s %12s \n'], ...
        '[]','[]','[]','[]','[]','[]','[]','[]','[m]','[m^(1-n)/MV]','[rad]','[rad/MHz]','[rad]',...
        '[m]','[m]','[m]','[m]','[m]','[rad]','[rad]','[rad]', ...
        '[m]','[m]','[m]','[rad]','[rad]','[rad]', ...
        '[GeV]',...
        '[m]','[rad]','[2PI]', '[m]','[rad]','[2PI]','[m]','[rad]','[m]','[rad]',...
        '[m]','[m]');
    
    
    for i = 1:length(list)
        fprintf(fid,['%8s %8s %10s %20s %20s %10s %10s %10s '...
            '%12.6f %16.12f %12.9f %12.9f %12.9f ',...
            '%12.6f %12.6f %12.6f %12.6f %12.6f %12.9f %12.9f %12.9f ',...
            '%12.6f %12.6f %12.6f %12.8f %12.8f %12.8f ',...
            '%12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f ',...
            '%12.4f %12.4f \n'], ...
            list(i).SECTION, ...
            list(i).SUBSECTION, ...
            list(i).CADRoom, ...
            list(i).NAME1, ...
            list(i).NAME2, ...
            list(i).GROUP,....
            list(i).CLASS, ...
            list(i).TYPE, ...
            list(i).L, list(i).KXL, list(i).E1, list(i).E2, list(i).TILT, ...
            list(i).S, list(i).ST,...
            list(i).X, list(i).Y, list(i).Z, ...
            list(i).THETA, -1*list(i).PHI, list(i).CHI, ...
            list(i).XPD, list(i).YPD, list(i).ZPD, ...
            list(i).THETAPD, -1*list(i).PHIPD, list(i).CHIPD, ...
            list(i).ENERGY, ...
            list(i).BETX, list(i).ALFX, list(i).MUX, ...
            list(i).BETY, list(i).ALFY, list(i).MUY, ...
            list(i).DX, list(i).DPX, list(i).DY, list(i).DPY, ...
            list(i).XAP, list(i).YAP);
    end
    
    fclose(fid);
    longlist=[longlist list];
end

list = longlist(2:end);
[~,index,~]= unique({list(1:end).NAME1},'stable');
list = list(index);
help = strcmp('HELP',{list.TYPE});
list = list(~help);
help = strncmp('MKL',{list.NAME1},3);
list = list(~help);
help = strncmp('MKS',{list.NAME1},3);
list = list(~help);
help = strncmp('MHELP',{list.NAME1},5);
list = list(~help);
fid = fopen('longlist.dat','w');

% print header
fprintf(fid,['%8s %8s %10s %20s %20s %10s %10s %10s ', ...
    '%10s %16s %12s %12s %12s ',...
    '%12s %12s %12s %12s %12s %12s %12s %12s ',...
    '%12s %12s %12s %12s %12s %12s ',...
    '%12s %12s %12s %12s %12s %12s %12s %12s %12s %12s %12s ', ...
    '%12s %12s \n'], ...
    'SECTION','SUBSECTION','CADRoom','NAME1','NAME2','GROUP','CLASS','TYPE',...
    'LENGTH','STRENGTH','E1/LAG','E2/FREQ','TILT',...
    'S','ST','X','Y','Z','THETA','PHI','CHI',...
    'XPD','YPD','ZPD','THETAPD','PHIPD','CHIPD',...
    'ENERGY','BETX','ALFX','MUX','BETY','ALFY','MUY','DX','DPX','DY','DPY',...
    'XAPER','YAPER');
fprintf(fid,['%8s %8s %10s %20s %20s %10s %10s %10s ', ...
    '%10s %12s %12s %12s %12s ',...
    '%12s %12s %12s %12s %12s %12s %12s %12s ',...
    '%12s %12s %12s %12s %12s %12s ',...
    '%12s %12s %12s %12s %12s %12s %12s %12s %12s %12s %12s ', ...
    '%12s %12s \n'], ...
    '[]','[]','[]','[]','[]','[]','[]','[]','[m]','[m^(1-n)/MV]','[rad]','[rad/MHz]','[rad]',...
    '[m]','[m]','[m]','[m]','[m]','[rad]','[rad]','[rad]', ...
    '[m]','[m]','[m]','[rad]','[rad]','[rad]', ...
    '[GeV]',...
    '[m]','[rad]','[2PI]', '[m]','[rad]','[2PI]','[m]','[rad]','[m]','[rad]',...
    '[m]','[m]');


for i = 1:length(list)
    fprintf(fid,['%8s %8s %10s %20s %20s %10s %10s %10s '...
        '%12.6f %16.12f %12.9f %12.9f %12.9f ',...
        '%12.6f %12.6f %12.6f %12.6f %12.6f %12.9f %12.9f %12.9f ',...
        '%12.6f %12.6f %12.6f %12.8f %12.8f %12.8f ',...
        '%12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f ',...
        '%12.4f %12.4f \n'], ...
        list(i).SECTION, ...
        list(i).SUBSECTION, ...
        list(i).CADRoom, ...
        list(i).NAME1, ...
        list(i).NAME2, ...
        list(i).GROUP,....
        list(i).CLASS, ...
        list(i).TYPE, ...
        list(i).L, list(i).KXL, list(i).E1, list(i).E2, list(i).TILT, ...
        list(i).S, list(i).ST,...
        list(i).X, list(i).Y, list(i).Z, ...
        list(i).THETA, -1*list(i).PHI, list(i).CHI, ...
        list(i).XPD, list(i).YPD, list(i).ZPD, ...
        list(i).THETAPD, -1*list(i).PHIPD, list(i).CHIPD, ...
        list(i).ENERGY, ...
        list(i).BETX, list(i).ALFX, list(i).MUX, ...
        list(i).BETY, list(i).ALFY, list(i).MUY, ...
        list(i).DX, list(i).DPX, list(i).DY, list(i).DPY, ...
        list(i).XAP, list(i).YAP);
end

fclose(fid);



%
% % check soll positions
%
% if isoll == 1
%     [a,b] = xlsread('Starts8.3.6.xlsx');
%     test = cell2struct(b(2:end,:),b(1,:),2);
%     for i = 1:length(test)
%         test(i).S = a(i,1);
%         test(i).X = a(i,2);
%         test(i).Y = a(i,3);
%         test(i).Z = a(i,4);
%         test(i).THETA = a(i,5);
%         test(i).PHI = a(i,6);
%         test(i).CHI = a(i,7);
%     end
%
%     err = 1e-6;
%     for i = 1:length(test)
%         isec = nameparser('SECTION',test(i).SECTION,list);
%         if isec ~= 0
%             istart = nameparser('NAME2',test(i).NAME2,list(isec));
%             if(abs(list(isec(istart)).X-test(i).X)>err || ...
%                     abs(list(isec(istart)).Y-test(i).Y)>err || ...
%                     abs(list(isec(istart)).Z-test(i).Z)>err)
%                 sprintf('Ist-Soll of %s %10.6f %10.6f %10.6f ',[list(isec(istart)).SECTION '.' list(isec(istart)).NAME2], ...
%                     list(isec(istart)).X-test(i).X, ...
%                     list(isec(istart)).Y-test(i).Y, ...
%                     list(isec(istart)).Z-test(i).Z)
%             end
%         end
%     end
%
%
% end
%
