
'use strict';


var twittCtrl = angular.module('twitter.controller',['ui.bootstrap','ngGrid']);

twittCtrl.controller("homeController",function($scope,tweetData,$modal){
	
	//console.log(tweetData.dataset);
	$scope.dataset= tweetData.dataset;

  $scope.switch = 1 ;

  $scope.srcd = "static/img/tick_grey1.jpg";

  $scope.imgChange = function(){

      
      $scope.switch = -1 * $scope.switch ;
      
      if($scope.switch == 1){
          $scope.srcd = "static/img/tick_grey1.jpg";
      }else{
          
          $scope.srcd = "static/img/green_tick_trans.png";
      }
  };

  //here the modals go

  $scope.name = 'sebin';
      
  $scope.showModal = function(tweet) {
        
  $scope.opts = {
      backdrop: true,
      backdropClick: true,
      dialogFade: true,
      keyboard: true,
      templateUrl : 'static/partials/modalContent.html',
      controller : ModalInstanceCtrl,
      resolve: {
          data : function(){
           return tweet;
            }
            } // empty storage
        };
          
        
        /*$scope.opts.resolve.item = function() {
            return angular.copy({name:$scope.name}); // pass name to Dialog
        }*/
        
          var modalInstance = $modal.open($scope.opts);
          
          modalInstance.result.then(function(){
            //on ok button press 
          },function(){
            //on cancel button press
            console.log("Modal Closed");
          });
      }; 

});

twittCtrl.controller("profileController",function($scope){
	
	alert("hello");
});

twittCtrl.controller("databaseController",function($scope,$http){
  
  $scope.getPosts = function(){


    //Get the posts from database
    $http({
      method:'get',
      url : "http://127.0.0.1:5000/twitter/api/v1.0/posts"
    }).success(function(result){

      $scope.postData = result;
      console.log("posts data :"+JSON.stringify(result,null,4));

    }).error(function(data){

        alert("posts failed "+data);
    });

    //Get the post headers from database
    $http({
      method:'get',
      url : "http://127.0.0.1:5000/twitter/api/v1.0/postsheaders"
    }).success(function(result){

      console.log("post headers :"+JSON.stringify(result,null,4));
      $scope.postDataHeaders = result;

    }).error(function(data){

        alert("postsheaders failed "+data);
    });

    $scope.gridOptions = { data: 'postData' };
  } 

  $scope.getPosts();
  
  $scope.myData = [{name: "Moroni", age: 50},
                 {name: "Tiancum", age: 43},
                 {name: "Jacob", age: 27},
                 {name: "Nephi", age: 29},
                 {name: "Enos", age: 34}];

  $scope.gridOptions = { data: 'postData' };


});

twittCtrl.controller("postController",function($scope){

  $scope.postit = "";
  
  $scope.postThePost = function(){

      alert($scope.postit);
  };
	
});


var ModalInstanceCtrl = function($scope, $modalInstance, $modal, data) {
    
     $scope.data = data;

    
      $scope.ok = function () {
        $modalInstance.close();
      };
      
      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
}

