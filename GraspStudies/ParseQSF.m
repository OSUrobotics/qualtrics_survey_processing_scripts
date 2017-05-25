function [  ] = ParseQSF( fname )
%ParseQSF Parse a qsf file and look for places to add names in loop fields
%   Also spits out in legible, nested form

fid = fopen( fname, 'r' );
str = fscanf(fid, '%s');

inQuote = false;
curlyBracketDepth = 1;

for k = 1:length(str)
    bDoCR = false;
    if str(k) == '{'
        curlyBracketDepth = curlyBracketDepth+1;
        fprintf('\n');
        for indent = 1:curlyBracketDepth
            fprintf(' ');
        end
    elseif str(k) == '}'
        curlyBracketDepth = curlyBracketDepth-1;
    elseif inQuote == false && str(k) == '"'
        inQuote = true;
    elseif inQuote == true && str(k) == '"'
        inQuote = false;
    end
    if bDoCR == true
        fprintf('\n');
    end
    
    fprintf('%s', str(k));
        
end

end

