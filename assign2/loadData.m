function data = loadData(fileName)

data = readtable(strcat('../data/', fileName), 'PreserveVariableNames', true);

end