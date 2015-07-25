'use strict';

var questionsController = angular.module('Questions.controllers', []);

questionsController.controller('QuestionCtrl', ['$scope', '$location', '$routeParams', '$interval', 'QuestionService',
    function ($scope, $location, $routeParams, $interval, QuestionService) {

      var timerPromise, deadlineTime;

      $scope.questions = [];
      $scope.question = {};

      $scope.questionId = $routeParams.questionId;

      QuestionService.getAllQuestions().then(function (questions) {
        $scope.questions = questions;
        if ($scope.questionId) {
          QuestionService.getQuestionById($scope.questionId).then(function (question) {
            deadlineTime = moment().add(2, 'minutes');
            startTimer();
            $scope.question = question;
          });
        }
      });

      function startTimer() {
        stopTimer();
        timerPromise = $interval(setTimer, 1000);
      }

      function stopTimer() {
        $interval.cancel(timerPromise);
      }

      function setTimer() {
        var diff = deadlineTime.diff(moment());
        if (diff < 0) {
          stopTimer();
          timesUp();
        }
        var durr = moment.duration(diff);
        $scope.countdown = durr.minutes() + ':' + durr.seconds();
      }

      function timesUp() {
        $scope.question.showHint = true;
      }

      $scope.$on('$destroy', function() {
        stopTimer();
      });

      $scope.changeChoice = function($index) {
        $scope.question.user_selected = $index;
      }

      $scope.saveSelection = function() {
        $scope.question.status = "saved";
        if (($scope.question.answer-1) == $index) {
          console.log($scope.question.answer);
        }
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
