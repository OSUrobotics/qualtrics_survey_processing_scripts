addpath('../ShapeComplexity/');
% Bail to the debugger if something goes boom
dbstop if error;

% [dataT, data] = ReadData('Range.csv');
% [ dataT, dataN ] = AddNoChecks( dataT, dataN, 'Use the image' );
% [validAnsws, nAnsw] = GetValidSurvey( dataT, data );
% 
% answSame = QuestionType( 'Do all of the above grasps look similar', dataT, data, validAnsws, 1 );
% fprintf('All 3 similar: %0.0f of %0.0f\n', sum( sum( answSame == 1 ) ), sum( sum( answSame ~= -1 ) ) );
% 
% answLR = QuestionType( 'Which grasp is most similar to the grasp in the middle', dataT, data, validAnsws, 1 );
% fprintf('Match left: %0.0f of %0.0f\n', sum( sum( answLR == 1 ) ), sum( sum( answLR ~= -1 ) ) );
% fprintf('Match right: %0.0f of %0.0f\n', sum( sum( answLR == 2 ) ), sum( sum( answLR ~= -1 ) ) );
% 
% answWork = QuestionType( 'Select grasps that you think would work', dataT, data, validAnsws, 3 );
% for k = 1:3
%     fprintf('All 3 work: %0.0f of %0.0f\n', sum( sum( answWork(k,:,:) == 1 ) ), sum( sum( answWork(k,:,:) ~= -1 ) ) );
% end

[dataT, data] = ReadData('Similar.csv');
[ dataT, data ] = AddNoChecksGroup( dataT, data, 'Top left grasp', 6 );
%[validAnsws, nAnsw] = GetValidSurvey( dataT, data );
validAnsws = zeros( size( dataT, 1 ), 1 ) == 0;
validAnsws(1:2) = false;

answF = QuestionType( 'Top left grasp (black border) is the prime grasp. Select those grasps that will function', dataT, data, validAnsws, 1 );
fprintf('Function same: %0.0f of %0.0f\n', sum( sum( answF == 1 ) ), sum( sum( answF ~= -1 ) ) );

answP = QuestionType( 'Top left grasp (black border) is the prime grasp. Select the grasps that have the same hand pose', dataT, data, validAnsws, 1 );
fprintf('PoseSame: %0.0f of %0.0f\n', sum( sum( answP == 1 ) ), sum( sum( answP ~= -1 ) ) );

answFT = QuestionTypeText( 'Why do you think these grasps will function ', dataT, validAnsws );
answPT = QuestionTypeText( 'How would you describe the hand pose ', dataT, validAnsws );
fprintf('\Function\n');
for k = 1:length(answFT)
    fprintf('%s\n', answFT{k} );
end
fprintf('\nPose\n');

for k = 1:length(answFT)
    fprintf('%s\n', answFT{k} );
end
