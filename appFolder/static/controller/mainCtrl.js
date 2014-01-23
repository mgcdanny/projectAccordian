

angular.module('angApp').controller('mainCtrl', ['$scope', '$http', '$filter', function($scope, $http, $filter){
    $scope.projects = {};

    $scope.getProjects = function(){
        $http.get('/api/project').success(function(res){
            $scope.projects = res['data']
        })
    }

    $scope.getProjects();

}])



