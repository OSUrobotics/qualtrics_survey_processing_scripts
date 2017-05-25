
%% LOAD4CLUSTERING Builds a csv file of clusters that should match
%==========================================================================
%
%
%==========================================================================

originalClusters = dir('data_for_matt_and_ryan');
handObjectLinkingFilePath = '../GraspingMetric/3D Exploration/pathMapping.csv';
allGrasps = table2cell( readtable( handObjectLinkingFilePath ) );
names = cell( size( allGrasps, 1 ), 1);
for c = 1:size(names, 1)
    strFull = allGrasps{c,4};
    len = length('handAndAlignment/hand/')+1;
    strClip = strFull( len:end-4 );
    names{c,1} = strClip;
end

% Match category
%  1 is match
%  0 is same obj, no match
match = zeros( size( allGrasps, 1 ) );

fid = fopen('SimilaritySaurabh.csv', 'w');
for c = 1:size(originalClusters,1)
    %For each original Cluster
    if strncmp( 'obj', originalClusters(c).name, 3 )        
        grasps = dir(sprintf('data_for_matt_and_ryan/%s/*.stl',originalClusters(c).name));
        if size(grasps,1) > 2
            for j = 1:size(grasps,1)-1
                for k = j+1:size(grasps,1)
                    %For each combination of grasps in the original cluster
                    name1I = strfind(names,grasps(j).name(1:end-4));
                    name2I = strfind(names,grasps(k).name(1:end-4));
                    name1I = find(~cellfun(@isempty,name1I));
                    name2I = find(~cellfun(@isempty,name2I));
                    %Set their values in the cluster matrix
                    match(name1I,name2I) = true;
                    match(name2I,name1I) = true;
                    fprintf(fid, '%sAreaIntersection.csv, %sAreaIntersection.csv, 1\n', ...
                        names{name1I}, names{name2I} );
                end
            end
        end
    end
end
for r = 1:length(names)
    for c = r+1:length(names)
        if allGrasps{r,5} == allGrasps{c,5}
            if ~match(r,c)
                fprintf(fid, '%sAreaIntersection.csv, %sAreaIntersection.csv, 0\n', ...
                    names{r}, names{c} );
            end
        end
    end
end
fclose(fid);


