 

 angular.module('angApp').controller('headerCtrl', ['$scope', '$location', function($scope, $location){
   
   $scope.setRoute = function(route){
   		$scope.nav = route;	
        $location.path(route);
    }
}])