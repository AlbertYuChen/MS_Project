%%
M_SCB = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/all_SP_scb.csv',0,1);

SUM_SCB = sum(M_SCB, 2);
C = (M_SCB~=0);
C = sum(C, 2);

AVE_SP_SCB = SUM_SCB ./ C;


%%
M_UD_BFS = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/all_SP_ud_bfs.csv',0,1);

SUM_UD_BFS = sum(M_UD_BFS, 2);
C = (M_UD_BFS~=0);
C = sum(C, 2);

AVE_SP_UD_BFS = SUM_UD_BFS ./ C;




%%
figure,
plot([4 6 8 10 12 14], AVE_SP_SCB, '-X')
hold on
plot([4 6 8 10 12 14], AVE_SP_UD_BFS, '-v')
grid on
xlim([2 16])
ylim([0 4e5])
legend('SCB','Up*/Down*')
xlabel('average degree')
ylabel('average saturation point (worms/sec/node)')




