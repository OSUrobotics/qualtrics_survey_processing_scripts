%% Process both the qualtrics survey format and the survey itself to map survey data to
% the questions answered

clear
clc

strSurveyData = 'Similar_cluster_detection.csv';
strSurveyQuestions = 'Similar_cluster_detection.qsf';
[dataT, data] = ReadData( strSurveyData );
[dataTMap, ~] = ReadData( 'SurveyMapping.csv' );

% Now get rid of the practice/unfinished ones
[ validAnsws, nQuestAnsw ] = GetValidSurvey( dataT, data );

% Now map the questions to a table of objects
validAnsws(1) = true;
validAnsws(2) = true;
[similarityMatrix] = FindSimilar( dataT(validAnsws,:), data(validAnsws,:) );


fid = fopen('Compare.csv', 'w');
ind = 2;
for o = 1:size( similarityMatrix.Questions, 1)
    m = similarityMatrix.Questions{o,1};
    for g = 1:9
        for q = 1:5
            fprintf(fid, '%s_AreaIntersection.csv,%s_AreaIntersection.csv,%0.6f\n', dataTMap{ind, 1}, dataTMap{ind, q+1}, ...
                m(g,q+1) / m(g, 1));
        end
        ind = ind+1;
    end    
end
fclose(fid);
%ParseQSF( strSurveyQuestions );