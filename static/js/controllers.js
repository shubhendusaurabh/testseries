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

      $scope.saveSelection = function() {
        $scope.question.status = "saved";
      };

      $scope.saveForReview = function() {
        $scope.question.status = "review";
      };

      $scope.clearSelection = function() {
        $scope.question.status = "viewed";
      };

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

questionsController.controller('TimerCtrl', ['$scope', 'TimerService',
  function($scope, TimerService) {
    $scope.remainingTime = function() {
      var time = new Date() - $scope.endTime;
      return time;
    };

    TimerService.getTime().then(function(time) {
      $scope.endTime = time.endtime;
      console.log(time.endtime);
    });
  }
]);
