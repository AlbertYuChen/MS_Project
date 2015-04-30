AVE_O_SP_SCB = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/O_SP_SCB.csv',1,1);
AVE_PT_SP_SCB = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/SP_SCB.csv',1,1);
AVE_O_SP_SCB = AVE_O_SP_SCB';
AVE_PT_SP_SCB = AVE_PT_SP_SCB';

dilation_SCB = AVE_PT_SP_SCB ./ AVE_O_SP_SCB;
mean_dilation_SCB = mean(dilation_SCB);
std_dilation_SCB = std(dilation_SCB);

%%
AVE_O_SP_UD_BFS = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/O_SP_UD_BFS.csv',1,1);
AVE_PT_SP_UD_BFS = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/SP_UD_BFS.csv',1,1);
AVE_O_SP_UD_BFS = AVE_O_SP_UD_BFS';
AVE_PT_SP_UD_BFS = AVE_PT_SP_UD_BFS';

dilation_UD_BFS = AVE_PT_SP_UD_BFS ./ AVE_O_SP_UD_BFS;
mean_dilation_UD_BFS = mean(dilation_UD_BFS);
std_dilation_UD_BFS = std(dilation_UD_BFS);

%%
AVE_O_SP_EDA = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/O_SP_EDA.csv',1,1);
AVE_PT_SP_EDA = csvread('/Users/chenyu/Workspace/Python/MS_Project/Stat_Result/raw_data/SP_EDA.csv',1,1);
AVE_O_SP_EDA = AVE_O_SP_EDA';
AVE_PT_SP_EDA = AVE_PT_SP_EDA';

dilation_EDA = AVE_PT_SP_EDA ./ AVE_O_SP_EDA;
mean_dilation_EDA = mean(dilation_EDA);
std_dilation_EDA = std(dilation_EDA);

%%
figure,
errorbar([4 6 8 10 12 14],Dialation_Ratio_SCB,std_dilation_SCB,'-x')
hold on
errorbar([4 6 8 10 12 14],Dialation_Ratio_UD,std_dilation_UD_BFS,'-x')
grid on


legend('SCB', 'Up*/Down*')
xlim([2 16])

xlabel('average degree')
ylabel('dilation ratio')






 












