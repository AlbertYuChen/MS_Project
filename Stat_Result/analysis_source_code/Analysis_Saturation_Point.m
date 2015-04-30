%%
M_10000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/10000.csv');
% M_180000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/180000.csv');
M_200000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/200000.csv');
% M_220000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/220000.csv');
M_240000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/240000.csv');
M_270000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/270000.csv');
M_285000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/285000.csv');
M_295000 = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/ete_delay/295000.csv');


%%
figure,
plot(M_10000(:,1),M_10000(:,2))
hold on
% plot(M_180000(:,1),M_180000(:,2))
% hold on
plot(M_200000(:,1),M_200000(:,2))
hold on
% plot(M_220000(:,1),M_220000(:,2))
% hold on
plot(M_240000(:,1),M_240000(:,2))
hold on
plot(M_270000(:,1),M_270000(:,2))
hold on
plot(M_285000(:,1),M_285000(:,2))
hold on
plot(M_295000(:,1),M_295000(:,2))
hold on

grid on
ylim([0 4e-5])

xlabel('simulation time(s)')
ylabel('average ete delay(s)')

h = legend('10,000 Worm/s/node','200,000 Worm/s/node','240,000 Worm/s/node','270,000 Worm/s/node','285,000 Worm/s/node','295,000 Worm/s/node');











