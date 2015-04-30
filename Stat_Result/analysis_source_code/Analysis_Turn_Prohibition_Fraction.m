%%
M_scb = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/SCB.csv',1,1);
M_scb = M_scb';

M_scb_ave = mean(M_scb);
M_scb_err = std(M_scb);

% figure,
% plot([4 6 8 10 12 14],M_scb_ave,'-*')
% ylim([0.1 0.5])
% xlim([2 16])
% grid on
% title('SCB turn prohibition fraction')
% xlabel('average degree')
% ylabel('fraction')

%%
M_eda = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/EDA.csv',1,1);
M_eda = M_eda';

M_eda_ave = mean(M_eda);
M_eda_err = std(M_eda);

% figure,
% plot([4 6 8 10 12 14],M_eda_ave,'-*')
% ylim([0.1 0.5])
% xlim([2 16])
% grid on
% title('EDA turn prohibition fraction')
% xlabel('average degree')
% ylabel('fraction')

%%
M_ud = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/UD_BFS.csv',1,1);
M_ud = M_ud';

M_ud_ave = mean(M_ud);
M_ud_err = std(M_ud);


%%
figure,
errorbar([4 6 8 10 12 14],M_ud_ave,M_ud_err,'-x')
% plot([4 6 8 10 12 14],M_ud_ave,'-*')
hold on
% plot([4 6 8 10 12 14],M_eda_ave,'-*')
% errorbar([4 6 8 10 12 14],M_eda_ave,M_eda_err,'-o')
% hold on
% plot([4 6 8 10 12 14],M_scb_ave,'-*')
errorbar([4 6 8 10 12 14],M_scb_ave,M_scb_err,'-v')


ylim([0.1 0.35])
xlim([2 16])

grid on

legend('UP-DOWN', 'SCB')
title('Up-Down & SCB turn prohibition fraction')
xlabel('average degree')
ylabel('fraction')






