'use strict';

var questionsController = angular.module('Questions.controllers', []);

questionsController.controller('QuesionListCtrl', ['$scope', 'QuestionService',
    function ($scope, QuestionService) {
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
        }();
    }
]);

questionsController.controller('QuestionDetailCtrl', ['$scope', '$routeParams', 'QuestionService',
    function ($scope, $routeParams, QuestionService) {
        $scope.questionId = $routeParams.questionId;
        $scope.getQuestion = function() {
            var promise = QuestionService.getQuestion($scope.questionId);
            promise.then(
                function(data) {
                    $scope.question = data.data;
                    console.log(data);
                },
                function(error) {
                    console.log('Error: ', error);
                }
            );
        }();
    }
]);
