function data = modifyData(table)

n = height(table);

table = table(:,{'날짜','종가'});
table = sortrows(table, '날짜');

array = table2array(table(:,{'종가'}));

data = [];
for i = 1:n
    data = [data; str2double(array(i,:))];
end

end