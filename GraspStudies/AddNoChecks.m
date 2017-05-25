function [ dataT, dataN ] = AddNoChecks( dataT, dataN, strQuest )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here


nRows = size( dataT, 1 );
nCols = size( dataN, 1 );

qNo = zeros(1, nCols) - 1;
qCount = 0;
for c = 1:nCols
    strQ = dataT{1,c};
    hasLParen = find( strQ == '(' );
    hasRParen = find( strQ == ')' );
    hasQ = find( strQ == 'Q' ) == 1;
    hasDollar = strncmp( strQuest, dataT{2,c}, length(strQuest) );
    if ~isempty(hasLParen) && ~isempty(hasRParen) && ~isempty(hasQ)
        qNoParen = str2num( strQ(hasLParen+1:hasRParen-1) );
        if hasDollar && qNoParen == 1
            qCount = qCount + 1;
            %fprintf('%s\n', dataT{1,c});
        end
        if qCount > 0
            qNo(c) = qCount;
        end
    end
end
for r = 3:nRows
    for q = 1:qCount
        if sum( dataN(r, qNo == q) ~= -1 ) > 0
            dataN(r, qNo == q & dataN(r,:) == -1) = 0;
        end
    end
end

end

