'use strict';


var twitter = angular.module('twitterApp',['ngRoute','twitter.controller','twitter.services']);

twitter.config(['$routeProvider',function($routeProvider){
	
	$routeProvider.
		when("/home",{
			templateUrl : "static/partials/home.html",
			controller : "homeController"
		}).
		when("/profile",{
			templateUrl : "static/partials/profile.html",
			controller : "profileController"
		}).
		when("/tweetpost",{
			templateUrl : "static/partials/tweetpost.html",
			controller : "postController"
		}).
		when("/database",{
			templateUrl : "static/partials/database.html",
			controller : "databaseController"
		}).
		otherwise({redirectTo : "/home"});
		
	
}]);
