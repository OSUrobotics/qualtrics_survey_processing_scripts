function [ dataT, dataN ] = AddNoChecksGroup( dataT, dataN, strQuest, nGroup )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here


nRows = size( dataT, 1 );
nCols = size( dataN, 2 );

qNo = zeros(1, nCols) - 1;
qCount = 1;
c = 1;
while c < nCols
    strQ = dataT{1,c};
    hasLParen = find( strQ == '(' );
    hasRParen = find( strQ == ')' );
    hasQ = find( strQ == 'Q' ) == 1;
    hasDollar = strncmp( strQuest, dataT{2,c}, length(strQuest) );
    if ~isempty(hasLParen) && ~isempty(hasRParen) && ~isempty(hasQ) && hasDollar
        qNo(c:c+nGroup);
        qCount = qCount + 1;
        c = c + nGroup;
    else
        c = c+1;
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

