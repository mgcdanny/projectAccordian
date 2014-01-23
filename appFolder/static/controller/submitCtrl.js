
angular.module('angApp').controller('submitCtrl', ['$scope', '$http', function($scope, $http){

    $scope.project = {};
    $scope.checked = true;
    $scope.render = false;

    $scope.submitProject = function(project){
    	console.log(project)
    }

    $scope.addField = function(group) {
    	temp = {nm:"", dsc:"", vl:""}
    	group.push(temp)
    }

    $scope.addNote = function(group) {
    	temp = {dt:"", txt:"", usr:""}
    	group.push(temp)
    }

    $scope.addTask = function(group) {
    	temp =
    		{
				"nm": "",
				"dsc": "",					
				"field":[
					{
						"nm":"", 
						"dsc":"", 
						"vl":""								
					}
				], 
				"note":[
					{
						"dt":"", 
						"txt":"", 
						"usr":""
					}
				]
			}
    	group.push(temp)
    }

    $scope.addMilestone = function(group) {
    	temp = 
    		{
				"nm":"Temp Name",
				"dsc": "",
				"field":[
					{
						"nm":"", 
						"dsc":"", 
						"vl":""
					}
				],
				"note":[
					{
						"dt":"", 
						"txt":"", 
						"usr":""
					}
				],
				"task":[
					{
						"nm": "",
						"dsc": "",					
						"field":[
							{
								"nm":"", 
								"dsc":"", 
								"vl":""								
							}
						], 
						"note":[
							{
								"dt":"", 
								"txt":"", 
								"usr":""
							}
						]
					}
				]
			}
    	group.push(temp)
    }


 	$scope.addProject = function(group) {
		temp = 
			{
				"nm": "       ",
				"dsc": "",
				"field":[
					{
						"nm":"", 
						"dsc":"", 
						"vl":""
					}
				],
				"note":[
					{
						"dt":"",
						"txt":"",
						"usr":""
					}
				],
				"milestone":[
					{
						"nm":"",
						"dsc": "",
						"field":[
							{
								"nm":"", 
								"dsc":"", 
								"vl":""
							}
						],
						"note":[
							{
								"dt":"", 
								"txt":"", 
								"usr":""
							}
						],
						"task":[
							{
								"nm": "",
								"dsc": "",					
								"field":[
									{
										"nm":"", 
										"dsc":"", 
										"vl":""								
									}
								], 
								"note":[
									{
										"dt":"", 
										"txt":"", 
										"usr":""
									}
								]
							}
						]
					}
				]
			}
		group.push(temp)
	}

}])





