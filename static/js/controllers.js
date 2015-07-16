'use strict';

var questionsController = angular.module('Questions.controllers', []);

questionsController.controller('QuestionCtrl', ['$scope', '$routeParams', 'QuestionService',
    function ($scope, $routeParams, QuestionService) {

        $scope.$on('$locationChangeStart', function(scope, next, current){
            console.log(current, next);
            $scope.questionId = $routeParams.questionId;
            if ($scope.questionId) {
                $scope.question = $scope.lookUp[$scope.questionId];
            }
            console.log($scope.lookUp);
            console.log($scope.question);
        });
        $scope.questions = [];
        $scope.getQuestions = function() {
            var promise = QuestionService.getQuestions();
            promise.then(
                function(data) {
                    $scope.questions = data.data.results;
                    console.log(data.data.results);
                },
                function(error) {
                    console.log('Error: ', error);
                }
            );
            $scope.lookUp = {};
            for (var i = 0; i < $scope.questions.ength; i++) {
                $scope.lookUp[$scope.questions[i].pk] = $scope.questions[i];
            }
        }();
        if ($scope.questionId) {
            $scope.question = $scope.lookUp[$scope.questionId];
        }

    }
]);
