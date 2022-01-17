function y = GaussianProcess(data, sig_f, sig_n, l, t)

n = size(data,1);
y = data;
x = transpose(1:n);

K = zeros(n,n);
for i = 1:n
    for j = 1:n
        K(i,j) = k(x(i), x(j), sig_f, sig_n, l);
    end
end

for i = 1:t
    xstar = n+i;
    Kstar = [];
    for j = 1:n
        Kstar = [Kstar, k(xstar, x(j), sig_f, sig_n, l)];
    end
        
    y_ = Kstar * K^(-1) * y(1:n);
    y = [y;y_];
end

end

function result = k(x, x_, sig_f, sig_n, l)

result = sig_f^2 * exp((-(x-x_)^2)/(2*l^2)) + sig_n^2*delta(x,x_);

end

function result = delta(x, x_)

if x == x_
    result = 1;
else
    result = 0;
end

end