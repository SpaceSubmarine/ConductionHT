%1-D Transient Heat Conduction With No Heat Generation [FDM][CN]
clear all
clc
clf
%% Variable Declaration
n = 21;                         %number of nodes
L = 1;                          %length of domain

A = sparse(n,n);                %initilizing Space
B = sparse(n,n);
Bx = zeros(n,1);
Ta = zeros(n,1);
Tb = zeros(n,1);

dx = L/(n-1);                    %domain element
dt = 20;                         %time step
tmax = 4000;                     %total Time steps (s)
t = 0:dt:tmax;
Tl = 100;                        %temperature at left face °C
Tr = 100;                        %temperature at right face °C

x =  linspace(0,L,n);            %linearly spaced vectors x direction
alpha = 1e-4;                    %thermal diffusivity (m^2/s)
r = alpha * dt /(2 *dx^2);       %for stability, must be 0.5 or less

%% Set Up Matrix
for i = 2 : n-1
    A(i,i-1) = -r;
        A(i,i ) = (1+2*r);       %Implicit Matrix
            A(i,i+1) = -r;
end
            A(1 ,1 ) = 1;
            A(n ,n ) = 1;

for j = 2 : n-1
    B(j,j-1) = r;
        B(j,j ) = (1-2*r);       %Explicit Matrix
            B(j,j+1) = r;
end
            B(1 ,1 ) = 1;
            B(n ,n ) = 1;
            
%% Boundry Condition
Bx(1,1) = Tl;            %Left Wall (Dirichlet conditions)
Bx(n,1) = Tr;            %Right Wall(Dirichlet conditions)

%% Solution
for k = 2 : length(t)   %time steps
    
        Bx(2 : n-1) = Tb(2 : n-1);
            Tb = B * Bx;
                        
        fprintf('Time t=%d\n',k-1);
    
end
            Ta = A\Tb;   %Solve CN Matrix
   
 %% Plot
 pos1 = [0.1 0.17 0.4 0.7];
    subplot('Position',pos1)
        plot(x,Ta);
        title('Nodes  Vs Temperature');
        xlabel('Nodes (i)');
        ylabel('Temperature °C');    
        grid on
        grid minor
    
    a=0:L;
    d=0:0;
    
 pos2 = [0.51 0.45 0.45 0.1];
    subplot('Position',pos2) 
    ax = gca;
    imagesc(a,d,Ta', 'Parent', ax);
    ax.YAxis.Visible = 'off';
        
        title('Temperature Gradient');
        xlabel('Nodes (i)');
        h = colorbar;
        ylabel(h, 'Temperature °C')
        colormap jet