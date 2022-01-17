function main(fileName, p, sig_f, sig_n, l, rate, t)

data = loadData(fileName);
data = modifyData(data);

N = size(data,1);
a = round(N*rate);
b = N-a;

AR = AutoregressiveModel(data(1:a), p, b+t);
GP = GaussianProcess(data(1:a), sig_f, sig_n, l, b+t);

plot(1:size(AR,1), AR, 'r--', 1:size(GP,1), GP, 'b--', 1:size(data,1), data, '-');

end