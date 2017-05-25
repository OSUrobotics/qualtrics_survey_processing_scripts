function [ validAnsws, nQuestAnsw ] = GetValidSurvey( dataT, data )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here


validAnsws = zeros( size( dataT,1 ), 1) == 0;
nQuestAnsw = zeros( size( data, 2 ), 1);
for k = 1:size(dataT,2)
    if strcmp(dataT{2,k}, 'Finished')
        validAnsws = validAnsws & data(:,k) == 1;
    end
    if strcmp(dataT{2,k}, 'workerId')
        validAnsws(1:2) = false;
        for p = 3:size( validAnsws, 1 )
            validAnsws(p) = validAnsws(p) & length( dataT{p,k} ) > 1;
        end
    end
    if strcmp(dataT{2,k}, 'IPAddress')
        validAnsws(1:2) = false;
        for p = 3:size( validAnsws, 1 )
            validAnsws(p) = validAnsws(p) & length( dataT{p,k} ) > 1;
        end
    end
    if strncmp(dataT{1,k},'Q', 1)
        nQuestAnsw(k) = sum( ( data(validAnsws,k) ) > -1 );
    end
end

end
