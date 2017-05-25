function [ commas, strAll ] = FindCommas( fid )
%FindCommas Read a csv file line with commas as deliminators
%   Deals with commas in "" correctly

commas = [];
bInQuote = false;

str = fgets(fid);
pos = 1;
strAll = str;
while bInQuote == true || length(commas) == 0
    for k = 1:length(str)
        if bInQuote
            if str(k) == '"'
                bInQuote = false;
            end
        elseif str(k) == '"'
            bInQuote = true;
        elseif str(k) == ','
            commas = [commas pos];
        end
        pos = pos + 1;
    end
    if bInQuote
        str = fgets(fid);
        strAll = [strAll, str];
    end
end

commas = [commas, length(str)];
end
