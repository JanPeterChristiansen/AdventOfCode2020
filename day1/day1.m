more off
close all
clear all
clc

%%

data = importdata('data.txt');

N = length(data);

res = [];
for i=1:N
    for j=1:N
        for k=1:N
            if (data(i)+data(j)+data(k) == 2020)
                res = data(i)*data(j)*data(k);
            end
        end
    end
end