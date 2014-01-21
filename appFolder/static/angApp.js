
var app = angular.module('angApp', ['ngResource', 'ngRoute','ui.bootstrap']);

app.config(['$routeProvider', function($routeProvider){
	$routeProvider.
        when('/', {
            templateUrl: '/static/partial/main.html',
            controller: 'mainCtrl'
        }).when('/test',{
            templateUrl: '/static/partial/test.html',
            controller: 'AccordionDemoCtrl'            
        }).otherwise({
            redirectTo: '/'
        });
}]);

//http://stackoverflow.com/questions/15610501/in-angular-i-need-to-search-objects-in-an-array
//not using this but is handy filter to get results by propertyname and value
app.filter('getByProperty', function() {
    return function(collection, propertyName, propertyValue) {
        var i=0, len=collection.length;
        for (; i<len; i++) {
            if (collection[i][propertyName] == propertyValue) {
                return collection[i]['vl'];
            }
        }
        return null;
    }
});



