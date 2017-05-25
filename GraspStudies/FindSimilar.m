function [ similarityMatrix ] = FindSimilar( dataT, data )
% Input: the string and number tables from the survey
% Output: For each object, for each grouped question, counts of similar for
% the six images given
%  
% Example string
strExample = 'Top left grasp (black border) is the prime grasp. Select those grasps that will function the same... (9)-${lm://Field/6}';

whichCols = [];
obj = [];
nObj = 0;

% Find the number of times we start one of these questions blocks
for k = 1:size( dataT, 2 )
    str = char( dataT(2,k) );
    % Have a string of the correct length
    if length( str ) == length(strExample)
        % Have a string of the correct form
        if strncmp( str, strExample, length( strExample ) - 20 )
            % Look for the first question in the lot
            strEnd = str( end-18:end );
            % Look for the first image of that question
            if strEnd(end-1) == '1'
                if strEnd(2) == '1'
                    nObj = nObj + 1;
                    fprintf(' Starting object %0.0f\n', nObj);
                end
                whichCols = [ whichCols, k ];
                obj = [obj nObj];
                fprintf('Found: %s\n', strEnd);
                
            end
        end
    end
end


similarityMatrix = struct;
similarityMatrix.Objects = obj;
similarityMatrix.Columns = whichCols;
similarityMatrix.Questions = cell(nObj, 1);

for k = 1:nObj
    cols = find( obj == k );
    objMatrix = zeros( length(cols), 6 );
    for c = 1:length(cols)
        col = whichCols( cols(c) );
        for r = 1:size( data, 1)
            if data(r,col) == 1
                objMatrix( c, 1:6 ) = objMatrix( c, 1:6 ) + (data (r, col:col+5) == 1);
            end
        end
    end
    fprintf('Found %0.0f questions for object %0.0f\n', length(cols), k);
    similarityMatrix.Questions{k,1} = objMatrix;
end

end