function [ dataT, dataN ] = ReadData( strFName )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

fid = fopen( strFName, 'r' );

nCols = length( FindCommas( fid ) );
nRows = 1;
while ~feof(fid)
    FindCommas(fid);
    nRows = nRows + 1;
end

fseek(fid, 0, 'bof');

dataT = cell(nRows, nCols);
dataN = zeros(nRows, nCols) - 1;
for r = 1:nRows
    [nCommas, str] = FindCommas(fid);
    nCommas = [ 0 nCommas ];
    for c = 1:nCols
        strItem = str(nCommas(c)+1:nCommas(c+1)-1);
        nItem = str2num( strItem );
        if ~isempty(nItem) && size(nItem,1) == 1 && size(nItem,2) == 1
            dataN(r,c) = nItem;
        else
            dataT{r,c} = strItem;
        end            
    end
    

end
fclose(fid);
end

