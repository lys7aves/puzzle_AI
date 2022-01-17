function data = AutoregressiveModel(data, p, t)

X = [];
y = [];

for i = p+1:size(data,1)
    y = [y;data(i)];
    x = [];
    for j = 1:p
        x = [x, data(i-j)];
    end
    X = [X; [1, x]];
end

b = (transpose(X) * X)^(-1) * transpose(X) * y;
    
for i = 1:t
    x = [];
    for j = 0:p-1
        x = [x, data(end-j)];
    end
    
    y_ = [1, x] * b;
    
    data = [data; y_];
end

end