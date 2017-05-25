function [ answ ] = QuestionTypeText( strStart, dataT, validAnsw )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

% First figure out how many questions total
colsWithAnsw = zeros( size(dataT, 2), 1 ) ~= 0;
for k = 1:size(dataT,2)
    if strncmp(dataT{1,k},'Q', 1) && strncmp(dataT{2,k}, strStart, length( strStart ))
        colsWithAnsw(k,1) = true;
    end
end

answ = cell( sum( validAnsw == true ) * sum( colsWithAnsw == true ) );

cols = find( colsWithAnsw );
count = 1;
for r = 3:size(dataT,2)
    for k = 1:length( cols )
        if ~isempty( dataT{r,k} )
            answ{count} = dataT{r,k};
            count = count + 1;
        end
    end
end
 
answ = answ{count};

end

