M = csvread('/Users/chenyu/Dropbox/yu_ms_project/tmp/AD10.csv');
% plot(M(:,1),M(:,2),'-x')
plot(M(:,1),M(:,2))
xlim([0 4e5])
ylim([0 6e-5])
% grid on
xlabel('Worm Generation Rate (Worms/Sec/Node)')
ylabel('Average End to End Delay')

