'use strict';

var questionsController = angular.module('Questions.controllers', []);

questionsController.controller('QuestionCtrl', ['$scope', '$location', '$routeParams', 'QuestionService',
    function ($scope, $location, $routeParams, QuestionService) {

      $scope.questions = [];
      $scope.question = {};

      $scope.questionId = $routeParams.questionId;

      QuestionService.getAllQuestions().then(function (questions) {
        $scope.questions = questions;
        if ($scope.questionId) {
          QuestionService.getQuestionById($scope.questionId).then(function (question) {
            $scope.question = question;
          });
        }
      });

      $scope.skipTo = function(questionId) {
        $location.path('/questions/' + questionId);
      }

      $scope.next = function() {
        $scope.questionId = parseInt($scope.questionId) + 1;
        $location.path('/questions/' + $scope.questionId);
      };

      $scope.previous = function() {
        $scope.questionId = parseInt($scope.questionId) - 1;
        $location.path('/questions/' + $scope.questionId);
      }
    }
]);
