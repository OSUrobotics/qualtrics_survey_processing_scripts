function [ answ ] = QuestionType( strStart, dataT, data, validAnsw, nAnswPer )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

% First figure out how many questions total
colsWithAnsw = zeros( size(dataT, 2), 1 ) ~= 0;
for k = 1:size(dataT,2)
    if strncmp(dataT{1,k},'Q', 1) && strncmp(dataT{2,k}, strStart, length( strStart ))
        colsWithAnsw(k,1) = true;
    end
end

answ = zeros( nAnswPer, sum( validAnsw == true ), sum( colsWithAnsw == true ) / nAnswPer );

cols = find( colsWithAnsw );
count = 1;
for k = 1:nAnswPer:length( cols )
    for a = 1:nAnswPer
        answ(a, :, count) = data( validAnsw, cols(k + a - 1) );
    end
    count = count + 1;
end
 
answ = squeeze(answ);

end

